# RPG-Game-in-Python
This project uses python and pygame to make a simple RPG multi-player shooter game. The game is played with two players, using different controls on the keyboard. There are two different game modes, the regular game mode and the domination game mode. In the regular game mode, the person who gets a certain amount of kills wins. In the domination game mode, the person with the most domination points wins. This game utilizes basic physics as users cannot move through each other or off the screen. 

Using the random module in python, random special powers are also drawn on the screen at random locations on the screen. If a user makes contact with these powers, they will gain an advantage for the rest of the game (shoot faster, move faster etc.). If a player is able to attack their opponent at close range, the "knife" special power will be activated, meaning that the opponent will lose points until they're able to get away from the "knife".

# Skills
In making this game, I had to use object oriented programming to create objects that represented players in the game. By doing this, I was able to substantially decrease the amount of code I had to write, thereby making the program more readable and efficient. Also, I had optimized many trivial aspects of the program such as writing functions that handled drawing and updating the screen. 
