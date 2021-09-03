#!/usr/bin/env python3
from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        case = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(case), expected)

    def test_double_name(self):
        case = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(case), expected)

    def test_type_error(self):
        self.assertRaises(AssertionError, rearrange_name, 123)

    def test_pattern_error(self):
        self.assertRaises(AssertionError, rearrange_name, 'No comma')


unittest.main()
