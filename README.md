# sp24-lab6
Materials for week 6 lab, which includes Ch. 8 "Functions & Closures" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 20, 2024_

Organization:
* SDX-ch8: The code files for the _SDX Ch. 8_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
* DRIVER: John Leeds
* NAVIGATOR: Clara Bates

You will switch halfway through the _SDX Ch. 8_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 8?

* Scoping rules and closures (new environment for different functions)
* Anonymous functions
* Functions as data

* What questions did you have about the material in the chapters? What did you find confusing?

* The naming and diagrams in the chapter was confusing
* What is stored when you set a variable to a function?

Write a short summary of what you did (which exercises) below.

Exercise 1)
When looking for the contents of a variable, you search through each environment in reverse order.
This way, you get the variable from the environment that was most recently added.

`env_set()` checks for a preexisting variable before creating a new one.

[
    {a = 10, b = 17},
    {a = 12}
]

Here if you search for a, it will return 12 and searching for b will give you 17.

We completed exercise 2, and exercise 3 A, B, C, and D!