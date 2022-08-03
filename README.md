# Computer-Vision-Rock-Paper-Scissors Project
In this lab, I create an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

The project is made up of four Milestones, and these are captured in files provided above.

## Milestone 1: Creating the model
This milestone will involve two tasks namely: Creating the image project model on [Teachable Machine](https://teachablemachine.withgoogle.com/), and downloading it. This model is called "keras_model.h5"

## Milestone 2: Installing the dependencies
We will be creating and activating the environment in conda terminal using the following codes:
* $ conda create --name presh
* $ conda activate presh

This environment will be called "presh". This is the environment where we will install and import the necessary python packages for the project. The downloaded libraries include opencv-python, tensorflow, and ipykernel. The code below shows how this was done.

## Milestone 3: Create a Rock-Paper-Scissors Game
Here, I will create a .py file called manual_rps.py that will be used to play the game without the camera.

A random module is used to pick a random option between rock, paper, and scissors and the input function to get the user's choice.

Two functions: get_computer_choice and get_user_choice, are then created. The first function randomly picks an option between "Rock", "Paper", and "Scissors" and returns the choice. The second function asks the user for an input and return it.

if-elif-else statements are then used to now choose a winner based on the classic rules of Rock-Paper-Scissors. This is wrapped in a function called get-winner.

A function called play() is then used to simulate the game.

## Milestone 4: Use the Camera to play the Rock-Paper-Scissors Game
Here, I will create a .py file called Camera_RockPaperScissors.py that will be used to play the game with the camera.

A new function called get_prediction that will return the output of the model used earlier is created.

A countdown timer that carries out a countdown before the input is requested for is added to the code.

Adding a method which takes one input at a time.
