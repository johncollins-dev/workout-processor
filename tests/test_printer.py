import pytest
from datetime import datetime
from data.data import Exercise, Set, Line, Block, Workout
from builder import build_tag, build_set, build_line, build_block
from printer import print_tag, print_line, print_block, print_workout

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
                     exercise=Exercise(name="BB Incline Press").name,
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
    assert 1 == 1
