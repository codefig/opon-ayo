from playerScript import playerScript
from computerScript import computerScript
from main import Main
from recurrencePredictor import compHandler
import copy

first=raw_input('\n computer is player 1 or 2:   ');

test = Main(1,int (first), (2-int (first)+1));

human = playerScript(test);
computer = computerScript(test);
# AImoves = gameStates(test);

def isgameOver():
	
	return test.isgameOver();

# test.printComputerState();
# test.printPlayerState();

# AImoves.getPossibleMoves(test);

test.printGameState();
ai=compHandler();

# test.println();
# test.printGameState();


if int (first)==1:
	while 1==1:
		# testClone=copy.deepcopy(test);
		if isgameOver() == 'false':
			# print isgameOver();
			position = ai.runMe(test,1);
			# print position+1;
			print '\nComputer plays hole ', position+1;
			computer.playPos(position+1);
			# computer.play();
			test.printGameState();
			# test.setCompWinnings();
		if isgameOver() =='false':
				# print 'player turn'
				human.play();
				print '\nPlayer plays hole ';
				test.printGameState();
		else:
			test.gameOverGamePlay();
			break;
		print 'computer has won so far: '
		print test.comp.getWinnings();
		print '\n player has won so far: '
		print test.human.getWinnings();
else:
	while 1==1:
		# testClone=copy.deepcopy(test);
		if isgameOver() =='false':
			# print 'player turn'
			human.play();
			print '\nPlayer plays hole ';
			test.printGameState();
		if isgameOver() == 'false':
			# print isgameOver();
			position = ai.runMe(test,1);
			# print position+1;
			# print 'current test is ', test.printGameState();
			print '\nComputer plays hole ', position+1;
			computer.playPos(position+1);
			# computer.play();
			test.printGameState();
			# test.setCompWinnings();
		else:
			test.gameOverGamePlay();
			break;
		print 'computer has won so far: '
		print test.comp.getWinnings();
		print '\n player has won so far: '
		print test.human.getWinnings();