import pytest
from data.data import Exercise, Set, Line, Block, Workout
from printer import print_line, print_block, print_workout

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
    assert 1 == 1

def test_print_workout():
    assert 1 == 1
