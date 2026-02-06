import random
import time
import sys

def hex_to_rgb(code):
    code = code.lstrip('#')
    return tuple(int(code[i:i+2], 16) for i in (0, 2, 4))

def rand_col():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def mixer(c1, c2, fac):
    r = int(c1[0] + (c2[0] - c1[0]) * fac)
    g = int(c1[1] + (c2[1] - c1[1]) * fac)
    b = int(c1[2] + (c2[2] - c1[2]) * fac)
    return (r, g, b)

def make_steps(cols, num):
    if num < 2:
        return [cols[0]] * num
    if len(cols) < 2:
        return [cols[0]] * num
    
    res = []
    seg = len(cols) - 1
    step_seg = num // seg
    rem = num % seg
    
    for i in range(seg):
        start = cols[i]
        end = cols[i+1]
        
        cur = step_seg + (1 if i < rem else 0)
        
        for j in range(cur):
            f = j / cur
            res.append(mixer(start, end, f))
            
    if len(res) < num:
        res.append(cols[-1])
        
    return res[:num]

def slow_print(txt, spd=0.05):
    for c in txt:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(spd)
    print()