#!/usr/bin/python

from player import player
from computer import computer
import sys
import copy


class Main:
	'Main class for the application'
	gameOverCheck='false';
	
	def __init__(self,difLevel,compStat,playerStat):
		self.difLevel=1;
		self.comp = computer([1,2,1,0,2,0],compStat);
		self.human = player([2,1,1,0,2,0],playerStat);
		self.alpha=-200;#for maximiser
		self.beta=200;#for minimizer

	"""Print out player 1 current game state"""
	def printPlayerState(self):
		print self.human.getState();

	"""Print out computer current game state"""
	def printComputerState(self):
		print self.comp.getState();
	#print both game status
	def printGameState(self):
		self.printComputerState();
		self.printPlayerState();

	#for returning current state of computer mainly for recursive purposes
	def getCompState(self):
		"""used for printing current game state"""
		return self.comp.getState();

	#for returning current state of player mainly for recursive purposes
	def getPlayerState(self):
		"""used for printing current game state"""
		return self.human.getState();

	#used if player just played it updates his game state
	def playerPlay(self, position):
		#check to make sure there are seeds to play
		self.comp.isPlaying('false');
		self.human.isPlaying('true');
		#check to see no disadvantage on player
		if(self.checkPlayerGameState()):
			self.playerStateEmpty();
			return;
		
		seeds=self.human.updateState(int (position)-1);
		if seeds > 0:
			self.computerExtraPlay(seeds);
		elif seeds == -1: #to know if player actually played a filled hole
			return -1;
		self.setPlayerWinnings();
		# self.printGameState();
		if(self.checkCompGameState()):
			self.compStateEmpty();
		return 0;
	#if there are cards left after computer plays
	def playerExtraPlay(self, seed):
		seeds = self.human.updateExtraState(seed);
		if seeds > 0:
			self.computerExtraPlay(seeds);

	#used when computer is to play
	def computerPlay(self,position):
		#check to make sure game isn't over
		self.comp.isPlaying('true');
		self.human.isPlaying('false');
		#make sure comp dont compute an ended game
		# if self.isgameOver()=='true':
		# 	return 0;
		#check to see no disadvantage on player
		if(self.checkCompGameState()):
			self.compStateEmpty();
			return;

		# self.checkTie();
		seeds = self.comp.updateState(int (position)-1);
		if seeds > 0:
			self.playerExtraPlay(seeds);
		elif seeds == -1:
			return -1; #to know if player actually played a filled hole
		self.setCompWinnings();
		# self.printGameState();
		if(self.checkPlayerGameState()):
			self.playerStateEmpty();
		return 0;
			
	#used to check if player is disadvantaged at the begining of the game
	def playerStateEmpty(self):
		# print 'Player state empty';
		self.human.setWinnings(200);
		self.gameOver();

	#used to check if computer is disadvantages at the begining of the game
	def compStateEmpty(self):
		# print 'computer state empty';
		self.comp.setWinnings(200);
		self.gameOver();

	#method to end a recursive game 
	def gameOverRecurse(self):
		self.human.setWinnings(sum(self.human.getState()));
		self.comp.setWinnings(sum(self.comp.getState()));
		self.gameOver();

	#called to add the current seeds in players hole in order to end their recursive game
	def recursionEndingWinnigs(self):
		self.human.setWinnings(sum(self.human.getState()));
		self.comp.setWinnings(sum(self.comp.getState()));
		self.gameEnd();

	#extra cards from the player for computer
	def computerExtraPlay(self, seed):
		seeds=self.comp.updateExtraState(seed);
		if seeds > 0:
			self.playerExtraPlay(seeds);
	#called after a play to set the computer winnigs in it variable
	def setCompWinnings(self):
		self.comp.setWinnings(self.human.getPlayerWinnings());

	#called after a play to set the player winnigs in it variable
	def setPlayerWinnings(self):
		self.human.setWinnings(self.comp.getPlayerWinnings());

	#Api to update winnings for com[puter]
	def setCompWinningsAPI(self,winn):
		self.comp.setWinnings(winn);

	#Api to set the winnings for player
	def setPlayerWinningsAPI(self,winn):
		self.human.setWinnings(winn);

	#called to check if player can still play if holes arent empty
	def checkPlayerGameState(self):
		return (sum(self.human.getState()) == 0);

	#called to check if computer can still play if holes arent empty
	def checkCompGameState(self):
		return (sum(self.comp.getState()) == 0);


	#checking for winners and ending game
	def gameOver(self):
		self.gameOverCheck='true';
	
	def removeGameOver(self):
		self.gameOverCheck='false';

	#for printing winners
	def gameOverGamePlay(self):
		if (self.comp.getWinnings() > self.human.getWinnings()):
			print '###########################';
			print 'The winner is computer';
			

		elif (self.comp.getWinnings() < self.human.getWinnings()):
			print '###########################';
			print 'The winner is player';
			

		else:
			print "It's a draw";

		print 'computer won: ';
		print self.comp.getWinnings();
		# self.comp.setWinnings(0);
		print '\n Player won: '
		print self.human.getWinnings();
		print '############################';


	#for depthgame over
	#checking for winners and ending game
	def gameOverDepth(self):
		# print 'checking for game over';
		if (self.comp.getWinnings() > self.human.getWinnings()):
			# print 'The winner is computer';
			pass;

		elif (self.comp.getWinnings() < self.human.getWinnings()):
			# print 'The winner is player';
			pass;

		else:
			pass
			# print "It's a draw";

		# print 'computer won: ';
		print self.comp.getWinnings();
		# self.comp.setWinnings(0);
		# print '\n Player won: '
		print self.human.getWinnings();
		# self.human.setWinnings(0);

	def println(self):
		print '\n';

	def isgameOver(self):
		return self.gameOverCheck;

	def getAlpha(self):
		return self.alpha;

	def setAlpha(self,alpha):
		self.alpha=alpha;

	def getBeta(self):
		return self.beta;

	def setBeta(self,beta):
		self.beta=beta;













