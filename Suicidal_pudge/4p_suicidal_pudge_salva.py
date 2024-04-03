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

def draw_text(surface, text, size, x, y, color):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, color)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text1(surface, text, size, x, y, color=WHITE):
	draw_text(surface, text, size, x, y, color)

def draw_text2(surface, text, size, x, y, color=BLACK):
	draw_text(surface, text, size, x, y, color)

def draw_hp_bar(surface, x, y, percentage, color1=GREEN, color2=WHITE):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, color1, fill)
	pygame.draw.rect(surface, color2, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	draw_hp_bar(surface, x, y, percentage, color1=BROWN, color2=BROWN)

def draw_mana_bar(surface, x, y, percentage):
	draw_hp_bar(surface, x, y, percentage, color1=BLUE)

player_keys = [
	#Player1 keys
	{
  'r': pygame.K_d, #right
  'l': pygame.K_a, #left
  'u': pygame.K_w, #up
  'd': pygame.K_s, #down
  's': None, #shoot
  },
	#Player2 keys
	{
  'r': pygame.K_RIGHT,
  'l': pygame.K_LEFT,
  'u': pygame.K_UP,
  'd': pygame.K_DOWN,
  's': None,
  },
	#Player3 keys
	{
  'r': pygame.K_h,
  'l': pygame.K_f,
  'u': pygame.K_t,
  'd': pygame.K_g,
  's': None,
  },
	#Player4 keys
	{
  'r': pygame.K_l,
  'l': pygame.K_j,
  'u': pygame.K_i,
  'd': pygame.K_k,
  's': None,
  },
	]

class Player(pygame.sprite.Sprite):
	def __init__(self, player_number, x, y):
		super().__init__()
		self.number = player_number
		self.initial_position = (x,y)
		self.keys = player_keys[self.number - 1]
		self.image = pygame.transform.scale(pygame.image.load("img/crystal_maiden.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.reset()
	
	def reset(self):
		self.rect.x, self.rect.y = self.initial_position
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
		if keystate[self.keys['l']]:
			self.speed_x = -3
		if keystate[self.keys['r']]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[self.keys['u']]:
			self.speed_y = -3
		if keystate[self.keys['d']]:
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

def direction(a,b):
	#x, y vector from a to b
	#pitagoras distance between a and b
	if hasattr(a,'rect'):
		xa = a.rect.centerx
		ya = a.rect.centery
	else:
		xa, ya = a
	if hasattr(b,'rect'):
		xb = b.rect.centerx
		yb = b.rect.centery
	else:
		xb, yb = b
	dx = xb - xa
	dy = yb - ya
	return dx, dy

def distance(a,b):
	#pitagoras distance between a and b
	dx, dy = direction(a,b)
	return (dx**2 + dy**2)**(1/2)

def u_direction(a,b):
	#x,y unitary vector from a to b
	ux, uy = 0,0
	radio = distance(a,b)
	if radio != 0:
		dx, dy = direction(a,b)
		ux, uy = dx/radio, dy/radio
	return ux, uy

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
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		
		if len(players) > 0:
			target = sorted(players, key = lambda x: distance(self,x))[0]
			x,y = u_direction(self, target)
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y
			
def show_go_screen():
	screen.fill(BLACK)#(background, [0,0])
	draw_text1(screen, "Suicidal Pudge", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Stay away from suicidal pudge", 20, WIDTH // 2, HEIGHT // 2)
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

pudge_images = [pygame.transform.scale(pygame.image.load(img).convert(),(50,65))
				for img in ["img/pudge.png"]]

def show_game_over_screen(player_n=1):
	screen.fill(BLACK)
	draw_text1(screen, f"Player {player_n} WINS", 20, WIDTH // 2, HEIGHT // 2)
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

def game_over(n=1):
	show_game_over_screen(n)
	screen.blit(background,(0,0))
	players.empty()
	all_sprites.empty()
	pudge_list.empty()
	pudge = Pudge()
	players.add(player1, player2, player3, player4)
	[p.reset() for p in players]
	all_sprites.add(player1, player2, player3, player4, pudge)
	pudge_list.add(pudge)
	

running = True
start = True
pudge_times = [
		11,20,27,35,42,49,55,59,63,66,70,73,76,79,83,86,89,92,95,97,99,
		101,103,105,107,109,111,113,115,116,117,118,119,120,121
		]
pudge_idx = 0
while running:
	
	if start:
		show_go_screen()
		start = False
		players = pygame.sprite.Group()
		all_sprites = pygame.sprite.Group()
		pudge_list = pygame.sprite.Group()
		player1 = Player(1, 500, 133)
		player2 = Player(2, 900, 133)
		player3 = Player(3, 500, 366)
		player4 = Player(4, 900, 366)
		pudge = Pudge()
		players.add(player1, player2, player3, player4)
		all_sprites.add(player1, player2, player3, player4, pudge)
		pudge_list.add(pudge)
		start_time = pygame.time.get_ticks()

	if len(players) == 1:
		game_over(players.sprites()[0].number)
		start_time = pygame.time.get_ticks()
		pudge_idx = 0

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

	# Checar colisiones - jugador4 - pudge
	hits = pygame.sprite.spritecollide(player4, pudge_list, False)
	for hit in hits:
		
		player4.hp -= 0.8

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)
	
	# Escudo.
	draw_text2(screen, "P1", 20, 10, 6)
	draw_text2(screen, "P2", 20, 300, 6)
	draw_text2(screen, "P3", 20, 600, 6)
	draw_text2(screen, "P4", 20, 900, 6)

	draw_hp_bar(screen, 20, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 45, 6)
	draw_hp_bar(screen, player1.rect.x, player1.rect.y - 10, player1.hp)

	draw_hp_bar(screen, 315, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 345, 6)
	draw_hp_bar(screen, player2.rect.x, player2.rect.y - 10, player2.hp)

	draw_hp_bar(screen, 615, 5, player3.hp)
	draw_text2(screen, str(int(player3.hp))+ "/100", 10, 645, 6)
	draw_hp_bar(screen, player3.rect.x, player3.rect.y - 10, player3.hp)

	draw_hp_bar(screen, 915, 5, player4.hp)
	draw_text2(screen, str(int(player4.hp))+ "/100", 10, 945, 6)
	draw_hp_bar(screen, player4.rect.x, player4.rect.y - 10, player4.hp)

	for pudge in pudge_list:
		draw_hp_bar2(screen, pudge.rect.x, pudge.rect.y - 10 , pudge.hp)
		#draw_text1(screen, str(int(pudge.hp)) + "/100", 10, pudge.rect.centerx + 20, pudge.rect.y - 10)

	draw_mana_bar(screen, 20, 15, player1.mana)
	draw_text1(screen, str(int(player1.mana))+ "/100", 10, 45, 16)

	draw_mana_bar(screen, 315, 15, player2.mana)
	draw_text1(screen, str(int(player2.mana))+ "/100", 10, 345, 16)

	draw_mana_bar(screen, 615, 15, player3.mana)
	draw_text1(screen, str(int(player3.mana))+ "/100", 10, 645, 16)

	draw_mana_bar(screen, 915, 15, player4.mana)
	draw_text1(screen, f"{player4.mana}/100", 10, 945, 16)

	#reloj
	draw_text1(screen, f"{((now//60)+60)%60}:{(now+60)%(60)}", 30, 570, 50)
	pygame.display.flip()

pygame.quit()