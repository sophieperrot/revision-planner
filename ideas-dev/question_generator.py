#!/usr/bin/env python3

"""
TODO list
# make the substitute value into variable in an equation work for negative numbers (i.e. no more +-)
# expression/formula rule (eg generate y value given expression and x value)
# complex rules: nested, relational, conditional, dependent rules
"""

import re
import random
import csv
import os

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
VARIABLES_FILENAME = os.path.join(os.getcwd(), "variables.csv")

def parse_variables(var_file):
    variables = {}
    with open(var_file) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            variables[row["name"]] = row["rule"]
        return variables

def parse_rule(rule):
    rule_type, rule_params = re.split(":", rule)
    match rule_type:
        case "range":
            start, end = re.split("-", rule_params)
            return random.randint(int(start), int(end))
        case "equation":
            print(rule)
            # TODO: figure something out
        

def generate_new_question(question_template, var_file):
    variables = parse_variables(var_file)
    for variable, rule in variables.items():
        pattern = "{" + variable + "}"
        new_val = str(parse_rule(rule))
        question_template = re.sub(pattern, new_val, question_template) 
    return question_template


print(generate_new_question(example_input, VARIABLES_FILENAME))