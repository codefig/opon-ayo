import pygame
import random
import copy
import BackEnd
import os
from BackEnd import gamePlay

negoBox=pygame.Rect(770,370,200,40);
negoBox1 = pygame.Rect(770,20,200,40);
_image_library = {};
clock = pygame.time.Clock();
input_box = pygame.Rect(350, 100, 140, 32);
color_inactive = pygame.Color('lightskyblue3');
color_active = pygame.Color('red');
color = color_inactive;
active = False;
text = '';
done = False;
negoButton = pygame.Rect(800,440,150,50);
compNegoButton = pygame.Rect(830,65,50,40);
compNonegoButton = pygame.Rect(910,65,50,40);
state=None;
status = 0;
currNego = False; #To know if a negotiation is going on

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

	#Draw the circle for keeping the scores player
	pygame.draw.circle(screen, (113,80,1),(240,200),80);

	#Draw the circle for keeping the scores computer
	pygame.draw.circle(screen, (113,80,1),(760,200),80);

	#Draw a rectangle
	pygame.draw.rect(screen, (113,80,1),pygame.Rect(200,100,600,200));

	#Draw a line between collector hole and normal hole Standard game look
	pygame.draw.rect(screen, (0,0,0), pygame.Rect(200,100,2,200));

	#Draw a line between collector hole and normal hole Standard game look
	pygame.draw.rect(screen, (0,0,0), pygame.Rect(798,100,2,200));


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
	# text = font.render('Winnings:',True, (0,0,0));
	# screen.blit(text, (800,40));
	# screen.blit(text, (800,440));

	text = font.render('Computer',True, (0,0,0));

	#Signify the computer position
	screen.blit(text,(200,30));

	text = font.render('Player',True, (0,0,0));

	#signify the player
	screen.blit(text,(200,400));
	# updateWinnings(0,0,screen);
	##################Negotiation Button############################
	font1=make_font('Helvetica',20);
	#Draw the negotiation button
	pygame.draw.rect(screen, (0,140,0),negoButton);
	pygame.draw.rect(screen, (0,140,0),compNegoButton);
	pygame.draw.rect(screen, (140,0,0),compNonegoButton);

	#Text to put there
	text1 = font1.render('Negotiate',True,(255,255,255));
	screen.blit(text1,(840,50));

	#Text to put there
	text2 = font1.render('Y',True,(255,255,255));
	screen.blit(text2,(850,80));

	#Text to put there
	text3 = font1.render('N',True,(255,255,255));
	screen.blit(text3,(930,80));

	#The text box for negotiating
	pygame.draw.rect(screen, (0,0,0), negoBox, 2);

	#The text box for negotiating for computer
	pygame.draw.rect(screen,pygame.Color('grey'),negoBox1,2)

	####################End of Negotiatoin Button####################

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

	##################Negotiation Button############################
	font1=make_font('Helvetica',20);
	#Draw the negotiation button
	pygame.draw.rect(screen, (0,140,0),negoButton);
	pygame.draw.rect(screen, (0,140,0),compNegoButton);
	pygame.draw.rect(screen, (140,0,0),compNonegoButton);

	#Text to put there
	text1 = font1.render('Negotiate',True,(255,255,255));
	screen.blit(text1,(840,455));

	#Text to put there
	text2 = font1.render('Y',True,(255,255,255));
	screen.blit(text2,(850,80));

	#Text to put there
	text3 = font1.render('N',True,(255,255,255));
	screen.blit(text3,(930,80));

	#The text box for negotiating
	pygame.draw.rect(screen, (0,0,0), negoBox, 2);
	#The text box for negotiating for computer
	pygame.draw.rect(screen,pygame.Color('grey'),negoBox1,2)

	####################End of Negotiatoin Button####################

#To show who wins
def showWinner(who,screen,font):
	updateSeeds(screen,[0,0,0,0,0,0],[0,0,0,0,0,0],moveSelector,0);
	# updateText([0,0,0,0,0,0],[0,0,0,0,0,0], font, screen);
	#Font for displaying text
	font = make_font('Helvetica',40);
	if (who=='Draw'):
		winner = "It is a Draw(OMI)";

	elif who=='Computer':
		winner="Computer Wins(OTA)";

	else:
		winner="Player Wins(OTA)";

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
	
	for i in range(player):
		distx =  random.randrange(790,815,4);
		disty = random.randrange(130,220,4)
		screen.blit(get_image("seeds/1i.png"),(distx, disty));

	for i in range(computer):
		
		distx =  random.randrange(162,185,4);
		disty = random.randrange(130,220,4)
		screen.blit(get_image("seeds/1i.png"),(distx, disty));



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

