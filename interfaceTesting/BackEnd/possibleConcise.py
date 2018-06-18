#!/usr/bin/python

from main import Main
from artificial import gameStates
import copy

def getPossibleMovesAI(originalBoard,recursionCounter,player):
	#check for recursion
	# recursionCounter=checkRecursion(originalBoard,recursionCounter);
	# if recursionCounter == -2:
	# 	print 'recursive state is', recursionCounter;
	# 	originalBoard.test.printGameState();
	# 	originalBoard.test.recursionEndingWinnigs();

	if originalBoard.test.isgameOver() == 'true':
		print 'returning';
		# print 'previous board is ', previousBoard.test.printGameState();
		return;

	else:
		#make a copy of the previous board in order to reuse it
		previousBoard=copy.deepcopy(originalBoard);	
		# print 'previous board', previousBoard.test.printGameState();		
	
		if player==originalBoard.ai:
			for i in range(0,len(originalBoard.test.human.getState())):
				print 'computer played', i+1;
				if (originalBoard.ai.playPos(i+1) == -1):
					print 'cant play hole ', i+1;
					continue;
				else:
					player=originalBoard.human;
			
				getPossibleMovesAI(originalBoard,recursionCounter,player);
				originalBoard=previousBoard;
				# print 'current board is';
				originalBoard.test.printGameState();
		else:
			for i in range(0,len(originalBoard.test.human.getState())):
				print 'player played ', i+1;
				if (originalBoard.human.playPos(i+1) == -1):
					print 'cant play hole ', i+1;
					continue;
				else:
					player=originalBoard.ai;
			
				getPossibleMovesAI(originalBoard,recursionCounter,player);
				originalBoard=previousBoard;
				# print 'current board is';
				originalBoard.test.printGameState();
		# print 'current board is';
		# originalBoard.test.printGameState();

# def checkRecursion(Board,recursionCounter):
# 	if (AImovesClone.test.getPlayerState() == Board.test.getPlayerState()) & (AImovesClone.test.getCompState()==Board.test.getCompState()):
# 		recursionCounter=recursionCounter+1;
# 		print 'found a recursionCounter', recursionCounter;
# 		if recursionCounter >= 2:
# 			return -2;
# 		else:
# 			return recursionCounter;
# 	else:
# 		return recursionCounter;


first=raw_input('\n computer is player 1 or 2:   ');

test = Main(1,int (first), (2-int (first)+1));
recursionCounter=0; #to keep of recursion, a score of 10 means recursion.
print 'Now starting AI';

test.printGameState();
AImoves = gameStates(test);
AImovesClone=copy.deepcopy(AImoves);
if int (first) == 1:
	getPossibleMovesAI(AImoves,recursionCounter,AImoves.ai);
else:
	getPossibleMovesAI(AImoves,recursionCounter,AImoves.human);
print 'done';
