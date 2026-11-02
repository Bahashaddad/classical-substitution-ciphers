# Classical Substitution Ciphers

A Python learning exercise comparing a fixed monoalphabetic substitution with a reversible variant that changes its mapping halfway through the message and swaps adjacent character pairs.

**Neither algorithm provides modern confidentiality.** The demonstration key is public, and the modified variant must not be described as proven secure or resistant to cryptanalysis.

## Objectives and features

Explore substitution mappings, reversible transformations, overlapping digram/trigram counts, input validation, and reproducible tests. The original notebooks' ASCII transformation is preserved for the supplied demonstration key. Input is normalized to lowercase; non-ASCII characters are preserved after that normalization instead of being misclassified as ASCII indices.

## Layout and tools

`ciphers.py` contains the shared standard-library implementation and CLI. `examples/plaintext.txt` is newly written synthetic text. `notebooks/` contains output-free traditional and modified demonstrations. `tests/` covers boundary cases and compares the modified algorithm against the original ASCII behavior. Python 3.12 was used; no runtime packages are required. A Jupyter-compatible notebook frontend is optional and is not required for the CLI.

## Usage

```sh
python ciphers.py encrypt examples/plaintext.txt --output generated/traditional.txt
python ciphers.py encrypt examples/plaintext.txt --modified --output generated/modified.txt
python ciphers.py decrypt generated/modified.txt --modified --output generated/recovered.txt
python ciphers.py analyze generated/modified.txt
python -m unittest discover -s tests -v
```

Choose new output filenames on subsequent runs: the CLI refuses to overwrite existing files. `--key` accepts a permutation of the 26 lowercase ASCII letters. The default is a public classroom mapping, not a secret. Notebook imports work from the repository root or its `notebooks/` directory.

## Security and limitations

Lowercasing loses original capitalization. Non-ASCII letters are not encrypted. Small deterministic modifications are not substitutes for authenticated modern encryption. No security claims are inferred from a different frequency distribution. The original report and potentially third-party sample text are excluded; algorithm descriptions and examples in this edition are new.

Future work could add controlled frequency-analysis comparisons and property-based tests. No cryptographic performance or resistance measurements are claimed.

## Authorship and license

Original academic author: Baha'a Aldeen Shaddad. Later code organization, tests, and synthetic examples are described in [NOTICE.md](NOTICE.md). Licensed under [MIT](LICENSE). Use only for education, not for protecting sensitive information.