#Set screen title
pygame.display.set_caption('Opon Ayo');

#call the backend awake
game=gamePlay();


#The screen for collecting player input as player1 or 2
def playerScreen():
	clock = pygame.time.Clock();
	input_box = pygame.Rect(350, 100, 140, 32);
	color_inactive = pygame.Color('lightskyblue3');
	color_active = pygame.Color('dodgerblue2');
	color = color_inactive;
	active = False;
	text = '';
	done = False;
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True;
			if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
				if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
					active = not active;
				else:
					active = False;
                # Change the current color of the input box.
					color = color_active if active else color_inactive;
			if event.type == pygame.KEYDOWN:
				if active:
					if event.key == pygame.K_RETURN:
						game.setWho(int(text));
						# print(text);
						return None;
					elif event.key == pygame.K_BACKSPACE:
						text = text[:-1];
					else:
						text += event.unicode;

		text4 = font.render('What player is computer:',True,(255,255,255));

		screen.fill((30, 30, 30));

        # Render the current text.
		txt_surface = font.render(text, True, color);

		#Render the text
		screen.blit(text4,(350,40));

        # Resize the box if the text is too long.
		width = max(200, txt_surface.get_width()+10);
		input_box.w = width;

        # Blit the text.
		screen.blit(txt_surface, (input_box.x+5, input_box.y+5));

        # Blit the input_box rect.
		pygame.draw.rect(screen, color, input_box, 2);

		pygame.display.flip();
		clock.tick(30);

#Font for displaying text
font = make_font('Helvetica',30);

def game_intro():

    #Create the buttons
    startButton = pygame.Rect(350,200,100,50);
    quitButton = pygame.Rect(550,200,100,50);

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit();
                quit();
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos;  # gets mouse position
                # checks if mouse position is over the button
                if startButton.collidepoint(mouse_pos):
                    # prints current location of mouse
                    playerScreen();
                    return None;
                elif quitButton.collidepoint(mouse_pos):
                	pygame.quit();
                	quit();


        screen.fill((255,255,255));
        font1=make_font('Helvetica',20);
        text = font.render('Welcome To Opon-Ayo Game',True,(0,0,0));
        text1 = font1.render('Start Game',True,(255,255,255));
        text2 = font1.render('Quit Game',True,(255,255,255));
        screen.blit(text,(350,40));
        
        pygame.draw.rect(screen, (0,140,0),startButton);
        pygame.draw.rect(screen, (140,0,0),quitButton);

        screen.blit(text1,(360,215));
        screen.blit(text2,(560,215));


        pygame.display.update();

        # clock.tick(15)
game_intro();



#used for drawing the holes
x=0;

#used to enforce waiting 
complete=False;

#Use white background for the screen
screen.fill((255,255,255));


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


#put the seeds into holes
updateSeeds(screen, game.test.getCompState(),game.test.getPlayerState(),moveSelector,1);

#Clear out x memory
x=0;

#clear out x memory
x=0;

#Draw the rectangle used for selecting the hole to play
rect=pygame.draw.rect(screen,(0,0,0), pygame.Rect(225,305,50,4));


#Draw a line between the 3 holes. Standard game look
pygame.draw.rect(screen, (0,0,0), pygame.Rect(500,100,2,200));

##################Negotiation Button############################
font1=make_font('Helvetica',20);
#Draw the negotiation button
pygame.draw.rect(screen, (0,140,0),negoButton);
pygame.draw.rect(screen, (0,140,0),compNegoButton);
pygame.draw.rect(screen, (140,0,0),compNonegoButton);

#Text to put there
text1 = font1.render('Negotiate',True,(255,255,255));
screen.blit(text1,(840,455));

#Text to put there
text2 = font1.render('Y',True,(255,255,255));
screen.blit(text2,(850,80));

#Text to put there
text3 = font1.render('N',True,(255,255,255));
screen.blit(text3,(930,80));

#The text box for negotiating for player
pygame.draw.rect(screen, (0,0,0), negoBox, 2);


