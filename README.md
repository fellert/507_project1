<h1>SI507 - Project 1</h1>

<h2>Project Description</h2>
  This project folder contains five  (excluding this one and the pycache):
  <br>
  <ul>
    <li>SI507F17_project1_cards.py: contains code for Cards(), Deck(),
    play_war_game(), and show_song() classes/functions.
    </li>
    <li>SI507F17_project1_tests.py: contains test cases for above file.
    </li>
    <li>code_description_507F17project1.txt: more in-depth description
    of functions in SI507F17_project1_cards.py and the expected output.
    </li>
    <li>helper_functions.py: additional functions (not tested)for the
    show_song() function.
    </li>
    <li>requirements.txt: contains short list of required packages that
    need to be installed prior to running either .py file.
    </li>
  </ul>

  The Cards() function takes two integers (0-3 for the first, and 1-13 for the
  second) and translates these to a suit ("Diamonds", "Clubs", "Hearts",
  "Spades") and card number (2-10, and "Jack", "Queen", "King", "Ace" for the
  numbers 1, 11, 12, and 13, respectively). The str() method then return a
  string that should read "{card number} of {suit}" (for example, the "King
  of Hearts", or the "5 of Clubs").

  The Deck() class contains various functions that use objects of the Card()
  class, including methods that remove a card (using the pop method),
  create a hand (of size indicated by user input), shuffle and sort
  the deck, and replace a missing card. More detailed descriptions of their
  respective outputs/return values can be found in the code_description file.

  The play_war_game() function creates two instances of the Card() class,
  compares the card number, and awards points to the player who has the
  higher card. A tuple of ("winner", int player1 score, int player2 score)
  is returned. The show_song() function takes an input, and searches the
  Apple iTunes API using this keyword, returning a song containing something
  relevant to the input. The song name and artist is printed.


<h2>Getting started/Installation:</h2>
  This program runs using python 3.6, so the user must have this version
  installed prior to use. All of the files can be found on GitHub under
  the fellert/507_project1 repository. Fork this folder to your GitHub account,
  make a folder on your computer (mkdir), and clone the 507_project1 folder you
  just forked to the to this folder using the git clone <url> command.
  The packages required to run the programs are listed in the requirements.txt
  file (included in the folder), and can be installed using the
  pip install -r requirements.txt command.

<h2>Running the Tests:</h2>
  Running the file SI507F17_project1_cards (using python3) will display the
  scores of each player from the war game, who won (or if there was
  a tie), and the name of the song an artist retrieved from the show_song()
  function. A window will open to iTunes.com as well, displaying the
  song, artist, and album for the object returned.

  Running SI507F17_project1_tests.py will run various tests on each of the
  functions in SI507F17_project1_cards.py, displaying any errors or failure
  along with explanations.
