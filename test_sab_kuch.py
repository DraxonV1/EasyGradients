import easygradients as eg
import time

print("Hey bro, checking everything now...")

print("\n--- Testing Gradient ---")
print(eg.gradient("Look bro this gradient is looking very nice", ["#ff0000", "#00ff00"]))

print("\n--- Testing Color ---")
print(eg.color("This is red color bro", "#ff0000"))

print("\n--- Testing Background ---")
print(eg.bg_color("Black background here", "#000000"))
print(eg.bg_gradient("Gradient background boss", ["#0000ff", "#ffffff"]))

print("\n--- Testing Styles ---")
print(eg.style("This is bold text", "bold"))
print(eg.style("This is italic text", "italic"))
print(eg.style("Line under text", "underline"))
print(eg.style("Cut the text", "strikethrough"))

print("\n--- Testing Rainbow ---")
print(eg.rainbow("Full rainbow color text here"))

print("\n--- Testing New Features ---")
print("Box check:")
print(eg.box("Hello Box"))
print(eg.box("Colored Box", "#00ff00"))

print("Center check:")
print(eg.center("I am in center"))

print("Typewriter check:")
eg.typewriter("I am typing very slow bro like hacker movie...")

print("\n--- Testing Presets ---")
presets = ["sunset", "ocean", "fire", "matrix", "gold", "blood"]
for p in presets:
    print(f"This is {p} style:")
    print(eg.gradient(f"Do you like {p}?", p))

print("\n--- Testing Random ---")
print("Wait, making something random...")
something = eg.random()
if isinstance(something, list):
    print(eg.gradient("Got a random gradient", something))
else:
    print(eg.color("Got a random color", something))

print(eg.gradient("Everything is working fine bro! Done.", "neon"))
