
Lesson 5 - Number of byes
=========================

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

We will try to write code to solve the following problem.

*In a tennis tournament, how many players need to be given byes?*

If the number of players who sign up for a tournament is not equal to
power of 2, some players need to be given byes and they automatically
move to second round. For example, if there are 21 people, 11 people
will need to be given byes. More details about this problem can be
found here:

http://draghuram.github.io/tournament/byes/2018/01/20/how-many-byes.html

Don't worry if the math on that page looks complicated. You don't need
that for writing code. You just need to know the solution which is
this:

*Find a power of 2 that is greater than number of players and subtract
number of players from that number.*

For example, if there are 21 people in the tournament, 32 is the
closest power of 2 that is greater than 21. So the number of byes
would be::

    32 - 21 = 11

This is all you need to know to start writing code.

Solution
--------

To solve this problem, we need to learn a function called ``log`` in
the module ``math``. This function computes the *logarithm* of a
*number* with respect to a *base*. Here are some examples::

    >>> import math

    >>> math.log(16, 2)
    4.0
    >>> math.log(8, 2)
    3.0
    >>> math.log(32, 2)
    5.0

Can you understand the return value of ``log()`` function? Here is
another way of understanding it::

    >>> 2 ** 3 # 2 to the power of 3
    8
    >>> math.log(8, 2)
    3.0

    >>> 2 ** 4 # 2 to the power of 4
    16
    >>> math.log(16, 2)
    4.0

    >>> 2 ** 5 # 2 to the power of 5
    32
    >>> math.log(32, 2)
    5.0

As you can see, ``log()`` is kind of opposite to ``power``
operator. Armed with this new function, let us proceed with the code
to solve our problem. Remember that this is the algorithm to solve our
"byes" problem:

*Find a power of 2 that is greater than number of players and subtract
number of players from that number.*

Let us assume that there are 21 players in a tournament. Our job is to
find the number of byes that need to be given.

    >>> math.log(21, 2)
    4.392317422778761

Note that we are getting a floating point number here because 21 is
not an exact power of 2 number. We need to convert this to an integer
first.

    >>> int(4.392317422778761)
    4

Note that 2 to the power of 4 will give us a power of 2 number that is
less than 21. But what we really want is a power of 2 that is greater
than 21. This is how we do it.

    >>> 2 ** (4 + 1)
    32

All we need to do now is to subtract number of players from this
number.

    >>> byes = 32 - 21

There you go! We now have code to solve the problem when the number of
players is 21. 

Assignment
----------

Write a program that accepts number of players as input (integer) and
prints number of byes that need to be given. You need to take code
explained above and generalize it. Try to write the code using
functions.::

    $ python3 num_byes.py 21
    11

    $ python3 num_byes.py 10
    6

Bonus points if you can write the program so that when a power of 2 is
given as input, the output is 0 (because there is no need to give byes
in this case).::

    $ python3 num_byes.py 16
    0

    $ python3 num_byes.py 128
    0
