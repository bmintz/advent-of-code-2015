#!/usr/bin/env python3
# encoding: utf-8

import sys

from ben import input_iter

def has_repeated_letter(s):
	for i in range(len(s) - 1):
		if s[i] == s[i+1]:
			return True
	return False


def is_nice_one(string):
	return (
		sum([c in 'aeiou' for c in string]) >= 3
		and has_repeated_letter(string)
		and not any(s in string for s in ('ab', 'cd', 'pq', 'xy'))
	)


def answer(predicate):
	return sum(predicate(s) for s in input_iter())


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	if mode == '1':
		func = is_nice_one
	elif mode == '2':
		func = is_nice_two

	print(answer(func))


if __name__ == '__main__':
	main()