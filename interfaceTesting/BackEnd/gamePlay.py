from playerScript import playerScript
from computerScript import computerScript
from main import Main
from recurrencePredictor import compHandler
import copy

class gamePlay(object):
	"""docstring for gamePlay"""
	def __init__(self):
		self.first=raw_input('\n computer is player 1 or 2:   ');
		self.test = Main(self.first,int (4), (2-int (self.first)+1));
		self.human = playerScript(self.test);	
		self.computer = computerScript(self.test);
		self.ai=compHandler();
# AImoves = gameStates(test);

	def isgameOver(self):
	
		return self.test.isgameOver();

	def whoPlay(self):
		return self.first;

# test.printComputerState();
# test.printPlayerState();

# AImoves.getPossibleMoves(test);

# test.printGameState();

# test.println();
# test.printGameState();


	def computerPlay(self):
			# testClone=copy.deepcopy(test);
		if self.isgameOver() == 'false':
			# print isgameOver();
			position = self.ai.runMe(self.test,1);
			# print position+1;
			self.computer.playPos(position+1);
			# computer.play();
			self.test.printGameState();
			# test.setCompWinnings();
			return [self.test.getCompState(),self.test.comp.getWinnings(),self.test.getPlayerState(),self.test.human.getWinnings()];
		else:
			return -2;
		

	def playerPlay(self,position):
		# testClone=copy.deepcopy(test);
		if self.isgameOver() =='false':
			# print 'player turn'
			state = self.human.playPos(position);
			if state == -1:
				return -1;
			self.test.printGameState();
			return [self.test.getCompState(),self.test.comp.getWinnings(),self.test.getPlayerState(),self.test.human.getWinnings()];
		else:
			return -2;

	def getWinner(self):
		if(self.test.human.getWinnings() > self.test.comp.getWinnings()):
			return "Player";
		elif(self.test.human.getWinnings() < self.test.comp.getWinnings()):
			return "Computer";
		else:
			return "Draw";
