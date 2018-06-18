import pygame
import random
import copy
import BackEnd
import os
from BackEnd import gamePlay

_image_library = {};
def get_image(path):
	global _image_library;
	image = _image_library.get(path);
	if image == None:
		canonicalized_path = path.replace('/', os.sep).replace('\\',os.sep);
		image = pygame.image.load(canonicalized_path);
		_image_library[path] = image;
	return image;


#Font used for displaying the text
def make_font(fonts, size):
	available = pygame.font.get_fonts(); #get the font installed in the pc

	choices = map(lambda x:x.lower().replace(' ', ''), fonts);

	for choice in choices:
		if choice in available:
			return pygame.font.SysFont(choice,size);
	
	#choice of font not on system, return a defaul
	return pygame.font.Font(None, size);


#For redrawing the game board
def redraw(moveSelector):

	x=0;
	#Draw a rectangle
	pygame.draw.rect(screen, (113,80,1),pygame.Rect(200,100,600,200));

	####################################################################
	#Fancy addition

	#draw a rectangle over a small area
	pygame.draw.rect(screen, (255,255,255),pygame.Rect(200,100,20,20));

	#draw a circle over that area
	pygame.draw.circle(screen, (113,80,1), (219,120), 20);


	#draw a rectangle over a small area
	pygame.draw.rect(screen, (255,255,255),pygame.Rect(200,280,20,20));

	#draw a circle over that area
	pygame.draw.circle(screen, (113,80,1), (219,280), 20);

	#draw a rectangle over a small area
	pygame.draw.rect(screen, (255,255,255),pygame.Rect(780,100,20,20));


	#draw a circle over that area
	pygame.draw.circle(screen, (113,80,1), (780,120), 20);

	#draw a rectangle over a small area
	pygame.draw.rect(screen, (255,255,255),pygame.Rect(780,280,20,20));

	#draw a circle over that area
	pygame.draw.circle(screen, (113,80,1), (780,280), 20);

	##################################################################

	#Draw a line between the 3 holes. Standard game look
	pygame.draw.rect(screen, (0,0,0), pygame.Rect(500,100,2,200));

	#Draw a circle that would be the hole. 6 of them for the first row
	for i in range(1,7):
		pygame.draw.circle(screen, (255,255,255), (250+x,130), 30);
		x+=100;

	#Clear out x memory
	x=0;

	#Draw for the second row
	for i in range(1,7):
		pygame.draw.circle(screen, (255,255,255), (250+x,265), 30);
		x+=100;

	rect=pygame.draw.rect(screen,(0,0,0), pygame.Rect(225+moveSelector,305,50,4));

	#Put the winnings to inform of current winner
	text = font.render('Winnings:',True, (0,0,0));
	screen.blit(text, (800,40));
	screen.blit(text, (800,440));
	updateWinnings(0,0,screen);

def clearMoveScreen(moveSelector,event):
	"""For clearing the move selector"""

	#Check if the move selector is at the end of the screen
	if(moveSelector==500) & (event==pygame.K_RIGHT):
		pygame.draw.rect(screen,(255,255,255), pygame.Rect(225+(moveSelector),305,50,4));
		moveSelector=-100;
		return moveSelector;

	#Check for if move selector is at first position
	elif (moveSelector == 0) & (event==pygame.K_LEFT):
		pygame.draw.rect(screen,(255,255,255), pygame.Rect(225-(moveSelector),305,50,4));
		moveSelector=600;
		return moveSelector;		

	#Clear recently drawm move selectors
	pygame.draw.rect(screen,(255,255,255), pygame.Rect(225+(moveSelector),305,50,4));

	return moveSelector;

#Used for updating the seeds displayed after a play event happens
def updateSeeds(screen,seeds1,seeds2,moveSelector,check):
	k=0;
	if check != 0:
		screen.fill((255,255,255));
		redraw(moveSelector);
	countx=205;
	county=85;
	dist=0;
	for i in seeds1:
		k=i;
		if i > 12:
			k=12;
		strr='seeds/'+str(k)+'.png';
			
		screen.blit(get_image(strr),(countx+dist, county));
		dist+=100;

	countx=200;
	county=220;
	dist=0;
	for i in seeds2:
		k=i;
		if i > 12:
			k=12;
		strr='seeds/'+str(k)+'.png';
		screen.blit(get_image(strr),(countx+dist, county));
		dist+=100;


