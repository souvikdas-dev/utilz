**`utilz`** is a simple, fast, and flexible Python utility package that provides a set of commonly used utility functions for tasks like string manipulation, file handling, and basic math operations. Whether you're working on a small script or a large project, **`utilz`** makes it easy to access useful utilities without reinventing the wheel.

---
## Installation

You can install **`utilz`** via `pip`: 

```bash 
pip install utilz
```

## Features

- String manipulation utilities (e.g., capitalize words, truncate strings)
- File handling utilities (e.g., read/write JSON files)
- Basic math utilities (e.g., GCD, LCM)

---

## Usage

Once installed, you can start using **`utilz`** by importing the relevant utilities into your Python code.

### Example 1: String Manipulation

```python
from utilz import capitalize_words, truncate

  

text = "hello world"

capitalized_text = capitalize_words(text)

print(capitalized_text)  # Output: "Hello World"

  

short_text = truncate(text, length=5)

print(short_text)  # Output: "hello..."
```

### Example 2: Math Utilities

```python
from utilz import gcd, lcm

  

a, b = 54, 24

print(f"GCD of {a} and {b}: {gcd(a, b)}")  # Output: 6

print(f"LCM of {a} and {b}: {lcm(a, b)}")  # Output: 216
```

### Example 3: File Handling (JSON)

```python
from utilz import read_json, write_json

  

# Writing data to a JSON file

data = {"name": "Alice", "age": 30}

write_json(data, "data.json")

  

# Reading the JSON file back

read_data = read_json("data.json")

print(read_data)  # Output: {"name": "Alice", "age": 30}
```

### Example 4: Convenience Function

```python
from utilz import process_text

  

text = "this is a really long sentence that needs truncation and capitalization"

processed_text = process_text(text)

print(processed_text)  # Output: "This Is A Really Long..."
```

## API Reference

### String Utilities

- `capitalize_words(text: str) -> str`: Capitalize the first letter of each word in the string.
- `truncate(text: str, length: int) -> str`: Truncate the string to a specified length, appending "..." if necessary.

### Math Utilities

- `gcd(a: int, b: int) -> int`: Compute the Greatest Common Divisor (GCD) of two numbers.
- `lcm(a: int, b: int) -> int`: Compute the Least Common Multiple (LCM) of two numbers.

### File Utilities

- `read_json(file_path: str) -> dict`: Read a JSON file and return the parsed content as a dictionary.
- `write_json(data: dict, file_path: str)`: Write a dictionary to a JSON file.

### Convenience Functions

- `process_text(text: str) -> str`: A convenience function that combines truncation and capitalization on the input string.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contributing

We welcome contributions to **`utilz`**. If you encounter a bug or want to add a new feature, please feel free to open an issue or submit a pull request.

To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request