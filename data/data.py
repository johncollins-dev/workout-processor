"""
data.py

Provides data structures for holding the all the data in an xlsx sheet
Structures will be used to enter data into reps database
"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime
from typing import Union

@dataclass
class Trainer:
    availability: [[0 for hour in range(24)] for day in range(7)]
    
@dataclass
class Athlete:
    goal: str
    injury_history: str
    availability: [[0 for hour in range(24)] for day in range(7)]

@dataclass
class User:
    first_name: str
    last_name: str
    dob: datetime
    role: Trainer | Athlete

@dataclass
class Muscle:
    name: str
    concentric_action: str
    eccentric_action: str
    isometric_action: str

@dataclass
class Tag:
    tag: str

@dataclass
class Equipment:
    name: str

@dataclass
class Movement:
    name: str

@dataclass
class Adaptation:
    name: str

@dataclass
class Exercise:
    name: str
    demo: str
    instructions: str
    description: str
    demo_w: str = ''
    prime_mover: Muscle | None = None
    synergist_list: list[Muscle] = field(default_factory=list)
    adaptation: Adaptation | None = None
    movement: Movement | None = None
    tag_list: list[Tag] = field(default_factory=list)
    equipment: Equipment | None = None
    difficulty: str = ''
    notes: str = ''


@dataclass
class Set:
    title: str
    rep_count: int
    resistance_kg: float
    intensity: float
    tempo: str
    volume: float
    order_index: int

@dataclass
class Line:
    seconds_rest_between_sets: int
    order_index: int
    exercise: Exercise | None = None
    set_list: list[Set] = field(default_factory=list)

@dataclass
class Block:
    title: str
    description: str
    assigned_timestamp: datetime
    minutes_to_complete: int
    line_list: list[Line] = field(default_factory=list)
    tag_list: list[Tag] = field(default_factory=list)

@dataclass
class Workout:
    title: str
    description: str
    notes: str
    assigned_timestamp: datetime
    minutes_to_complete: int
    line_and_block_list: list[Line | Block] = field(default_factory=list)
    tag_list: list[Tag] = field(default_factory=list)

@dataclass
class Period:
    title: str
    description: str
    notes: str
    start_date: datetime
    end_date: datetime
    workout_list: list[Workout] = field(default_factory=list)
    tag_list: list[Tag] = field(default_factory=list)

@dataclass
class Training_Program:
    author: User
    title: str
    description: str
    notes: str
    start_date: datetime
    end_date: datetime
    date_created: datetime
    period_and_workout_list: list[Period | Workout] = field(default_factory=list)
    tag_list: list[Tag] = field(default_factory=list)
