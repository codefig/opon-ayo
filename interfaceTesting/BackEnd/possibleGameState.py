#!/usr/bin/python

from main import Main
from artificial import gameStates
import copy

# playing='ai';

def getPossibleMovesAI(originalBoard,recursionCounter):
	#check for recursion
	recursionCounter=checkRecursion(originalBoard,recursionCounter);
	if recursionCounter == -2:
		originalBoard.test.recursionEndingWinnigs();

	#make a copy of the previous board in order to reuse it
	previousBoard=copy.deepcopy(originalBoard);
	if originalBoard.test.isgameOver() == 'true':
		print 'returning';
		return previousBoard;

	else:
		for i in range(0,len(originalBoard.test.human.getState())):
			
			print 'computer played';
			print i;
			
			if (originalBoard.ai.playPos(i+1) == -1):
				print 'cant play hole ', i;
				continue;
		
			getPossibleMovesPlayer(originalBoard,recursionCounter);
			originalBoard=previousBoard;
			originalBoard.test.printGameState();
			


def  getPossibleMovesPlayer(originalBoard,recursionCounter):
	#check for recursion
	recursionCounter=checkRecursion(originalBoard,recursionCounter);
	if recursionCounter == -2:
		originalBoard.test.recursionEndingWinnigs();
		
	previousBoard=copy.deepcopy(originalBoard);
	#check if game is over before playing
	if originalBoard.test.isgameOver() == 'true':
		print 'returning';
		return previousBoard;
	else:
		for j in range(0,len(originalBoard.test.human.getState())):
			
			print 'player played';
			print j;
			# originalBoard.test.printGameState();
			if (originalBoard.human.playPos(j+1) == -1):
				print 'cant play hole', j;
				continue;
			
			getPossibleMovesAI(originalBoard,recursionCounter);
			originalBoard=previousBoard;
			originalBoard.test.printGameState();
			
def checkRecursion(Board,recursionCounter):
	if recursionCounter >= 10:
		return -2 #code for recursion, force a game over
	elif (AImovesClone.test.getPlayerState() == Board.test.getPlayerState()) & (AImovesClone.test.getCompState()==Board.test.getCompState()):
		print 'found a recursionCounter', recursionCounter;
		recursionCounter=recursionCounter+1;
		return recursionCounter;
	else:
		return recursionCounter;

first=raw_input('\n computer is player 1 or 2:   ');

test = Main(1,int (first), (2-int (first)+1));
recursionCounter=0; #to keep of recursion, a score of 10 means recursion.
print 'Now starting AI';

test.printGameState();
AImoves = gameStates(test);
AImovesClone=copy.deepcopy(AImoves);
if int (first) == 1:
	getPossibleMovesAI(AImoves,recursionCounter);
else:
	getPossibleMovesPlayer(AImoves,recursionCounter);
print 'done';

	