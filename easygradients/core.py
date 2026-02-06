from . import utils
from . import presets
import shutil

STYLES = {
    'bold': '1',
    'dim': '2',
    'italic': '3',
    'underline': '4',
    'blink': '5',
    'reverse': '7',
    'hidden': '8',
    'strikethrough': '9'
}

def _apply_rgb(r, g, b, bg=False):
    layer = 48 if bg else 38
    return f"\033[{layer};2;{r};{g};{b}m"

def _reset():
    return "\033[0m"

def style(text, styles):
    if isinstance(styles, str):
        styles = [styles]
    
    code_str = ""
    for s in styles:
        if s.lower() in STYLES:
            code_str += f"\033[{STYLES[s.lower()]}m"
            
    return f"{code_str}{text}{_reset()}"

def color(text, rgb_code, bg=False):
    if isinstance(rgb_code, str):
        if rgb_code in presets.gradients:
             pass 
        elif rgb_code.startswith('#'):
            rgb_code = utils.hex_to_rgb(rgb_code)
            
    r, g, b = rgb_code
    return f"{_apply_rgb(r, g, b, bg)}{text}{_reset()}"

def gradient(text, colors, bg=False):
    if not text:
        return ""
    
    if isinstance(colors, str):
        if colors in presets.gradients:
            colors = presets.gradients[colors]
        else:
             colors = [colors] 

    rgb_colors = []
    for c in colors:
        if isinstance(c, str) and c.startswith('#'):
            rgb_colors.append(utils.hex_to_rgb(c))
        else:
            rgb_colors.append(c)
            
    steps = utils.make_steps(rgb_colors, len(text))
    
    result = ""
    for char, rgb in zip(text, steps):
        r, g, b = rgb
        result += f"{_apply_rgb(r, g, b, bg)}{char}"
        
    result += _reset()
    return result

def bg_color(text, rgb_code):
    return color(text, rgb_code, bg=True)

def bg_gradient(text, colors):
    return gradient(text, colors, bg=True)

def rainbow(text, bg=False):
    return gradient(text, presets.gradients['rainbow'], bg=bg)

def random(query=None):
    import random as rnd
    
    if query == 'color':
        return utils.rand_col()
    elif query == 'gradient':
        return [utils.rand_col(), utils.rand_col()]
    elif query == 'preset':
        return rnd.choice(list(presets.gradients.keys()))
    else:
        if rnd.choice([True, False]):
            return utils.rand_col()
        else:
            return [utils.rand_col(), utils.rand_col()]

def typewriter(text, speed=0.05):
    utils.slow_print(text, speed)

def center(text):
    cols, _ = shutil.get_terminal_size()
    return text.center(cols)

def box(text, col=None):
    lines = text.split('\n')
    width = max(len(l) for l in lines)
    
    top = "+" + "-" * (width + 2) + "+"
    bot = "+" + "-" * (width + 2) + "+"
    
    res = top + "\n"
    for l in lines:
        res += "| " + l.ljust(width) + " |\n"
    res += bot
    
    if col:
        if isinstance(col, list):
            return gradient(res, col)
        else:
            return color(res, col)
    return res
