#!/usr/bin/env python3
# encoding: utf-8

import nice_strings


def test_has_repeated_letter():
	for test_case in ('xx', 'abcdde', 'aabbccdd'):
		assert nice_strings.has_repeated_letter(test_case)

	assert not nice_strings.has_repeated_letter('jchzalrnumimnmhp')


def test_has_repeated_pair():
	for test_case in ('xyxy', 'aabcdefgaa'):
		assert nice_strings.has_repeated_pair(test_case)

	assert not nice_strings.has_repeated_pair('aaa')


def test_is_nice_one():
	for test_case in ('ugknbfddgicrmopn', 'aaa'):
		assert nice_strings.is_nice_one(test_case)

	for test_case in (
			'jchzalrnumimnmhp',
			'haegwjzuvuyypxyu',
			'dvszwmarrgswjxmb'):
		assert not nice_strings.is_nice_one(test_case)


def test_is_nice_two():
	for test_case in ('qjhvhtzxzqqjkmpb', 'xxyxx'):
		assert nice_strings.is_nice_two(test_case)

	for test_case in ('uurcxstgmygtbstg', 'ieodomkazucvgmuy'):
		assert not nice_strings.is_nice_two(test_case)
