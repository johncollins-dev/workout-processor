"""
data.py
"""

from dataclasses import dataclass
import datetime

@dataclass
class Muscle:
    name: str

# Enum potential. Using class to allow user customization/specification
@dataclass
class Adaptation:
    name: str

# Enum potential. Using class to allow user customization/specification
@dataclass
class Movement:
    name: str

@dataclass
class Tag:
    name: str

@dataclass
class Equipment:
    name: str

@dataclass
class Exercise:
    name: str
    demo: str
    prime_mover: Muscle
    synergists: list[Muscle] = field(default_factory=list)
    adaptation: Adaptation
    movement: Movement
    tags: list[Tag] = field(default_factory=list)
    equipment: Equipment
    instructions: str
    description: str
    notes: str
    progression: Exercise
    regression: Exercise

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

@dataclass
class Block:
    title: str
    date: datetime
    exercises: list[Exercise] = field(default_factory=list)
    tags: list[Tag] = field(default_factory=list)

@dataclass
class Workout:
    name: str
    date: datetime
    blocks: list[Block] = field(default_factory=list)
    exercises: list[Exercise] = field(default_factory=list)

