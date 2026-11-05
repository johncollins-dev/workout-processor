'''
printer.py
'''
from jinja2 import Environment, FileSystemLoader
from data.data import Tag, Line, Block, Workout, Period, Training_Program

def print_tag(tag: Tag):
    return f"#{tag.tag}"

def print_line(line: Line):
    line_dict = {}
    line_dict["Exercise"] = line.exercise.name
    for set in line.set_list:
        # if sets do not use weight, the rep count will be printed without weight in kg
        if(set.resistance_kg > 0):
            line_dict[set.title] = f"{set.rep_count}x{set.resistance_kg:g}kg"
        else:
            line_dict[set.title] = f"{set.rep_count}"

    line_dict["Rest"] = f"{line.seconds_rest_between_sets}s"
    return line_dict


def print_block(block: Block):
    block_dict = {}
    block_dict["Title"] = block.title
    block_dict["Description"] = block.description
    block_dict["Assigned"] = f"{block.assigned_timestamp.month}/{block.assigned_timestamp.day}"
    block_dict["Duration"] = f"{block.minutes_to_complete} min"
    block_dict["Lines"] = [print_line(line) for line in block.line_list]
    block_dict["Tags"] = [print_tag(tag) for tag in block.tag_list]
    return block_dict

def print_workout():
    return 0


class Printer:
    environment = Environment(loader=FileSystemLoader("templates/"))

    def __init__(self, obj):
        if isinstance(obj, Line):
            line_dict = print_line(obj)
            template = self.environment.get_template("line.html")
            self.html = template.render(line=line_dict)
        elif isinstance(obj, Block):
            raise NotImplementedError("Printer does not support Block yet")
        elif isinstance(obj, Workout):
            raise NotImplementedError("Printer does not support Workout yet")
        elif isinstance(obj, Period):
            raise NotImplementedError("Printer does not support Period yet")
        elif isinstance(obj, Training_Program):
            raise NotImplementedError("Printer does not support Training_Program yet")
        else:
            raise TypeError(f"Printer does not support type {type(obj).__name__}")

    def write(self, filename):
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(self.html)
