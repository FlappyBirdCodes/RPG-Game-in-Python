import pygame
import sys

class Player:
	def __init__(self, surface, player, x, y, controls, velocity, colour, gun_direction):
		#Instance variables of each player
		self.surface = surface
		self.player = player
		self.x = x
		self.y = y
		self.width = 100
		self.height = 100
		self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
		self.health = 100
		self.control = controls
		self.velocity = velocity
		self.colour = colour
		self.gun_x, self.gun_y, self.gun_width, self.gun_height = (self.x + 100, self.y + 35, 40, 30)
		self.gun_direction = gun_direction
		self.right, self.left, self.up, self.down = self.gun_direction
		self.second_player = None
		self.bullet_velocity = 20
		self.bullet_shot = False
		self.bullet_sound = True
		self.current_bullet = []
		self.player_speeds = [13, 14]
		self.bullet_speeds = [22, 24, 26]
		self.is_animation = True
		self.deaths = 0

	#Creates player and gun
	def draw_player(self):
		#Draws player 
		pygame.draw.rect(self.surface, self.colour, (self.x, self.y, self.width, self.height))
		#Checks direction that player is moving and sets the position of the gun accordingly
		if self.right:
			self.gun_x = self.x + 100
			self.gun_y = self.y + 35
			self.gun_width = 40
			self.gun_height = 30
		if self.left:
			self.gun_x = self.x - 40
			self.gun_y = self.y + 35
			self.gun_width = 40
			self.gun_height = 30
		if self.up:
			self.gun_x = self.x + 35
			self.gun_y = self.y - 35
			self.gun_width = 30
			self.gun_height = 40
		if self.down:
			self.gun_x = self.x + 35
			self.gun_y = self.y + 100
			self.gun_width = 30
			self.gun_height = 40
		#Draws gun
		pygame.draw.rect(self.surface, self.colour, (self.gun_x, self.gun_y, self.gun_width, self.gun_height))	
	
	#Allows player to move
	def movement(self, reset = None):
		#Checks if function reset attributes has evaluated to True and changes gun direction accordingly
		if self.has_died() or reset:
			if self.player == "PlayerA":
				self.right, self.left, self.up, self.down = [True, False, False, False]
			elif self.player == "PlayerB":
				self.right, self.left, self.up, self.down = [False, True, False, False]
		#Checks if player is using correct controls and moves player according to direction
		keys = pygame.key.get_pressed()
		if self.control == "letters" and keys[pygame.K_a] or self.control == "arrows" and keys[pygame.K_LEFT]:
			self.x -= self.velocity
			self.right, self.left, self.up, self.down = [False, True, False, False]
		elif self.control == "letters" and keys[pygame.K_d] or self.control == "arrows" and keys[pygame.K_RIGHT]:
			self.x += self.velocity
			self.right, self.left, self.up, self.down = [True, False, False, False]
		elif self.control == "letters" and keys[pygame.K_w] or self.control == "arrows" and keys[pygame.K_UP]:
			self.y -= self.velocity
			self.right, self.left, self.up, self.down = [False, False, True, False]
		elif self.control == "letters" and keys[pygame.K_s] or self.control == "arrows" and keys[pygame.K_DOWN]:
			self.y += self.velocity
			self.right, self.left, self.up, self.down = [False, False, False, True]

	#Prevents player from going off screen and from colliding with the second player
	def create_border(self):
		if self.x <= 0:
			self.x = 0
		if self.x  >= 1100:
			self.x = 1100
		if self.y <= 0:
			self.y = 0
		if self.y >= 600:
			self.y = 600
		player_rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
		second_player_rectangle = pygame.Rect(self.second_player.x, self.second_player.y, self.second_player.width, self.second_player.height)	
		#Checks if player has collided with second player and prevents the players from overlapping
		if player_rectangle.colliderect(second_player_rectangle):
			if self.x >= self.second_player.x - 100 and self.x <= self.second_player.x and self.right:
				self.x = self.second_player.x - 100
			elif self.x <= self.second_player.x + 200 and self.x >= self.second_player.x and self.left:
				self.x = self.second_player.x + 100
			elif self.y >= self.second_player.y - 100 and self.y <= self.second_player.y and self.down:
				self.y = self.second_player.y - 100
			elif self.y <= self.second_player.y + 200 and self.y >= self.second_player.y and self.up:
				self.y = self.second_player.y + 100

	#Shoots bullet from gun and checks if opponent has been hit
	def shoots_bullet(self):
		keys = pygame.key.get_pressed()
		#Checks if shot command has been made
		if keys[pygame.K_f] and self.control == "letters" or keys[pygame.K_RSHIFT] and self.control == "arrows":
			self.bullet_shot = True
		#Sets the direction of the gun
		if self.bullet_shot:
			if self.right:
				bullet_direction = "right"
				bullet_x = self.x + 155
				bullet_y = self.y + 50
			elif self.left:
				bullet_direction = "left"
				bullet_x = self.x - 55
				bullet_y = self.y + 50
			elif self.up:
				bullet_direction = "up"
				bullet_x = self.x + 50
				bullet_y = self.y - 52
			else:
				bullet_direction = "down"
				bullet_x = self.x + 50
				bullet_y = self.y + 155 		
			self.current_bullet.append([bullet_direction, bullet_x, bullet_y])
			#Draws bullet
			pygame.draw.circle(self.surface, (0, 0, 0), (self.current_bullet[0][1], self.current_bullet[0][2]), 18)
			#Changes positioning of the bullet
			if self.current_bullet[0][0] == "right":
				self.current_bullet[0][1] += self.bullet_velocity
			elif self.current_bullet[0][0] == "left":
				self.current_bullet[0][1] -= self.bullet_velocity
			elif self.current_bullet[0][0] == "up":
				self.current_bullet[0][2] -= self.bullet_velocity
			else:
				self.current_bullet[0][2] += self.bullet_velocity
			#Attributes of the bullet and opponent
			bullet_rectangle = pygame.Rect(self.current_bullet[0][1], self.current_bullet[0][2], 36, 36)
			second_player_rectangle = pygame.Rect(self.second_player.x, self.second_player.y, self.second_player.width, self.second_player.height)	
			#Checks if bullet is off the screen
			if self.current_bullet[0][1] >= 1200 or self.current_bullet[0][1] <= 0 or self.current_bullet[0][2] >= 700 or self.current_bullet[0][2] <= 0: 
				self.current_bullet = []
				self.bullet_shot = False
			#Checks if bullet has hit the opponent and sets attributes accordingly
			if bullet_rectangle.colliderect(second_player_rectangle):
				self.current_bullet = []
				self.bullet_shot = False
				self.second_player.colour = (255, 100, 100)
				self.second_player.health -= 5

	#Shows the health of the player
	def show_health(self):
		myfont = pygame.font.SysFont('Comic Sans MS', 40)
		textsurface = myfont.render(str(self.health), False, (0, 0, 0))
		#Blits the position of the text depending on the score
		if self.health == 100:
			self.surface.blit(textsurface, (self.x + 15, self.y + 25))
		elif self.health >= 10 and self.health <= 95:
			self.surface.blit(textsurface, (self.x + 25, self.y + 25))
		else:
			self.surface.blit(textsurface, (self.x + 35, self.y + 25))
			
	#Resets the attributes of player after the player has died
	def has_died(self):
		if self.health == 0:
			if self.player == "PlayerA":
				self.x = 50
				self.y = 300
				self.health = 100
			elif self.player == "PlayerB":
				self.x = 1050
				self.y = 300
				self.health = 100
			self.deaths += 1
			return True

	#Full player movement and shooting
	def play(self):
		self.draw_player()
		self.movement()
		self.create_border()

		#Changes colour back to original after the opponent has been hit
		if self.second_player.colour == (255, 100, 100):
			self.second_player.colour = (100, 100, 100)

		self.has_died()
		self.shoots_bullet()
		self.show_health()