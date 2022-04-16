To begin our drawing program, let's assume that a picture is stored in a file & we wish to read this file when the program is started.
We'll assume that each line of the file contains a drawing command & it's associated data.
We'll keep it simple & stick to drawing commands that look like this in the input file:

goto, x, y, linewidth, color
circle, radius, linewidth, color
beginfill, color
endfill
penup
pendown

sequence of the command may vary but syntax must be same.

Initially we'll keep this aaplication very simple & we'll look how we can take it to next level. :)