# Utility functions for files

# file_utils.py

import json
import os


def read_json(file_path):
    """Read a JSON file and return the parsed content."""
    with open(file_path, "r") as file:
        return json.load(file)


def write_json(data, file_path):
    """Write data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def read_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    with open(file_path, "r") as file:
        return file.read()


def write_to_file(file_path: str, content: str) -> None:
    """
    Writes content to a file, overwriting it if it already exists.
    """
    with open(file_path, "w") as file:
        file.write(content)


def file_exists(file_path: str) -> bool:
    """
    Returns True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)
