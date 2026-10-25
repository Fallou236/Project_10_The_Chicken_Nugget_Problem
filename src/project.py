# Task 1: Check if an amount can be made using the given box sizes.
import math

def can_make(n: int, a: int, b: int, c: int) -> bool:
    """Check whether n can be made using boxes of sizes a, b and c."""
    if n < 0:
        return False

    if min(a, b, c) <= 0:
        raise ValueError("Box sizes must be positive integers.")

    for i in range(n // a + 1):
        for j in range(n // b + 1):
            for k in range(n // c + 1):
                if i * a + j * b + k * c == n:
                    return True

    return False

# Task 2: Return all amounts that cannot be made up to the given limit.
def cannot_be_made(a: int, b: int, c: int, limit: int = 100) -> list[int]:
    """Return all amounts that cannot be made up to limit."""
    if limit < 0:
        raise ValueError("Limit must be non-negative.")

    impossible = []

    for n in range(limit + 1):
        if not can_make(n, a, b, c):
            impossible.append(n)

    return impossible

# Task 3: Find the largest impossible amount up to the given limit.
def largest_impossible(
    a: int, b: int, c: int, limit: int = 100
) -> int | None:
    """Return the largest impossible amount up to limit."""
    impossible = cannot_be_made(a, b, c, limit)

    if len(impossible) == 0:
        return None

    return max(impossible)

# Task 4: Count the combinations that make exactly the given amount.
def count_ways(n: int, a: int, b: int, c: int) -> int:
    """Count the combinations that make exactly n."""
    if n < 0:
        return 0

    if min(a, b, c) <= 0:
        raise ValueError("Box sizes must be positive integers.")

    count = 0

    for i in range(n // a + 1):
        for j in range(n // b + 1):
            for k in range(n // c + 1):
                if i * a + j * b + k * c == n:
                    count += 1

    return count



# Task EXTRA: Check the largest impossible amount for coprime box sizes.
def check_largest(a: int, b: int, c: int = 1000) -> bool:

    """Check the formula a * b - a - b for coprime a and b."""
    if math.gcd(a, b) != 1:
        raise ValueError("The box sizes a and b must be coprime.")

    return max(cannot_be_made(a, b, c)) == a * b - a - b