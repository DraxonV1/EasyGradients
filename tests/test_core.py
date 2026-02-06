import unittest
import easygradients as eg
from io import StringIO
import sys

class TestMyCode(unittest.TestCase):

    def test_styling(self):
        styled_txt = eg.style("hello", "bold")
        self.assertIn("\033[1m", styled_txt)

    def test_coloring(self):
        colored_txt = eg.color("hello", "#FF0000")
        self.assertIn("255;0;0", colored_txt)

    def test_gradient_mixing(self):
        grad_txt = eg.gradient("hello", ["#FF0000", "#0000FF"])
        self.assertIn("\033[38;2;", grad_txt)

    def test_radom_info(self):
        temp_screen = StringIO()
        sys.stdout = temp_screen
        eg.random(show_info=True)
        sys.stdout = sys.__stdout__
        self.assertIn("I found this radom", temp_screen.getvalue())

    def test_presets_work(self):
        sun_txt = eg.gradient("hello", "sunset")
        self.assertIn("\033[38;2;", sun_txt)

    def test_making_box(self):
        box_txt = eg.box("hi")
        self.assertIn("+----+", box_txt)

if __name__ == '__main__':
    unittest.main()