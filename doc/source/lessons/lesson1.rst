
Lesson 1 - Numbers, Strings
===========================

Welcome to the very first lesson on Python. I am sure you are going to
have a very nice time learning to program.

Python is a very popular programming language that is used in a wide
variety of applications, games, and in building web sites. In this
course, we will only focus on the very basic features of the language
as the main emphasis here is not to master the language but rather to
understand general programming concepts. Keep in mind that many things
you learn here apply to other programming languages as well.

Data Types
----------

When you start learning any programming language, the very first thing
you should do is to understand what types of data that it can work with
and what kind of operations that it supports on them. This is
generally referred to as *types* or *data types*. The most basic data
types that all languages support are numbers and strings so we will
start with those.

Python supports all kinds of numbers that you know from your Maths
class. 
::

    >>> 42
    42

    >>> 10.0
    10.0

Python supports all the usual arithmetic operations on numbers so you
can use it as a calculator::

    >>> 42 + 10
    52
    >>> 42  * 10
    420
    >>> 42/2
    21.0
    >>> 42 - 10
    32

    # Here is how you can calculate remainders.
    >>> 42 % 10
    2

    # to calculate powers - called "exponential" operator
    >>> 2 ** 3
    8

BTW, did you notice how you can write comments in the code using ``#``
symbol? Any text following this character is ignored by Python so you
can use it to write comments in your code (to explain what your code
is doing if it is not already clear).

Let us now move to "strings". You will need to manipulate strings in
many programs so it is very useful to have good knowledge about
them. A string is a sequence of characters. A single character is also a
string which has a length of 1. In Python, strings are enclosed in
either double quotes or single quotes. ::

    >>> "test string"
    'test string'

    >>> "c"
    'c'

Python supports several operations on Strings. Here are some of
them.::

    # to convert a string to upper case
    >>> "test".upper()
    'TEST'

    # to convert to lower case
    >>> "TEST".lower()
    'test'

    # to replace some parts of the string
    >>> "abcda".replace("a", "x")
    'xbcdx'
    >>> "aabbcc".replace("aa", "xx")
    'xxbbcc'

    >>> "test".capitalize()
    'Test'

You can combine two strings using ``+`` operator.::

    >>> "test " + "string"
    'test string'

Note that the first string contains a "space" which is no different
from any other character.

print() function
----------------

You can print various values using the function ``print()``. You can
either print single values or a combination of them.::

    >>> print(42)
    42

    >>> print("test string")
    'test string'

    >>> print("My age is", 11)
    'my age is 11'

    >>> print("I am", 11, "years old")
    I am 11 years old

Notice how Python is adding a "space" between items that are passed to
"print".

As you have already seen, you use a function by passing it some values
in parenthesis. However, passing values is not mandatory (but you
still need parenthesis). Here is an example:

    >>> print()

Python has many other functions which we will learn in later lessons. 

Variables
---------

Many times in your program, you need to store values before
using them later. For this, you use "variables". Here is an example::

    >>> age = 42

Here, we could have used "42" directly but instead, we created a
variable called "age" which now contains the value "42". You can now
use "age" to mean 42 at any place in the code.

``=`` is known as `assignment operator` which assigns values from
right side to variables on the left side.

You can choose any name you want for variables (subject to some rules)
but it is very important that you name them appropriately. **In
particular, variables should be named such that they describe the
values they may contain.**. This helps you and others in understanding
the code, especially when you are reading it at a later time.

Apart from naming variables descriptively, you should not use Python
function names to name your variables.

Formatting strings
------------------

You can combine strings and integers and even other data types in any
format you want to form a new string. This is especially useful if you
want to print some information to the console.

Here is an example::

    >>> teststring = "This year: {}, Month: {}, Date: {}".format(2019, 2, 22)
    >>> print(teststring)
    'This year: 2019, Month: 2, Date: 22'

Here, ``{}`` are just place holders. They will be replaced by the
values you pass to ``format()`` function.

