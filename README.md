# EasyGradients 🌈

![Icon](icon.png)

Hello friend! I made this library because I love colors in my terminal.
 It is very easy to use and even a small child can use it. No complex coding here, just simple things that work like magic!

## How to Install this?

Just type this simple command in your black screen (terminal):

```bash
pip install easygradients
```

## How to use it? (Examples for you)

First you must bring the library in your code:

```python
import easygradients as eg
```

### 1. Simple Colors
If you want to make text red or green, just do this:

```python
# Use hex code like this
print(eg.color("I am red color!", "#FF0000"))

# Or use simple numbers (RGB)
print(eg.color("I am green color!", (0, 255, 0)))
```

### 2. Beautiful Gradients
Gradient means many colors mixing together. It looks very nice!

```python
# Mix red and blue
print(eg.gradient("Mixing colors wow!", ["#FF0000", "#0000FF"]))

# You can even use many colors
print(eg.gradient("So many colors!", ["#FF0000", "#FFFF00", "#00FF00", "#0000FF"]))
```

### 3. Using Presets (Shortcuts)
I have already made some nice color sets for you. You don't need to find hex codes!

```python
print(eg.gradient("Sunset is looking good", "sunset"))
print(eg.gradient("Ocean is blue", "ocean"))
print(eg.gradient("I am hacker in matrix", "matrix"))
```

### 4. Background Colors
You can even change the back side of the text:

```python
print(eg.bg_color("Black background here", "#000000"))
print(eg.bg_gradient("Gradient background is crazy!", ["#FF5F6D", "#FFC371"]))
```

### 5. Styling Text
Make it bold or italic or draw line under it:

```python
print(eg.style("I am very BOLD", "bold"))
print(eg.style("I am leaning (italic)", "italic"))
print(eg.style("Line under me", "underline"))
```

### 6. Special Tricks
Some more things I added because I was bored:

```python
# Rainbow!
print(eg.rainbow("FULL RAINBOW TEXT!!!"))

# Type like a movie hacker
eg.typewriter("System is hacking now... please wait...")

# Put text in the middle
print(eg.center("I am sitting in the middle"))

# Put text inside a box
print(eg.box("Special Message for you", border_col="gold"))
```

### 7. Random (If you are lazy)
If you can't choose color, let the computer choose:

```python
# Computer will pick anything!
my_luck = eg.random(show_info=True) 
print(eg.gradient("I don't know what color this is!", my_luck))

# Ask for random preset only
preset_luck = eg.random(what_you_want='preset', show_info=True)
print(eg.gradient("Random preset used!", preset_luck))
```

## All my Presets:
`rainbow`, `sunset`, `ocean`, `morning`, `matrix`, `fire`, `night`, `candy`, `neon`, `cool`, `hot`, `simple`, `grass`, `sky`, `blood`, `gold`.

## License
It is MIT license. You can use it anywhere you want, I don't care! Just enjoy the colors.

Made with love by DraxonV1.
