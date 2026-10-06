'''
builder.py
'''
from data.data import Block, Line, Tag, Exercise
from datetime import datetime

def build_exercise(name: str, demo: str, instructions: str, description: str):
    return Exercise(name=name.strip().title(), demo=demo, instructions=instructions, description=description)


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
