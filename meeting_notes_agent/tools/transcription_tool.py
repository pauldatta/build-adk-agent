import os
import google.generativeai as genai

def transcribe_audio(file_path: str) -> str:
    """Transcribes an audio file using the Gemini API."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file was not found at: {file_path}")
    
    audio_file = genai.upload_file(path=file_path)
    model = genai.GenerativeModel(model_name="gemini-2.5-pro")
    response = model.generate_content(
        ["Transcribe the following audio:", audio_file]
    )
    return response.text
