# Portfolio review: Classical Substitution Ciphers

Prepared 2026-11-02. Original input: `Traditional MonoAlphaBetic.zip`. The owner approved separate copies and improvements, and confirmed contributor publication agreement. Originals remain unchanged. Phase 4 approval is recorded; Phase 5 changes are in this copy. Phase 6 is bounded by the checks and remaining gates below.

## 1. Actual purpose

Traditional substitution and a modified mapping that reverses halfway through the message and swaps adjacent pairs; notebooks also calculate overlapping digrams and trigrams.

## 2. Quality and public suitability

The exercise is small and appropriate for a fundamentals repository. Original notebooks shared output filenames, mixed definitions/execution, lacked validation, and treated Unicode isalpha() as ASCII indexing. The copy shares a tested CLI/library, retains two clean notebooks, and uses synthetic text.

## 3. Security and evidence concerns

Severity is a qualitative project-context assessment, not a CVSS calculation. Confirmed source behavior is distinguished from unavailable evidence and potential privacy risks.

| Severity | Affected original file/area | Problem and impact | Remediation/status | Before publication? |
|---|---|---|---|---|
| High if used for security | Notebooks/report | Classical ciphers and deterministic modification do not provide modern confidentiality. | Explicit educational-only boundary; remove unsupported stronger-security claims. | Yes; documented |
| Medium | Notebook encrypt/decrypt functions | Unicode alphabetic characters caused invalid mapping/index operations; malformed keys not validated. | Restrict substitution to ASCII a-z; validate a 26-character permutation; preserve other normalized characters. | Yes; fixed and tested |
| Medium | Both notebooks; encrypted.txt/decrypted.txt | Shared generated filenames overwrite results; outputs may retain source text or local paths. | No stored outputs; new synthetic sample; CLI refuses existing destinations. | Yes; fixed |
| Privacy/rights | Cryptography Project.pdf; plaintext.txt | Cover identifier and uncertain provenance of original sample/report material. | Keep original PDF and text outside public edition; new examples and prose. | Yes; excluded |

## 4. File-by-file disposition

See `docs/file-classification.csv` for every original archive entry/file and its KEEP/MODIFY/REMOVE/PRIVATE/OPTIONAL disposition. Originals containing sensitive material are not placed in the upload copy. New files are additions, not original coursework artifacts.

## 5. Complete resulting tree

The full tree is recorded in `docs/directory-tree.txt`. Runtime/cache files are excluded.

## 6. README assessment and complete replacement

No README was supplied. The complete new README explains algorithm behavior, lowercase normalization, CLI/notebook use, non-overwriting outputs, and why neither algorithm is suitable for sensitive data.

The complete improved README is the repository's root `README.md`, rather than a second divergent copy pasted into this report.

## 7. Specific improvements and corrected code

The files in this prepared copy are the exact replacements/additions. `CHANGELOG.md` identifies behavior changes. Source PDFs, runtime data, and credential files were not rewritten in place. Do not interpret new tests or editorial additions as work performed during the original course.

## 8. Before-publication checklist

- [x] Separate copy created; original preserved.
- [x] Public README and clean directory structure provided.
- [x] Runtime data, keys, original identifiers, and unsafe original screenshots excluded.
- [x] MIT license and third-party notice supplied following contributor agreement.
- [ ] Review attribution and explain later AI-assisted improvements if discussing the project.
- [ ] Optional: run notebooks in your preferred Jupyter frontend; their code cells were checked separately.

Review `docs/verification.md` for exact executed checks and remaining limits. Hosted Actions results and manual review must not be reported as completed merely because a workflow exists.

## 9. Skills and CV wording

Python functions, reversible transformations, input validation, frequency-analysis basics, notebooks, boundary tests. No modern cipher design or cryptographic security proof.

Suggested wording: “Implemented and tested traditional and modified substitution-cipher exercises, with reproducible n-gram analysis and clear limitations for real-world confidentiality.”

## 10. Honest original score

| Dimension | Original score / 10 |
|---|---|
| Code quality | 4 |
| Security | 3 |
| Documentation | 4 |
| Organization | 4 |
| Professional presentation | 3 |
| Portfolio value | 6 |

**4.0/10 original**. Scores assess supplied evidence, not personal ability. Documentation-only artifacts are not assigned invented code/security scores. Improvements do not establish a certified security posture or guarantee a hiring outcome.

## Repository metadata

- Name: `classical-substitution-ciphers`
- Description: Educational substitution-cipher exercises with validated keys, reproducible n-gram analysis, and behavior tests.
- Topics: python, cryptography, classical-ciphers, substitution-cipher, frequency-analysis, jupyter-notebook
- Release: consider `v0.1.0` after the remaining verification and rights gates pass. Documentation/data corrections should have a changelog entry and updated version; do not retag a changed release.
- Screenshots: optional, synthetic and sanitized only. No original screenshots are cleared for public reuse.
- License: MIT for original code/documentation; third-party rights remain separate. Underlying data provenance may impose additional limits.
