Guidelines
==========

Please follow these principles while writing programs.

- Name variables descriptively. One should be able to understand the
  purpose of the variable by its name. Same principle applies to other
  things such as program names, function names etc.

- Write comments in your code if you think the code is not easy to
  understand. comments start with ``#`` character. Here is an example:: 

    # Split the match score string to get scores for each set.
    set_scores = match_score.split(" ")

  At the same time, your first priority is to write code that is easy
  to understand without comments. Only when the intent of the code is
  difficult to follow, should you write the comments.

- Your program should gracefully handle error conditions as much as
  possible. You should always assume that the input given to the
  program may be invalid and should try to print an error message in
  that case.

- Break down the problem into smaller sub-problems and try to solve
  them independently. Use `functions` where ever you can.

- Test your program thoroughly. Test with valid inputs as well as
  invalid ones.



