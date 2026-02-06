import easygradients as eg
import time

print("Oye sun, check kar raha hu sab kuch chal raha hai ki nahi")

print("\n--- Pehle Gradient check karte hai ---")
print(eg.gradient("Dekh bhai gradient mast lag raha hai na", ["#ff0000", "#00ff00"]))

print("\n--- Ab color check ---")
print(eg.color("Ye laal hai bhai", "#ff0000"))

print("\n--- Background bhi dekh le ---")
print(eg.bg_color("Iske piche kala hai", "#000000"))
print(eg.bg_gradient("Piche gradient hai boss", ["#0000ff", "#ffffff"]))

print("\n--- Styling wyling ---")
print(eg.style("Mota text hai ye", "bold"))
print(eg.style("Teda text", "italic"))
print(eg.style("Line mar diya niche", "underline"))
print(eg.style("Kaat diya isko", "strikethrough"))

print("\n--- Rainbow wali feeling ---")
print(eg.rainbow("Rang barse bhige chunar wali"))

print("\n--- Presets ka scene ---")
presets = ["sunset", "ocean", "fire", "matrix"]
for p in presets:
    print(f"Ye hai {p} wala style:")
    print(eg.gradient(f"Kaisa laga {p}?", p))

print("\n--- Random kuch bhi ---")
print("Ruk randomly kuch generate karta hu...")
kuch_bhi = eg.random()
if isinstance(kuch_bhi, list):
    print(eg.gradient("Ye le random gradient", kuch_bhi))
else:
    print(eg.color("Ye le random color", kuch_bhi))

print(eg.gradient("Bas ho gaya bhai, sab set hai! Maja aa gaya.", "neon"))
