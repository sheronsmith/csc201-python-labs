# CSC 201 Python Labs

Python programs I wrote for CSC 201 (Intro to Computer Programming) at Converse University, Fall 2026.

## Programs

| File | What it does | Skills shown |
|---|---|---|
| `temperature_graph.py` | Draws a bar graph of a week of real daily high temperatures in Spartanburg, SC | Graphics, real-world data from the Open-Meteo weather API |
| `lab08_this_old_man.py` | Prints all ten verses of "This Old Man" using one reusable function | Functions, parameters, avoiding repeated code |
| `lab11_valid_date.py` | Checks whether a day, month, and year form a real calendar date | Decisions, edge cases, Gregorian leap-year rules |
| `lab12_class_standing.py` | Finds a student's class standing from their credit hours and handles bad input without crashing | Input validation, exception handling (`try`/`except`) |
| `lab13_gcd.py` | Finds the greatest common divisor of two numbers, including negatives and zero | Euclid's algorithm, `while` loops |

All programs use type hints so they can be checked with [mypy](https://mypy-lang.org/).

## How to run

You need Python 3.9 or newer.

```
python lab13_gcd.py
```

`temperature_graph.py` also needs John Zelle's `graphics.py` in the same folder. It is available from the [Python Programming textbook site](https://mcsp.wartburg.edu/zelle/python/).
