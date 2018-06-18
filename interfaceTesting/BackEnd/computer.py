#!/usr/bin/python

class computer:
	state=[];
	winnings=0;
	playerWinnings=0;
	position=0;
	seeds=0;
	playing='false';
	'Player class for the computer'
	
	def __init__(self,state,player):
		self.state=state;
		self.player=player;

	def getState(self):
		return self.state;

	def isPlaying(self,value):
		self.playing = value;

	def updateState(self, positions):
		# print 'updating computer';
		"""used for updating seeds from own's play"""
		self.seeds = self.state[positions]; #get current seed number in borad position
		if self.seeds > 0: #check to make sure that the hole isn't empty
			self.position = positions; #update the position in order to skip for reference
			self.state[positions]=0;
			for number in range(1,self.position+1):
				if self.seeds==0:
					break;
				self.state[self.position-number]=self.state[self.position-number]+1;
				self.seeds=self.seeds-1;
			return self.seeds;
		else:
			return -1;

	def updateExtraState(self,seed):
		self.seeds=seed;
		
		length=len(self.state);
		while length > 0:
			length=length-1;
			if length==self.position:
				if self.playing=='true':
					continue;
			self.seeds=self.seeds-1;
			self.state[length]=self.state[length]+1;
			if self.seeds == 0:
				break;
		#get the player wining if current player is not player
		if self.seeds == 0:
			if self.playing=='false':
				self.setPlayerWinnings(length);

		return self.seeds;

	#for setting the winnings of the opponent
	def setPlayerWinnings(self, hole):
		#clear winnigs
		self.playerWinnings=0;
		#check from the current ending hole to last hole for player 1
		for i in range(hole,len(self.state)):
			# print 'checking player wins'
			if (self.state[i] <= 4) & (self.state[i] >= 2):
				# print 'player won seed';
				#update the player winings by one as long as the value of hole is less than 4
				self.playerWinnings=self.playerWinnings+self.state[i];
				self.state[i]=0;
			else:
				break;


	#for getting the other players winning
	def getPlayerWinnings(self):
		# print 'sending winnigs'
		retValue=self.playerWinnings; #so i can clear temp winnings
		self.playerWinnings=0;
		return retValue;

	#setting personal winnigs
	def setWinnings(self, winnings):
		self.winnings=self.winnings+winnings;
		# print  self.winnings;

	def getWinnings(self):
		return self.winnings;
