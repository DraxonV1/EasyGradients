from . import utils as help_tools
from . import presets as my_styles
import shutil

STYLE_CODES = {
    'bold': '1',
    'dim': '2',
    'italic': '3',
    'underline': '4',
    'blink': '5',
    'reverse': '7',
    'hidden': '8',
    'strikethrough': '9'
}

def _put_rgb(r, g, b, back_ground=False):
    layer_num = 48 if back_ground else 38
    return f"\033[{layer_num};2;{r};{g};{b}m"

def _clear_all():
    return "\033[0m"

def style(input_text, style_names):
    if isinstance(style_names, str):
        style_names = [style_names]
    
    start_codes = ""
    for s in style_names:
        if s.lower() in STYLE_CODES:
            start_codes += f"\033[{STYLE_CODES[s.lower()]}m"
            
    return f"{start_codes}{input_text}{_clear_all()}"

def color(input_text, col_code, back_ground=False):
    if isinstance(col_code, str):
        if col_code.startswith('#'):
            col_code = help_tools.hex_to_rgb(col_code)
        elif col_code in my_styles.gradients:
            col_code = help_tools.hex_to_rgb(my_styles.gradients[col_code][0])
            
    r_val, g_val, b_val = col_code
    return f"{_put_rgb(r_val, g_val, b_val, back_ground)}{input_text}{_clear_all()}"

def gradient(input_text, list_of_cols, back_ground=False):
    if not input_text:
        return ""
    
    if isinstance(list_of_cols, str):
        if list_of_cols in my_styles.gradients:
            list_of_cols = my_styles.gradients[list_of_cols]
        else:
             list_of_cols = [list_of_cols] 

    real_rgb_list = []
    for ek_col in list_of_cols:
        if isinstance(ek_col, str) and ek_col.startswith('#'):
            real_rgb_list.append(help_tools.hex_to_rgb(ek_col))
        elif isinstance(ek_col, tuple):
            real_rgb_list.append(ek_col)
        else:
            real_rgb_list.append((255, 255, 255))
            
    every_step = help_tools.make_steps(real_rgb_list, len(input_text))
    
    final_output = ""
    for letter, rgb_val in zip(input_text, every_step):
        rv, gv, bv = rgb_val
        final_output += f"{_put_rgb(rv, gv, bv, back_ground)}{letter}"
        
    final_output += _clear_all()
    return final_output

def bg_color(input_text, col_code):
    return color(input_text, col_code, back_ground=True)

def bg_gradient(input_text, list_of_cols):
    return gradient(input_text, list_of_cols, back_ground=True)

def rainbow(input_text, back_ground=False):
    return gradient(input_text, my_styles.gradients['rainbow'], back_ground=back_ground)

def random(what_you_want=None, show_info=False):
    import random as radom_tool
    
    output_val = None
    messge = ""
    
    if what_you_want == 'color':
        output_val = help_tools.rand_col()
        messge = f"Color: {output_val}"
    elif what_you_want == 'gradient':
        output_val = [help_tools.rand_col(), help_tools.rand_col()]
        messge = f"Gradient: {output_val}"
    elif what_you_want == 'preset':
        output_val = radom_tool.choice(list(my_styles.gradients.keys()))
        messge = f"Preset: {output_val}"
    else:
        luck = radom_tool.choice(['color', 'gradient', 'preset'])
        if luck == 'color':
            output_val = help_tools.rand_col()
            messge = f"Color: {output_val}"
        elif luck == 'gradient':
            output_val = [help_tools.rand_col(), help_tools.rand_col()]
            messge = f"Gradient: {output_val}"
        else:
            output_val = radom_tool.choice(list(my_styles.gradients.keys()))
            messge = f"Preset: {output_val}"
            
    if show_info:
        print(f"I found this radom {messge} for you!")
        
    return output_val

def typewriter(input_text, wait_time=0.05):
    help_tools.slow_print(input_text, wait_time)

def center(input_text):
    screen_width, _ = shutil.get_terminal_size()
    return input_text.center(screen_width)

def box(input_text, border_col=None):
    all_lines = input_text.split('\n')
    max_len = max(len(ek_line) for ek_line in all_lines)
    
    top_border = "+" + "-" * (max_len + 2) + "+"
    bottom_border = "+" + "-" * (max_len + 2) + "+"
    
    full_box = top_border + "\n"
    for ek_line in all_lines:
        full_box += "| " + ek_line.ljust(max_len) + " |\n"
    full_box += bottom_border
    
    if border_col:
        if isinstance(border_col, list) or (isinstance(border_col, str) and border_col in my_styles.gradients):
            return gradient(full_box, border_col)
        else:
            return color(full_box, border_col)
    return full_box