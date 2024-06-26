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
	BAR_LENGHT = 210
	BAR_HEIGHT = 15
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
	BAR_LENGHT = 210
	BAR_HEIGHT = 15
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
		self.rect.y = HEIGHT // 3
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
	if radio != 0:
		x, y = (dx/radio, dy/radio)
	else:
		x, y = (0, 0)
	return x, y

class Pudge(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pudge_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(300, WIDTH - 30)
		self.rect.y = random.randrange(50, HEIGHT - 250)
		self.hp = 100
		self.speed = 2

	def update(self):
		self.hp -= 0.3
		if self.hp <= 0:
			self.hp = 0
			self.kill()
		
		target = player1
		x,y = direction(self, target)
		self.rect.centerx += self.speed*x
		self.rect.centery += self.speed*y

with open("data1.txt", mode="r") as file:
	high_score = int(file.read())

def show_go_screen():
	screen.fill(BLACK)
	draw_text1(screen, "Suicidal Pudge", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Stay away from suicidal pudge", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Record: " + str(high_score) + " segundos", 80, WIDTH // 2, HEIGHT*3//5)
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

pudge_images = []
pudge_list = ["img/pudge.png"]
for img in pudge_list:
	pudge_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(50,65)))


def show_game_over_screen():
	screen.fill(BLACK)
	with open("data1.txt", mode="r") as file:
		high_score = int(file.read())
	if score > high_score:
		draw_text1(screen, "¡high score!", 60, WIDTH  // 2, HEIGHT //4)
		draw_text1(screen, "Record: " + str(score) + " segundos", 80, WIDTH // 2, HEIGHT // 2)
		draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	else:
		draw_text1(screen, "Record: " + str(score) + " segundos", 80, WIDTH // 2, HEIGHT // 2)
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

game_over = False

running = True
start = True
pudge_times = [
		11,20,27,35,42,49,55,59,63,66,70,73,76,79,83,86,89,92,95,97,99,
		101,103,105,107,109,111,113,115,116,117,118,119,120,121
		]
pudge_idx = 0
while running:
	if game_over:
		show_game_over_screen()
		with open("data1.txt", mode="w") as file:
			if score > high_score:
				high_score = score
				file.write(str(score))
		screen.blit(background,(0,0))
		game_over = False
		
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		
		pudge = Pudge()
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		start_time = pygame.time.get_ticks()
		pudge_idx = 0
		score = 0
	
	if start:
		show_go_screen()
		start = False
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		
		pudge = Pudge()
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
		pudge = Pudge()
		all_sprites.add(pudge)
		pudge_list.add(pudge)
		pudge_idx += 1
		if pudge_idx == len(pudge_times):
			pudge_idx = 0

	
	if player1.hp <= 0:
		score += now
		game_over = True
	
	all_sprites.update()
	
	# Checar colisiones - jugador1 - pudge
	hits = pygame.sprite.spritecollide(player1, pudge_list, False)
	for hit in hits:
		
		player1.hp -= 0.8

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)
		
	# Escudo.
	draw_text1(screen, "P1", 20, 10, 6)
	
	draw_hp_bar1(screen, 515, 660, player1.hp)
	draw_text1(screen, str(int(player1.hp)) + "/100", 13, 620, 660)
	draw_hp_bar(screen, player1.rect.x, player1.rect.y - 10, player1.hp)

	for pudge in pudge_list:
		draw_hp_bar2(screen, pudge.rect.x, pudge.rect.y - 10 , pudge.hp)

	draw_mana_bar(screen, 515, 680, player1.mana)
	draw_text1(screen, str(int(player1.mana))+ "/100", 13, 620, 680)

	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)

	pygame.display.flip()
pygame.quit()