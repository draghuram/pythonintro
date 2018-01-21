
Lesson 5 - Functions - Contd
============================

Built-in function `int`
-----------------------

The built-in function `int` can be used to convert strings or floating
point numbers to integers.

    >>> int("10")
    10

    >>> int(5.123)
    5

    >>> int(5.9)
    5

Number of byes in a tournament
------------------------------

We will try to write code for the following problem.

"In a tennis tournament, how many players need to be given byes?"

If the number of players who sign up for a tournament is not equal to
power of 2, some players need to be given byes and they automatically
move to second round. For example, if there are 21 people, 11 people
will need to be given byes. More details about this problem can be
found here:

http://draghuram.github.io/tournament/byes/2018/01/20/how-many-byes.html

The solution is to find a power of 2 that is greater than number of
players and subtract number of players from that number. For example,
if there are 21 people in the tournament, 32 is the closest power of 2
that is greater than 21. So the number of byes would be::

    32 - 21 = 11

Guidelines for writing functions
--------------------------------

- Name functions descriptively.

- Keep all the functions at beginning of the file and write the main
  code after that.

- Functions should not have large number of parameters. If you ever
  end up writing a function that accepts large number of parameters,
  you can usually break it in to multiple functions where each
  function accepts small number of parameters.

Assignment
----------

There is no assignment :-). However, we will have a quiz during next
lesson so make sure you go through all the lesson notes.
