
Lesson 2 - Lists, for and if statements
=======================================

In the last lesson, we learned basic data types - numbers and
strings - and also about lists. In this lesson, we will study some
more operations that Python provides for these data types.

As you have already seen, it is useful to store values in variables so
that our code is more readable. Example::

    >>> count = 10

Now, if we want to increment this counter or add a number to it, this
is how we do it::

    >>> count = count + 1
    >>> count = count + 10
    >>> print(counter)
    21

In addition to ``print()`` function, Python supports many other
functions called *built-in functions*. These are called *built-in*
because they are provided by the language itself. As you will learn
later, you can also write functions and in fact, that is how you will
organize your code for the most part. For a full list of built-in
functions, see `here <https://docs.python.org/3/library/functions.html>`_.

You will use the built-in function ``len()`` to find the size of the
lists as well as that of strings. Examples::

    >>> len("test")
    4
    >>> colors = ["red", "green", "blue"]
    >>> len(colors)
    3

    # Empty string
    >>> len("")
    0

Now, let us move on to couple of very useful operations on strings
called *split* and *join*. As the name indicates, you would use
*split* to break a string into multiple components and *join* is used
to do the reverse.
::

    >>> "a/b/c".split("/")
    ['a', 'b', 'c']
    >>> "one two".split()
    ['one', 'two']
    >>> "/".join(['a', 'b', 'c'])
    'a/b/c'
    >>> ' '.join(['one', 'two'])
    'one two'

Boolean expressions
-------------------

Many times in a program, you need to do something depending on whether
some condition is true or false. For example, this is how you check if
a number is even::

    >>> i = 5
    >>> if i % 2 == 0:
    ...    print("even")
    ... else:
    ...    print("odd")

As you can see, you use ``if-else`` statements to do this. This
statement contains a *condition* that can be *true* or *false*. In the
above code, the condition is ``i % 2 == 0``. Here, we are checking if
the remainder when a number is divided by 2 is 0. Apart from the
condition itself, there is a block of code that is run when the
condition is true and another block of code that gets run when the
condition is false. Did you notice ``:`` after the condition and after
``else``? That is how we indicate a block of code to Python. Also
note that the code block is indented by few spaces. It is very
important to use same number of spaces for a code block. The
convention is to use 4 spaces.

Now, there are may operators that you can use as part of
conditions. Some examples::

    >>> i > 4
    >>> i < 4
    >>> i == 4 # to check if value of "i" is 4.

To check if two strings are equal::

    >>> s == "test"

    >>> test_string = "abc"
    >>> len(test_string) < 5

Note that ``=`` is used to assign a value while ``==`` is used to
check for equality.

The operator ``in`` is used to see if an element is in a list::

    >>> "red" in colors

BTW, "else" part of the "if" statement is optional. For example::

    >>> i = 5
    >>> if i % 2 == 0:
    ...    print("even")

In this case, nothing happens if the number is not even.

Finally, you can combine multiple conditions, like so::

    >>> if (i > 4) and (j < 2):
    ...     print("do something")

Here, print() will be run only if *both* conditions are true.

    >>> if (i > 4) or (j < 2):
    ...     print("do something")

Here, print() will be run if *one* of the conditions is true. 

    >>> if not some_condition:
    ...     print("condition is not true")

Some more examples::

    >>> if "red" in colors:
    ...     print("red is present")

    >>> if "red" not in colors:
    ...     print("red is not present")

The operators *and*, *or*, *not* are known as *logical operators*. 

Accessing list elements
-----------------------

Sometimes, we need to access individual elements of a list.::

    >>> colors = ["red", "green", "blue"]
    >>> print(colors[0])
    'red'

Here, we are accessing the first element of the list. Note that the
counting of the elements in a list starts with "0". So to print all
the elements of this list, here is one way::

    >>> print(colors[0])
    >>> print(colors[1])
    >>> print(colors[2])

The number we use to access an element is called *index*. The index
starts from 0 and goes all the way up to the one less than the size of
the list.

You will get an error if you try to use an invalid index.::

    >>> print(colors[3])

    IndexError: list index out of range

Processing all elements of a list
---------------------------------

Let us say that we have a list and we want to do some operation on all
the elements of the list. For example, to print entire list, we can do
something like::

    >>> print(colors)
    ['red', 'green', 'blue']

But what if we want to print each color on a different line? Here is
one way to do it::

    >>> for color in colors:
    ...    print(color)

    red
    green
    blue

You use *for* loop to go over each item in the list and do something
with it. This process is called *iteration*. In each iteration, one
item will be available for you to process. 

To sum all the numbers in a list::

    >>> numbers = [10, 1, 3, 4]
    >>> total = 0
    >>> for num in numbers:
    ....    total = total + num

    >>> print(total)
    18

Note that you can also use iteration to process each letter in a
string. ::

    >>> for x in "test":
    ...   print(x)
    ... 
    t
    e
    s
    t

Command line arguments
----------------------

In the last lesson, we saw how we can write code in a file and run it
(using `pythonanywhere <https://www.pythonanywhere.com/>`_). Now, let
us see how we can pass data to a program. 

Open a file, say "test.py" and add the following code in it.::

    import sys

    print(sys.argv[1])

From Dashboard, click on ``$ Bash``. You will get a terminal where you
can enter commands. ::

    $ ls

This should list all the files including your new file "test.py". Let
us run it.::

    $ python3 test.py Hi
    Hi

    $ python3 test.py Hello
    Hello

    $ python3 test.py "Hello World!"
    Hello World!

As you can see, our little program is printing whatever value we are
passing from the command line. The values we enter at the command
are available in the list ``sys.argv``. The very first element in this
list is the name of the program itself so our input starts from
index 1. That is why we used ``sys.argv[1]`` to get the input here.

Now, let us write a program that takes a number as input and prints if
that number is even or odd. We already saw how to do this when we
studied boolean operations but now, our code should work with any
number.

Open a file called "even_odd.py" and enter the following code::

    import sys

    # We use `int' built-in function to convert input string to a number.
    num = int(sys.argv[1])

    if num % 2 == 0:
        print("even")
    else:
        print("odd")

Now, let us run the program from Bash console.::

    $ python3 even_odd.py 4
    even
    $ python3 even_odd.py 5
    odd

Assignment
----------

Given three integers indicating the length of a triangle's sides, your
program should print the type of the triangle. Remember that if all
three sides are equal, the triangle is "equilateral". If only two
sides are equal, it is "isosceles". If all three sides are different,
the triangle is "scalene".

Here are some examples::

    $ python3 triangle_type.py 10 10 10
    equilateral

    $ python3 triangle_type.py 10 10 15
    isosceles

    $ python3 triangle_type.py 10 11 12
    scalene

Note that you can get the value of sides in your pgoram as follows::

    import sys

    side1 = int(sys.argv[1])
    side2 = int(sys.argv[2])
    side3 = int(sys.argv[3])





