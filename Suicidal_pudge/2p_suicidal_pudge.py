import pygame, random
from random import randint

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)
BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Suicidal Pudge")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BROWN, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		
		self.image = pygame.transform.scale(pygame.image.load("img/crystal_maiden.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = HEIGHT // 2
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		

	def update(self):
		
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -3
		if keystate[pygame.K_d]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -3
		if keystate[pygame.K_s]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

class Player2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		#self.image = pygame.image.load("img/player2.png").convert()
		self.image = pygame.transform.scale(pygame.image.load("img/crystal_maiden.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 1100
		self.rect.y = HEIGHT // 2
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		

	def update(self):
		
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -3
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -3
		if keystate[pygame.K_DOWN]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

def distance(a,b):
	#pitagoras distance between a and b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	return (dx**2 + dy**2)**(1/2)

def direction(a,b):
	#x,y unitary vector from a to b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	return dx/radio, dy/radio


class Pudge(pygame.sprite.Sprite):

	def __init__(self,target):
		super().__init__()
		self.image = pudge_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(300, WIDTH - 30)
		self.rect.y = random.randrange(50, HEIGHT - 250)
		self.hp = 100
		self.target = target
		self.speed = 2


	def update(self):
		alist = [player1, player2]
		self.hp -= 0.3
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()

		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) < 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player1
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) > 
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = player2
		
		try:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
		except(UnboundLocalError):
			pass
		
		if ((((self.rect.centery - player1.rect.centery)**2 + (self.rect.centerx - player1.rect.centerx)**2)**(1/2)) ==
		(((self.rect.centery - player2.rect.centery)**2 + (self.rect.centerx - player2.rect.centerx)**2)**(1/2))):
			self.target = random.choice(alist)


def show_go_screen():
	
	screen.fill(BLACK)#(background, [0,0])
	draw_text1(screen, "Suicidal Pudge", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Stay away from suicidal pudge", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	#draw_text(screen, "Created by: Francisco Carvajal", 10,  60, 625)
	
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False


pudge_images = []
pudge_list = ["img/pudge.png"]
for img in pudge_list:
	pudge_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(50,65)))


def show_game_over_screenp1():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Record: " + str(score) + " segundos", 80, WIDTH // 2, 250)
	draw_text1(screen, "Player 1 WINS", 20, WIDTH // 2, 400)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp2():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Record: " + str(score) + " segundos", 80, WIDTH // 2, 250)
	draw_text1(screen, "Player 2 WINS", 20, WIDTH // 2, 400)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

background = pygame.transform.scale(pygame.image.load("img/5.png").convert(), (1300,700))

counter1 = True
counter2 = True
counter3 = True
counter4 = True
counter5 = True
counter6 = True
counter7 = True
counter8 = True
counter9 = True
counter10 = True
counter11 = True
counter12 = True
counter13 = True
counter14 = True
counter15 = True
counter16 = True
counter17 = True
counter18 = True
counter19 = True
counter20 = True
counter21 = True
counter22 = True
counter23 = True
counter24 = True
counter25 = True
counter26 = True
counter27 = True
counter28 = True
counter29 = True
counter30 = True
counter31 = True
counter32 = True
counter33 = True
counter34 = True
counter35 = True
counter36 = True
counter37 = True
counter38 = True
counter39 = True
counter40 = True
game_over1 = False
game_over2 = False
running = True
start = True
while running:
	if game_over1:

		show_game_over_screenp1()
		screen.blit(background,(0,0))
		game_over1 = False
		counter1 = True
		counter2 = True
		counter3 = True
		counter4 = True
		counter5 = True
		counter6 = True
		counter7 = True
		counter8 = True
		counter9 = True
		counter10 = True
		counter11 = True
		counter12 = True
		counter13 = True
		counter14 = True
		counter15 = True
		counter16 = True
		counter17 = True
		counter18 = True
		counter19 = True
		counter20 = True
		counter21 = True
		counter22 = True
		counter23 = True
		counter24 = True
		counter25 = True
		counter26 = True
		counter27 = True
		counter28 = True
		counter29 = True
		counter30 = True
		counter31 = True
		counter32 = True
		counter33 = True
		counter34 = True
		counter35 = True
		counter36 = True
		counter37 = True
		counter38 = True
		counter39 = True
		counter40 = True
		
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)

		pudge = Pudge(any)
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		start_time = pygame.time.get_ticks()
		score = 0

	if game_over2:

		show_game_over_screenp2()
		screen.blit(background,(0,0))
		game_over2 = False
		counter1 = True
		counter2 = True
		counter3 = True
		counter4 = True
		counter5 = True
		counter6 = True
		counter7 = True
		counter8 = True
		counter9 = True
		counter10 = True
		counter11 = True
		counter12 = True
		counter13 = True
		counter14 = True
		counter15 = True
		counter16 = True
		counter17 = True
		counter18 = True
		counter19 = True
		counter20 = True
		counter21 = True
		counter22 = True
		counter23 = True
		counter24 = True
		counter25 = True
		counter26 = True
		counter27 = True
		counter28 = True
		counter29 = True
		counter30 = True
		counter31 = True
		counter32 = True
		counter33 = True
		counter34 = True
		counter35 = True
		counter36 = True
		counter37 = True
		counter38 = True
		counter39 = True
		counter40 = True
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)

		pudge = Pudge(any)
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		start_time = pygame.time.get_ticks()
		score = 0

	if start:
		show_go_screen()
		start = False
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)

		pudge = Pudge(any)
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		start_time = pygame.time.get_ticks()
		score = 0	
		
		
	

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	now = (pygame.time.get_ticks() - start_time)//1000
	
	if counter1:
		if now == 11:
			counter1 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter2:
		if now == 20:
			counter2 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter3:
		if now == 27:
			counter3 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter4:
		if now == 35:
			counter4 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter5:
		if now == 42:
			counter5 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter6:
		if now == 49:
			counter6 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter7:
		if now == 55:
			counter7 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter8:
		if now == 59:
			counter8 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter9:
		if now == 63:
			counter9 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter10:
		if now == 66:
			counter10 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter11:
		if now == 70:
			counter11 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter12:
		if now == 73:
			counter12 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter13:
		if now == 76:
			counter13 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter14:
		if now == 79:
			counter14 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter15:
		if now == 83:
			counter15 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter16:
		if now == 86:
			counter16 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter17:
		if now == 89:
			counter17 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter18:
		if now == 92:
			counter18 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter19:
		if now == 95:
			counter19 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter20:
		if now == 97:
			counter20 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter21:
		if now == 97:
			counter21 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter22:
		if now == 99:
			counter22 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)	
	if counter23:
		if now == 101:
			counter23 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter24:
		if now == 103:
			counter24 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter25:
		if now == 105:
			counter25 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter26:
		if now == 107:
			counter26 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter27:
		if now == 109:
			counter27 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter28:
		if now == 111:
			counter28 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter29:
		if now == 113:
			counter29 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter30:
		if now == 115:
			counter30 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter31:
		if now == 116:
			counter31 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter32:
		if now == 117:
			counter32 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter33:
		if now == 118:
			counter33 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter34:
		if now == 119:
			counter34 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter35:
		if now == 120:
			counter35 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)
	if counter36:
		if now == 121:
			counter36 = False
			pudge = Pudge(any)
			all_sprites.add(pudge)
			pudge_list.add(pudge)


	if player1.hp <= 0:
		game_over2 = True
		score += now
	if player2.hp <= 0:
		game_over1 = True
		score += now
	
	all_sprites.update()
	
	
	# Checar colisiones - jugador1 - pudge
	hits = pygame.sprite.spritecollide(player1, pudge_list, False)
	for hit in hits:
		
		player1.hp -= 0.8
		
		
	# Checar colisiones - jugador2 - pudge
	hits = pygame.sprite.spritecollide(player2, pudge_list, False)
	for hit in hits:
		
		player2.hp -= 0.8


	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	
	# Escudo.
	draw_text2(screen, "P1", 20, 10, 6)
	draw_text2(screen, "P2", 20, 600, 6)

	draw_hp_bar(screen, 20, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 70, 6)

	draw_hp_bar(screen, 615, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 670, 6)

	draw_hp_bar2(screen, 400, 50, pudge.hp)
	draw_text2(screen, str(int(pudge.hp)) + "/100", 10, 450, 51)

	draw_mana_bar(screen, 20, 15, player1.mana)
	draw_text1(screen, str(int(player1.mana))+ "/100", 10, 70, 16)

	draw_mana_bar(screen, 615, 15, player2.mana)
	draw_text1(screen, str(int(player2.mana))+ "/100", 10, 670, 16)

	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
	
	

	pygame.display.flip()
pygame.quit()