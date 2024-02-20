# sp24-lab6
Materials for week 6 lab, which includes Ch. 8 "Functions & Closures" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 20, 2024_

Organization:
* SDX-ch8: The code files for the _SDX Ch. 8_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Jacob
Grant

## Team Roles for Part 1
Who will start out as
* DRIVER: Grant
* NAVIGATOR: Jacob

You will switch halfway through the _SDX Ch. 8_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 8?
Some of the main ideas from the chapter were closures and function captures. We learned about how closure makes it so that nothing else in the program can see how info generated in other scopes of the program was generated.
* What questions did you have about the material in the chapters? What did you find confusing?

Write a short summary of what you did (which exercises) below.

#### Exercise 1
##### env_set:
this function is used to keep track of variables and functions for any scope in the process. when we use do_set (or define a function or variable), env_set is then used to add this to the current environment 
##### env_get:
this function is used to retrieve the functions and variables from a name when it is needed for a call to a function or retrieval of a variable value. this way we can check if that function or variable at that name is in the current enviroment so we can then execute do_call and do_get with no errors


