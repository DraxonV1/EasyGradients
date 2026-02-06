# EasyGradients

A Python library to easily apply RGB gradients and colors to terminal text.

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

Apply a gradient to text using a list of RGB tuples or hex codes.

```python
# Using RGB tuples
my_gradient = [(255, 0, 0), (0, 0, 255)]
print(eg.gradient("Hello World", my_gradient))

# Using Hex codes
hex_gradient = ["#FF0000", "#00FF00", "#0000FF"]
print(eg.gradient("Colorful Text", hex_gradient))
```

### Solid Colors

Apply a single solid color.

```python
# Using RGB tuple
print(eg.color("Red Text", (255, 0, 0)))

# Using Hex code
print(eg.color("Green Text", "#00FF00"))
```

### Random Generation

Generate random colors or gradients.

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
```

## License

MIT
