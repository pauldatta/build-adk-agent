import pytest
import os
from meeting_notes_agent.tools.file_writer import save

def test_save_success():
    file_path = "test_notes.md"
    content = "These are my notes."
    
    result = save(content, file_path)
    
    assert result["success"] == True
    assert result["message"] == f"File saved to {file_path}"
    
    with open(file_path, "r") as f:
        assert f.read() == content
        
    os.remove(file_path)

def test_save_path_is_directory():
    dir_path = "test_dir"
    os.mkdir(dir_path)
    
    with pytest.raises(IsADirectoryError):
        save("some content", dir_path)
        
    os.rmdir(dir_path)
