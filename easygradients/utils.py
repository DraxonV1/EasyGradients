import random
import time
import sys

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def rand_col():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def mixer(col1, col2, factor):
    r = int(col1[0] + (col2[0] - col1[0]) * factor)
    g = int(col1[1] + (col2[1] - col1[1]) * factor)
    b = int(col1[2] + (col2[2] - col1[2]) * factor)
    return (r, g, b)

def make_steps(all_cols, total_steps):
    if total_steps < 2:
        return [all_cols[0]] * total_steps
    if len(all_cols) < 2:
        return [all_cols[0]] * total_steps
    
    final_list = []
    sections = len(all_cols) - 1
    steps_per_sec = total_steps // sections
    extra_steps = total_steps % sections
    
    for i in range(sections):
        start_c = all_cols[i]
        end_c = all_cols[i+1]
        
        current_steps = steps_per_sec + (1 if i < extra_steps else 0)
        
        for j in range(current_steps):
            f = j / current_steps
            final_list.append(mixer(start_c, end_c, f))
            
    if len(final_list) < total_steps:
        final_list.append(all_cols[-1])
        
    return final_list[:total_steps]

def slow_print(my_text, my_speed=0.05):
    for ek_char in my_text:
        sys.stdout.write(ek_char)
        sys.stdout.flush()
        time.sleep(my_speed)
    print()
