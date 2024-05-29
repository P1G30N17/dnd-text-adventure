## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

# Classic DnD Text Adventure Game

Classic hangman is a throw back to the old hangman game we used to play as kids. A simple stick man drawing portrays the end result of failure (being hung), and failure being unable to guess the hidden word. The user is given a basic layout and simple on screen keyboard with which to input their chosen letter in an attempt to guess the hidden word and save the stickman from being hung. If the user is struggling their is a hint option that when clicked will reveal helpful information associated with the hidden word in question. My inspiration for this game came from my two sons who love playing old school games like this on our digital white board with me, along with 'I spy' and 'Pictionary', Hangman is a great way for them to improve their vocabulary. As such a majority of the words used in this game are catered towards their academic level, Year 6 and below. 

![Responsive Mockup](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/viewports.png?raw=true)

## User Stories
- A quick and fun way to test my vocab knowledge.
- My son loves trying to guess the words without using hints.
- The design is very basic but works well for the simple task this game sets out to achieve.

## Features 

The Hangman game is a simple one page project, where the user is presented with the game upon page load and a game already loaded up for them to play. Whether they are new or a returning user, navigating the game is very easy and fairly intuitive. 

### Existing Features

- __The Game__

  - Taking center stage is the game container and within it the hangman game.
  - The user has everything right in front of them with which to interact and play the game.

![The Game](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/game.png?raw=true)

- __The Hangman Stockade__

  - This is the classic hangman stockade associated with almost all iterations of the hangman game.
  - The stickman will, piece by piece, be drawn onto the stock as if he is being hung.
  - This acts as a visual queu to the user for the number of attempts left  to guess the word and helps to portray the gravity of the situation. 

![The Hangman Stockade-1](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/stockade-1.png?raw=true)
![The Hangman Stockade-2](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/stockade-2.png?raw=true)

- __The word to guess__

  - Here the user will be offered a word, that they must guess, hidden by underscores until a correct letter is guessed.
  - Upon the correct choice of letter the underscore will be removed and the afore mentioned correct letter will replace it.
  - This helps to give a visual queue to the user as to what the word could potentially be.

![The guess word](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/guess-word.png?raw=true)

- __Attempts left indicator__ 

- This is a more direct indicator of how many attempts the user has to guess the correct word.
- This helps to assist new users, or users who have never played hangman before associate the number of attempts left with the parts left on the hangman body in the stockade image.

![Attempts left indicator](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/attempts.png?raw=true)

- __The hint button and hint text__ 

  - The user can click on the hint button to reveal a hint associated with the current hidden word.
  - The hint button disappears upon click and the hint remains on screen until the user either is succesful or not.
  - Upon a new game iniating the hint disappears for the old word and the hint button returns linked to the new word hint.

![Hint Button and hint text-1](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/hint-1.png?raw=true)
![Hint Button and hint text-2](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/hint-2.png?raw=true)

- __The onscreen keyboard__

  - The intention for an onscreen keyboard was to simplify the process across mobile, tablet and desktop.
  - The user is given the ability to select a letter from an onscreen keyboard representing the english alphabet.
  - Once a key is clicked, whether it is right or wrong for the hidden word, it is then grey out and unclickable so as to avoid a user using up for than one attempt on a repeated letter.

![The onscreen keyboard](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/keyboard.png?raw=true)

- __Victory and Game Over message__

- Once the user has guessed the correct word within the given attempts limit, they are shown a victory message.
- Once the user has failed to guess the correct word within the given attempts limit, they are shown a game over message.
- Both messages offer a 'Play again' and 'Try again' button respectively that will reset the game, choose a new hidden word and hide the hint text (if clicked previously).

![Victory and Game Over message-1](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/victory.png?raw=true)
![Victory and Game Over message-2](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/game-over.png?raw=true)

### Features Left to Implement

- Game Difficulty
- Score Tracker

## Testing 

- This Classic Hangman game project was tested on the following devices: Desktop pc (1920 x 1080), iPad Air (2360 x 1640) and iPhone XR (1792 × 828) along with the Google Chrome inspect tool for responive dimension testing.
- This Classic Hangman game project was tested on the following web browsers: Google Chrome, Microsoft Edge and Safari.

### Device Testing
- The project is responsive in almost all dimensions bar a few outliers such as a smart watch.
- This was achieved in a sense due to the simplicity of the game, the game container scales to almost all device sizes allowing multiple platforms to play the game.

![Responsive Mockup](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/viewports.png?raw=true)

### Web Browser Testing

- The project obtained a great lighthouse rating with the Google Lighthouse Dev Tool.

![Lighthouse Score](https://github.com/P1G30N17/hangman/blob/main/assets/readme-media/lighthouse.png?raw=true)

- The various web browsers the project was tested on had mostly optimal results, with little to no errors between all 3.

### Page Testing

- I have checked that the game loads a new game correctly after each attempt, success or failure included.
- I have checked that all on screen keyboard buttons return the correct keystroke.
- I have checked that the hint button reveals the correct word hint linked to its associated word.

### Bugs

- I had found that on the rare occasion the game will load the same word twice in a row. This was due to the word being selected randomly from a list of words. As the size of the list is increased the probability of this bug occuring will be less but not zero. (This Bug was fixed by adding a tracker to the random word selected and then using an if/else statement to prevent it from being pulled directly after a round was over).

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
- Javascript
  - No errors were found but a few warnings were noted when passing through the official [(JSHint) validator](https://jshint.com/)
    - These warnings were that "Swal" and "wordList" were undefinied vairables, Swal is the variable for the alerts generated using the Sweet Alerts 2 website (more information in credits) and the wordList is a variable declared in a seperate script that holds the words and hints required for the hangman project.
    - A third warning was that "showHint" was an unused variable, however it is a function that is called via an onclick button event from the index.html page.

### Unfixed Bugs

- None that I am aware of. 

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Main Branch
  - Once the Main branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://p1g30n17.github.io/hangman/

## Credits 

### Code

- Coding assisstance and reference taken from the Love Maths Tutorial project from Code Institute.
- Coding assisstance and reference taken from the Hangman project and Rock, Paper, Scissors project from https://www.codingnepalweb.com/

### Media 

- Hangman Stock and body drawn by page owner (James King) in MS Paint.

### Content 

- The favicon was generated using https://favicon.io/
- The victory and game over alerts were generated using https://sweetalert2.github.io/