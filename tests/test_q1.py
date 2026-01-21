"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome
def test_simple_palindrome():
    assert is_palindrome("racecar") is True


def test_simple_non_palindrome():
    assert is_palindrome("hello") is False


def test_case_insensitive():
    assert is_palindrome("RaceCar") is True


def test_with_spaces():
    assert is_palindrome("nurses run") is True


def test_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama!") is True


def test_numbers():
    assert is_palindrome("12321") is True


def test_mixed_alphanumeric():
    assert is_palindrome("1a2b2a1") is True


def test_empty_string():
    assert is_palindrome("") is True


def test_only_non_alphanumeric():
    assert is_palindrome("!!!") is True


def test_single_character():
    assert is_palindrome("x") is True
