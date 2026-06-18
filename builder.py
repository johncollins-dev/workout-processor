'''
builder.py
'''
from data.data import Block, Line, Tag
from datetime import datetime

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
