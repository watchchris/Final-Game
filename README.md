# Final-Game
Final Game for CIS 120

“Get Rich with Chris” will be a basic arcade game that will use pygame and simpleGE.

The game is still based on collecting as much money as falling from the sky, but the goal will be to collect a certain amount to continue to get the highest score possible. The speed at which the coins fall will increase. The next addition to the game will be a coin that will increase the user set for a limited time, allowing the user to reach higher scores than possible with the original game. If a user catches the coin, the speed will be increased from 5 to 8 for 10 seconds. After 10 seconds, the user will return to speed five and continue at that speed until the game is over or another purple coin falls from the sky. The purple coin will only fall from the sky rarely. Once the game is over the user will be shown there score and be giving the option to play the game again or exit.

 
The game is a standard 2D two-state system. The user will first to sent to the intro scene. This scene will take the user response sending them into the game play or exiting the game completely. If the user chooses to play the game will run for a set amount of time and after the timer has expired it will send the users score back to the intro scene.



 
This scene has four main functions.
1.	Instruction – a label the user cannot interact with, but it tells the user how to play the game.
2.	playButton –  Starts the game
3.	quitButton – End the game and exit the program
4.	prevScore – Tells the user the score on the most recent round. This will be on a label the user can not interact with.

If the user chooses to start the game they will be move to the next screen where they will see the character Chris at the bottom of the screen and they will be able to move him side to side trying to collect as many coin as possible in the provided time. At the end of the time, the user will be taken back to the intro screen, where the user will be able to see the exact number of coins they collected in the score label. At this point, the user can decide if they want to click the start button and play the game again or if they want to quit the game and exit the program by clicking the quit button.

 


The game class will consist of:
1.	chris- the instance of the Chris class
2.	coins – a list of instances of the Coin class
3.	lblScore- an instance of the LabelScore class
4.	lblTime- an instance of the LabelTime class
5.	purpleCoin – a list of instance of the Purplecoin class



Init(score) :
	Set image to skyline
	Set reponse to “Start”
	Create instructions 
	Explain the instructions
	Set instructions center to (320, 240)
	Set instructions size to (500, 250)
	
	Copy score parameter to previousScore attribute
	Create labelScore
	Set text to  “Last score: to previousScore
	Set center to (320, 400)

	Create quitButton
	Set too “Quit”
	Set center to (550, 400)
	
	Add labelInstruction, labelScore, quitButton and startButton to sprites

Create process():
	If the quit button is pressed:
	Set response to “Quit”
	End the game
	If the “Start” button is pressed 
	Set response to “Start”
	Start the game

Init:
	Set image to skyline
	Create timer
	Set timer total to 15 seconds
	Set initial score to 0
	Initialize moneySound to money sound effect
	Create instance of Chris -> chris
	Create list of money (10) money instances -> money
	Create purplecoin set to 1 -> purple
	Create instance for labelScore
	Create instance for labelTime
	Add chris, money, purple,  labelScore, labelTime to sprites

Process:
	For each money in the money list:
	If that money collides with chris:
	Play the money sound (moneySound)
	Reset the money
	Add one to the score
	Update labelScore to new score

	For each purple in purple
	If purple collides with chris
	Play the powerup sound 
	Reset the purple
	Change Chris speed to original plus 10

	Update the labelTimer with the current time left
	If the timer left is less than 0:
	Print the score and stop the game 
	
Components of the game

	Each of the visuals of the game is an extension of simpleGE element
	
Chris
	Chris is a subclass of simpleGE.Sprite
	The image an image I created using Final Cut Pro
	Size should be 50 by 50 
	Transparent background Is preferred
	Initial position is center bottom of screen 
	moveSpeed attribute is an integer start at 5 

init:
	Set image to chris.png
	Set size to 50 by 50 
	Set position to (320, 400)
	Set moveSpeed to 5 

Process:
	If left key is pressed
	Subtract move speed from x
	If right key is pressed 
add moveSpeed to x

Money
	Money is a subclass of simpleGE.Sprite
	The image is an encumbrance- free image
	It has a transparent background
	Reset method sets money to top of screen in random position
	Fall speed is 3 to 8 ppf
	Money falls down screen 
	If money passes bottom of screen, reset 
	Coin had 3 methds
		Init – standard initialization
		Reset – custom method to set speed and position
		checkBounds – overwrite existing checkBounds to handle bottom of screen

init():
	set image to money.png	
	set size to 25 by 25
	call reset()
reset():
	set y to 10 
	set x to random from 0 to screen width 
	set dy to random between 3 and 8 

Purple:
	Purple is a subclass of simpleGE.Sprite
	The image has a transparent background 
	Reset method set purple to top of screen in random position
	Purple falls at speed 7 to 8
	If purple passes bottom of screen,reset

Init():
	set image to money.png	
	set size to 25 by 25
	call reset()

Reset():
	set y to 1
	set x to random from 0 to screen width 
	set dy to random between 7 and 8 

checkBounds():
	If bottom is larger than screen width:
	Calls reset()

labelScore
	labelScore is a subclass of the simpleGE.Label
	
	init():
	set text to “TimeLeft: 15”
	set center to (500, 30)

Main() function

	The main function will manage the high-level state transition between intro and start states.
	Standard main loop
		Instruction – an instance of the instruction class
		Game -  an instance of the game class
		keepGoing the Boolean sentry
		score – the current score
	
main():
	Set keepGoing to True
	Set score to zero
	While keepGoing is true: 
	Create an instance of instruction -> instructions
	Pass the current score to instruction as parameter
	Start instruction 
	When instruction ends, 
	If instructions.response is “Start”:
	Create an instance of Game -> game
	Start game
	When game is over, copy game.score to score
	If instruction.response is any other than “Start”
	Set keepGoing to False, which will end the game 




 
Create by Chris Johnson using Final Cut Pro

  
Coins download from 

PickupCoin.wav, powerup.wav   downloaded from sfxr.com 


 

Skyline.jpg downloaded from https://unsplash.com/photos/photography-of-cityscape-heIaYq6A7tg

![image](https://github.com/watchchris/Final-Game/assets/169475928/20808267-e10b-4544-9f92-fb31cd004f92)
