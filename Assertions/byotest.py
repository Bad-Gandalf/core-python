def even_number_of_evens(numbers):
    return 0

def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
  
test_are_equal(even_number_of_evens(7), 0)  # failed test test_are_equal(even_number_of_evens(7), 1)
test_not_equal(even_number_of_evens(6), 3)  # failed test test_not_equal(even_number_of_evens(6), 0)
test_is_in([1, 2, 3, 4, 5], 3)   # failed test test_is_in([1, 2, 3, 4, 5], 9)
