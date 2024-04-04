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
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar1(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 50
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
		self.rect.x = 500
		self.rect.y = 133
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
		if self.hp == 0:
			self.kill()
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
		self.rect.x = 900
		self.rect.y = 133
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
		if self.hp == 0:
			self.kill()
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


class Player3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		#self.image = pygame.image.load("img/player2.png").convert()
		self.image = pygame.transform.scale(pygame.image.load("img/crystal_maiden.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 700
		self.rect.y =  466
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
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_j]:
			self.speed_x = -3
		if keystate[pygame.K_l]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_i]:
			self.speed_y = -3
		if keystate[pygame.K_k]:
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
		self.target = None
		self.speed = 2

	def update(self):
		self.hp -= 0.3
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		target_list = [player1, player2, player3]
		target_list = [t for t in target_list if t.hp >0]
		distance_list = [(distance(self,t),t) for t in target_list]
		if len(distance_list)==0:
			distance_list = [(0,self.target)]
		self.target = sorted(distance_list, key=lambda x: x[0])[0][1]
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

def show_game_over_screenp3():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Player 3 WINS", 20, WIDTH // 2, HEIGHT // 2)
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

game_over1 = False
game_over2 = False
game_over3 = False
running = True
start = True
pudge_times = [
		11,20,27,35,42,49,55,59,63,66,70,73,76,79,83,86,89,92,95,97,99,
		101,103,105,107,109,111,113,115,116,117,118,119,120,121
		]
pudge_idx = 0
while running:
	if game_over1:
		show_game_over_screenp1()
		screen.blit(background,(0,0))
		game_over1 = False
		
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		all_sprites.add(player1, player2, player3)
		
		pudge = Pudge(any)
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		start_time = pygame.time.get_ticks()
		score = 0
		pudge_idx = 0

	if game_over2:
		show_game_over_screenp2()
		screen.blit(background,(0,0))
		game_over2 = False
		
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		all_sprites.add(player1, player2, player3)
		
		pudge = Pudge(any)
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		start_time = pygame.time.get_ticks()
		score = 0
		pudge_idx = 0

	if game_over3:
		show_game_over_screenp3()
		screen.blit(background,(0,0))
		game_over3 = False
		
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		all_sprites.add(player1, player2, player3)

		pudge = Pudge(any)
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		start_time = pygame.time.get_ticks()
		score = 0
		pudge_idx = 0

	if start:
		show_go_screen()
		start = False
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		all_sprites.add(player1, player2, player3)

		pudge = Pudge(any)
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		start_time = pygame.time.get_ticks()
		score = 0	
		
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

	now = (pygame.time.get_ticks() - start_time)//1000
	if now % 121 in pudge_times[pudge_idx:]:
		pudge = Pudge(any)
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		pudge_idx += 1
		if pudge_idx == len(pudge_times):
			pudge_idx = 0

	if player1.hp <= 0 and player2.hp <= 0:
		game_over3 = True
		score += now
	if player2.hp <= 0 and player3.hp <= 0:
		game_over1 = True
		score += now
	if player1.hp <= 0 and player3.hp <= 0:
		game_over2 = True
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
		
	# Checar colisiones - jugador3 - pudge
	hits = pygame.sprite.spritecollide(player3, pudge_list, False)
	for hit in hits:
		player3.hp -= 0.8
	
	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	# Escudo.
	draw_text1(screen, "P1", 20, 10, 6)
	draw_text1(screen, "P2", 20, 400, 6)
	draw_text1(screen, "P3", 20, 800, 6)

	draw_hp_bar1(screen, 20, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 70, 6)
	if player1.hp > 0:
		draw_hp_bar(screen, player1.rect.x, player1.rect.y - 10, player1.hp)

	draw_hp_bar1(screen, 415, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 470, 6)
	if player2.hp > 0:
		draw_hp_bar(screen, player2.rect.x, player2.rect.y - 10, player2.hp)

	draw_hp_bar1(screen, 815, 5, player3.hp)
	draw_text2(screen, str(int(player3.hp))+ "/100", 10, 870, 6)
	if player3.hp > 0:
		draw_hp_bar(screen, player3.rect.x, player3.rect.y - 10, player3.hp)

	for pudge in pudge_list:
		draw_hp_bar2(screen, pudge.rect.x, pudge.rect.y - 10 , pudge.hp)
		
	draw_mana_bar(screen, 20, 15, player1.mana)
	draw_text1(screen, str(int(player1.mana))+ "/100", 10, 70, 16)

	draw_mana_bar(screen, 415, 15, player2.mana)
	draw_text1(screen, str(int(player2.mana))+ "/100", 10, 470, 16)

	draw_mana_bar(screen, 815, 15, player3.mana)
	draw_text1(screen, str(int(player3.mana))+ "/100", 10, 870, 16)

	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
	
	pygame.display.flip()
pygame.quit()