"""
data.py

Provides data structures for holding the all the data in an xlsx sheet
Structures will be used to enter data into reps database
"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime

@dataclass
class Trainer:
    """
    The trainer-specific role a User can hold.

    Attributes:
        availability: a 7 (day of week) by 24 (hour of day) grid marking the trainer's open
                       hours.
    """
    availability: [[0 for hour in range(24)] for day in range(7)]

@dataclass
class Athlete:
    """
    The athlete-specific role a User can hold.

    Attributes:
        goal: the athlete's stated training goal.
        injury_history: written history of the athlete's injuries.
        availability: a 7 (day of week) by 24 (hour of day) grid marking the athlete's open
                       hours.
    """
    goal: str
    injury_history: str
    availability: [[0 for hour in range(24)] for day in range(7)]

@dataclass
class User:
    """
    A person using the system, either as a Trainer or an Athlete.

    Attributes:
        first_name: the user's first name.
        last_name: the user's last name.
        dob: the user's date of birth.
        role: holds the Trainer or Athlete role-specific data for this user.
    """
    first_name: str
    last_name: str
    dob: datetime
    role: Trainer | Athlete

@dataclass
class Muscle:
    """
    A single muscle, as referenced by an Exercise's prime mover/synergist fields.

    Attributes:
        name: the muscle's name.
        concentric_action: the muscle's concentric (shortening) action.
        eccentric_action: the muscle's eccentric (lengthening) action.
        isometric_action: the muscle's isometric (static) action.
    """
    name: str
    concentric_action: str
    eccentric_action: str
    isometric_action: str

@dataclass
class Tag:
    """
    A label that can be attached to an Exercise, Block, Workout, Period, or Training_Program.

    Attributes:
        tag: the tag's text, stored without a leading "#" (that's added when printed/rendered).
    """
    tag: str

@dataclass
class Equipment:
    """
    A piece of equipment used by an Exercise.

    Attributes:
        name: the equipment's name.
    """
    name: str

@dataclass
class Movement:
    """
    The primary movement pattern occurring in an Exercise (e.g. hinge, squat, push).

    Attributes:
        name: the movement's name.
    """
    name: str

@dataclass
class Adaptation:
    """
    A training adaptation an Exercise is designed to elicit (e.g. hypertrophy, strength).

    Attributes:
        name: the adaptation's name.
    """
    name: str

@dataclass
class Exercise:
    """
    Contains information useful in conveying an exercise including text and video instruction plus
    metadata

    Attributes:
        name: the exercise's name.
        demo: url to a video demonstration of the exercise. defaults to empty string.
        instructions: written instructions. defaults to empty string.
        description: written description. defaults to empty string.
        demo_w: url to a video demonstration of the exercise by a female athlete. defaults to empty
                string
        prime_mover: holds the Muscle that is the exercise's designated prime mover. defaults to
                     none.
        synergist_list: list of Muscles that are the exercise's designated synergists. defaults to
                        empty list.
        adaptation: holds the adaptation that the exercise elicits. defaults to none.
        movement: holds the primary movement occurring in the exercise. defaults to none.
        tag_list: list of Tags that belong to the exercise. defaults to empty list.
        equipment: holds the equipment used in the exercise. defaults to none.
        difficulty: specifies the relative difficulty of the exercise. defaults to empty string.
        notes: holds notes related to the exercise. defaults to empty string.
    """
    name: str
    demo: str = ''
    instructions: str = ''
    description: str = ''
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
    """
    A single set of an exercise

    Attributes:
        title: the set's label (e.g. "Set 1", "Warm-up Set").
        rep_count: the number of reps performed.
        resistance_kg: the resistance/weight used, in kilograms.
        intensity: the set's intensity as a fraction of 1RM.
        tempo: the tempo the set was/should be performed at.
        volume: the set's volume load (rep_count * resistance_kg), computed by
                builder.get_volume rather than supplied directly.
        order_index: the set's position within its Line's set_list.
    """
    title: str
    rep_count: int
    resistance_kg: float
    intensity: float
    tempo: str
    volume: float
    order_index: int

@dataclass
class Line:
    """
    A single exercise entry within a Block or Workout, pairing an Exercise with its Sets.

    Attributes:
        seconds_rest_between_sets: rest time between sets, in seconds.
        order_index: the line's position within its parent Block/Workout.
        exercise: the Exercise being performed on this line. defaults to none.
        set_list: list of Sets performed for this line's exercise. defaults to empty list.
    """
    seconds_rest_between_sets: int
    order_index: int
    exercise: Exercise | None = None
    set_list: list[Set] = field(default_factory=list)

@dataclass
class Block:
    """
    A titled group of Lines (and/or nested Blocks) within a Workout (e.g. "Warm Up",
    "Superset A").

    Attributes:
        title: the block's title.
        description: written description of the block.
        assigned_timestamp: the date/time the block is assigned for.
        minutes_to_complete: estimated time to complete the block, in minutes.
        line_list: list of Lines that make up the block. defaults to empty list.
        tag_list: list of Tags that belong to the block. defaults to empty list.
    """
    title: str
    description: str
    assigned_timestamp: datetime
    minutes_to_complete: int
    line_list: list[Line] = field(default_factory=list)
    tag_list: list[Tag] = field(default_factory=list)

@dataclass
class Workout:
    """
    A single day's workout, holding Lines and/or Blocks directly (a Workout doesn't have to go
    through Block to hold a Line).

    Attributes:
        title: the workout's title (e.g. "Day 1").
        description: written description of the workout.
        notes: notes related to the workout.
        assigned_timestamp: the date/time the workout is assigned for.
        minutes_to_complete: estimated time to complete the workout, in minutes.
        line_and_block_list: list of Lines and/or Blocks that make up the workout. defaults to
                              empty list.
        tag_list: list of Tags that belong to the workout. defaults to empty list.
    """
    title: str
    description: str
    notes: str
    assigned_timestamp: datetime
    minutes_to_complete: int
    line_and_block_list: list[Line | Block] = field(default_factory=list)
    tag_list: list[Tag] = field(default_factory=list)

@dataclass
class Period:
    """
    A titled span of time (e.g. a training block/phase) containing a list of Workouts.

    Attributes:
        title: the period's title.
        description: written description of the period.
        notes: notes related to the period.
        start_date: the date the period begins.
        end_date: the date the period ends.
        workout_list: list of Workouts that make up the period. defaults to empty list.
        tag_list: list of Tags that belong to the period. defaults to empty list.
    """
    title: str
    description: str
    notes: str
    start_date: datetime
    end_date: datetime
    workout_list: list[Workout] = field(default_factory=list)
    tag_list: list[Tag] = field(default_factory=list)

@dataclass
class Training_Program:
    """
    The top-level container for an entire workout program, holding Periods and/or Workouts
    directly (a Training_Program doesn't have to go through Period to hold a Workout).

    Attributes:
        author: the User (Trainer or Athlete) who authored the program.
        title: the program's title.
        description: written description of the program.
        notes: notes related to the program.
        start_date: the date the program begins.
        end_date: the date the program ends.
        date_created: the date the program was created.
        period_and_workout_list: list of Periods and/or Workouts that make up the program.
                                  defaults to empty list.
        tag_list: list of Tags that belong to the program. defaults to empty list.
    """
    author: User
    title: str
    description: str
    notes: str
    start_date: datetime
    end_date: datetime
    date_created: datetime
    period_and_workout_list: list[Period | Workout] = field(default_factory=list)
    tag_list: list[Tag] = field(default_factory=list)
