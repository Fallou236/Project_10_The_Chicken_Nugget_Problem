# The Chicken Nugget Problem

## Overview

This project explores the **Chicken Nugget Problem**, a mathematical problem about determining which amounts can be formed using boxes of fixed sizes.

A shop sells chicken nuggets in boxes of **6, 9, and 20 nuggets**. The goal is to determine whether a given amount can be obtained by combining these boxes, identify amounts that cannot be made, find the largest impossible amount within a given range, and count the possible combinations.

The project also explores other box sizes to understand how the results change.

## Objectives

The main objectives are to:

- Determine whether a given amount can be made using specified box sizes.
- Find all amounts that cannot be made up to a given limit.
- Find the largest impossible amount within a given range.
- Count the different combinations that produce an exact amount.
- Explore even box sizes and understand why some amounts remain impossible.
- Test the mathematical formula for two coprime box sizes.

## Project Structure

```text
Project_10_The_Chicken_Nugget_Problem/
├── src/
│   ├── __init__.py
│   └── project.py
├── test_project.py
├── README.md
└── REFLECTION.md
```

- `src/project.py`: Contains the implementation of the functions.
- `test_project.py`: Contains tests for the functions and displays their results.
- `README.md`: Documents the project.
- `REFLECTION.md`: Contains reflections and observations about the problem.

## Requirements

- Python 3.10 or later.
- No external libraries are required; the project uses Python's standard library.

## Installation

Clone the repository:

```bash
git clone https://github.com/Fallou236/Project_10_The_Chicken_Nugget_Problem.git
```

Navigate to the project directory:

```bash
cd Project_10_The_Chicken_Nugget_Problem
```

## Implementation

### Task 1: Check Whether an Amount Can Be Made

The function `can_make(n, a, b, c)` determines whether the amount `n` can be obtained using boxes of sizes `a`, `b`, and `c`.

It returns:

- `True` if the amount can be made.
- `False` otherwise.

Example:

```python
can_make(20, 6, 9, 20)  # True
can_make(7, 6, 9, 20)   # False
can_make(44, 6, 9, 20)  # True
```

### Task 2: Find All Impossible Amounts

The function `cannot_be_made(a, b, c, limit=100)` returns a list of all amounts from `0` to `limit` that cannot be made using the given box sizes.

Example:

```python
cannot_be_made(6, 9, 20)
```

Expected result:

```python
[1, 2, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16,
 17, 19, 22, 23, 25, 28, 31, 34, 37, 43]
```

### Task 3: Find the Largest Impossible Amount

The function `largest_impossible(a, b, c, limit=100)` returns the largest amount that cannot be made within the specified range.

Example:

```python
largest_impossible(6, 9, 20)  # 43
```

For box sizes 6, 9, and 20, the largest impossible amount up to 100 is **43**.

### Task 4: Count the Number of Combinations

The function `count_ways(n, a, b, c)` counts the non-negative integer combinations of the three box sizes that produce exactly `n` nuggets.

Different orders of choosing the boxes are not counted as different combinations.

Examples:

```python
count_ways(20, 6, 9, 20)  # 1
count_ways(60, 6, 9, 20)  # 5
```

### Think and Explain: Even Box Sizes

Consider box sizes 4, 6, and 10:

```python
cannot_be_made(4, 6, 10)
```

Expected result:

```python
[1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
```

Since all three sizes are even, every combination produces an even amount. Therefore, **every odd amount is impossible**.

When checking amounts from 0 to 100, the impossible amounts are all the odd numbers in that range, and the largest is **99**.

However, there is **no largest impossible amount overall**, because odd numbers are infinite.

### Extra Task: Other Box Sizes

The project also examines box sizes 5, 8, and 12.

Example:

```python
cannot_be_made(5, 8, 12)
```

Expected result:

```python
[1, 2, 3, 4, 6, 7, 9, 11, 14, 19]
```

The largest impossible amount up to 100 is **19**.

#### Formula for Two Coprime Box Sizes

For two positive, coprime integers `a` and `b`, the largest amount that cannot be expressed as a non-negative integer combination of `a` and `b` is:

\[
ab-a-b
\]

The project tests this formula with the following pairs:

| Box sizes | Largest impossible amount |
|---|---:|
| 3 and 5 | 7 |
| 4 and 7 | 17 |
| 5 and 8 | 27 |

A third box size of 1000 is used to reuse the existing function for these tests. Since the amounts being checked are below 1000, this third box does not affect the listed largest impossible amounts.

## Running the Tests

From the root directory, execute:

```bash
python test_project.py
```

The test file checks the functions and prints their results, including:

- Whether each amount can be made.
- The list of impossible amounts.
- The largest impossible amount.
- The number of combinations for selected amounts.
- The results of the extra tests.

If all assertions pass, the test sections display successful statuses.

## Expected Results

For box sizes 6, 9, and 20:

| Operation | Expected result |
|---|---|
| `can_make(0, 6, 9, 20)` | `True` |
| `can_make(7, 6, 9, 20)` | `False` |
| `can_make(43, 6, 9, 20)` | `False` |
| `can_make(44, 6, 9, 20)` | `True` |
`cannot_be_made(6, 9, 20)` | `[1, 2, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 22, 23, 25, 28, 31, 34, 37, 43]` |
| `largest_impossible(6, 9, 20)` | `43` |
| `count_ways(20, 6, 9, 20)` | `1` |
| `count_ways(60, 6, 9, 20)` | `5` |

## Mathematical Observations

This project illustrates several mathematical ideas:

1. **Integer combinations:** Each amount is formed using non-negative integer multiples of the box sizes.
2. **Impossible amounts:** Some amounts cannot be represented by the available box sizes.
3. **Parity:** When every box size is even, odd amounts can never be made.
4. **Coprime integers:** When two box sizes are coprime, the largest impossible amount is given by \(ab-a-b\).
5. **Counting combinations:** A single amount may be formed using several different combinations of box sizes.

## Technologies

- Python
- Git and GitHub

## Contributors

This project was developed collaboratively as part of a programming assignment. Contributors can be listed here:

- Fallou Diouck
- Soro Koulatioloma Daouda
- Metcha Tremouafo Danielle Franchesquine
- Mouhamadou Kandé
- Tahir Hawa Mahamat

## License

This project was created for educational purposes.