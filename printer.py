'''
printer.py
'''
from jinja2 import Environment, FileSystemLoader

def print_tag(tag: Tag):
    return tag.tag

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
