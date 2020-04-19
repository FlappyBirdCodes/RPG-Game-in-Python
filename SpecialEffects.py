import pygame
import sys
import random

class SpecialEffect:
    def __init__(self, surface, player1, player2):
        #Instance variables of special effects
        self.surface = surface
        self.player1 = player1
        self.player2 = player2
        self.position_x = None
        self.position_y = None
        self.special_power = None
        self.drawn = False
        self.area_drawn = False
        self.black = (0, 0, 0)

    #Chooses and assigns special power 
    def choose_special_power(self):
        special_powers = ["bullet speed", "bullet speed", "moving speed", "moving speed", "health"]
        random_power = random.choice(special_powers)
        self.special_power = random_power

    #Checks if special item should be drawn at any given time
    def choose_time(self, lst_length = 400):
        numbers = list(range(lst_length))
        random_number = random.choice(numbers)
        if random_number == 3:
            return True

    #Chooses and assigns position of the special item
    def choose_position(self):
        random_x = random.randint(100, 1100)
        random_y = random.randint(50, 650)
        self.position_x = random_x
        self.position_y = random_y

    #Draws special item onto the screen if conditions match
    def draw_special_item(self):
        self.choose_time()
        if self.choose_time() and not self.drawn:
            self.choose_special_power()
            self.choose_position()
            self.drawn = True
        if self.drawn: 
            if self.special_power == "bullet speed":
                pygame.draw.rect(self.surface, self.black, (self.position_x, self.position_y, 50, 50))
            elif self.special_power == "moving speed":
                pygame.draw.rect(self.surface, (0, 0, 100), (self.position_x, self.position_y, 50, 50))
            else:
                pygame.draw.rect(self.surface, (200, 0, 0), (self.position_x, self.position_y, 50, 50))

    #Checks if player has made contact with the special power and returns which player
    def made_contact(self):
        player1_rectangle = pygame.Rect(self.player1.x, self.player1.y, self.player1.width, self.player1.height)
        player1_gun = pygame.Rect(self.player1.gun_x, self.player1.gun_y, self.player1.gun_width, self.player1.gun_height)
        player2_rectangle = pygame.Rect(self.player2.x, self.player2.y, self.player2.width, self.player2.height)
        player2_gun = pygame.Rect(self.player2.x, self.player2.y, self.player2.width, self.player2.height)
        
        if self.position_x and self.position_y:
            special_item_rectangle = pygame.Rect(self.position_x, self.position_y, 50, 50)
            
            if player1_gun.colliderect(special_item_rectangle) or player1_rectangle.colliderect(special_item_rectangle):
                return "Player1"
            if player2_gun.colliderect(special_item_rectangle) or player2_rectangle.colliderect(special_item_rectangle):
                return "Player2"

    def add_power(self):
        #Adds special power to player1 if player1 has made contact with the special item
        if self.made_contact() == "Player1":
            if self.special_power == "bullet speed":
                self.player1.bullet_velocity = self.player1.bullet_speeds[0]
                if len(self.player1.bullet_speeds) > 1:
                    self.player1.bullet_speeds.pop(0)
            elif self.special_power == "moving speed":
                self.player1.velocity = self.player1.player_speeds[0]
                if len(self.player1.player_speeds) > 1:
                    self.player1.player_speeds.pop(0)
            else:
                self.player1.health = 100
            self.drawn = False
        #Adds special power to player2 if player2 has made contact with the special item
        if self.made_contact() == "Player2":
            if self.special_power == "bullet speed":
                self.player2.bullet_velocity = self.player2.bullet_speeds[0]
                if len(self.player2.bullet_speeds) > 1:
                    self.player2.bullet_speeds.pop(0)
            elif self.special_power == "moving speed":
                self.player2.velocity = self.player2.player_speeds[0]
                if len(self.player2.player_speeds) > 1:
                    self.player2.player_speeds.pop(0)
            else:
                self.player2.health = 100
            self.drawn = False

    #Initializes special item with all functioning attributes
    def initialize_special_item(self):
        self.draw_special_item()
        self.made_contact()
        self.add_power()
