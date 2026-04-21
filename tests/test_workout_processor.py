import workout_processor.workout_processor as wp
import pytest

def test_validate_file():
    assert wp.validate_file("Example Workout.xlsx") == True
    with pytest.raises(FileNotFoundError):
        wp.validate_file("filename.txt")

def test_get_extension():
    assert wp.get_extension("filename.txt") == '.txt'
