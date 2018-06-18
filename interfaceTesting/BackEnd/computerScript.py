#!/usr/bin/python
import copy

class computerScript(object):		

	def __init__(self, instance):
		self.test = instance;
	def play(self):
		position = raw_input('\nWhat play is computer making ');
		result = self.test.computerPlay(position);
		if result == -1:
			self.play();

	def playPos(self,position):
		# position = raw_input('\nWhat play is computer making ');
		result = self.test.computerPlay(position);
		if result == -1:
			return -1;

	def playPosai(self,position):
		print 'about to play on board', self.test.printGameState();
		self.test.computerPlay(position);
		print 'done playing now board is ', self.test.printGameState();
		return self.test;

	def updateBoard(self, board):
		self.test=copy.deepcopy(board);


		