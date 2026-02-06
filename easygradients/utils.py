import random

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def interpolate(color1, color2, factor):
    r = int(color1[0] + (color2[0] - color1[0]) * factor)
    g = int(color1[1] + (color2[1] - color1[1]) * factor)
    b = int(color1[2] + (color2[2] - color1[2]) * factor)
    return (r, g, b)

def generate_gradient_steps(colors, steps):
    if steps < 2:
        return [colors[0]] * steps
    if len(colors) < 2:
        return [colors[0]] * steps
    
    result = []
    segments = len(colors) - 1
    steps_per_segment = steps // segments
    remainder = steps % segments
    
    for i in range(segments):
        start_color = colors[i]
        end_color = colors[i+1]
        
        current_steps = steps_per_segment + (1 if i < remainder else 0)
        
        for j in range(current_steps):
            factor = j / current_steps
            result.append(interpolate(start_color, end_color, factor))
            
    if len(result) < steps:
        result.append(colors[-1])
        
    return result[:steps]
