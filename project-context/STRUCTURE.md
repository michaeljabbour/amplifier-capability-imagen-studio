# Project Structure

| Path | Purpose |
|---|---|
| `bundle.md` | Root bundle entry point and pinned foundation composition |
| `behaviors/` | Full and self-contained à-la-carte behavior definitions |
| `bundles/` | Pre-composed local and provider variants |
| `agents/` | Specialist agent instructions |
| `context/` | Adaptive router and production policy loaded into sessions |
| `skills/` | Lazily discoverable production and ASCII-art workflows |
| `modules/tool-imagen/` | Native Amplifier adapter for the external MCP contract |
| `docs/` | Human-readable capability and workflow references |
| `schemas/` | Machine-readable artifact manifest contract |
| `evals/` | Versioned scenarios, deterministic high-risk harness/tests, and dated machine-readable evidence |
| `scripts/` | Static repository validation and behavioral-evaluation entry point |
| `.github/workflows/` | CI automation |
| `project-context/` | Persistent state, glossary, provenance, structure, and handoff |

New product guidance belongs in `context/` when it is an always-on invariant,
in a specialist or skill when it is role/workflow-specific, and in `docs/` when
it is reference material. Machine-enforceable shapes belong in `schemas/` and
behavioral expectations in `evals/`.

`project-context/WAYSOFWORKING.md` records repository-specific verification and
failure recovery steps; keep the final command set there when release checks
change.

## Portable consolidation (2026-10-28)

`skills/imagen-studio/` owns the canonical method, generated references, license, and local ASCII converter. `docs/source-methods/`, native `context/`, and `schemas/` are canonical mirror sources. `scripts/sync_skill.py --check` enforces drift; `scripts/capability.py` owns static site/install packaging; `scripts/local_runtime.py` emits ignored machine-local YAML. `scripts/check_external_contract.py` accepts an explicit independent executable and checks initialize/discovery only.

`tests/test_ascii_tones.py` checks black/white endpoint semantics for standard, detailed and inverted ramps.
