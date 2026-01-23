#!/usr/bin/env python3

"""
TODO list
# make the substitute value into variable in an equation work for negative numbers (i.e. no more +-)
# expression/formula rule (eg generate y value given expression and x value)
# complex rules: nested, relational, conditional, dependent rules
"""

import re
import random

"""
EXAMPLE QUESTION
y=2x^3-4x+5
Find the equation of the tangent to the curve at the point P(2, 13).
Write your answer in the form y=mx+c, where m and c are integers to be found. [5]
"""

example_input = """
y={a,range:1,10}x^3+{b,range:0,5}x^2+{c,range:0,15}x+{d,range:0,20}
Find the equation of the tangent to the curve at the point P({x,range:4,10}, {y}).
Write your answer in the form y=mx+c, where m and c are integers to be found. [5]
"""


def parse_variables(input):
    variables = {}
    input_variables = re.findall("{([a-z0-9]+),([^\}]+)}", input)
    for var_name, rule in input_variables:
        if var_name not in variables.keys():
            variables[var_name] = rule
    return variables

def parse_rule(rule):
    rule_type, rule_params = re.split(":", rule)
    if rule_type == "range":
        start, end = re.split(",", rule_params)
        return random.randint(int(start), int(end))

def generate_new_question(question_template, variables):
    for variable, rule in variables.items():
        pattern = "{" + variable + "," + rule + "}"
        new_val = str(parse_rule(rule))
        question_template = re.sub(pattern, new_val, question_template) 
    return question_template

variables = parse_variables(example_input)
print(generate_new_question(example_input, variables))