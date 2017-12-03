#!/usr/bin/env python3
# encoding: utf-8

def which_floor(parens):
	floor = 0
	for paren in parens:
		floor += delta(paren)
	return floor


def basement_index(parens):
	floor = 0
	# this problem is one-indexed
	for i, paren in enumerate(parens, 1):
		floor += delta(paren)
		if floor == -1:
			return i
	raise ValueError


def delta(paren):
	if paren == '(':
		return +1
	elif paren == ')':
		return -1
	else:
		print(paren)
		return 0


def main():
	import sys
	parens = input()
	if sys.argv[1] == '1':
		print(which_floor(parens))
	elif sys.argv[1] == '2':
		print(basement_index(parens))
	else:
		print('1 or 2 only', file=sys.stderr)
		sys.exit(1)


if __name__ == '__main__':
	main()
