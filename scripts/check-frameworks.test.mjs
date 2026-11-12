// The framework check against real data and against broken copies: every seed conforms, and each
// fixture under test/fixtures/broken fails with the words that name its fault. Run: npm test
import assert from 'node:assert/strict';
import { readdirSync } from 'node:fs';
import path from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';
import { checkFramework } from './check-frameworks.mjs';

const repo = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const broken = (name) => checkFramework(path.join(repo, 'test', 'fixtures', 'broken', name));
const says = (problems) => problems.map((problem) => `${problem.path}: ${problem.message}`);

test('every seed conforms', () => {
  const seeds = readdirSync(path.join(repo, 'seeds'), { withFileTypes: true }).filter((entry) => entry.isDirectory());
  assert.ok(seeds.length >= 3);
  for (const seed of seeds) assert.deepEqual(checkFramework(path.join(repo, 'seeds', seed.name, '.eidos', 'Framework.yaml')), [], seed.name);
});

test('a type outside the seven is a fault', () => {
  assert.deepEqual(says(broken('unknown-type.yaml')), ['properties.custom[0].type: is not one of the seven types (Text, List, Number, Checkbox, Date, Date & time, Object), matched in any case']);
});

test('a collection has one default at most', () => {
  assert.deepEqual(says(broken('two-defaults.yaml')), ['folders[0].variants: marks more than one variant `default: true`; a collection has one default at most']);
});

test('none is never a variant’s name', () => {
  assert.deepEqual(says(broken('variant-none.yaml')), ['folders[0].variants[1].name: is named none, which a blueprint writes in `variant` for no template']);
});

test('an owner is @<tool>/<kind>, @eidos/collections is the one @eidos/ kind, and variants are a collection’s', () => {
  assert.deepEqual(says(broken('eidos-owner.yaml')), [
    'folders[0].owned_by: names an @eidos/ kind the standard does not define; it defines @eidos/collections alone',
    'folders[1].owned_by: is not an owner (@<tool>/<kind>, lowercase letters, digits, hyphens)',
    'folders[2]: carries variants or folders, which only a folder owned by "@eidos/collections" has',
  ]);
});

test('folders nest to any depth, and the older grouping still conforms', () => {
  assert.deepEqual(checkFramework(path.join(repo, 'test', 'fixtures', 'nested-folders.yaml')), []);
});

test('a collection carries grouping or the folder keys, never both, and a folder entry names one folder', () => {
  assert.deepEqual(says(broken('folders.yaml')), [
    'folders[0]: carries the older `grouping` beside the folder keys; a collection carries one or the other',
    'folders[1].folders[0].folders[0].name: is a path; a folder entry names one folder, and its `folders` hold the ones beneath it',
    'folders[2]: carries variants or folders, which only a folder owned by "@eidos/collections" has',
  ]);
});

test('options are a non-empty list, and never on an Object', () => {
  assert.deepEqual(says(broken('options.yaml')), ['properties.custom[0].options: is an empty list', 'properties.custom[1]: carries options on an Object, which is a fault']);
});

test('the document’s own shape: its version, naming, keys, entries, templates, tool names, and terms', () => {
  const problems = broken('shape.yaml');
  assert.deepEqual(says(problems), [
    '(the document): eidos_version is missing',
    '(the document): collections is not a key the standard names here',
    'naming: must be one of kebab-case, TitleCase, Title Case',
    'top_level[0]: description is missing',
    'folders[0].variants[0].template: is not a template path (templates/<unit>.<variant>.md, lowercase)',
    "properties.tools: eidos is not a tool's name (lowercase letters, digits, hyphens; eidos is reserved)",
    'vocabulary[0].means: is empty',
    'vocabulary[0].not: must be a list',
  ]);
  assert.equal(problems.find((problem) => problem.path === 'naming')?.line, 2, 'each problem names its line');
});
