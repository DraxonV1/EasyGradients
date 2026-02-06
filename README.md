# EasyGradients

hello friends this is my project easygradients u can use it for color text and many things i dont know complex coding but it works nicely.

## how to install

just type this command:

pip install easygradients

## how to use it

first u import the library like this:

import easygradients as eg

### gradients

u can make text gradient like this very easy:

# use rgb codes
print(eg.gradient("hello world", [(255, 0, 0), (0, 0, 255)]))

# use hex codes
print(eg.gradient("color text", ["#FF0000", "#00FF00", "#0000FF"]))

# use 4 colors or more
print(eg.gradient("many colors wow", ["#00d9f5", "#00f5a0", "#ff00ff", "#ffff00"]))

# use presets names
print(eg.gradient("sunset view", "sunset"))

### simple colors

if u want one color only:

print(eg.color("red text", "#FF0000"))

### background colors

change backgroud color also:

print(eg.bg_color("black bg", "#000000"))
print(eg.bg_gradient("gradient bg", ["#0000FF", "#00FFFF"]))

### styles

make text bold or italic:

print(eg.style("bold text", "bold"))
print(eg.style("italic text", "italic"))

styles available: bold, italic, underline, blink, etc.

### special things

# rainbow text
print(eg.rainbow("rainbow text wow"))

# type writer effect
eg.typewriter("typing slowly like hacker...")

# center text
print(eg.center("middle of screen"))

# box text
print(eg.box("text in box"))

### random

if u lazy use random:

# random style
print(eg.random())

# random preset
print(eg.random('preset'))

## presets list

we have many presets like:
rainbow, sunset, ocean, fire, matrix, night, neon, cool, hot, simple, gold...

## license

mit license free for use enjoy.
