import os

def read_file(file_path: str) -> str:
    """Reads the content of a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file was not found at: {file_path}")
    with open(file_path, "r") as f:
        return f.read()
