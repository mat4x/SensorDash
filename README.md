
# SensorDash

*Immerse yourself into the gaming experience with not just button presses and cursor movement, but using motion.*

Inspired by the classic arcade game **[Dance Dance Revolution (DDR)](https://en.wikipedia.org/wiki/Dance_Dance_Revolution "DDR")**, this project has seamlessly integrated Android devices into a Python-based gaming platform to create _**SensorDash**_. It is a game where players must match a sequences of arrows on screen, by swinging their arms.

The objective is simple: mimic the movements, swing and dance to the rhythm, and strive for the high score.

## System Requirements
- 2 Android phones with [SensorStream application](https://play.google.com/store/apps/details?id=com.sensorsensei)
- Windows system with Python v3.x and [pygame](https://pypi.org/project/pygame/) installed.

## How to play
![menu screenshot](https://drive.google.com/uc?id=10KssBpmusdoRCWdiw6VcSB9JkLTeuQWv "Game menu")
- Download the `code` folder from the repository.
- Connect all the 3 devices onto the same LAN network.
- Hold the two android devices with the (SensorStream app installed) in both of the player's hands.
- Launch the game on you PC/laptop (run the `main.py` file)
- Input the given IP address on the python console into the SensorSteam app on the android devices.<br>_Note that each device must have the different port number (5000/5001)._
- Switch on the **Gyroscope** sensor toggle switchs in the app. If successful you will see `CONNECTED` printed onto the console.
- Press the `S` key (or swing your left hand down) to start the game.

#### Gameplay
- Arrows spawn from the bottom of the screen moving towards the top. When they reach the target arrows on the top swing your arm in the direction the arrow is facing.
- The screen is divided into two; the left side arrows indicate left hand swing, similarly for the right side.
- Score are awarded according to the accuracy of the motion; arrows being close to the target.

## Technical details
SensorStream app allows transmitting Android sensor data over a wireless network. This program uses the gyroscope sensor data to identify the player arm 'swing motion' and ' swing direction' to get the input.

The main game has two thread processes running simultaneously - the **game app** and the **sensor server**.
The **game app** is responsible for handling the game loop and event like spawning arrows and their motion, checking user inputs and awarding points.
The **sensor server** gather data from the Android devices and calculates the user inputs.

The arrow spawning the controlled using a text file `levels.txt` that can be randomly generated using `level_gen.py` file.

## Customize the game
The game controls like _arrow movement speed, background song, scoring system_ can be changed in the `DashClass.py` file.

The level's "easiness" can be changed in the `level_gen.py` file.

##
A mini-project by:
[Mayur Sharma](https://github.com/mat4x), [Rohan deep Kujur](https://github.com/Rdk07145) and [Atharva Karve](https://github.com/Atharva-Karve).


Special thanks to [Priyankar Kumar's](https://github.com/priyankark/SensorStreamServer) SensorStream application for making this project a success.