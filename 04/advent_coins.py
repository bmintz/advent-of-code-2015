#!/usr/bin/env python3
# encoding: utf-8

from hashlib import md5
import itertools
import sys


def to_bytes(str):
	return str.encode('utf-8')


def mine(sekrit_key, difficulty):
	sekrit_key = to_bytes(sekrit_key)
	for nonce in itertools.count():
		nonce = to_bytes(str(nonce))
		if md5(sekrit_key + nonce).hexdigest().startswith('0'*difficulty):
			return nonce.decode('utf-8')


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	if mode == '1':
		difficulty = 5
	elif mode == '2':
		difficulty = 6
	print(mine('ckczppom', difficulty))


if __name__ == '__main__':
	main()