#The text box for negotiating for computer
pygame.draw.rect(screen,pygame.Color('grey'),negoBox1,2)

####################End of Negotiatoin Button####################
#Put the winnings to inform of current winner
# text = font.render('Winnings:',True, (0,0,0));
# screen.blit(text, (800,40));
# screen.blit(text, (800,440));
# updateWinnings(0,0,screen);

#Put a small rectangle in front of players to indicate current leader
#pygame.draw.rect(screen, (0,140,0),pygame.Rect(925,40,20,20));
#pygame.draw.rect(screen, (0,140,0),pygame.Rect(925,440,20,20));

def playFirst():
	if int(game.whoPlay()) == 1:
		state=game.computerPlay();
		if state == -2:
			showWinner(game.getWinner(), screen,font);
		else:
			updateSeeds(screen,state[0],state[2],moveSelector,1);
			# updateText(state[2],state[0], font, screen);
			updateWinnings(state[1],state[3],screen);
			complete=False;
		pygame.display.flip();

playFirst();

#For the negotiation
#For now the computer reeieves the negotiations from the player and considers if it suits him or not. If the computer sees that its winnigs plus all the
#remainig seeds is smaller than the players winnings, he accepts and displays winner Else he doesn't. Also, if the computer sees that 
#its winnings plus the negotiated seeds is greater than the platers winnigs and remaining seed, he accepts the negotiation.
def toNegotiate(seeds):

	#Realised an error was thrown when the state is empty
	try:
		if (seeds > sum(state[2])):
			return -2;
		# This is for the computer thinking about the deal
		print('Test 1 :');
		if((state[1]+(sum(state[0]) + sum(state[2]))) <= state[3]):#check for the first condition
			print ("Computer Accepts Shamefully since it knows it can not win again");
			return sum(state[0])/2;#Computer gives half its seeds
		print('Test 2 :');
		if(state[1]+seeds >= state[3]+(sum(state[0]) + sum(state[2]))):#Check for the second condition
			print("Computer's winnigs is far greater or at least I dont loose, I take the deal");
			return sum(state[0]);#Computer reyturns all its seeds
		print('Test 3 :');
		if(state[1]+seeds > 24):#Check if the computer already won
			print('Computer already won');
			return sum(state[0]);#Computer returns all its seeds
		print('Test 4 :');
		if(state[1]+seeds+sum(state[0]) > 24):#check if the computer has enough seeds to win
			#Implement logice for how much seed to release
			print('Computer would win by not giving any seed');#but if it can find a balance, return the value to win
			need = 25-(state[1]+seeds);#Get the seeds needed to win
			if(sum(state[0])>need):#See if computer has more seeds return the remaining if true
				return sum(state[0])-need;
			else:
				return 0;
			return 0;
		print('Test 5 :');
		if(state[3] > 24):#If the player already has more seeds, forget it
			print('Player already has upper hand');
			return sum(state[1])/2;

		#Complementary test 
		print('Test 6 :');
		if(state[1]+seeds > state[3]+(sum(state[0])+sum(state[2]))):#If the user is offering too much seeds, accepts.
			print('User is too generous, I graciously accept');
			return sum(state[0]);

		print('Test 7 :');
		if(state[1]+seeds > state[3]):#If the amount of seeds the user is offering is making computer having more seeds, let's check if it is a good deal
			if((sum(state[2])-seeds)+state[3] > state[1]+seeds):#If the players seeds+remainingSeedOnBoard is greater
				return 0;
			else:
				return sum(state[0])/2;
		return -1;

	except Exception as e:
		print('Fatal error for release');
		return -1;
		
		# else:
		# 	#The computer proposing a new deal
		# 	if(state[1]+sum(state[2])+sum(state[0]) < state[3]):
		# 		print("jj");
		# 		font1=make_font('Helvetica',20);
		# 		txt_surface = font1.render(str(state[1]/2), True, (0,0,0));

		# 	    # Resize the box if the text is too long.
		# 		width = max(200, txt_surface.get_width()+10);
		# 		negoBox1.w = width;

		# 		        # Blit the text.
		# 		screen.blit(txt_surface, (negoBox1.x+5, negoBox1.y+5));

		# 		        # Blit the input_box rect.
		# 		pygame.draw.rect(screen, color, negoBox1, 2);
		# 		# compNegotiate(0)
		# 		status = 0;
		# 		return True;

		# 	elif(state[1]+seeds > state [3]+sum(state[2])-seeds):
		# 		print("jt");

		# 		font1=make_font('Helvetica',20);
		# 		txt_surface = font1.render(str(state[1]/2), True, (0,0,0));

		# 	    # Resize the box if the text is too long.
		# 		width = max(200, txt_surface.get_width()+10);
		# 		negoBox1.w = width;

		# 		        # Blit the text.
		# 		screen.blit(txt_surface, (negoBox1.x+5, negoBox1.y+5));

		# 		        # Blit the input_box rect.
		# 		pygame.draw.rect(screen, color, negoBox1, 2);
		# 		status = 1;
		# 		return True;

		# 	elif(state[1]+seeds+sum(state[0])/2 > state[3]+(sum(state[2])-seeds)):
		# 		print("ss");
		# 		font1=make_font('Helvetica',20);
		# 		txt_surface = font1.render(str(state[1]/2), True, (0,0,0));

		# 	    # Resize the box if the text is too long.
		# 		width = max(200, txt_surface.get_width()+10);
		# 		negoBox1.w = width;

		# 		        # Blit the text.
		# 		screen.blit(txt_surface, (negoBox1.x+5, negoBox1.y+5));

		# 		        # Blit the input_box rect.
		# 		pygame.draw.rect(screen, color, negoBox1, 2);
		# 		status = 2;
		# 		return True;
		# 	else:
		# 		return False;
	

