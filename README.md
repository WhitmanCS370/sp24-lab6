# sp24-lab6
Materials for week 6 lab, which includes Ch. 8 "Functions & Closures" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 20, 2024_

Organization:
* SDX-ch8: The code files for the _SDX Ch. 8_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Marlyn, Coden

## Team Roles for Part 1
Who will start out as
* DRIVER: Marlyn 
* NAVIGATOR: Coden

You will switch halfway through the _SDX Ch. 8_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 8?
How to define functions using the do function.
* What questions did you have about the material in the chapters? What did you find confusing?
Closures was a bit confusing. How does it work with functins with multiple arguments?

Write a short summary of what you did (which exercises) below.
env_get: this function searches the dictionary for the varable, looking in the inner scope 
env_set: this function sets the name of the function as a new varible putting it in the inner scope

We did exercise 2. To test our changes, we modified the func.tll file to include tests that are 
applicable to the functionality we added. While it would be good to write tests before, it isn't clear
what each thing (both in the code and in the tests) is supposed to do.

We attempted to define named functions, but we weren't really sure of where we should do this. Beyond
this, we were under the impression that we needed "func" to actually use functions, and it isn't clear
how we're supposed to do this while also allowing the original thing to still work.