
Lesson 4 - Functions
====================

We have been learning about various data types and operations on those
types. In this lesson, we will focus on the organization of the code
itself. 

Till now, we have only seen very small programs that span only around
10 lines. But in practice, the programs are usually much larger
extending to hundreds or even thousands of lines. In order to maintain
such large code, various techniques are used and we will learn one
such technique called `functions`.

Functions
---------

You have been already using functions such as `len()` and `sorted()` in
your programs so far. They are called `builtin` functions because
Python language itself supports them. But there is nothing special
about them. You can write your own functions and use them in your
code. Here is an example::

    def sum(a, b):
        return a + b

This is a simple function that takes two parameters and returns their
sum. This code shows all the main components of a function:

- Name. Every function should have a name (with few exceptions that
  you don't need to worry about now).

- Input parameters. A function can take any number of input
  parameters. It is also possible that a function doesn't take any
  parameters at all.

- Body. A function has a body of statements that does some work.

- Return value. A function usually does some work and returns a
  value. It is possible to return more than one value but we will talk
  about that later.

  Note that a function can return any type and in some cases, it
  doesn't return any value at all.

Now, you can call this function any where in your code where you need
to add two numbers. Here is a sample::

    import sys

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    total = sum(num1, num2)
    print("Total =", total)

*Write a function that checks if a number is even or off*::

    is_even(n) # returns True or False

Here is a function that reverses a string::

    def reverse_string(s):
        return "".join(reversed(s))

Advantages of functions
-----------------------

As has already been mentioned, the main advantage of functions is that
it helps in breaking code into small manageable units. But there is
one more important advantage as well. Some times, you need to do same
computation at many different places in the code. In these cases, you
will write a function to do the computation and then just call the
function at other places.

This way, the actual computation is present in only place. If you find
a bug in the code later on, you only need to fix at one place.

As an example, once you have the function `sum()` as shown above, you
can now call it everywhere in your code where you need to add two
numbers. In this case, the actual code is extremely simple but in many
cases, the code in function will be larger.

Assignment
----------

Write a program that accepts a word and then prints if it is
palindrome or not. Examples::

    $ python3 palindrome.py eve
    is a palindrome.

    $ python3 palindrome.py abc
    is not a palindrome

Remember to use functions that we learned in this lesson.





