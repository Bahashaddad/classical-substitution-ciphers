import unittest
import random
import string
from ciphers import transform, DEMO_KEY, analyze_text


class CipherTests(unittest.TestCase):
    def test_reference_example(self):
        self.assertEqual(transform("abc XYZ!"), "ihv syr!")

    def test_roundtrip_boundaries(self):
        for modified in [False, True]:
            for text in [
                "",
                "A",
                "Ab",
                "Abc",
                "abcde",
                "Unicode café العربية 123!",
                "a b\nc",
            ]:
                with self.subTest(modified=modified, text=text):
                    self.assertEqual(
                        transform(
                            transform(text, modified=modified),
                            decrypt=True,
                            modified=modified,
                        ),
                        text.lower(),
                    )

    def test_matches_original_ascii_algorithm(self):
        rng = random.Random(23)
        for length in range(1, 100):
            text = "".join(
                rng.choice(string.ascii_lowercase + " !123") for _ in range(length)
            )
            active = list(DEMO_KEY)
            output = ""
            for count, char in enumerate(text, 1):
                output += active[ord(char) - 97] if char.isalpha() else char
                if count == len(text) // 2:
                    active = active[::-1]
            expected = "".join(
                output[i : i + 2][::-1] for i in range(0, len(output), 2)
            )
            self.assertEqual(transform(text, modified=True), expected)

    def test_invalid_keys(self):
        for key in ["", "a" * 26, string.ascii_uppercase]:
            with self.assertRaises(ValueError):
                transform("abc", key)

    def test_overlapping_ngrams(self):
        self.assertEqual(analyze_text("aaaa")[2]["aa"], 3)


if __name__ == "__main__":
    unittest.main()
