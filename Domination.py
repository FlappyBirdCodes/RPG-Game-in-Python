import pygame
import sys
import random
from SpecialEffects import SpecialEffect

class Domination:
    def __init__(self, surface, player1, player2):
        self.surface = surface
        self.player1 = player1
        self.player2 = player2
        self.player1_points = 0
        self.player2_points = 0
        self.area_x = None
        self.area_y = None
        self.area_width = None
        self.area_height = None
        self.area_colour = (200, 0, 0)

    #Chooses domination area for the domination game mode
    def create_domination_area(self):
        random_x = random.randint(100, 500)
        random_y = random.randint(0, 600)
        random_width = random.randint(100, 500)
        random_height = random.randint(100, 500)
        self.area_x, self.area_y, self.area_width, self.area_height = (random_x, random_y, random_width, random_height)
        
    def draw_domination_area(self):
        pygame.draw.rect(self.surface, self.area_colour, (self.area_x, self.area_y, self.area_width, self.area_height))

    #Checks if either players are in the rectangle area
    def in_domination_area(self, player1, player2):
        player1_rectangle = pygame.Rect(player1.x, player1.y, player1.width, player1.height)
        player2_rectangle = pygame.Rect(player2.x, player2.y, player2.width, player2.height)
        domination_rectangle = pygame.Rect(self.area_x, self.area_y, self.area_width, self.area_height)
        
        if player1_rectangle.colliderect(domination_rectangle) and player2_rectangle.colliderect(domination_rectangle):
            self.area_colour = (200, 0, 0)
        elif player1_rectangle.colliderect(domination_rectangle):
            self.area_colour = (0, 0, 128)
            self.player1_points += 1    
        elif player2_rectangle.colliderect(domination_rectangle):
            self.area_colour = (0, 0, 128)
            self.player2_points += 1
        else:
            self.area_colour = (200, 0, 0)

    def initialize_domination_area(self):
        if self.area_x is None or SpecialEffect.choose_time(100):
            self.create_domination_area()
        self.in_domination_area(self.player1, self.player2)
        self.draw_domination_area()