from . import utils

def color(text, rgb_code):
    if isinstance(rgb_code, str) and rgb_code.startswith('#'):
        rgb_code = utils.hex_to_rgb(rgb_code)
    
    r, g, b = rgb_code
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def gradient(text, colors):
    if not text:
        return ""
        
    rgb_colors = []
    for c in colors:
        if isinstance(c, str) and c.startswith('#'):
            rgb_colors.append(utils.hex_to_rgb(c))
        else:
            rgb_colors.append(c)
            
    steps = utils.generate_gradient_steps(rgb_colors, len(text))
    
    result = ""
    for char, rgb in zip(text, steps):
        r, g, b = rgb
        result += f"\033[38;2;{r};{g};{b}m{char}"
        
    result += "\033[0m"
    return result

def random(query=None):
    if query == 'color':
        return utils.random_color()
    elif query == 'gradient':
        return [utils.random_color(), utils.random_color()]
    else:
        import random as rnd
        if rnd.choice([True, False]):
            return utils.random_color()
        else:
            return [utils.random_color(), utils.random_color()]
