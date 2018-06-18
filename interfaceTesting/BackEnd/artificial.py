#!/usr/bin/python

# from possibleGameState import gameStates
from main import Main
from computerScript import computerScript
from playerScript import playerScript

class gameStates(object):
	"""docstring for gameStates"""
	def __init__(self, test):
		self.test = test;
		self.human = playerScript(self.test);
		self.ai = computerScript(self.test);

	def getPlayer(self):
		if (self.who == 'ai'):
			# self.who == 'human';
			return self.ai;
		else:
			# self.who ='ai';
			return self.human;

	def switch(self):
		if self.who=='ai':
			self.who='human';
		else:
			self.who='ai';
	def getOriginalBoard(self):
		return self.test;

