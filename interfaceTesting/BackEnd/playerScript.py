#!/usr/bin/python
import copy

class playerScript(object):		

	def __init__(self, instance):
		self.test = instance;
	def play(self):
		position = raw_input('\nWhat play is player making ');
		result = self.test.playerPlay(position);
		if result == -1:
			return -1;

	def playPos(self,position):
		# position = raw_input('\nWhat play is player making ');
		result = self.test.playerPlay(position);
		if result==-1:
			return -1;

	def updateBoard(self,currentBoard):
		self.test=copy.deepcopy(currentBoard);