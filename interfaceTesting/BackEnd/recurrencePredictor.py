#!/usr/bin/python

from main import Main
from artificial import gameStates
import copy

class compHandler(object):
	"""docstring for compHandler"""
	def __init__(self):
		self.best_score=0;
		
	def getPossibleMovesAI(self,originalBoard,player,depth,boards,alpha_beta_board,nextPlay,scores):
		if (originalBoard.test.comp.getState()+originalBoard.test.human.getState()) in boards:
			# print '^^^^^^^^^^^^^^^^^^^^';
			# print ' possible recurence'
			# print '^^^^^^^^^^^^^^^^^^^^^';
			originalBoard.test.gameOverRecurse();
			self.best_score= min((originalBoard.test.comp.getWinnings()-originalBoard.test.human.getWinnings()),self.best_score);
			return
			

		elif (originalBoard.test.isgameOver() == 'true') | (depth==5):
			# if (depth==20):
			# 	print '***************************************************************';
			# 	print 'DEPTH IS ',depth, 'ALREADY, THERE EXIST A RECURRENCE LIKELYHOOD';
			# 	print '***************************************************************';
			# 	originalBoard.test.gameOver();
			# 	print '**********************************************************';
			# print 'returning';

			self.best_score= originalBoard.test.comp.getWinnings()-originalBoard.test.human.getWinnings();
			# print 'best_score is ',self.best_score;
			return;


		boards=boards+[(originalBoard.test.comp.getState()+originalBoard.test.human.getState())];
		alpha_beta_board=alpha_beta_board+[copy.deepcopy(originalBoard)];
		previousBoard=copy.deepcopy(originalBoard);	
		previousdepth=copy.deepcopy(depth);

		if player==originalBoard.ai:
			for i in range(0,len(originalBoard.test.human.getState())):
				
				# print 'computer played', i+1;
				
				# if (self.best_score > self.previousScore):
					# continue;

				if (originalBoard.ai.playPos(i+1)==-1):
					# print 'cant play hole ', i+1;
					nextPlay[i]=-200;
					continue;
				else:
					player=originalBoard.human;
					
				depth=depth+1;
				
				self.getPossibleMovesAI(originalBoard,player,depth,boards,alpha_beta_board,nextPlay,scores);
				if depth == 1:	
					nextPlay[i]=self.best_score;
					# print ' game moves are: ', nextPlay;
					# print 'the play recorded is ',nextPlay;
				originalBoard=copy.deepcopy(previousBoard);
				# print 'the board at depth 1 is ', originalBoard.test.printGameState();
				self.best_score=max(originalBoard.test.getAlpha(),self.best_score);
				originalBoard.test.setAlpha(self.best_score);
				# print 'the score after min is ', self.best_score;
				depth=copy.deepcopy(previousdepth);
				# print ' ',originalBoard.test.getAlpha(),'',alpha_beta_board[len(alpha_beta_board)-2].test.getBeta();
				if len(alpha_beta_board)>1:
					if(originalBoard.test.getAlpha() >= alpha_beta_board[len(alpha_beta_board)-2].test.getBeta()):
						# print 'alpha score of ',originalBoard.test.getAlpha(), ' is large than beta score of ',(alpha_beta_board[len(alpha_beta_board)-1]).test.getBeta(), 'therefore returning';
						return;
				

		else:
			for j in range(0,len(originalBoard.test.human.getState())):

				# print 'player placyed ', j+1;
				

				if (originalBoard.human.playPos(j+1) == -1):
					# print 'cant play hole ', j+1;
					continue;
				
				else:
					player=originalBoard.ai;
				depth=depth+1;
				self.getPossibleMovesAI(originalBoard,player,depth,boards,alpha_beta_board,nextPlay,scores);
				originalBoard=copy.deepcopy(previousBoard);

				self.best_score=min(originalBoard.test.getBeta(),self.best_score);
				originalBoard.test.setBeta(self.best_score);
				# print 'the board at depth 1 is ', originalBoard.test.printGameState();
				# print 'the score after max is ', self.best_score;
				depth=copy.deepcopy(previousdepth);
				# print 'boards at minimizing player is', boards;
				# print ' ',originalBoard.test.getBeta(),'',alpha_beta_board[len(alpha_beta_board)-2].test.getAlpha();
				if len(alpha_beta_board) > 1:
					if(originalBoard.test.getBeta() <= (alpha_beta_board[len(alpha_beta_board)-2]).test.getAlpha()):
						# print 'beta score of ',originalBoard.test.getBeta(), ' is less than alpha score of ',(alpha_beta_board[len(alpha_beta_board)-1]).test.getAlpha(), 'therefore returning';
						return;

		# print ' game moves are: ', nextPlay;
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
		
		if int (first) == 1:
			
			return self.getPossibleMovesAI(AImoves,AImoves.ai,depth,boards,alpha_beta_board,nextPlay,scores);
			
		else:
			
			return self.getPossibleMovesAI(AImoves,AImoves.human,depth,boards,alpha_beta_board,nextPlay,scores);
			