def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with zeros if they are smaller than 2
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Add the first elements of both tuples
    sum_first = tuple_a[0] + tuple_b[0]

    # Add the second elements of both tuples
    sum_second = tuple_a[1] + tuple_b[1]

    return (sum_first, sum_second)

