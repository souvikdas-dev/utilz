# Utility functions for files

# file_utils.py

import json


def read_json(file_path):
    """Read a JSON file and return the parsed content."""
    with open(file_path, "r") as file:
        return json.load(file)


def write_json(data, file_path):
    """Write data to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
