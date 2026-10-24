# Task 1: Check if an amount can be made using the given box sizes.

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
    pass


# Task 3: Find the largest impossible amount up to the given limit.
def largest_impossible(
    a: int, b: int, c: int, limit: int = 100
) -> int | None:
    pass

# Task 4: Count the combinations that make exactly the given amount.
def count_ways(n: int, a: int, b: int, c: int) -> int:
    pass