
Lesson 2 - Lists, for and if statements
=======================================

In the last lesson, we learned basic data types - numbers and
strings. In this lesson, we will study a new data type called
`List`. We will also learn about some more operations that Python
provides for these data types.

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
functions, see `here
<https://docs.python.org/3/library/functions.html>`_.

Lists
-----

Let us now get back to learning about data types supported by
Python. Here we learn about "list" type. A list is a collection of
other types. For example: a list of strings or a list of integers. A
list is formed by enclosing the items with "square brackets", like
so:: 

    >>> ["red", "green", "blue"]

Let us use a variable to contain a list and then, we can see some list
operations. ::

    >>> colors = ["red", "green", "blue"]

    >>> print(colors)
    ['red', 'green', 'blue']

    # To add items to a list at the end.
    >>> colors.append("magenta")
    >>> print(colors)
    ['red', 'green', 'blue', 'magenta']

    # To remove an item
    >>> colors.remove("red")
    >>> print(colors)
    ['green', 'blue', 'magenta']

Notice how the variable "colors" contains a list and various
list operations can be performed using the variable.

A list contains elements of different data types. For example, the
following list contains both strings and integers.::

    >>> testlist = ["abc", "def", 1, 2]

Even though this is possible, most of the times, a list contains
elements all of the same type.

Here are some more operations possible on lists.

To sort the list alphabetically:
::

    >> colors.sort()
    >>> print(colors)
    ['blue', 'green', 'magenta']

To reverse a list:::

    >> colors.reverse()
    >>> print(colors)
    ['magenta', 'blue', 'green']

Notice how "sort" and "reverse" operations changed the data stored in
the variable "colors". What if we don't want to affect the data but
want to get a new list that is sorted or reversed?
::

    >>> print(colors)
    ['magenta', 'blue', 'green']

    # This gives a new list, leaving the original list unaffected.
    >>> sorted(colors)
    ['blue', 'green', 'magenta']
    >>> print(colors)
    ['magenta', 'blue', 'green']
    
    >>> reversed(colors)
    ['blue', 'green', 'magenta']
    >>> print(colors)
    ['magenta', 'blue', 'green']

len()
-----

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

Finally, it is possible to check for multiple conditions using a
different variation of ``if`` statement. In the following example, we
are checking if a number ``n`` is

- less than 10
- between 10 and 20
- or above 20

::

    >>> n = 10
    >>> if n < 10:
    ...     print("less than 10")
    ... elif n < 20:
    ...     print("less than 20")
    ... else:
    ...     print("above 20")
    ... 
    less than 20
    

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

It is also possible to access elements from the end of the list
instead of from the start. For example, the following will give you
the last element of a list::

    >>> colors[-1]
    >>> # To access second element from the last:
    >>> colors[-2]

Assignment
----------

There is a new object in the solar system that is found to be
traveling at 40000 miles per hour. 

Write a program that calculates the number of days it takes this
object to travel from Sun to Earth. Your program should print the
following when run: ::

    It takes N days

where ``N`` is the value your program should calculate.

**Note**. This object is named 
`Oumuamua <https://en.wikipedia.org/wiki/%CA%BBOumuamua>`_ and in
reality, it doesn't travel from Sun to Earth in straight line. 

