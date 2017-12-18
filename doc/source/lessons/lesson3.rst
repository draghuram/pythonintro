
Lesson 3 - Problem solving techniques
=====================================

In the last lesson, we learned control flow statements such as
``if-else`` and ``for``.

In this lesson, let us try to write a program for this problem:

    "Given a day, the program should print if it is a weekday or
    weekend."

::

    $ python3 day_of_the_week.py monday
    weekday

    $ python3 day_of_the_week.py sunday
    weekend

First, we need to accept the input from the command line.::

    import sys

    day = sys.argv[1]

Now, we need to find what type of day it is. The most straightforward
way of doing it is checking the input against each day, like so::

    if day == "monday":
        print("weekday")
    elif day == "tuesday":
        print("weekday")
    elif day == "wednesday":
        print("weekday")
    elif day == "thursday":
        print("weekday")
    elif day == "friday":
        print("weekday")
    elif day == "saturday":
        print("weekend")
    elif day == "sunday":
        print("weekend")

Notice, how multiple if conditions can be combined using ``elif``. 

The program works but there are some issues with it. First, code looks
a bit cluttered. Second, what if you need to write a similar program but
with a bigger list? You can't keep adding ``elif`` statements. 

What we are trying to do here is to see if a given input (name of the
day in this case) belongs to a group (such as "weekday" or
"weekend"). Such problems can be solved by using lists. Since there
are two types of days here for the purpose of this
problem, let us define two lists.::

    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    weekend = ["saturday", "sunday"]

We can simply check if the input is in the first list or second
list::

    if day in weekdays:
        print("weekday")
    elif day in weekend:
        print("weekend")
    else:
        print("not a day")

Notice how the second version is much smaller and much easier to
read. In general, you should try to use types such as lists (and
others provided by Python which we will see later) to solve problems. 

Also note how we added ``else`` clause at the very end. Now our
program gives a proper error message if the input is not valid. This
is another thing you need to keep in mind when you accept inputs. **Your
code needs to be prepared to handle both valid and invalid inputs**.
In the case of latter, the program should provide a good error
message.

Problem solving techniques
--------------------------

- Divide the problem into smaller ones and solve them. Once smaller
  problems are solved, you just need to figure out how to combine
  them. This technique is called `divide and conquer`.

- Don't try to write a perfect working program in the first
  go. Instead, write something that works and slowly improve it.

- Don't try to write the program directly. First solve the problem for
  some example inputs and see how you are solving it (you can use paper
  and pencil for this). Then, try to convert the solution into a
  program.

Assignment
----------

Given a word, your program should print number of vowels in the word,
like so::

    $ python3 count_vowels.py "test"
    Number of vowels: 1

    $ python3 count_vowels.py "it is snowing"
    Number of vowels: 4

    $ python3 count_vowels.py "xyz"
    Number of vowels: 0

You will be using most of the concepts you learned in this lesson and
the previous ones to solve this problem, so go over the notes if
required.





