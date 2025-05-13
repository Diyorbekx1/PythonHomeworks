import os
import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero")

# string_utils.py
# -------------------

def reverse_string(s):
    return s[::-1]


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# geometry package
# geometry/__init__.py

# geometry/circle.py

import math

def calculate_area(radius):
    return math.pi * (radius ** 2)


def calculate_circumference(radius):
    return 2 * math.pi * radius

# file_operations package
# file_operations/__init__.py

# file_operations/file_reader.py

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")

# file_operations/file_writer.py

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file: {e}")
