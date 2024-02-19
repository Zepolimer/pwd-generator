import string
import random
from functools import reduce


class Pwd:
    LOWER_CASES = string.ascii_lowercase
    UPPER_CASES = string.ascii_uppercase
    LETTERS = string.ascii_letters
    DIGITS = string.digits
    SPECIALS = string.punctuation

    def __init__(self):
        self.value = None
        self.choices = []

    def _set(self, length=None):
        if length is not None and length <= 0:
            raise ValueError('Password length cannot be less than or equal to 0')
        if len(self.choices) == 0:
            raise ValueError('You must select at least one parameter if you wish to generate a password')

        self.value = ''.join(
            random.choices(
                reduce(lambda x, y: x + y, self.choices),
                k=length or 10
            )
        )
        return self


class LowerCasesPassword(Pwd):
    def __init__(self):
        super().__init__()

    def generate(self, length=None):
        """
        Generate a password containing only lower-case letters
            :param int length: optional parameter (10 by default)
        """

        self.choices = [self.LOWER_CASES]
        return self._set(length=length)


class UpperCasesPassword(Pwd):
    def __init__(self):
        super().__init__()

    def generate(self, length=None):
        """
        Generate a password containing only upper-case letters
            :param int length: optional parameter (10 by default)
        """

        self.choices = [self.UPPER_CASES]
        return self._set(length=length)


class LettersPassword(Pwd):
    def __init__(self):
        super().__init__()

    def generate(self, length=None):
        """
        Generate a letter-only password
            :param int length: optional parameter (10 by default)
        """

        self.choices = [self.LETTERS]
        return self._set(length=length)


class DigitsPassword(Pwd):
    def __init__(self):
        super().__init__()

    def generate(self, length=None):
        """
        Generate a number-only password
            :param int length: optional parameter (10 by default)
        """

        self.choices = [self.DIGITS]
        return self._set(length=length)


class SpecialsPassword(Pwd):
    def __init__(self):
        super().__init__()

    def generate(self, length=None):
        """
        Generate a password containing only special characters
            :param int length: optional parameter (10 by default)
        """

        self.choices = [self.SPECIALS]
        return self._set(length=length)


class Password(Pwd):
    def __init__(self):
        super().__init__()

    def generate(
            self,
            length=None,
            lower_cases=True,
            upper_cases=True,
            digits=True,
            specials=True
    ):
        """
        Generate a password containing only special characters
            :param int length: optional parameter (10 by default)
            :param bool lower_cases: optional parameter (True by default)
            :param bool upper_cases: optional parameter (True by default)
            :param bool digits: optional parameter (True by default)
            :param bool specials: optional parameter (True by default)
        """

        self.choices = [
            self.LOWER_CASES,
            self.UPPER_CASES,
            self.DIGITS,
            self.SPECIALS
        ]

        if not lower_cases:
            self.choices.remove(self.LOWER_CASES)
        if not upper_cases:
            self.choices.remove(self.UPPER_CASES)
        if not digits:
            self.choices.remove(self.DIGITS)
        if not specials:
            self.choices.remove(self.SPECIALS)

        return self._set(length=length)
