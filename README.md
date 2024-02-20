# sp24-lab6
Materials for week 6 lab, which includes Ch. 8 "Functions & Closures" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 20, 2024_

Organization:
* SDX-ch8: The code files for the _SDX Ch. 8_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Gabriel Paris-Moe
* NAVIGATOR: Jack Allard
* NAVIGATOR: Sam Boerner

You will switch halfway through the _SDX Ch. 8_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 8?
the main ideas from the chapter is that it was trying to add anonymus function declerations to the interpreter. we has so far been building a python interpreter inside of pything and this was just another step
functions are just another data structure

* What questions did you have about the material in the chapters? What did you find confusing?
    env.append(dict(zip(params, values)))
    What is the line above doing?


Short paragraphs describing the functions:

env_get scans the environment list for the names of variables. if the variable name is not located inside of the the environment, we return false, otherwise return the values associated with the variable.

env_set sets new variables inside the environment if not alrady included. it first scans the list if it already exists, in which case just return the associated value, otherwise it appends the new variable to the end of the list and its associated value



Write a short summary of what you did (which exercises) below.

We finished the first excercise which was to rewrite enviornment creation.
