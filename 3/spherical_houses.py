#!/usr/bin/env python3
# encoding: utf-8

import sys

from ben import input_iter

class Santa:

	def __init__(self):
		self._visited_houses = set()
		self.x = 0
		self.y = 0
		self._give_gift()

	def move(self, direction):
		xs = {'<': -1, '>': +1}
		ys = {'v': -1, '^': +1}
		# get from ys if not in xs
		if direction in xs:
			self.x += xs[direction]
		elif direction in ys:
			self.y += ys[direction]
		else:
			raise ValueError

		self._give_gift()

	def _give_gift(self):
		self._visited_houses.add((self.x, self.y))

	@property
	def visited_houses(self):
		return len(self._visited_houses)


class RoboSantaPair:

	def __init__(self):
		self._santa = Santa()
		self._robo_santa = Santa()
		self.turn = 0

	def move(self, direction):
		if self.turn == 0:
			self._santa.move(direction)
			self.turn = 1
		else:
			self._robo_santa.move(direction)
			self.turn = 0

	@property
	def visited_houses(self):
		return len(
			self._santa._visited_houses
			| self._robo_santa._visited_houses
		)


def num_houses(directions, SantaType):
	sleigh = SantaType()
	for direction in directions:
		sleigh.move(direction)

	return sleigh.visited_houses


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	if mode == '1':
		SantaType = Santa
	elif mode == '2':
		SantaType = RoboSantaPair

	print(num_houses(input(), SantaType))


if __name__ == '__main__':
	main()
