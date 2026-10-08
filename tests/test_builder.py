import pytest
from datetime import datetime
from builder import (
    build_muscle, build_tag, build_equipment, build_movement, build_adaptation,
    build_exercise, get_volume, build_set, build_line, build_block,
    build_workout, build_period, build_training_program,
)
from data.data import (
    Muscle, Tag, Equipment, Movement, Adaptation, Exercise, Set, Line, Block,
    Workout, Period, Training_Program,
)

def test_build_muscle():
    concentric_action = (
        "Concentrically accelerates shoulder flexion (clavicular fibers), "
        "horizontal adduction, and internal rotation"
    )
    eccentric_action = (
        " Eccentrically decelerates shoulder extension, horizontal abduction, "
        "and external rotation. "
    )
    isometric_action = "       ISOMETRICALLY STABILIZES THE SHOULDER GIRDLE "
    result = build_muscle(
        " Pectoralis        Major      ", concentric_action, eccentric_action, isometric_action
    )
    expected = Muscle(
        name="Pectoralis Major",
        concentric_action=(
            "Concentrically accelerates shoulder flexion (clavicular fibers), "
            "horizontal adduction, and internal rotation"
        ),
        eccentric_action=(
            "Eccentrically decelerates shoulder extension, horizontal abduction, "
            "and external rotation."
        ),
        isometric_action="Isometrically stabilizes the shoulder girdle",
    )
    assert result == expected

def test_build_tag():
    result = build_tag("unilateral")
    assert result == Tag(tag="#unilateral")

def test_build_equipment():
    result = build_equipment("  resistance band ")
    assert result == Equipment(name="Resistance Band")

def test_build_movement():
    result = build_movement("  horizontal push ")
    assert result == Movement(name="Horizontal Push")

def test_build_adaptation():
    result = build_adaptation(" hypertrophy ")
    assert result == Adaptation(name="Hypertrophy")

def test_build_exercise():
    demo = "url for bench press"
    instructions = "push the bench with your chest"
    description = "a good exercise for pectoralis major hypertrophy and strength"
    result = build_exercise("   bench press", demo, instructions, description)
    expected = Exercise(
        name="Bench Press", demo=demo, instructions=instructions, description=description
    )
    assert result == expected

def test_get_volume():
    assert get_volume(10, 60.0) == 600.0

def test_build_set():
    result = build_set("  back squat ", 5, 100.0, 80.0, " 3-1-1 ", 1)
    expected = Set(
        title="Back Squat",
        rep_count=5,
        resistance_kg=100.0,
        intensity=80.0,
        tempo="3-1-1",
        volume=500.0,
        order_index=1,
    )
    assert result == expected

def test_build_line():
    exercise = build_exercise(
        "back squat",
        "url for back squat",
        "brace and squat down",
        "a compound lower body strength exercise",
    )
    sets = [
        build_set("back squat", 5, 100.0, 80.0, "3-1-1", 1),
        build_set("back squat", 5, 100.0, 80.0, "3-1-1", 2),
    ]
    result = build_line(90, 1, exercise=exercise, sets=sets)
    expected = Line(seconds_rest_between_sets=90, order_index=1, exercise=exercise, set_list=sets)
    assert result == expected

def test_build_block():
    exercise = build_exercise(
        "back squat",
        "url for back squat",
        "brace and squat down",
        "a compound lower body strength exercise",
    )
    line = build_line(
        90,
        1,
        exercise=exercise,
        sets=[build_set("back squat", 5, 100.0, 80.0, "3-1-1", 1)],
    )
    tag = build_tag("strength")
    timestamp = datetime(2026, 1, 5)
    result = build_block(
        " strength ",
        "lower body strength work",
        timestamp,
        45,
        lines=[line],
        tags=[tag],
    )
    expected = Block(
        title="Strength",
        description="lower body strength work",
        assigned_timestamp=timestamp,
        minutes_to_complete=45,
        line_list=[line],
        tag_list=[tag],
    )
    assert result == expected