def compNegotiate(status):
	font1=make_font('Helvetica',20);
	txt_surface = font1.render(str(state[1]/2), True, (0,0,0));

		    # Resize the box if the text is too long.
	width = max(200, txt_surface.get_width()+10);
	negoBox1.w = width;

			        # Blit the text.
	screen.blit(txt_surface, (negoBox1.x+5, negoBox1.y+5));

			        # Blit the input_box rect.
	pygame.draw.rect(screen, color, negoBox1, 2);
	# if(status == 0):
	# 	return True;
	if status == 0:
		return 0;
	elif status == 1:
		return sum(state[0])/2;
	else:
		return sum(state[0])/2;

#Adding an event listener using a while loop
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True;
		if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
			if active:
				text = ''
				# pygame.draw.rect(screen,color,negoBox,2);
				# Render the current text.
				font1=make_font('Helvetica',20);
				txt_surface = font1.render(text, True, (0,0,0));

			        # Resize the box if the text is too long.
				width = max(200, txt_surface.get_width()+10);
				negoBox.w = width;

			        # Blit the text.
				screen.blit(txt_surface, (negoBox.x+5, negoBox.y+5));
				#Cover the whole screen
				pygame.draw.rect(screen, (255,255,255), negoBox);

			        # Blit the input_box rect.
				pygame.draw.rect(screen, color, negoBox, 2);
				pygame.draw.rect(screen, color, negoBox1, 2);


		#Used for checking for right key press
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			currNego = False;
			moveSelector = clearMoveScreen(moveSelector,event.key);
			moveSelector+=100;
			rect=pygame.draw.rect(screen,(0,0,0), pygame.Rect(225+moveSelector,305,50,4));

		#used for checking for left key press
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			currNego = False;
			moveSelector = clearMoveScreen(moveSelector, event.key);
			moveSelector-=100;
			rect=pygame.draw.rect(screen,(0,0,0), pygame.Rect(225+moveSelector,305,50,4));

		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			currNego = False;
			position=((rect.center[0]-250)/100)+1;
			state=game.playerPlay(position);
			if state==-1:	
				continue;

			elif state==-2:
				showWinner(game.getWinner(), screen,font);
				continue;

			else:
				updateSeeds(screen,state[0],state[2],moveSelector,1);
				# updateText(state[2],state[0], font, screen);
				updateWinnings(state[1],state[3],screen);
				complete = True;

			if complete==True:
				state=game.computerPlay();
				if state == -2:
					showWinner(game.getWinner(), screen,font);
					continue;
				else:
					updateSeeds(screen,state[0],state[2],moveSelector,1);
					# updateText(state[2],state[0], font, screen);
					updateWinnings(state[1],state[3],screen);
					complete=False;
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
			currNego = False;
			game = gamePlay();
			#put the seeds into holes
			updateSeeds(screen, game.test.getCompState(),game.test.getPlayerState(),moveSelector,1);
			# updateText(game.test.getCompState(),game.test.getPlayerState(), font, screen);
			updateWinnings(game.test.comp.getWinnings(),game.test.human.getWinnings(),screen);
			clearWinner();
			playFirst();

		elif event.type == pygame.KEYDOWN:
			if active:
				currNego = False;
				print('active');
				text += event.unicode;
				# pygame.draw.rect(screen,color,negoBox,2);
				# Render the current text.
				font1=make_font('Helvetica',20);
				txt_surface = font1.render(text, True, (0,0,0));

			        # Resize the box if the text is too long.
				width = max(200, txt_surface.get_width()+10);
				negoBox.w = width;

			        # Blit the text.
				screen.blit(txt_surface, (negoBox.x+5, negoBox.y+5));

			        # Blit the input_box rect.
				pygame.draw.rect(screen, color, negoBox, 2);
				
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = event.pos;  # gets mouse position
            # If the user clicked on the input_box rect.
			if negoBox.collidepoint(event.pos):
                    # Toggle the active variable.
				active = True;
					# toNegotiate(int(text));
			elif negoButton.collidepoint(mouse_pos):

				#Cover the computer screen
				pygame.draw.rect(screen, (255,255,255), negoBox1);
				pygame.draw.rect(screen,pygame.Color('grey'),negoBox1,2)

				currNego = True;
				result = toNegotiate(int(text));
                # checks if mouse position is over the button
				if(result < 0):
					hold_text = text;
					text ='';
					print('Computer would release: ');
					print (result);
					# Render the current text.
					if(result < 0 & result > -2):
						result = 'No Deal';
					elif(result < -1):
						result = 'Not enough seeds';
					font1=make_font('Helvetica',20);
					txt_surface1 = font1.render(str(result), True, (0,0,0));
					# Blit the text.
					screen.blit(txt_surface1, (negoBox1.x+5, negoBox1.y+5));
					# pygame.draw.rect(screen,color,negoBox,2);
				        # Resize the box if the text is too long.
					width = max(200, txt_surface.get_width()+10);
					negoBox.w = width;

					#Cover the whole screen
					pygame.draw.rect(screen, (255,255,255), negoBox);

					

				        # Blit the input_box rect.
					pygame.draw.rect(screen, (255,0,0), negoBox, 2);

					

				else:
					hold_text = text;
					text ='';
					#Cover the computer screen
					pygame.draw.rect(screen, (255,255,255), negoBox1);
					pygame.draw.rect(screen,pygame.Color('grey'),negoBox1,2)

					print('Computer would release: ');
					print(result);
					# Render the current text.
					if(result < 0 & result > -2):
						result = 'No Deal';
					elif(result < -1):
						result = 'Not enough seeds';
					font1=make_font('Helvetica',20);
					txt_surface1 = font1.render(str(result), True, (0,0,0));
					# Blit the text.
					screen.blit(txt_surface1, (negoBox1.x+5, negoBox1.y+5));
					# pygame.draw.rect(screen,color,negoBox,2);
				        # Resize the box if the text is too long.
					width = max(200, txt_surface.get_width()+10);
					negoBox.w = width;

					#Cover the whole screen
					pygame.draw.rect(screen, (255,255,255), negoBox);

				        # Blit the input_box rect.
					pygame.draw.rect(screen, (0,141,0), negoBox, 2);
					#compNegotiate(status);
					
			elif compNegoButton.collidepoint(mouse_pos):
				print('Prevoious winnigs were')
				print("Human Winnings: ",game.test.human.getWinnings());
				print("Computer Winnings: ",game.test.comp.getWinnings());
				#Updating both winnigs
				game.test.setPlayerWinningsAPI(result+((sum(game.test.getPlayerState()))-int(hold_text)));
				game.test.setCompWinningsAPI(int(hold_text)+(sum(game.test.getCompState())-result));
				print('After updating, winnigs were')
				print("Human Winnings: ",game.test.human.getWinnings());
				print("Computer Winnings: ",game.test.comp.getWinnings());
				hold_text='';
				game.test.gameOver();
				showWinner(game.getWinner(), screen,font);

			elif compNonegoButton.collidepoint(mouse_pos):
				print('No Accepts');
				print(currNego);
			else:
				currNego = False;
				active = False;
                # Change the current color of the input box.
				color = color_active if active else color_inactive;
		
	
		
			

	pygame.display.flip();