// Checks framework documents (.eidos/Framework.yaml) against schema/framework.schema.yaml, the
// rules EIDOS.md sets for one. The file stays YAML: it is parsed, and the schema is applied to
// what it holds. Prints one line per violation with the file, its YAML path, and its line, and
// exits 1 on any.
// Usage: node scripts/check-frameworks.mjs [Framework.yaml ...]
// With no paths, every seed's .eidos/Framework.yaml is checked.
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import Ajv2020 from 'ajv/dist/2020.js';
import { LineCounter, parse, parseDocument } from 'yaml';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const schema = parse(readFileSync(path.join(repo, 'schema', 'framework.schema.yaml'), 'utf8'));
const validate = new Ajv2020({ allErrors: true, strict: false, verbose: true }).compile(schema);

const seedFrameworks = () =>
  readdirSync(path.join(repo, 'seeds'), { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => path.join(repo, 'seeds', entry.name, '.eidos', 'Framework.yaml'))
    .filter((file) => existsSync(file));

// `/folders/2/variants/0` as a reader finds it in the file: folders[2].variants[0]
const yamlPath = (segments) => segments.reduce((written, segment) => (/^\d+$/.test(segment) ? `${written}[${segment}]` : written === '' ? segment : `${written}.${segment}`), '') || '(the document)';

// What a failed keyword means, in the words EIDOS.md uses for it.
// A rule the schema words itself (`x-says`) is said that way.
function said(error) {
  const { keyword, params, message, parentSchema } = error;
  if (keyword === 'contains' && params.maxContains !== undefined) return parentSchema?.['x-says'] ?? message;
  if (parentSchema?.['x-says'] && !['type', 'required'].includes(keyword)) return parentSchema['x-says'];
  if (keyword === 'required' && parentSchema?.['x-says']) return parentSchema['x-says'];
  if (keyword === 'additionalProperties') return `${params.additionalProperty} is not a key the standard names here`;
  if (keyword === 'required') return `${params.missingProperty} is missing`;
  if (keyword === 'type') {
    const yamlWords = { array: 'a list', object: 'a mapping', string: 'text', boolean: 'true or false', number: 'a number', null: 'empty' };
    return `must be ${[params.type]
      .flat()
      .map((type) => yamlWords[type] ?? type)
      .join(' or ')}`;
  }
  if (keyword === 'enum') return `must be one of ${params.allowedValues.join(', ')}`;
  if (keyword === 'const') return `must be ${JSON.stringify(params.allowedValue)}`;
  if (keyword === 'not') return 'is not allowed here';
  if (keyword === 'minLength' && params.limit === 1) return 'is empty';
  if (keyword === 'minItems' && params.limit === 1) return 'is an empty list';
  return message;
}

export function checkFramework(file) {
  const text = readFileSync(file, 'utf8');
  const lineCounter = new LineCounter();
  const document = parseDocument(text, { lineCounter });
  if (document.errors.length > 0) return document.errors.map((error) => ({ path: '(the document)', line: error.linePos?.[0]?.line ?? null, message: `is not YAML: ${error.message.split('\n')[0]}` }));
  const data = document.toJS() ?? {};
  if (validate(data)) return [];
  const seen = new Set();
  const problems = [];
  for (const error of validate.errors ?? []) {
    // an if/then or a oneOf failing repeats what its branches already said
    if (error.keyword === 'if' || error.keyword === 'propertyNames' || (error.keyword === 'contains' && error.params.maxContains === undefined)) continue;
    // a branch of a oneOf that has its own wording says it once, on the oneOf
    if (error.schemaPath.includes('/oneOf/')) continue;
    const segments = error.instancePath
      .split('/')
      .slice(1)
      .map((segment) => segment.replaceAll('~1', '/').replaceAll('~0', '~'));
    const node =
      segments.length === 0
        ? document.contents
        : document.getIn(
            segments.map((segment) => (/^\d+$/.test(segment) ? Number(segment) : segment)),
            true,
          );
    const line = node?.range ? lineCounter.linePos(node.range[0]).line : null;
    const named = error.propertyName === undefined ? '' : `${error.propertyName} `;
    const problem = { path: yamlPath(segments), line, message: `${named}${said(error)}` };
    const key = `${problem.path}\u0000${problem.message}`;
    if (seen.has(key)) continue;
    seen.add(key);
    problems.push(problem);
  }
  return problems;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const files = process.argv.length > 2 ? process.argv.slice(2).map((file) => path.resolve(file)) : seedFrameworks();
  let failed = 0;
  for (const file of files) {
    const shown = path.relative(process.cwd(), file) || file;
    if (!existsSync(file)) {
      console.log(`✗ ${shown}: no such file`);
      failed += 1;
      continue;
    }
    const problems = checkFramework(file);
    if (problems.length === 0) {
      console.log(`✓ ${shown}`);
      continue;
    }
    failed += 1;
    for (const problem of problems) console.log(`✗ ${shown}:${problem.line ?? ''} ${problem.path}: ${problem.message}`);
  }
  console.log(failed === 0 ? `${files.length} framework${files.length === 1 ? '' : 's'} conform` : `${failed} of ${files.length} framework${files.length === 1 ? '' : 's'} do not conform`);
  process.exit(failed === 0 ? 0 : 1);
}