#Update the text revealing seed number
def updateText(seedNum1, seedNum2, font, screen):

	#Clear out the text under holes
	pygame.draw.rect(screen, (255,255,255),pygame.Rect(200,70,600,20));
	pygame.draw.rect(screen, (255,255,255),pygame.Rect(200,320,600,20));

	count = 0;
	#update the seed number from the game board returned second row
	for i in seedNum1:
		text = font.render(str(i),True, (0,0,0));
		#put the seed number under hole
		screen.blit(text, (250+count,320));
		count+=100;

	count=0;
	#update the seed number from the game board returned first row
	for i in seedNum2:
		text = font.render(str(i),True, (0,0,0));
		#put the seed number under hole
		screen.blit(text, (250+count,70));
		count+=100;

#To show who wins
def showWinner(who,screen,font):
	updateSeeds(screen,[0,0,0,0,0,0],[0,0,0,0,0,0],moveSelector,0);
	updateText([0,0,0,0,0,0],[0,0,0,0,0,0], font, screen);
	#Font for displaying text
	font = make_font('Helvetica',40);
	if (who=='Draw'):
		winner = "It is a Draw";

	elif who=='Computer':
		winner="Computer Wins";

	else:
		winner="Player Wins";

	text = font.render(winner,True, (158,142,136));
	#place text way under second player
	for i in range(0,100,10):
		rect=pygame.draw.rect(screen, (255,255,255),pygame.Rect(i-50,445,700,50));
		screen.blit(text, (i,450));
		pygame.display.flip();

#to clear winner
def clearWinner():
	rect=pygame.draw.rect(screen, (255,255,255),pygame.Rect(80,445,720,50));
	pygame.display.flip();

#update the winnings
def updateWinnings(computer, player,screen):
	#Clear out the text under holes
	pygame.draw.rect(screen, (255,255,255),pygame.Rect(900,40,25,20));
	pygame.draw.rect(screen, (255,255,255),pygame.Rect(900,440,25,20));

	color=(169,42,0);
	computerColor=(0,140,0)
	playerColor=(0,140,0);
	if computer > player:
		# computerColor=(0,140,0);
		# playerColor=color;
		#Put a small rectangle in front of players to indicate current leader
		pygame.draw.rect(screen, (0,140,0),pygame.Rect(925,40,20,20),);
		pygame.draw.rect(screen, (169,42,0),pygame.Rect(925,440,20,20));

	elif player > computer:
		# playerColor=(0,140,0);
		# computerColor=color;
		pygame.draw.rect(screen, (169,42,0),pygame.Rect(925,40,20,20));
		pygame.draw.rect(screen, (0,140,0),pygame.Rect(925,440,20,20));

	else:
		pygame.draw.rect(screen, (0,140,0),pygame.Rect(925,40,20,20));
		pygame.draw.rect(screen, (0,140,0),pygame.Rect(925,440,20,20));

	#For the computer winnings
	text = font.render(str(computer),True, (0,0,0));
	screen.blit(text, (900,40));
	#For the player winnings
	text = font.render(str(player),True, (0,0,0));
	screen.blit(text, (900,440))


####################################################################
#Pygames code start here
#
#
#0
###################################################################
pygame.init();
screen = pygame.display.set_mode((1000,500),0);
done=False;
moveSelector=0;

#used for drawing the holes
x=0;

#used to enforce waiting 
complete=False;

#Use white background for the screen
screen.fill((255,255,255));

#Set screen title
pygame.display.set_caption('Opon Ayo');

#Font for displaying text
font = make_font('Helvetica',30);

#Draw a rectangle
pygame.draw.rect(screen, (113,80,1),pygame.Rect(200,100,600,200));

####################################################################
#Fancy addition

#draw a rectangle over a small area
pygame.draw.rect(screen, (255,255,255),pygame.Rect(200,100,20,20));

#draw a circle over that area
pygame.draw.circle(screen, (113,80,1), (219,120), 20);


