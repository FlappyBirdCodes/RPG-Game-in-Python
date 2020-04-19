import pygame
import sys
from Domination import Domination

class Screen:
    def __init__(self, surface, domination = None):
        #Instance variables of each screen
        self.surface = surface
        self.domination = domination
        self.background_colour = (192, 192, 192)
        self.button_colour = (131, 139, 139)
        self.black = (0, 0, 0)

    #Draws text onto the screen
    def create_text(self, font_size, text, position):
        myfont = pygame.font.SysFont('Comic Sans MS', font_size)
        textsurface = myfont.render(text, False, self.black)
        self.surface.blit(textsurface, position)

    #Creates button on the screen
    def create_button(self, x, y, width, height, font_size, button_colour, text, position):
        pygame.draw.rect(self.surface, button_colour, (x, y, width, height))
        pygame.draw.line(self.surface, self.black, (x, y), (x, y + height), 5)
        pygame.draw.line(self.surface, self.black, (x + width, y), (x + width, y + height), 5)
        pygame.draw.line(self.surface, self.black, (x, y), (x + width, y), 5)
        pygame.draw.line(self.surface, self.black, (x, y + height), (x + width, y + height), 5)
        self.create_text(font_size, text, position)

    #Changes the colour of the button when the mouse is on the button
    def change_button_colour(self, x, y, width, height, font_size, text, position):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect(x, y, width, height).collidepoint(mouse_pos):
            self.create_button(x, y, width, height, font_size, (255, 100, 100), text, position)

    #Initializes button with all capabilities
    def initialize_button(self, x, y, width, height, font_size, button_colour, text, position):
        self.create_button(x, y, width, height, font_size, button_colour, text, position)
        self.change_button_colour(x, y, width, height, font_size, text, position)

    #Checks if button has been pressed
    def button_pressed(self, x, y, width, height):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect(x, y, width, height).collidepoint(mouse_pos):
            return True

    #Resets the attributes of all players to original form
    def initialize_players(self, player1, player2):
        player1.x, player1.y = (50, 300)
        player2.x, player2.y = (1050, 300)        
        player1.health, player2.health = (100, 100)
        player1.deaths, player2.deaths = (0, 0)
        player1.movement(True)
        player2.movement(True)
        player1.velocity, player2.velocity = (12, 12)
        player1.bullet_velocity, player2.bullet_velocity = (20, 20)
        player1.player_speeds, player1.bullet_speeds = [[13, 14], [22, 24, 26]]
        player2.player_speeds, player2.bullet_speeds = [[13, 14], [22, 24, 26]]

    #Creates the home screen of the game
    def create_home_screen(self):
        self.surface.fill(self.background_colour)
        self.create_text(100, "CrossFire", (365, 50))
        self.initialize_button(430, 500, 300, 100, 50, self.button_colour, "Start Game", (440, 510))

    #Creates the option screen of the game
    def create_option_screen(self):
        self.surface.fill(self.background_colour)
        self.initialize_button(420, 170, 340, 100, 45, self.button_colour, "Fight to Death", (435, 185))
        self.initialize_button(420, 370, 340, 100, 45, self.button_colour, "Domination", (470, 390))
        self.initialize_button(0, 0, 130, 100, 50, self.button_colour, "Back", (10, 10))

    #Creates the end screen of the game
    def create_end_screen(self, winner):        
        self.surface.fill(self.background_colour)
        self.create_text(80, winner.second_player.player + " has won!", (270, 100))
        self.initialize_button(120, 450, 340, 100, 45, self.button_colour, "Other Games", (145, 465))
        self.initialize_button(700, 450, 340, 100, 45, self.button_colour, "Play Again", (760, 465))

    #Creates the fight to death screen of the game
    def create_fight_to_death_screen(self, player1, player2):
        self.surface.fill(self.background_colour)
        self.create_text(45, "First to 5 Points Wins", (360, 630))
        self.create_text(45, "PlayerA: " + str(player2.deaths), (30, 10))
        self.create_text(45, "PlayerB: " + str(player1.deaths), (950, 10))
        player1.play()
        player2.play()

    #Creates the domination screen of the game
    def create_domination_screen(self, player1, player2):
        self.surface.fill(self.background_colour)
        self.create_text(45, "PlayerA: " + str(self.domination.player1_points), (30, 10))
        self.create_text(45, "PlayerB: " + str(self.domination.player2_points), (910, 10))




