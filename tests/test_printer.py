import pytest
from datetime import datetime
from data.data import Exercise, Set, Line, Block, Workout
from builder import build_tag, build_set, build_line, build_block
from printer import print_tag, print_line, print_block, print_workout, Printer

@pytest.fixture
def warmup_tags():
    return [build_tag('warm-up'), build_tag('stretch'), build_tag('mobility')]

@pytest.fixture
def warmup_line_1():
    return build_line(0, 1, Exercise('WGS', 'youtube-link', 'half-kneel, hands on the floor, go under armpit with inner hand, reach for ceiling', 'full body stretch', 'youtube-link'), ['Set 1', 8, 0.0, 0.0, 'slow', 0.0, 1])

@pytest.fixture
def warmup_line_2():
    return build_line(0, 2, Exercise('Corner Pec Stretch', 'youtube link', 'with your hands up, split stance and lean against corner, move back and forth', 'stretch for the pecs', 'youtube-link'), ['Set 1', 8, 0.0, 0.0, 'slow', 0.0, 1])

@pytest.fixture
def warmup_line_3():
    return build_line(0, 3, Exercise('Supine Piriformis Stretch', 'youtube-link', 'lay flat on mat, bring one ankle to knee, hold hamstring, pull toward face', 'stretch for the piriformis', 'youtube-link'), ['Set 1', 8, 0.0, 0.0, 'slow', 0.0, 1])

@pytest.fixture
def warmup_line_4():
    return build_line(0, 4, Exercise('Supine Lumbar Rotation', 'youtube-link', 'lay flat on mat, pick up legs, rotate around waist', 'stretch for the L spine', 'youtube-link'), ['Set 1', 8, 0.0, 0.0, 'slow', 0.0, 1])

@pytest.fixture
def warmup_line_5():
    return build_line(0, 5, Exercise('TRX Lat Stretch', 'youtube-link', 'hold on to trx and sit back, relax shoulders, tilt side to side', 'stretch for the lats', 'youtube-link'), ['Set 1', 8, 0.0, 0.0, 'slow', 0.0, 1])

@pytest.fixture
def warmup_block():
    return build_block('Warm Up', 'Full Body Warm Up', datetime(2026, 10, 20, 15, 30, 45), 5, [warmup_line_1, warmup_line_2, warmup_line_3, warmup_line_4, warmup_line_5], warmup_tags)

def test_print_tag():
    expected = "#hypertrophy"
    result = print_tag(build_tag("hypertrophy"))
    assert result == expected

def test_print_line():
    expected = {"Exercise": "BB Incline Press",
                "Set 1": "10x55kg",
                "Set 2": "10x60kg",
                "Set 3": "8x65kg",
                "Set 4": "8x65kg",
                "Rest": "60s"
    }
    test_line = Line(seconds_rest_between_sets=60,
                     order_index=1,
                     exercise=Exercise(name="BB Incline Press"),
                     set_list=[Set(title="Set 1", rep_count=10, resistance_kg=55, intensity=0.50,
                                   tempo="slow", volume=550, order_index=1),
                               Set(title="Set 2", rep_count=10, resistance_kg=60, intensity=0.50,
                                   tempo="slow", volume=550, order_index=2),
                               Set(title="Set 3", rep_count=8, resistance_kg=65, intensity=0.50,
                                   tempo="slow", volume=550, order_index=3),
                               Set(title="Set 4", rep_count=8, resistance_kg=65, intensity=0.50,
                                   tempo="slow", volume=550, order_index=4),
                    ]
                )
    result = print_line(test_line)
    assert result == expected


def test_printer_line():
    test_line = Line(seconds_rest_between_sets=60,
                     order_index=1,
                     exercise=Exercise(name="BB Incline Press"),
                     set_list=[Set(title="Set 1", rep_count=10, resistance_kg=55, intensity=0.50,
                                   tempo="slow", volume=550, order_index=1)])
    result = Printer(test_line)
    assert "BB Incline Press" in result.html
    assert "10x55kg" in result.html


def test_print_block():
    tags = [
        build_tag("lower"),
        build_tag("stretch"),
        build_tag("warmup"),
        build_tag("activation"),
    ]

    lines = [
        build_line(0, 1, Exercise("WGS"),
                   [build_set("Set 1", 8, 0.0, 0.0, "slow", 1)]),
        build_line(0, 2, Exercise("Quad and Hamstring Stretch"),
                   [build_set("Set 1", 8, 0.0, 0.0, "slow", 1)]),
        build_line(0, 3, Exercise("90/90 Hip Drive Stretch"),
                   [build_set("Set 1", 8, 0.0, 0.0, "slow", 1)]),
        build_line(0, 4, Exercise("Glute Bridge"),
                   [build_set("Set 1", 8, 0.0, 0.0, "slow", 1)]),
        build_line(0, 5, Exercise("DNS Star"),
                   [build_set("Set 1", 8, 0.0, 0.0, "slow", 1)]),
    ]

    expected = {"Title": "Warm Up",
                "Description": "Stretch Hips and Hamstrings, activate glutes",
                "Assigned": "10/20",
                "Duration": "10 min",
                "Lines": [print_line(line) for line in lines],
                "Tags": [print_tag(tag) for tag in tags],
    }

    test_block = build_block("Warm Up",
                             "Stretch Hips and Hamstrings, activate glutes",
                             datetime(2026, 10, 20, 15, 30, 45),
                             10,
                             lines,
                             tags,
                 )

    result = print_block(test_block)

    assert result == expected

def test_print_workout():
    tags = [
        build_tag("kettlebell"),
        build_tag("strength"),
        build_tag("functional"),
        build_tag("full-body")
    ]

    lines = [

    ]
    blocks = [
        build_block
    ]

def test_print_period():
    pass

def test_print_training_program():
    pass
