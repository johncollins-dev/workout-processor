from workout_processor import workout_processor as wp
import pytest

def test_validate_file():
    assert wp.validate_file("Example Workout.xlsx") == True
    with pytest.raises(FileNotFoundError):
        wp.validate_file("filename.txt")

def test_check_extension():
    assert wp.check_extension("filename.xlsx") == '.xlsx'
