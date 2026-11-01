# Handoff

Last updated: 2026-10-30 — CI formatting recovery.

The CI Python matrix stopped on formatting in `scripts/capability.py` before
running later gates. The film renderer now uses the configured formatter's
layout and a named local helper instead of an assigned lambda. The development
formatter is pinned to the CI-observed Ruff 0.17.3; adapter runtime and policy
sources are unchanged.

Local Python 3.12 checks pass: full configured format/lint, bundle validation,
3 deterministic policy tests plus replay of the existing 5-case/5-mutation
record, 36 adapter tests (1 explicit external-contract skip) at 85.33% coverage,
3 local workflow/ASCII tests, isolated wheel build/install smoke, and static
site build/check/JavaScript syntax. Declared dependencies and the extra ASCII
test dependency were installed only from the existing cache in task-owned
environments. No provider call or new behavioral result was produced.

Next: publish the exact tested commit and verify the remote Python matrix.
Existing result records, media and portable method bytes remain unchanged.

Last updated: 2026-10-28 — public marketing refinement.

The current task adds a clearer customer introduction, fictional artifact preview, first-use prompt and complete public clone/install instructions. Shared static UI retains canonical method/package bytes and native execution boundaries. See README, capability.json and docs/INSTALL.md. No provider call, real-user store, enrollment or live experiment is part of this change.

Earlier consolidation context (historical):

Last updated: 2026-10-28 — local portable consolidation, no publication.

Canonical entry: `skills/imagen-studio/SKILL.md`. Original production and ASCII bodies are preserved in `docs/source-methods/`; generated reference mirrors carry source/output hashes. The local ASCII converter moves with the canonical portable folder. Native adapter/MCP-only boundary, eight-tool allowlist, and all July hash-bound policy/harness/case/result bytes remain.

Actual checks: 36 adapter tests pass (one opt-in checkout test skipped), coverage85.33%; July deterministic5/5+5/5 record reproduces; 6 workflow/local/ASCII tests pass; independent executable initialization/discovery of8tools passes with keys removed and no generation. See `docs/VALIDATION.md` for exact scope.

A new local runtime materializer emits an absolute-path YAML behavior with no provider/session/enrollment. Retained immutable v2 entrypoints stay untouched. No provider-package import, sibling discovery, paid call, or remote publication added. Old release history remains in `docs/NATIVE-HANDOFF.md`.

Next: review local site/package, compare actual behavior only under a separately frozen study, and preserve the independent provider-server release lifecycle.

## 2026-11-01 — ASCII luminance boundary correction

The local ASCII converter now follows its documented dark-to-light ramp: black maps to the dense endpoint and white to the space endpoint; inversion reverses those choices. Added four endpoint regressions across standard, detailed and inverted ramps. All six local runtime/ASCII tests pass without a provider call. Existing method IDs, provider policies, media and installation routes are unchanged. No image-generation or outside-user result is inferred from these deterministic tests.

## 2026-11-01: Optional coaching documentation

Added a local opt-in practice/review guide and entry links. Preserve the native direct path, existing execution budgets and source evidence. No learner trace is saved by default. Next: verify standalone guide packaging and seek authentic human/outside-user evidence before any benefit claim. No provider call or live user study is part of this documentation change.
