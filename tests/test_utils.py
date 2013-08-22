# -*- coding: utf8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import unittest

from nose import tools
from justext.paragraph import normalize_whitespace
from justext.core import is_blank


class TestUtils(unittest.TestCase):
    def test_empty_string_is_blank(self):
        tools.assert_true(is_blank(""))

    def test_string_with_space_is_blank(self):
        tools.assert_true(is_blank(" "))

    def test_string_with_nobreak_space_is_blank(self):
        tools.assert_true(is_blank("\u00A0\t "))

    def test_string_with_narrow_nobreak_space_is_blank(self):
        tools.assert_true(is_blank("\u202F \t"))

    def test_string_with_spaces_is_blank(self):
        tools.assert_true(is_blank("    "))

    def test_string_with_newline_is_blank(self):
        tools.assert_true(is_blank("\n"))

    def test_string_with_tab_is_blank(self):
        tools.assert_true(is_blank("\t"))

    def test_string_with_whitespace_is_blank(self):
        tools.assert_true(is_blank("\t\n "))

    def test_string_with_chars_is_not_blank(self):
        tools.assert_false(is_blank("  #  "))

    def test_normalize_no_change(self):
        string = "a b c d e f g h i j k l m n o p q r s ..."
        tools.assert_equal(string, normalize_whitespace(string))

    def test_normalize_dont_trim(self):
        string = "  a b c d e f g h i j k l m n o p q r s ...  "
        expected = " a b c d e f g h i j k l m n o p q r s ... "
        tools.assert_equal(expected, normalize_whitespace(string))

    def test_normalize_newline_and_tab(self):
        string = "123 \n456\t\n"
        expected = "123 456 "
        tools.assert_equal(expected, normalize_whitespace(string))

    def test_normalize_non_break_spaces(self):
        string = "\u00A0\t €\u202F \t"
        expected = " € "
        tools.assert_equal(expected, normalize_whitespace(string))
