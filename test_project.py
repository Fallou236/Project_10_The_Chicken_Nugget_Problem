from src.project import (
    can_make,
    cannot_be_made,
    largest_impossible,
    count_ways,
)


def test_can_make():
    print("\n--- TEST can_make() ---")

    cases = [
        (0, True),
        (7, False),
        (43, False),
        (44, True),
    ]

    for n, expected in cases:
        result = can_make(n, 6, 9, 20)
        print(f"can_make({n}, 6, 9, 20) = {result}")
        assert result == expected

    print("PASS: can_make()")

# Test 2 

"""def test_cannot_be_made():
    print("\n--- TEST cannot_be_made() ---")

    result = cannot_be_made(6, 9, 20)

    print("Liste des montants impossibles :")
    print(result)

    assert isinstance(result, list)
    assert result == [
        1, 2, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16,
        17, 19, 22, 23, 25, 28, 31, 34, 37, 43
    ]

    print("PASS: cannot_be_made()")"""


#Test 3
"""def test_largest_impossible():
    print("\n--- TEST largest_impossible() ---")

    result = largest_impossible(6, 9, 20)
    print(f"Plus grand montant impossible = {result}")

    assert result == 43

    print("PASS: largest_impossible()")"""


"""def test_count_ways():
    print("\n--- TEST count_ways() ---")

    cases = [
        (20, 1),
        (60, 5),
    ]

    for n, expected in cases:
        result = count_ways(n, 6, 9, 20)
        print(f"count_ways({n}, 6, 9, 20) = {result}")
        assert result == expected

    print("PASS: count_ways()")"""


def test_invalid_inputs():
    print("\n--- TEST des entrées invalides ---")

    try:
        can_make(10, 0, 9, 20)
    except ValueError:
        print("Taille nulle : ValueError correctement levée.")
    else:
        raise AssertionError("ValueError attendue")


# Think and explain: Test even box sizes (4, 6, 10).
"""def test_even_box_sizes():
    print("\n--- TEST EVEN BOX SIZES (4, 6, 10) ---")

    result = cannot_be_made(4, 6, 10)

    print("Amounts that cannot be made:")
    print(result)

    print("Largest impossible amount up to 100:")
    print(max(result))

    assert all(n % 2 != 0 for n in result)
    assert max(result) == 99

    print("PASS: Even box sizes test")"""

if __name__ == "__main__":
    print("===== CHICKEN NUGGET PROBLEM =====")

    test_can_make()
    #test_cannot_be_made()
    #test_largest_impossible()
    #test_count_ways()
    test_invalid_inputs()
    #test_even_box_sizes()

    print("\n===== TOUS LES TESTS SONT PASSÉS =====")
