#  --------------------------------------------------------------------------
#  Copyright (c) 2020, antuit.ai. All rights reserved.
#  Proprietary and confidential
#  Unauthorized copying of this file, via any medium, is strictly prohibited.
#  --------------------------------------------------------------------------

from unittest import TestCase

from tobacco import pipe


@pipe
def plus_one(a: int) -> int:
    return a + 1


@pipe
def minus_amount(b: int, amount: int = 2) -> int:
    return b - amount


@pipe
def plus_amount(c: int, amount: int = 5) -> int:
    return c + amount


@pipe
def bang_string(x: str) -> str:
    return x + "!"


@pipe
def strike_string(x: str) -> str:
    return f"~~{x}~~"


class TestPipe(TestCase):

    def test_single_pipe(self):
        res = 0 >> plus_one
        self.assertEqual(res, 1)

    def test_long_pipe(self):
        # 3 + 1 - 2 + 5 = 7
        res = 3 >> plus_one >> minus_amount >> plus_amount
        self.assertEqual(res, 7)

    def test_keywords(self):
        # 5 - 2 + 8 = 11
        res = 5 >> minus_amount(amount=2) >> plus_amount(amount=8)
        self.assertEqual(res, 11)

    def test_string_pipe(self):
        res = "foo" >> bang_string >> strike_string
        self.assertEqual(res, "~~foo!~~")

    def test_reverse_string_pipe(self):
        res = "foo" >> strike_string >> bang_string
        self.assertEqual(res, "~~foo~~!")
