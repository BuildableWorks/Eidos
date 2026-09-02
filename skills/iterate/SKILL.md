---
name: iterate
description: >-
  Interrogate one rough idea until both of you understand what it actually is — the shape it takes, the intent behind it, and how it fits the blueprints already there. A question-and-answer pass that writes nothing: it ends with an understanding the owner can stand behind, handed to `eidos` to author. Use when someone has an idea but not yet a blueprint — "I want to add X, help me think it through", "flesh this out", "I'm not sure what this actually is", "what am I really building here", "poke holes in this before I write it", "help me scope this feature". Also use before authoring when a request arrives as one vague line. To reshape a draft that already exists, use `format`; to write the blueprint once it's understood, use `eidos`.
---

# Iterate

One idea, questioned until it holds still. The owner arrives with something half-formed — a feature, a chapter, a study, a scene — and leaves knowing what it is, what it isn't, and where it sits. **You write no file here.** The whole output is a shared understanding; `eidos` turns it into a blueprint afterward.

This is the pass that usually gets skipped. A blueprint authored straight from one line of prompt reads as settled while nobody has decided anything, and the cost shows up later as scope nobody agreed to. Eidos leans on the owner's thinking; this skill is how that thinking gets pulled out.

Companion to `eidos` (authors and validates) and `format` (reshapes a draft already written). Reach for this one when there is still thinking to do.

## Before you ask anything

**Read the actor.** `_eidos/me.md` for the role and calibration, then that role's own contract in `_eidos/roles/<role>.md`, and follow it — it sets the vocabulary, the depth, what to surface, and who holds decisions. Read the contract itself; don't infer a role from its filename. A blank or absent `me.md` means default to full facilitation; offer `whoami`.

**Read the framework.** `_eidos/Framework.md` for the collections, their flavors, their grouping, and the Schema. No `_eidos/` means no framework — stop and offer `install`.

**Read the neighbors.** The target collection's `index.md`, and any blueprint the idea sounds adjacent to. Questions asked against what already exists are worth ten asked in a vacuum: you can ask whether this is really separate from something already written, and the owner can see it is.

Never open the interrogation cold. Two minutes of reading turns generic prompts into specific ones.

## The three passes

Run them in order — each needs the one before it — but treat them as a conversation, not a script. Skip what the owner has already made obvious, and go back a pass when an answer undoes an earlier one.

### 1. Which shape

Where does this live, and what body does it take? From the Framework, propose the collection and flavor you think it fits, say why in a sentence, and **ask**. The owner corrects placement faster than they describe it.

Three answers matter more than a smooth fit:

- **It fits no collection.** Don't force it. Either it's a top-level doc (one of a kind, free-form) or the framework is missing a collection — `configure` adds one. A forced fit is a wrong blueprint that validates.
- **It fits two.** Usually two ideas wearing one name. Say so and offer to split; splitting here is cheap and later it isn't.
- **It's bigger than a blueprint.** Several blueprints and a theme. Name the pieces and ask which one this session is about — one idea at a time is the whole discipline.

Once placed, read that flavor's shape. Its sections are what you need to know by the end; let them steer the rest, and use the shape's own names for things rather than generic ones.

### 2. What is the intent

Why does this exist, and what does it observably do? Push until the answer is specific enough that someone else could tell whether it had been built.

- **Who is it for, and what changes for them?** "Users want it" is not yet an answer.
- **What does it do that nothing here does today?** If the honest answer is "nothing", that's a finding.
- **What breaks, or stays broken, if it's never made?** The clearest test of whether an idea is real.
- **What will it deliberately not do?** Press hardest here, and keep pressing — the standard puts the most weight on non-goals, and this is where scope is actually held. An owner who can't name a single non-goal hasn't bounded the idea yet. Offer candidates for them to reject: "so this doesn't cover X?" is easier to answer than an open question.

### 3. How it fits

A blueprint in isolation is a wish. Place it against everything else.

- **What must exist first?** Dependencies, in and out of the blueprints.
- **What does it touch?** The blueprints it connects to, and what flows between them.
- **Where's the seam?** Take the nearest existing blueprint and ask what falls on each side. A boundary nobody can state is a boundary that will be argued about later.
- **Does it change anything already written?** New work often quietly obsoletes or contradicts an existing blueprint. Name the blueprint and ask.
- **Where in the grouping?** If the collection groups its blueprints, which group — and if the answer is "a new one", that's a decision worth making on purpose.

## How to ask

- **Small batches.** Two to four questions at a time, tightest first. A wall of questions gets one answer.
- **Concrete beats open.** "Does this cover the offline case?" gets a real answer; "what are the edge cases?" gets silence.
- **Never answer your own question.** Proposing an option for the owner to accept or reject is facilitation. Recording your own guess as their answer is authoring, and it is the one failure this skill exists to prevent.
- **"I don't know" is a result.** Write it down as an open question and move on. A blueprint may ship carrying open questions; what it may not carry is a gap nobody noticed.
- **Play back what you heard.** Every few rounds, restate the idea in two or three sentences and let the owner correct it. The corrections are the real content.
- **Don't run the shape as a form.** The shape tells you what to find out, not what to recite. Nobody wants to be walked down a checklist.

## When you're done

Stop at the first of these:

- **You can state it.** Three or four sentences the owner agrees with: what it is, what it deliberately won't do, where it sits, and what it depends on. Say them out loud and get the nod.
- **Two rounds add nothing.** If questions stop producing new information, the idea is as understood as it's going to get today. Say so rather than grinding.
- **The owner is out of answers.** Stop and list what's still open. Half an idea, honestly marked, beats a whole one invented.

Then close with a short recap — the placement (collection and flavor), the intent, the non-goals, the connections, and the open questions — and offer to author it with `eidos`. Hand over the recap; don't make the next skill re-ask what you already asked.

If the session ends without a blueprint, that is a fine outcome. Learning that an idea is two ideas, or already covered, or not worth doing, is the cheapest thing this skill can produce.
