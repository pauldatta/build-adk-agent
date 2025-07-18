import os

def save(content: str, output_path: str) -> dict:
    """Saves content to a file, creating the directory if it doesn't exist."""
    if os.path.isdir(output_path):
        raise IsADirectoryError
    
    # Create the directory if it doesn't exist
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
        
    with open(output_path, "w") as f:
        f.write(content)
    return {"success": True, "message": f"File saved to {output_path}"}
