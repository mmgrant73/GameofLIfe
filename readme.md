[![Published on webcomponents.org](https://img.shields.io/badge/webcomponents.org-published-blue.svg)](https://www.webcomponents.org/element/owner/my-element)
# Game of Life:

### What is it?
It was invented by John Horton Conway in 1970's to see how complex behavior can take shape from a simple rule set.  It is a form of cellular 
automaton (a discrete model studied in computer science). A cellular automaton consists of a regular grid of cells, each in one of a finite 
number of states, such as on and off (ie. alive or dead).  How these cells evolve off time is define by a simple rule set.

Rule Set:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:
1. Any live cell with two or three neighbors survives.
2. Any dead cell with three live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead. 

![Alt text](https://github.com/mmgrant73/gameoflife/blob/master/life.png?raw=true "Image-RevealBox")

[For more infomation:](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) 

### Programming:
This was written using the Processing Programming Language in Python Mode.  Processing is an open source framework that lets a user write programs 
with a visual context using javascript, java or python.  Processing has promoted software literacy, particularly within the visual arts, and 
visual literacy within technology.  And personally I think it is a great for people just getting into programming. 
[For more infomation:](https://processing.org/) 

### How to use it?
To use this program, just download the Processing IDE at https://processing.org/download/ clone this respository.  Install and open the IDE and open 
the lifepy_ps.pyde file.

I made the program so that it can read the different life formatted files (files that hold the initial state of the cells).  There any many
examples in the lifeexample folder that you can explore.  You can also define and save your own life files.  If you have any question feel 
free to ask