def test_build_workout():
    exercise = build_exercise(
        "back squat",
        "url for back squat",
        "brace and squat down",
        "a compound lower body strength exercise",
    )
    line = build_line(
        90,
        1,
        exercise=exercise,
        sets=[build_set("back squat", 5, 100.0, 80.0, "3-1-1", 1)],
    )
    tag = build_tag("strength")
    timestamp = datetime(2026, 1, 5)
    block = build_block(
        "strength",
        "lower body strength work",
        timestamp,
        45,
        lines=[line],
        tags=[tag],
    )
    result = build_workout(
        " day 1 ",
        "lower body day",
        "felt strong",
        timestamp,
        60,
        lines_and_blocks=[block],
        tags=[tag],
    )
    expected = Workout(
        title="Day 1",
        description="lower body day",
        notes="felt strong",
        assigned_timestamp=timestamp,
        minutes_to_complete=60,
        line_and_block_list=[block],
        tag_list=[tag],
    )
    assert result == expected

def test_build_period():
    exercise = build_exercise(
        "back squat",
        "url for back squat",
        "brace and squat down",
        "a compound lower body strength exercise",
    )
    line = build_line(
        90,
        1,
        exercise=exercise,
        sets=[build_set("back squat", 5, 100.0, 80.0, "3-1-1", 1)],
    )
    tag = build_tag("strength")
    timestamp = datetime(2026, 1, 5)
    block = build_block(
        "strength",
        "lower body strength work",
        timestamp,
        45,
        lines=[line],
        tags=[tag],
    )
    workout = build_workout(
        "day 1",
        "lower body day",
        "felt strong",
        timestamp,
        60,
        lines_and_blocks=[block],
        tags=[tag],
    )
    start_date = datetime(2026, 1, 5)
    end_date = datetime(2026, 1, 11)
    result = build_period(
        " week 1 ",
        "first week of the block",
        "start of a new cycle",
        start_date,
        end_date,
        workouts=[workout],
        tags=[tag],
    )
    expected = Period(
        title="Week 1",
        description="first week of the block",
        notes="start of a new cycle",
        start_date=start_date,
        end_date=end_date,
        workout_list=[workout],
        tag_list=[tag],
    )
    assert result == expected

def test_build_training_program():
    exercise = build_exercise(
        "back squat",
        "url for back squat",
        "brace and squat down",
        "a compound lower body strength exercise",
    )
    line = build_line(
        90,
        1,
        exercise=exercise,
        sets=[build_set("back squat", 5, 100.0, 80.0, "3-1-1", 1)],
    )
    tag = build_tag("strength")
    timestamp = datetime(2026, 1, 5)
    block = build_block(
        "strength",
        "lower body strength work",
        timestamp,
        45,
        lines=[line],
        tags=[tag],
    )
    workout = build_workout(
        "day 1",
        "lower body day",
        "felt strong",
        timestamp,
        60,
        lines_and_blocks=[block],
        tags=[tag],
    )
    start_date = datetime(2026, 1, 5)
    end_date = datetime(2026, 1, 11)
    period = build_period(
        "week 1",
        "first week of the block",
        "start of a new cycle",
        start_date,
        end_date,
        workouts=[workout],
        tags=[tag],
    )
    program_start = datetime(2026, 1, 5)
    program_end = datetime(2026, 3, 29)
    date_created = datetime(2026, 1, 1)
    author = "Coach"
    result = build_training_program(
        author,
        " strength block 1 ",
        "a 12 week strength block",
        "built for an intermediate lifter",
        program_start,
        program_end,
        date_created,
        periods_and_workouts=[period],
        tags=[tag],
    )
    expected = Training_Program(
        author=author,
        title="Strength Block 1",
        description="a 12 week strength block",
        notes="built for an intermediate lifter",
        start_date=program_start,
        end_date=program_end,
        date_created=date_created,
        period_and_workout_list=[period],
        tag_list=[tag],
    )
    assert result == expected
