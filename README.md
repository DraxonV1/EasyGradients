# EasyGradients

A Python library to easily apply RGB gradients, colors, and styles to terminal text.

## Installation

```bash
pip install easygradients
```

## Usage

Import the library:

```python
import easygradients as eg
```

### Gradients

Apply a gradient to text using RGB tuples, hex codes, or preset names.

```python
# Using RGB tuples
my_gradient = [(255, 0, 0), (0, 0, 255)]
print(eg.gradient("Hello World", my_gradient))

# Using Hex codes
hex_gradient = ["#FF0000", "#00FF00", "#0000FF"]
print(eg.gradient("Colorful Text", hex_gradient))

# Using multiple Hex codes (e.g., 4 colors)
multi_hex = ["#00d9f5", "#00f5a0", "#ff00ff", "#ffff00"]
print(eg.gradient("Multi-stop Gradient", multi_hex))

# Using Presets
print(eg.gradient("Sunset Text", "sunset"))
print(eg.gradient("Ocean Vibes", "ocean"))
```

### Solid Colors

Apply a single solid color.

```python
# Using RGB tuple
print(eg.color("Red Text", (255, 0, 0)))

# Using Hex code
print(eg.color("Green Text", "#00FF00"))
```

### Backgrounds

Apply colors or gradients to the background.

```python
# Solid background
print(eg.bg_color("Black Text on White BG", "#FFFFFF"))

# Gradient background
print(eg.bg_gradient("Cool Background", ["#0000FF", "#00FFFF"]))
```

### Text Styling

Apply styles like bold, italic, underline, etc.

```python
print(eg.style("Bold Text", "bold"))
print(eg.style("Italic Text", "italic"))
print(eg.style("Underlined", "underline"))
print(eg.style("Multiple Styles", ["bold", "underline", "blink"]))
```

Available styles: `bold`, `dim`, `italic`, `underline`, `blink`, `reverse`, `hidden`, `strikethrough`.

### Special Effects

```python
# Rainbow text
print(eg.rainbow("Rainbow Text"))
```

### Random Generation

Generate random colors, gradients, or styling.

```python
# Generate a random color or gradient
style = eg.random()
if isinstance(style, list):
    print(eg.gradient("Random Style", style))
else:
    print(eg.color("Random Style", style))

# Force random color
rand_color = eg.random('color')
print(eg.color("Random Color", rand_color))

# Force random gradient
rand_grad = eg.random('gradient')
print(eg.gradient("Random Gradient", rand_grad))

# Random Preset
preset_name = eg.random('preset')
print(eg.gradient("Random Preset", preset_name))
```

## Available Presets

- rainbow
- sunset
- ocean
- morning
- matrix
- fire
- night
- candy
- neon

## License

MIT