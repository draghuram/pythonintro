Who won the match?
==================

Given the score for a tennis match, your program should print which
player (player 1 or player 2) won the match. Here is an example run::

    $ python3 tennis_scores.py "6-4 6-4"
    Player 1 won the match

    $ python3 tennis_scores.py "4-6 4-6"
    Player 2 won the match

    $ python3 tennis_scores.py "4-6 6-4 4-6"
    Player 2 won the match

    $ python3 tennis_scores.py "6-4 5-7 6-4"
    Player 1 won the match

You can assume that the scores will be given as a single string as
shown above so you need to split the string to get scores for
individual sets. You need to further split the set score to find the
games won by each player.

Even though examples above show scores for best of 3 sets match, your
program should work for best of 5 sets as well, such as this::

    $ python3 tennis_scores.py "6-4 5-7 6-4 7-6"
    Player 1 won the match

Bonus points if you can handle invalid input and print error
message as follows::

    $ python3 tennis_scores.py "6-4 5-7 6-4 6-7"
    Invalid input


