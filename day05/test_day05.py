from day05 import find_median_of_unsorted_update


def test_find_median_of_unsorted_update():
    # Use an example of "normal" order except 3 and 4 have traded places.
    must_not_sees = {1: {}, 2: {1}, 3: {1, 2, 4}, 4: {1, 2}, 5: {1, 2, 3, 4}}
    update = [5, 4, 2, 3, 1]

    assert find_median_of_unsorted_update(must_not_sees, update) == 4
