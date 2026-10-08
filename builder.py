'''
builder.py
'''
from data.data import (
    Muscle, Tag, Equipment, Movement, Adaptation, Exercise, Set, Line, Block,
    Workout, Period, Training_Program,
)
from datetime import datetime

def build_muscle(name: str, concentric_action: str, eccentric_action: str, isometric_action: str) -> Muscle:
    return Muscle(
            name=" ".join(name.split()).title(),
            concentric_action=concentric_action.strip().capitalize(),
            eccentric_action=eccentric_action.strip().capitalize(),
            isometric_action=isometric_action.strip().capitalize()
    )

def build_tag(name: str) -> Tag:
    return Tag(tag=f"#{name.strip()}")

def build_equipment(name: str) -> Equipment:
    return Equipment(name=name.strip().title())

def build_movement(name: str) -> Movement:
    return Movement(name=name.strip().title())

def build_adaptation(name: str) -> Adaptation:
    return Adaptation(name=name.strip().title())

def build_exercise(name: str, demo: str, instructions: str, description: str, demo_w: str = '') -> Exercise:
    return Exercise(name=name.strip().title(), demo=demo, instructions=instructions, description=description, demo_w=demo_w)

def get_volume(rep_count: int, resistance_kg: float) -> float:
    return rep_count * resistance_kg

def build_set(title: str, rep_count: int, resistance_kg: float, intensity: float, tempo: str, order_index: int) -> Set:
    return Set(
            title=title.strip().title(),
            rep_count=rep_count,
            resistance_kg=resistance_kg,
            intensity=intensity,
            tempo=tempo.strip(),
            volume=get_volume(rep_count, resistance_kg),
            order_index=order_index
    )

def build_line(seconds_rest_between_sets: int, order_index: int, exercise: Exercise | None = None, sets: list[Set] | None = None) -> Line:
    return Line(
            seconds_rest_between_sets=seconds_rest_between_sets,
            order_index=order_index,
            exercise=exercise,
            set_list=sets or []
    )

def build_block(title: str, description: str, assigned_timestamp: datetime, minutes_to_complete: int, lines: list[Line] | None = None, tags: list[Tag] | None = None) -> Block:
    return Block(
            title=title.strip().title(),
            description=description,
            assigned_timestamp=assigned_timestamp,
            minutes_to_complete=minutes_to_complete,
            line_list=lines or [],
            tag_list=tags or []
    )

def build_workout(title: str, description: str, notes: str, assigned_timestamp: datetime, minutes_to_complete: int, lines_and_blocks: list[Line | Block] | None = None, tags: list[Tag] | None = None) -> Workout:
    return Workout(
            title=title.strip().title(),
            description=description,
            notes=notes,
            assigned_timestamp=assigned_timestamp,
            minutes_to_complete=minutes_to_complete,
            line_and_block_list=lines_and_blocks or [],
            tag_list=tags or []
    )

def build_period(title: str, description: str, notes: str, start_date: datetime, end_date: datetime, workouts: list[Workout] | None = None, tags: list[Tag] | None = None) -> Period:
    return Period(
            title=title.strip().title(),
            description=description,
            notes=notes,
            start_date=start_date,
            end_date=end_date,
            workout_list=workouts or [],
            tag_list=tags or []
    )

def build_training_program(author, title: str, description: str, notes: str, start_date: datetime, end_date: datetime, date_created: datetime, periods_and_workouts: list[Period | Workout] | None = None, tags: list[Tag] | None = None) -> Training_Program:
    return Training_Program(
            author=author,
            title=title.strip().title(),
            description=description,
            notes=notes,
            start_date=start_date,
            end_date=end_date,
            date_created=date_created,
            period_and_workout_list=periods_and_workouts or [],
            tag_list=tags or []
    )
