'''
printer.py
'''
from jinja2 import Environment, FileSystemLoader

def print_line(line: Line):
    line_dict = {}
    line_dict["Exercise"] = line.exercise
    for set in line.set_list:
        line_dict[set.title] = f"{set.rep_count}x{set.resistance_kg}kg"
    
    line_dict["Rest"] = f"{line.seconds_rest_between_sets}s"
    return line_dict


def print_block():
    return 0

def print_workout():
    return 0
