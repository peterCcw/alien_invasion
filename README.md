# Alien Invasion
Alien Invasion is my implementation of the game based on tutorial from "Python Crash Course, 2nd Edition". It contains
some additional features which expand project from the book.
### Table of contents
* [Description](#description)
    * [About](#about)
    * [Additional features](#additional-features)
    * [Images and sounds](#images-and-sounds)
* [Technologies](#technologies)
* [How to play](#how-to-play)
    * [Installation](#installation)
    * [Manual](#manual)
    
    
### Description  
##### About
This project was made to practise **Python 3**. It is based on tutorial from the book, but I added some original 
features to make the game more similar to the arcade ***Space Invaders*** game. Game is very simple, my main goal was to
write good quality code according to the **Python Enhancement Proposals**. I also wanted to work with **VCS** and have 
some fun with creating new features to the game.
##### Additional features
Besides content provided by tutorial, the game contains also:
* **Bouncing movement of aliens** - aliens go little up and down during their movement
* **Saving best score** - best score is saved to the file
* **Sounds** - added sounds of shoots, explosions etc.
* **Shooting aliens** - aliens also can shoot and destroy the player
* **Covers** - added destroyable covers for the player
##### Images and sounds
###### Images
Images of the player's ship and aliens are part of the tutorial and are downloaded from 
[here](https://ehmatthes.github.io/pcc_2e/).
Icon and images of covers were made by me with **Microsoft Paint**.
###### Sounds
Sounds were downloaded from [**Freesound**](https://freesound.org/). Exact list is below:
* [**Alien blaster**](https://freesound.org/people/astrand/sounds/328011/)
* [**Player blaster**](https://freesound.org/people/SeanSecret/sounds/440667/)
* [**Alien explosion**](https://freesound.org/people/Cyberios/sounds/145788/)
* [**Cover damage**](https://freesound.org/people/BranRainey/sounds/108737/)
* [**Player explosion**](https://freesound.org/people/V-ktor/sounds/435414/)
* [**Level Up**](https://freesound.org/people/Beetlemuse/sounds/528958/)
* [**End of Game**](https://freesound.org/people/dmjames/sounds/140095/)
### Technologies
* [**Python 3.8.5**](https://www.python.org/)
* [**Pygame 1.9.6**](https://www.pygame.org/)
### How to play
##### Launching up
Requirements:
both mentioned in [Technologies](#technologies) section. If you do not have **Pygame** installed, use:
```commandline
pip install pygame
```
Download all files manually and place them in a specific directory.
If you have git installed, you can also use code below (in specific directory):
```commandline
git clone https://github.com/peterCcw/alien_invasion
```
Move to directory with the game files and use:
```commandline
python alien_invasion.py
```
The game should start in a window.

##### Manual
Game runs in the window 1024x768 pix. To start game click **Play** button with the mouse or press **G** key.
Use arrows to move ship left and right. To shoot press **Space**. You can shoot max three times at once (three bullets 
visible) Your goal is to destroy all aliens. You can hide behind covers, which can be damaged and destroyed by the shots
of aliens or yours. Your ship will be destroyed if the alien hits you, collide with you or if the alien reaches bottom 
edge of the screen.

For every destroyed alien you get points. If you destroy all aliens, you start new level, the game becomes faster and 
you get more point for each alien. If you want to reset best score, delete **best_score.txt** file.

![Interface](/readme_images/interface.png)