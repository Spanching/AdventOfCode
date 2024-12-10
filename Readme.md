
# My journey through Advent of Code

A couple of years ago I came across very interesting puzzles, called the [Advent of Code](https://adventofcode.com/). Ever since then I wanted to do all the puzzles at the day they were supposed to be done. Time never allowed me to do that though, so this year (i.e. 2024) I am trying to get my full pass for the first time. 

### What is Advent of Code

In short Advent of Code is a way to have fun, get motivated (and frustrated at times) with coding in the time leading to christmas. Every day from the first of December until 25th of December a coding challenge will be made available at 6am. It always consists of two parts and you have to solve the first one to get access to the second part.
This repository also shows a bit of my evolution when it comes to the setup. Now I use a general `main.py` that I run with the following command to start the current day either with sample input (default) or the real one (main).

```
python main.py [main]
```

Each day has its own folder in which there is a `input.txt` and `sample_input.txt` for the two inputs, as well as a `tasks.py` for my solutions. The main method automatically uses the `task1(...)` and `task2(...)` for the current day. Additionally you can control the input variable with the `input()` method. It returns one of the strings "oneline", "intlist", "raw" and the default is a list of strings that are the lines of the input. 

If you want to test things out, you will have to create the `input.txt` and `sample_input.txt` and fill them with the content from [Advent of Code](https://adventofcode.com/). The creators do not want us to publish the input or the puzzles, which I do very much respect. Also the inputs do vary by user, so if you want to go through it yourself my inputs won't be any help anyway.

### The rules I set for myself are very simple:

1. I until 6am the next day to finish solving a puzzle, no exact starting time or anyting like that, just if I need more time than 6am the next day, I failed that day
1. A day counts as failed if I can only do the first part of the puzzle
1. The efficiency of a solution does not play a role

With those rulse and a lot of motivation, I set out to conquer this dream. The following are my impressions:

## Day 1-3

The first days were very much what I expected. When thinking about the problem a bit I got there pretty fast, even though my solution was not always the fastest or best looking.

## Day 4

Today I did have my first hickup so to speak. I just could not wrap my head around a very simple solution. So it took me quite a long time until I understood what to do and then I finished it in about 5 minutes. 

## Day 5-8

I noticed the increase in difficulty and that sometimes I didn't know how to use certain datastructures in python that I never used here. So it shows that there is a lot to learn from these challenges. I also had a solution that ran for almost 9 minutes (Day 6), but it was correct on the first try, so I am pretty proud of that.

## Day 9

This was my first day of almost failing. Moving blocks around in a filesystem basically just wrecked my brain. It seemed so simple that I did not start with a sketch or notes first, which was definitely not a great idea. I almost got there multiple times but the whole solution just got so complicated that I did not want to leave it like that, so I started over multiple times. But in the end I managed to get there, but it definitely caused me some headache. But this is over a third of the way to the finish which definitely motivates me to go on and get this challgenge done!

## Day 10

In stark contrast to Day 9, I really enjoyed and had no problem at all with todays puzzle, both parts took like 10 minutes or so and the second one was just a minor change in my code. So, I am glad to have a day with less headaches today.