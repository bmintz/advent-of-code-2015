#!/usr/bin/env python3
# encoding: utf-8

import sys

from ben import input_iter


def has_repeated_letter(s, offset=1):
	for i in range(len(s) - offset):
		if s[i] == s[i+offset]:
			return True
	return False


def has_repeated_pair(s):
	for i in range(len(s) - 3):
		pair = s[i:i+2]
		if pair in s[i+2:]:
			return True
	return False


def is_nice_one(string):
	return (
		sum([c in 'aeiou' for c in string]) >= 3
		and has_repeated_letter(string)
		and not any(s in string for s in ('ab', 'cd', 'pq', 'xy'))
	)


def is_nice_two(string):
	return (
		has_repeated_letter(string, 2)
		and has_repeated_pair(string)
	)


def answer(predicate):
	return sum(predicate(s) for s in input_iter())


def err(*args):
	print(*args, file=sys.stderr)
	sys.exit(1)


def main():
	if len(sys.argv) == 1:
		err('Usage:', sys.argv[0], '<1|2> < input')

	mode = sys.argv[1]
	if mode not in '12':
		err('Invalid mode. 1 or 2 only.')

	predicate = is_nice_one if mode == '1' else is_nice_two

	print(answer(predicate))


if __name__ == '__main__':
	main()
