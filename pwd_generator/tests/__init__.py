import unittest

from pwd_generator import (
    LowerCasesPassword,
    UpperCasesPassword,
    LettersPassword,
    DigitsPassword,
    SpecialsPassword,
    Password
)


class GeneratePasswordTestCase(unittest.TestCase):
    def test_generate_lower_cases_password(self):
        password = LowerCasesPassword()

        password.generate()
        self.assertEqual(len(password.value), 10)

        password.generate(length=20)
        self.assertEqual(len(password.value), 20)
        self.assertEqual(password.value.islower(), True)

    def test_generate_upper_cases_password(self):
        password = UpperCasesPassword()

        password.generate()
        self.assertEqual(len(password.value), 10)

        password.generate(length=12)
        self.assertEqual(len(password.value), 12)
        self.assertEqual(password.value.isupper(), True)

    def test_generate_letters_password(self):
        password = LettersPassword()

        password.generate()
        self.assertEqual(len(password.value), 10)

        password.generate(length=15)
        self.assertEqual(len(password.value), 15)

    def test_generate_digits_password(self):
        password = DigitsPassword()

        password.generate()
        self.assertEqual(len(password.value), 10)

        password.generate(length=17)
        self.assertEqual(len(password.value), 17)
        self.assertEqual(password.value.isnumeric(), True)

    def test_generate_specials_password(self):
        password = SpecialsPassword()

        password.generate()
        self.assertEqual(len(password.value), 10)

        password.generate(length=19)
        self.assertEqual(len(password.value), 19)

    def test_generate_custom_password(self):
        password = Password()

        password.generate()
        self.assertEqual(len(password.value), 10)

        password.generate(
            length=20,
            specials=False,
            digits=True,
            lower_cases=False
        )
        self.assertEqual(len(password.value), 20)
