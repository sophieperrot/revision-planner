#!/usr/bin/env python3

import re

"""
EXAMPLE QUESTION
y=2x^3-4x+5
Find the equation of the tangent to the curve at the point P(2, 13).
Write your answer in the form y=mx+c, where m and c are integers to be found. [5]
"""

example_input = """
y={a}x^3+{b}x^2+{c}x+{d}
Find the equation of the tangent to the curve at the point P({x}, {y}).
Write your answer in the form y=mx+c, where m and c are integers to be found. [5]
"""

variables = set()
def parse_variables(input):
   return re.findall("{([a-z0-9]+)}", input)


print(parse_variables(example_input))