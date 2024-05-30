# Classic DnD Text Adventure Game

This game is a throw back to the classic style text adventure games of old. The basic premise is that you enter a command and the game will execute that command if possible, such as 'move north', moving the player North, or 'get item', allowing the player to collect an item. The overarching story in the game is that the player is a villager from the lost village, a village that is currently being terrorised by the local Vampire Lord residing in the Whispering Crypt. So it is up to the player to explore the surrounding lands and collect all the necessary items and blessing to prepare themselves to be able to deal with the vampire menace. Failing to adequately prepare themselves will lead to their untimely doom and the eventual destruction of their village. 

![Launch Screen](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/viewports.png?raw=true)

## User Stories
- I love the old school feel to it.
- The need to type every action gives you a sense of intimacy with the game.
- Good fun, I had to try a couple of times before finding all the items and beating the boss.

## Features 

The text adventure game is a very simple premise. The player inputs available commands and the game with execute those commands if possible. To assist with what commands are available, there is an onscreen prompt showing the user their available interactions and options for movement. The player then needs to explore the various rooms, collecting items along the way and iteracting with terrain features to gain their buff. Once the 'dungeon' is fully explored the user can then take on the games boss, and if they have collected all the necessary items the will win, otherwise the will suffer defeat. 

### Existing Features

- __The Game__

  - The game is interacted with through a terminal window.
  - The user can give commands to their avatar by typing in the requested command into the terminal.
  - If the command is valid the avatar will attempt to perform said action.

![The Game](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/game.png?raw=true)

- __Giving Commands__

  - The user only needs to type in their required action to perform it.
  - Typing 'move', 'get', 'use' will allow the user's avatar to perform the corresponding action
  - Following an action move with the direction, item, or terrain feature will complete the action.
  - For example, 'get item', 'move north' or 'use terrain feature' will all execute their given task. 

![Using Commands](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/stockade-1.png?raw=true)

- __The user HUD__

  - Within the terminal of the game, the user will always be presented with their current location, available interactions and current inventory.
  - These user displays will change depending on which room they are in and how many items they have collected.

![HUD Display](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/guess-word.png?raw=true)

- __Message Bar__ 

- This will display the effects of the users last command

![Player message](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/attempts.png?raw=true)

- __Victory and Game Over state__

- Whether the player is able to win or not, they will be displayed with a corresponding end message and then be presented with the game over screen.
- From here the user can choose to either play again or exit the game by follwing the on screen prompts.

![Victory and Game Over state](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/victory.png?raw=true)

### Features Left to Implement

- In game map display
- Boss room prepared message to alert the player that the boss is ahead
- Potentially adding a combat simulator (such as random damage from the players avatar to the boss, and vice versa, adjusting for current inventory increasing said damage)

## Testing 

- The text adventure game was continuosly tested throughout its development within the gitpod terminal along with being tested once deployed to Heroku.
- Numerous commands were entered to test that no errors occured and if incorrect commands were entered by the user that the user was alerted to this rather than the game crashing, or throwing an unknown error message.
- The text adventure game was tested on the following web browsers: Google Chrome and Microsoft Edge.
- I have checked that the game loads a new game correctly once prompted to do so.
- I have checked that the 'help' command presents the user with an informative display of all available commands to them.

### Bugs

- There is currently a bug on the Game Over screen that if the user enters something other than the onscreen prompts it displays the correct user input error but then loops back to the boss battle victory or loss text.

### Validator Testing 

- Python
  - A few errors were found and some warnings were noted when passing through the official [(CI Python Linter](https://pep8ci.herokuapp.com/)
    - These erros were "E203 whitespace before ' ", "E501 line too long", "E128 continuation line under-indented for visual indent " and "E722 do not use bare 'except' "
    - These warnings were "W291 trailing whitespace ", "W293 blank line contains whitespace " (when trying to fix these messages by removing blank or trailing whitespace it would incur a different warning of "E231 missing whitespace after ' ")

### Unfixed Bugs

- Game Over screen bug as stated in the bugs section, with incorrect user input causing the wrong display message to be raised. 

## Deployment

1. **Sign Up/Login to Heroku**
      - If you haven't already, sign up for a Heroku account at [Heroku's website](https://www.heroku.com/) or log in if you already have an account.

  2. **Create a New App on Heroku**
       - Once logged in, navigate to your Heroku dashboard and click on the **New** button, then select **Create new app**.
       - Choose a unique name for your app and select your region.

  3. **Connect GitHub Repository**
       - After creating your app, go to the **Deploy** tab within your app's dashboard.
       - Under the **Deployment method** section, select **GitHub** as the deployment method.
       - Search for your GitHub repository in the **Connect to GitHub** section and click **Connect**.

  4. **Configure Deployment Options**
       - Once connected, choose the branch you want to deploy (e.g. *main*) and optionally enable automatic deploys for future commits.

  5. **Select Framework**
      - Since the DnD Text Adventure Game includes both Python and Node.js components, you need to specify the correct buildpacks for deployment. 
       - Under the *Settings* tab of your Heroku app, navigate to the **Buildpacks** section and add the appropriate buildpacks for Python and Node.js. (Make sure that they are in this correct order, Python above Node.js)
       - Also, add the following environment variables:
       - **PORT** set to **8000** to specify the port on which your app will run.

  6. **Deploy Branch**
       - After configuring the deployment options, manually deploy your application by clicking the **Deploy Branch** button.

  7. **Monitor Deployment Progress**
       - Heroku will start deploying your application from the selected GitHub branch. You can monitor the deployment progress from the activity log on the same page.

  8. **View Application**
      - Once the deployment is complete, Heroku will provide you with a URL to access your deployed application. Click on **View** button to open your application in a new tab.

## Credits 

### Code

- Coding assisstance and reference taken from the Love Sandwiches Tutorial project from Code Institute.
- Coding assisstance and explanations taken from [Python Tutor](https://pythontutor.com/)