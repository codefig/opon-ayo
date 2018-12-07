#!/usr/bin/python

class player:
	state=[];
	winnings=0;
	playerWinnings=0;
	seeds=0;
	position=0;
	playing='true';
	'Player class for the human player'
	def __init__(self,state,player):
		self.state=state;
		self.player=player;
		# self.playState=playState;

	def getState(self):
		"""used for printing current game state"""
		return self.state;

	def isPlaying(self, value):
		self.playing = value;

	def updateState(self, positions):
		# print 'updating player';
		"""used for updating seeds from own's play"""
		self.seeds = self.state[positions]; #get current seed number in borad position
		if self.seeds > 0: #check to make sure that the hole isn't empty
			self.position = positions; #update the position in order to skip for reference
			self.state[positions]=0;
			hole = positions+1;
			while (hole <= len(self.state)-1):
				if self.seeds==0:
					break;
				self.seeds=self.seeds-1;
				self.state[hole]=self.state[hole]+1;
				hole = hole+1;

			# print 'remaining seeds is', self.seeds;
			return self.seeds;
		else:
			return -1;

	def updateExtraState(self,seed):
		# print 'extra seed from computers';
		"""used for updating seeds left from computers play"""
		self.seeds = seed;

		for i in range(0,len(self.state)):
			if i==self.position:
				if self.playing=='true':
					continue;
			self.seeds=self.seeds-1;
			self.state[i]=self.state[i]+1;
			if self.seeds == 0:
				break;
		#get the player wining if current player is not player
		if self.seeds == 0:
			if self.playing=='false':
				self.setPlayerWinnings(i);
			
		return self.seeds;

	#for setting the winnings of the opponent
	def setPlayerWinnings(self, hole):
		# print hole;
		#clear out winnigs
		self.playerWinnings=0;
		#check from the current ending hole to last hole for player 1
		while(hole>=0):
			#check to see if end isn't past full
			if self.state[hole] > 3:
				break;
			# print 'collating winnings';
			# print 'checking computer wins';
			if (self.state[hole] < 4) & (self.state[hole] >= 2):
				# print 'computer won seed';
				#update the player winings by one as long as the value of hole is less than 4
				self.playerWinnings=self.playerWinnings+self.state[hole];
				self.state[hole] = 0;
				hole=hole-1;
			else:
				break;

	#for getting the other players winning
	def getPlayerWinnings(self):
		retValue=self.playerWinnings; #so i can clear temp winnings
		self.playerWinnings=0;
		return retValue;

	#setting personal winnigs
	def setWinnings(self, winnings):
		self.winnings=self.winnings+winnings;

	def getWinnings(self):
		return self.winnings;

		