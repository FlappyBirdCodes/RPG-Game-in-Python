#Date: March 21st, 2020
#Written by: Me and my friend
#Description: First project made in pygame, simple RPG multiplayer game

import sys
import pygame
import time
from Players import Player
from Screens import Screen
from SpecialEffects import SpecialEffect
from Domination import Domination

#Initializing PyGame Module
pygame.init()
pygame.display.set_caption("RPG Game")

#Setting up screen for game
screen_width = 1200
screen_height = 700
size = (screen_width, screen_height)
win = pygame.display.set_mode(size)

#Setting up framerate for game
clock = pygame.time.Clock()

#Colours in the game
shadow = (192, 192, 192)
black = (0, 0, 0)

#Players in the game
player1 = Player(win, "PlayerA", 50, 300, "letters", 12, (100, 100, 100), [True, False, False, False])
player2 = Player(win, "PlayerB", 1050, 300, "arrows", 12, (100, 100, 100), [False, True, False, False])

#Setting the second player of each player 
player1.second_player = player2
player2.second_player = player1

#Indicates the screen that the user is currently on
on_home_screen = True
on_option_screen = False
on_fight_to_death_screen = False
on_domination_screen = False
game_started = False
on_end_screen = False

#Indicates which game mode the user has just finished playing
played_fight_to_death = False
played_domination = False

#Special powers in the game
special_power = SpecialEffect(win, player1, player2)
domination = Domination(win, player1, player2)

#Different screens of the game
home_screen = Screen(win)
option_screen = Screen(win)
fight_to_death_screen = Screen(win)
domination_screen = Screen(win, domination)
end_screen = Screen(win)

#Music and sound effects for the game
music = pygame.mixer.music.load("Music.mp3")
pygame.mixer.music.play(-1)

while True:
	#Setting frames per second
	clock.tick(60)

	#Exiting game if user pressed exit button
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		#Checks if mouse has been pressed
		if event.type == pygame.MOUSEBUTTONDOWN:
			
			#Checks if Start Game button has been pressed
			if on_home_screen and home_screen.button_pressed(430, 500, 300, 100):
				on_home_screen = False
				on_option_screen = True

			#Checks if Back button has been pressed
			if on_option_screen and option_screen.button_pressed(0, 0, 130, 100):
				on_option_screen = False
				on_home_screen = True
				home_screen.initialize_players(player1, player2)

			#Checks if Fight to Death button
			if on_option_screen and option_screen.button_pressed(420, 170, 340, 100):
				on_option_screen = False
				on_fight_to_death_screen = True
				game_started = True

			#Checks if Domination button has been pressed
			if on_option_screen and option_screen.button_pressed(420, 370, 340, 100):
				on_option_screen = False
				on_domination_screen = True
				game_started = True

			#Checks if user has chosen to play game mode again
			if on_end_screen and end_screen.button_pressed(700, 450, 340, 100):
				on_option_screen = False
				game_started = True
				#Plays to fight to death again
				if played_fight_to_death:
					on_fight_to_death_screen = True
					played_fight_to_death = False
				#Plays domination again
				elif played_domination:
					on_domination_screen = True
					played_domination = False

			#Checks if Other Games button has been pressed
			if on_end_screen and end_screen.button_pressed(120, 450, 340, 100):
				on_end_screen = False
				on_option_screen = True
				played_fight_to_death = False
				played_domination = False

	#Checks if user is currently on the home screen
	if on_home_screen:
		home_screen.create_home_screen()
		player1.play()
		player2.play()
		
	#Checks if user is currently on the option screen
	elif on_option_screen:
		option_screen.create_option_screen()

	#Checks if user is currently on the fight to death screen
	elif on_fight_to_death_screen:
		#Resets attributes of characters if game has started
		if game_started:
			fight_to_death_screen.initialize_players(player1, player2)
			game_started = False

		fight_to_death_screen.create_fight_to_death_screen(player1, player2)
		special_power.initialize_special_item()

		#Ends game if either player dies 5 times
		if player1.deaths == 5 or player2.deaths == 5:
			on_fight_to_death_screen = False
			game_started = True
			played_fight_to_death = True
			on_end_screen = True
			special_power.drawn = False
			time.sleep(1)
		if player1.deaths == 5:
			winner = player1
		elif player2.deaths == 5:
			winner = player2

	#Checks if user is curently on the domination screen
	elif on_domination_screen:
		#Resets attributes of characters if game has started
		if game_started:
			domination_screen.initialize_players(player1, player2)
			game_started = False

		domination_screen.create_domination_screen(player1, player2)
		special_power.initialize_special_item()
		domination.initialize_domination_area()
		domination_screen.create_text(45, "First to 2500 Points Wins", (350, 630))
		player1.play()
		player2.play()

		#Ends game if either player has 2500 points
		if domination.player1_points == 2500 or domination.player2_points == 2500:
			on_domination_screen = False
			game_started = True
			played_domination = True
			on_end_screen = True
			special_power.drawn = False
			time.sleep(1)
		if domination.player1_points == 2500:
			domination.player1_points = 0
			domination.player2_points = 0
			winner = player2
		elif domination.player2_points == 2500:
			domination.player1_points = 0
			domination.player2_points = 0
			winner = player1

	#Checks if user is currently on the end screen
	elif on_end_screen:
		end_screen.create_end_screen(winner)

	pygame.display.update()