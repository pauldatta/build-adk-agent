import pytest
import os
from unittest.mock import patch, MagicMock
from meeting_notes_agent.tools.transcription_tool import transcribe_audio

def test_transcribe_audio_file_not_found():
    with pytest.raises(FileNotFoundError):
        transcribe_audio("non_existent_file.mp3")

@patch('google.generativeai.GenerativeModel')
@patch('google.generativeai.upload_file')
def test_transcribe_audio_success(mock_upload_file, mock_generative_model):
    # Arrange
    mock_audio_file = MagicMock()
    mock_upload_file.return_value = mock_audio_file
    
    mock_response = MagicMock()
    mock_response.text = "This is a test transcript."
    
    mock_model_instance = MagicMock()
    mock_model_instance.generate_content.return_value = mock_response
    mock_generative_model.return_value = mock_model_instance
    
    # Create a dummy file to transcribe
    dummy_file_path = "test.mp3"
    with open(dummy_file_path, "w") as f:
        f.write("dummy audio data")

    # Act
    result = transcribe_audio(dummy_file_path)

    # Assert
    assert result == "This is a test transcript."
    mock_upload_file.assert_called_once_with(path=dummy_file_path)
    mock_model_instance.generate_content.assert_called_once_with(
        ["Transcribe the following audio:", mock_audio_file]
    )

    # Cleanup
    os.remove(dummy_file_path)
