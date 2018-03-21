Special SSN
===========

Given a 9 digit number, check if it follows this pattern:

- First digit should be divisble by 1.

- First and second digits together should be divisble by 2.

- And so on. Full number should be divisble by 9.

Here is an example: 123252561.

Here "1" is divisble by 1, "12" is divisble by 2 etc.

Example run::

    $ python3 special_ssn.py 123252561
    123252561 follows special SSN pattern.

    $ python3 special_ssn.py 123252562
    123252562 doesn't follow special SSN pattern.

If the length of the input number is not exactly 9, your program
should print an error message. Like so::

    $ python3 special_ssn.py 123252
    input is invalid.


