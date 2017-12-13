#!/usr/bin/env python3
# encoding: utf-8

import sys

def surface_area(*dimensions):
	l, w, h = dimensions
	sides = l*w, w*h, h*l
	area = min(sides) # slack
	for side in sides:
		area += 2*side
	return area


def ribbon(*dimensions):
	l, w, h = dimensions
	perimeters = [2*x for x in (l+w, w+h, h+l)]
	smallest_side = min(perimeters)
	return smallest_side + l*w*h


def xinput():
	while True:
		try:
			yield map(int, input().split('x'))
		except EOFError:
			return


def get_ans(func):
	total = 0
	for dimensions in xinput():
		total += func(*dimensions)
	return total


def main():
	import sys
	func = None
	if sys.argv[1] == '1':
		func = surface_area
	elif sys.argv[1] == '2':
		func = ribbon
	else:
		print('1 or 2 only', file=sys.stderr)
		sys.exit(1)
	print(get_ans(func))


if __name__ == '__main__':
	main()