#draw a rectangle over a small area
pygame.draw.rect(screen, (255,255,255),pygame.Rect(200,280,20,20));

#draw a circle over that area
pygame.draw.circle(screen, (113,80,1), (219,280), 20);

#draw a rectangle over a small area
pygame.draw.rect(screen, (255,255,255),pygame.Rect(780,100,20,20));


#draw a circle over that area
pygame.draw.circle(screen, (113,80,1), (780,120), 20);

#draw a rectangle over a small area
pygame.draw.rect(screen, (255,255,255),pygame.Rect(780,280,20,20));

#draw a circle over that area
pygame.draw.circle(screen, (113,80,1), (780,280), 20);

##################################################################


#Draw a circle that would be the hole. 6 of them for the first row
for i in range(1,7):
	pygame.draw.circle(screen, (93,80,38), (250+x,130), 25);
	x+=100;

#Clear out x memory
x=0;

#Draw for the second row
for i in range(1,7):
	pygame.draw.circle(screen, (93,80,38), (250+x,250), 25);
	x+=100;

#call the backend awake
game=gamePlay();

#put the seeds into holes
updateSeeds(screen, game.test.getCompState(),game.test.getPlayerState(),moveSelector,1);

#Clear out x memory
x=0;

#put the seed numer under the first hole
for i in [4,4,4,4,4,4]:
		text = font.render(str(i),True, (0,0,0));
		#put the seed number under hole
		screen.blit(text, (250+x,75));
		x+=100;

#clear out x memory
x=0;

#put the seed numer under the second hole
for i in [4,4,4,4,4,4]:
		text = font.render(str(i),True, (0,0,0));
		#put the seed number under hole
		screen.blit(text, (250+x,320));
		x+=100;

#Draw the rectangle used for selecting the hole to play
rect=pygame.draw.rect(screen,(0,0,0), pygame.Rect(225,305,50,4));


#Draw a line between the 3 holes. Standard game look
pygame.draw.rect(screen, (0,0,0), pygame.Rect(500,100,2,200));

#Put the winnings to inform of current winner
text = font.render('Winnings:',True, (0,0,0));
screen.blit(text, (800,40));
screen.blit(text, (800,440));
updateWinnings(0,0,screen);

#Put a small rectangle in front of players to indicate current leader
pygame.draw.rect(screen, (0,140,0),pygame.Rect(925,40,20,20));
pygame.draw.rect(screen, (0,140,0),pygame.Rect(925,440,20,20));

#Adding an event listener using a while loop
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True;

		#Used for checking for right key press
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			moveSelector = clearMoveScreen(moveSelector,event.key);
			moveSelector+=100;
			rect=pygame.draw.rect(screen,(0,0,0), pygame.Rect(225+moveSelector,305,50,4));

		#used for checking for left key press
		if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			moveSelector = clearMoveScreen(moveSelector, event.key);
			moveSelector-=100;
			rect=pygame.draw.rect(screen,(0,0,0), pygame.Rect(225+moveSelector,305,50,4));

		if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			position=((rect.center[0]-250)/100)+1;
			state=game.playerPlay(position);
			if state==-1:	
				continue;

			elif state==-2:
				showWinner(game.getWinner(), screen,font);
				continue;

			else:
				updateSeeds(screen,state[0],state[2],moveSelector,1);
				updateText(state[2],state[0], font, screen);
				updateWinnings(state[1],state[3],screen);
				complete = True;

			if complete==True:
				state=game.computerPlay();
				if state == -2:
					showWinner(game.getWinner(), screen,font);
					continue;
				else:
					updateSeeds(screen,state[0],state[2],moveSelector,1);
					updateText(state[2],state[0], font, screen);
					updateWinnings(state[1],state[3],screen);
					complete=False;
		if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
			game = gamePlay();
			#put the seeds into holes
			updateSeeds(screen, game.test.getCompState(),game.test.getPlayerState(),moveSelector,1);
			updateText(game.test.getCompState(),game.test.getPlayerState(), font, screen);
			updateWinnings(game.test.comp.getWinnings(),game.test.human.getWinnings(),screen);
			clearWinner();
			
			

	pygame.display.flip();