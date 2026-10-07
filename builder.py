'''
builder.py
'''
from data.data import Block, Line, Tag, Exercise
from datetime import datetime

def build_muscle()
def build_tag()
def build_equipment()
def build_movement()
def build_adaptation()
def build_exercise(name: str, demo: str, instructions: str, description: str):
    return Exercise(name=name.strip().title(), demo=demo, instructions=instructions, description=description)
def get_volume()
def build_set()
def build_line()
def build_block(title: str, date: datetime, purpose: str, description: str,lines: list[Line], tags: list[Tag]) -> Block:
    block = Block(
            title,
            date,
            purpose,
            description,
            lines,
            tags
    )
    return block
def build_workout()
def build_period()
def build_training_program()

