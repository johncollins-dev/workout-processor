"""
data.py
"""
from __future__ import annotations
from dataclasses import dataclass, field
import datetime

# used in exercise
@dataclass
class Muscle:
    name: str

# Enum potential. Using class to allow user customization/specification
# used in Exercise
@dataclass
class Adaptation:
    name: str

# Enum potential. Using class to allow user customization/specification
# used in Exercise
@dataclass
class Movement:
    name: str

# used in Exercise and Block
@dataclass
class Tag:
    name: str

# used in Exercise
@dataclass
class Equipment:
    name: str

@dataclass
class Exercise:
    name: str
    demo: str = 'ADD DEMONSTRATION'
    prime_mover: Muscle | None = None
    equipment: Equipment | None = None
    instructions: str = 'ADD INSTRUCTIONS'
    description: str = 'ADD DESCRIPTION'
    notes: str = 'ADD NOTES'
    progression: 'Exercise | None' = None
    regression: 'Exercise | None' = None
    adaptation: Adaptation | None = None
    movement: Movement | None = None
    synergists: list[Muscle] = field(default_factory=list)
    tags: list[Tag] = field(default_factory=list)

'''
Cells are to be used in lines
They are essentially key value pairs, where the key is a string value such as "Set 1" and the value
is a string that the user can input
Cells can also be used for Tempo and Rest, which would contain their respective inputable string
values
'''
@dataclass
class Cell:
    key: str
    value: str

'''
Lines contain a single exercise an an optional set of sets and other modifiers for that specific
exercise.
Used by Blocks and Workouts, user can modify number of sets and what other variables there are
(tempo, intensity, rest, etc.)
Doesn't have to hold an exercise, can hold a string like "Push Up"
a Line is declared with exercise/string as first argument then an arbitrary list keys in kv pairs
'''
@dataclass
class Line:
    exercise: Exercise
    cells: list[Cell] = field(default_factory=list)

'''
Blocks are an abstraction layer for organizing lines into workouts. They can take the form of
traditional blocks such as warm ups, activation, strength, cool down, etc. or they can encapsulate
lines into a singular workout. Blocks can contain other blocks. You can have a workout block that
contains a warm up and strength block and even a block that contains workout blocks, a block that
contains blocks of blocks that contain workouts, etc.
'''
# TODO: implement super/giant set functionality
@dataclass
class Block:
    title: str
    date: datetime | None = None
    purpose: str = 'ADD PURPOSE'
    description: str = 'ADD DESCRIPTION'
    lines: list[Line] = field(default_factory=list)
    tags: list[Tag] = field(default_factory=list)







'''
replaced by Block class
@dataclass
class Workout:
    name: str
    date: datetime
    blocks: list[Block] = field(default_factory=list)
    exercises: list[Exercise] = field(default_factory=list)
'''
