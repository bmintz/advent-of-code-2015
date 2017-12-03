#!/usr/bin/env python3
# encoding: utf-8

import sys

from ben import input_iter


def answer_one():
	...


def answer_two():
	...


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	if mode == '1':
		print(answer_one())
	elif mode == '2':
		print(answer_two())


if __name__ == '__main__':
	main()