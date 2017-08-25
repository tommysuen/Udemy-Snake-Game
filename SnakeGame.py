import pygame, sys, random, time

check_errors = pygame.init()
#Initialize PyGame
if check_errors[1] > 0:
	print("Bad")
	sys.exit(-1)

else: 
	print("Good")

#Sets Display Size - Set_mode takes Tuple
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake')

#Game Colors
red = pygame.Color(255, 0, 0) #Game Over
green = pygame.Color(0, 255, 0) #Snake
black = pygame.Color(0, 0, 0) #Score
white = pygame.Color(255, 255, 255) #Background
brown = pygame.Color(165, 42, 42) #Food

#Frames per Second Controller
FPS = pygame.time.Clock()

#[X,Y] Coordinates 
SnakePos = [100,50]
SnakeBody = [[100,50],[90,50],[80,50]]

#The Snake is interval by 10 so Must multiply by 10
FoodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
FoodSpawn = True

Direction = 'RIGHT'
ChangeTo = Direction
score = 0

def gameOver():
	myFont = pygame.font.SysFont('monaco', 72)
	GOsurf = myFont.render('Game over!', True, red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop= (360, 15)
	playSurface.blit(GOsurf, GOrect)
	showScore(0)
	pygame.display.flip()
	time.sleep(4)
	pygame.quit()
	sys.exit()

def showScore(choice =1):
	myFont = pygame.font.SysFont('monaco', 24)
	Ssurf = myFont.render('Score: {0}'.format(score), True, black)
	Srect = Ssurf.get_rect()
	if choice == 1:
		Srect.midtop = (80,10)
	else:
		Srect.midtop = (360,120)
	playSurface.blit(Ssurf, Srect)
	pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				ChangeTo = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				ChangeTo = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				ChangeTo = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				ChangeTo = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))

	if ChangeTo == 'RIGHT' and not Direction == 'LEFT':
		Direction = 'RIGHT'
	if ChangeTo == 'LEFT' and not Direction == 'RIGHT':
		Direction = 'LEFT'
	if ChangeTo == 'UP' and not Direction == 'DOWN':
		Direction = 'UP'
	if ChangeTo == 'DOWN' and not Direction == 'UP':
		Direction = 'DOWN'

	if Direction == 'RIGHT':
		SnakePos[0] += 10
	if Direction == 'LEFT':
		SnakePos[0] -=10
	if Direction == 'UP':
		SnakePos[1] -= 10
	if Direction == 'DOWN':
		SnakePos[1] += 10


	SnakeBody.insert(0, list(SnakePos))
	if SnakePos[0] == FoodPos[0] and SnakePos[1] == FoodPos[1]:
		score +=1
		FoodSpawn = False
	else:
		SnakeBody.pop()

	if FoodSpawn == False:
		FoodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]

	FoodSpawn = True

	playSurface.fill(white)
	for pos in SnakeBody:
		pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1], 10, 10))

	pygame.draw.rect(playSurface, brown, pygame.Rect(FoodPos[0],FoodPos[1], 10, 10))
	
	if SnakePos[0] >710 or SnakePos[0] < 0:
		gameOver()

	if SnakePos[1] > 450 or SnakePos[1] <0:
		gameOver()

	for block in SnakeBody[1:]:
		if SnakePos[0] == block[0] and SnakePos[1] == block[1]:
			gameOver()

	#flip updates the entire screen
	showScore()
	pygame.display.flip()
	FPS.tick(25)
	
	