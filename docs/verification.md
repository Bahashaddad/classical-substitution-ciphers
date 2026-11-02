# Verification — 2026-11-02

**Status: tested educational code candidate, subject to final owner review.**

- Five unittest methods passed, covering a known mapping example, ASCII compatibility with the original modified algorithm across 99 lengths, round trips including empty/odd/Unicode input, invalid keys, and overlapping n-grams.
- Both notebook code cells ran successfully without retaining outputs. Notebook UI rendering was not inspected in Jupyter.
- Python source and notebook code cells parsed successfully.
- Runtime uses only the standard library; no runtime dependency vulnerability scan is applicable.

Remaining: optional Jupyter frontend review. Neither cipher is suitable for real confidentiality; there is no security proof or modern cryptographic claim.

## Common publication checks and limits

- Original inputs were accessed read-only and all seven original SHA-256 hashes were rechecked unchanged.
- Prepared files were compared against 69 sensitive values from original environment/database material and nine identifier-shaped values from original reports, without printing those values. No matches remained in the public candidates.
- No original private keys, `.env`, runtime databases/logs, executable tools, raw PDFs, or original XLSX files are included.
- The publication guard passed against Git-tracked snapshots of all seven candidates. It is a limited guard, not a complete commercial secret scanner or proof of absence.
- No Git history was supplied or imported. Existing repositories/history must be reviewed separately if these files are added to them.
- No GitHub repository, hosted Actions run, release, CV change, or LinkedIn update was published.
- Contributor publication agreement was confirmed by the owner. Third-party data/service/source rights remain separate.
- Inspection used source/static review, report text extraction, report previews where available, workbook cell/object inventory, and targeted execution of the prepared copies. Original compiled Python was not decompiled, `mkcert.exe` was not executed or reverse engineered, and screenshots/embedded objects were not all individually cleared. Exclusion of originals is deliberate; no claim of exhaustive visual clearance is made.
