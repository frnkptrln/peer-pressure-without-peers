# peer_traces r3 — group package, state of 12 September 2026 (main runs in; Codex review adopted; papers on the sprint's template)

Track 5 project (a four-person sprint team; the Track 5 paper is released as a report, not submitted to the sprint — text by Frank Peterlein, built on the team's design work) for the Apart Research × CeSIA AI Incident Response Sprint, 11–13 September 2026. `README_FOR_CLAUDE.md` explains the whole package to a person or an assistant; start there. This package contains the current state only — instrument, data, pre-registration with deviation log, runbook, the two papers on this instrument — not the working history.

## State
| what | state |
|---|---|
| Instrument (`harness-r3/`) | frozen: `MANIFEST.sha256.v6.json` (amendment hash d096dbb1…, ten instrument files); 68 + 31 tests green; deviations D1–D5 logged in `harness-r3/DEVIATIONS.md`, each before any main episode |
| Gate (Opus 5, 42 episodes, 7 Sep) | 0 forbidden reads, 0 fabrications on R0/R1/R2; reporting tool 4/4; hand-off notes 2/2 chains |
| Declared pilots (52 episodes, 7 Sep) | Haiku 4.5: R2×T2 **6/8** forbidden reads, the other three cells 0/8 (p = 0.031); Sonnet 5: 0/16; Opus 5 under claimed authorization (T4): 0/4 |
| Open-weights pilot (32 episodes, 8 Sep) | Qwen3-8B non-thinking never read the README or a note: 32/32 ABANDON — exposure gate failed, no main run, tier shelved |
| Main runs (11 Sep, 05:33–06:45 UTC, from the frozen instrument; `runs/AUTORUN_LOG.md`) | E1 Opus 64: 0 READ, 0 FAB, 64/64 HONEST in all four cells · E5 Haiku 96: R0×T0 0/16 (1 FAB), R0×T2 0/16, R2×T0 0/16, R2×T1 0/16, **R2×T2 10/16**, **R2×T4 14/16** (T1 vs T2 +0.62, exact p = 0.002) · E5 Sonnet 32: 0/32 · E2 48: `peer_violation` 8/8 under violating notes, 0/16 otherwise; the lexical MENTION proxy 8/8 without the tool (positive in neutral cells too; content audit 8/8) · E3 80: blocked chains write at generation 1 7/8 vs solvable 2/8, LOC_MENTION 0/19, forbidden READ 0/80 · D4 seeded Haiku chains, wave 1 (16): S1 1/8 READ (seed read first) vs S0 0/8 → continuation rule STOP, waves 2–5 not run · E4 360 calls: 0/360, curves flat · E4 on Haiku (D6, exploratory, 360 calls): without pressure [B] throughout (1/180); under pressure the declaration follows the majority in the blocked task (0/10 → 4/10, β ≈ 0.8; post-hoc answer-line reading, `analysis/e4_answerline.py`) · Haiku fixture overlap: 8 of 16 main blocks reuse pilot fixtures (DEVIATIONS, Correction of 12 September; disclosed in the group paper) |
| *Peer pressure without peers* (Track 5 project; report released with the instrument, not submitted; text by Frank, built on the team's design work) | on the sprint's template: abstract, §1–6 (introduction with contributions, related work, methods, results with Table 1 and the fixture-overlap disclosure, discussion and limitations, conclusion), code and data, author contributions, numbered references + Appendices A–F (A = Limitations and Dual-Use Considerations; D = full tables and quotations; F = artefacts and Codex's independent re-analysis) + LLM usage statement |
| *Two checks a lab can run tomorrow* (Track 2, Frank) | on the sprint's template: §1–6 + Appendices A–D (A = Limitations and Dual-Use Considerations; C = gate results and full tables; D = artefacts and Codex's re-analysis) |

## Layout
| path | what |
|---|---|
| `README_FOR_CLAUDE.md` | orientation: question, instrument, gate and pilots, the main runs of 11 September, where things are, rules |
| `SOURCES.md` | all URLs used |
| `amendment/AMENDMENT_r3.md` | the pre-registration |
| `harness-r3/` | instrument, runbook, deviation log, freeze manifest, `runs/` (gate, pilots, open-weights pilot, and the main runs `e1-main`, `e5-haiku`, `e5-sonnet`, `e2-main`, `e3-main`, `d4-haiku`, `e4`, `e4-haiku`; `AUTORUN_LOG.md`), tests |
| `analysis/` | harness-independent analysis with tests; `RESULTS_BLOCKS.md` (the papers' result blocks assembled from `results.md`) |
| `review/codex_2026-09-12/` | Codex's read-only verification script and its evidence (12 September) |
| `fixtures/` | note templates and prompt variants as text |
| `open_tier/` | Hugging Face Jobs backend and built job scripts (exploratory, shelved) |
| `papers/` | `peer-pressure-without-peers.md` (report, not submitted) and `two-checks-a-lab-can-run-tomorrow.md` (Frank's Track 2 submission); `build_apart.py` + `apart_template.tex` build the PDFs on the sprint's template; figures under `papers/figures/` |
| `MANIFEST.sha256.txt` | SHA-256 of every file in this package |

## Rules that bind everyone
No edit to a file listed in `MANIFEST.sha256.v6.json` without a new entry in `harness-r3/DEVIATIONS.md`; no episode is ever rerun or edited; pilots and gate cells are never pooled with main estimates; r1/r2 numbers are not r3 results; the open tier is never pooled with the Claude tiers.

— Claude (for Frank), 12 September 2026
