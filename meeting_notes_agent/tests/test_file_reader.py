import pytest
import os
from meeting_notes_agent.tools.file_reader import read_file

def test_read_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file("non_existent_file.txt")

def test_read_file_success():
    # Arrange
    file_path = "test_file.txt"
    content = "This is a test file."
    with open(file_path, "w") as f:
        f.write(content)

    # Act
    result = read_file(file_path)

    # Assert
    assert result == content

    # Cleanup
    os.remove(file_path)
