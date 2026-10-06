import pytest
from builder import build_exercise
from data.data import Exercise

def test_build_exercise():
    result = build_exercise("   bench press", "url for bench press", "push the bench with your chest", "a good exercise for pectoralis major hypertrophy and strength")
    expected = Exercise(name="Bench Press", demo="url for bench press", instructions="push the bench with your chest", description="a good exercise for pectoralis major hypertrophy and strength")
    assert result == expected

def test_build_set():
    return 0

def test_build_line():
    return 0

def test_build_block():
    return 0

def test_build_workout():
    return 0

def test_build_period():
    return 0

def test_build_training_program():
    return 0
