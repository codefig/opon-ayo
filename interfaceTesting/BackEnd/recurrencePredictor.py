#!/usr/bin/python

from main import Main
from artificial import gameStates
import copy

class compHandler(object):
	"""docstring for compHandler"""
	def __init__(self):
		self.best_score=0;
		self.counter=0;
		self.file = open("gametree4.txt","w");
		
	def getPossibleMovesAI(self,originalBoard,player,depth,boards,alpha_beta_board,nextPlay,scores):
		# self.file.write('***************************************************************\n');
		self.file.write('Current board is \n'+str(originalBoard.test.comp.getState())+'\n' + str(originalBoard.test.human.getState())+'\n');
		# holldd='Alpha beta values to pass down are '+str(originalBoard.test.getAlpha()) + ' ' + str(originalBoard.test.getBeta());
		# self.file.write(holldd+'\n');
		# self.file.write('***************************************************************\n');
		if (originalBoard.test.comp.getState()+originalBoard.test.human.getState()) in boards:
			self.counter +=1;
			# print '^^^^^^^^^^^^^^^^^^^^';
			# print ' possible recurence'
			# print '^^^^^^^^^^^^^^^^^^^^^';
			# if(self.counter>1):
			originalBoard.test.gameOverRecurse();
			self.best_score= self.best_score+(originalBoard.test.comp.getWinnings()-originalBoard.test.human.getWinnings());
			# print 'best_score is ',self.best_score;
			self.counter=0;
			return
			

		elif (originalBoard.test.isgameOver() == 'true') | (depth==7):
			self.best_score= self.best_score+originalBoard.test.comp.getWinnings()-originalBoard.test.human.getWinnings();
			holldd='player winnigs is '+str(self.best_score);
			self.file.write(holldd+'\n');
			holldd='Alpha beta values to pass down are '+str(originalBoard.test.getAlpha()) + ' ' + str(originalBoard.test.getBeta());
			self.file.write(holldd+'\n');
			if (depth==7):
				self.file.write('***************************************************************\n');
				self.file.write('Returning back to previos board since depth is now 8\n');
				self.file.write('***************************************************************\n');

				# originalBoard.test.gameOver();
				# print '**********************************************************';
			# print 'returning';
				# pass;

			# print 'best_score is ',self.best_score;
			return;
		

		boards=boards+[(originalBoard.test.comp.getState()+originalBoard.test.human.getState())];
		alpha_beta_board=alpha_beta_board+[copy.deepcopy(originalBoard)];
		previousBoard=copy.deepcopy(originalBoard);	
		previousdepth=copy.deepcopy(depth);

		if player==originalBoard.ai:
			

			# self.file.write(str(originalBoard.test.comp.getState())+'\n' + str(originalBoard.test.human.getState())+'\n');
			holldd='Player Winnings is '+str(self.best_score);
			self.file.write(holldd+'\n');
			holldd='Alpha beta values to pass down are '+str(originalBoard.test.getAlpha()) + ' ' + str(originalBoard.test.getBeta());
			self.file.write(holldd+'\n');
			for i in range(0,len(originalBoard.test.human.getState())):
				
				# print 'computer played hole ', i+1;
				
				# if (self.best_score > self.previousScore):
					# continue;

				if (originalBoard.ai.playPos(i+1)==-1):
					# print 'cant play hole because it is empty ', i+1;
					nextPlay[i]=-100000;
					continue;
				else:
					holldd='Computer PLAYING HOLE '+str(i+1);
					self.file.write(holldd+'\n');
					# self.file.write(str(originalBoard.test.comp.getState())+'\n' + str(originalBoard.test.human.getState())+'\n');
					player=originalBoard.human;
					
				depth=depth+1;
				
				self.getPossibleMovesAI(originalBoard,player,depth,boards,alpha_beta_board,nextPlay,scores);

				if depth == 1:	
					nextPlay[i]=self.best_score;
					# print ' game moves are: ', nextPlay;
					# print 'the play recorded is ',nextPlay;
				

				originalBoard=copy.deepcopy(previousBoard);
				self.file.write('Current board is \n'+str(originalBoard.test.comp.getState())+'\n' + str(originalBoard.test.human.getState())+'\n');
				# print 'the board at depth 1 is ', originalBoard.test.printGameState();
				holldd='Comparing Alpha value '+str(originalBoard.test.getAlpha()) +' to ' +str(self.best_score);
				self.file.write(holldd+'\n');
				self.best_score=max(originalBoard.test.getAlpha(),self.best_score);
				originalBoard.test.setAlpha(self.best_score);
				holldd='Updating Alpha values to '+str(originalBoard.test.getAlpha());
				self.file.write(holldd+'\n');
				# print 'the score after min is ', self.best_score;
				depth=copy.deepcopy(previousdepth);
				
				if len(alpha_beta_board)>1:
					holldd='Comparing Alpha value to Beta value ';
					self.file.write(holldd+'\n');
					if(originalBoard.test.getAlpha() >= alpha_beta_board[len(alpha_beta_board)-1].test.getBeta()):
						holldd='alpha score of '+str(originalBoard.test.getAlpha())+ ' is greater than beta score of '+str(alpha_beta_board[len(alpha_beta_board)-1].test.getBeta())+'therefore returning';
						self.file.write(holldd+'\n');
						return;
					else:
						holldd='alpha score of '+str(originalBoard.test.getAlpha())+ ' is lesser than beta score of '+str(alpha_beta_board[len(alpha_beta_board)-1].test.getBeta())+'therefore continuing';
						self.file.write(holldd+'\n');
				

		else:


			# self.file.write(str(originalBoard.test.comp.getState())+'\n' + str(originalBoard.test.human.getState())+'\n');
			holldd='Computer Winnings is '+str(self.best_score);
			self.file.write(holldd+'\n');
			holldd='Alpha beta values are '+str(originalBoard.test.getAlpha()) + ' ' + str(originalBoard.test.getBeta());
			self.file.write(holldd+'\n');
			for j in range(0,len(originalBoard.test.human.getState())):

				# print 'player played hole ', j+1;
				

				if (originalBoard.human.playPos(j+1) == -1):
					nextPlay[j]=-100000;
					
					# print 'cant play hole because it is empty ', j+1;
					continue;
				
				else:
					holldd='Player PLAYING HOLE '+str(j+1);
					self.file.write(holldd+'\n');
					# self.file.write(str(originalBoard.test.comp.getState())+'\n' + str(originalBoard.test.human.getState())+'\n');
					player=originalBoard.ai;
						
				depth=depth+1;
				
				self.getPossibleMovesAI(originalBoard,player,depth,boards,alpha_beta_board,nextPlay,scores);
				holldd='Comparing beta value '+str(originalBoard.test.getBeta()) +' to ' +str(self.best_score);
				self.best_score=min(originalBoard.test.getBeta(),self.best_score);
				originalBoard=copy.deepcopy(previousBoard);
				# originalBoard=copy.deepcopy(previousBoard);

				self.file.write(holldd+'\n');
				originalBoard.test.setBeta(self.best_score);
				holldd='Updating Beta values to '+str(originalBoard.test.getBeta());
				self.file.write(holldd+'\n');

				# print 'the board at depth 1 is ', originalBoard.test.printGameState();
				# print 'the score after max is ', self.best_score;
				depth=copy.deepcopy(previousdepth);
				self.file.write('Current board is \n'+str(originalBoard.test.comp.getState())+'\n' + str(originalBoard.test.human.getState())+'\n');
				# print 'boards at minimizing player is', boards;
				# print ' ',originalBoard.test.getBeta(),'',alpha_beta_board[len(alpha_beta_board)-2].test.getAlpha();
				if len(alpha_beta_board) > 1:
					holldd='Comparing Bata value to Alpha value ';
					self.file.write(holldd+'\n');
					if(originalBoard.test.getBeta() <= (alpha_beta_board[len(alpha_beta_board)-1]).test.getAlpha()):
						holldd= 'beta score of '+str(originalBoard.test.getBeta())+ ' is lesser than alpha score of '+str(alpha_beta_board[len(alpha_beta_board)-1].test.getAlpha())+'therefore returning';
						self.file.write(holldd+'\n');
						return;
					else:
						holldd='beta score of '+str(originalBoard.test.getBeta())+ ' is greater than alpha score of '+str(alpha_beta_board[len(alpha_beta_board)-1].test.getAlpha())+'therefore continuing';
						self.file.write(holldd+'\n');

		self.file.write('-----------------------------------------------------------------------------------'+'\n');
		self.file.write('End of reasoning, Current playmatrix is  '+str(self.best_score));
		self.file.write('\n-----------------------------------------------------------------------------------'+'\n');

		return nextPlay.index(max(nextPlay));

	def runMe(self,test1,first):
		self.best_score=0;
		depth=0;
		
		scores=0;
		
		test=copy.deepcopy(test1);
		AImoves = gameStates(test);
		boards=[];
		alpha_beta_board=[];
		nextPlay=[0]*len(test.getCompState());
		# self.file = open("gametree.txt","a");
		
		if int (first) == 1:
			
			return self.getPossibleMovesAI(AImoves,AImoves.ai,depth,boards,alpha_beta_board,nextPlay,scores);
			
		else:
			
			return self.getPossibleMovesAI(AImoves,AImoves.human,depth,boards,alpha_beta_board,nextPlay,scores);
			
