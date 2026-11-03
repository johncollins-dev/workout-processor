'''
printer.py
'''
from jinja2 import Environment, FileSystemLoader
from data.data import Tag

def print_tag(tag: Tag):
    return f"#{tag.tag}"

def print_line(line: Line):
    line_dict = {}
    line_dict["Exercise"] = line.exercise
    for set in line.set_list:
        line_dict[set.title] = f"{set.rep_count}x{set.resistance_kg}kg"

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

environment = Environment(loader=FileSystemLoader("templates/"))
workout_filename = "workout.html"
template = environment.get_template("workout.html")

with open(workout_filename, mode="w", encoding="utf-8") as workout:
    workout.write(template.render(workout_title="Day 1 11/3"))
    print(f"... wrote {template}")
