from itertools import accumulate, islice, repeat


def first(it):
    return next(iter(it))


def recur(seed=(1, 1)):
    "Generate Fibonacci numbers or generalizations thereof"
    return map(first, accumulate(repeat(seed), lambda s, _: (s[1], sum(s))))


if __name__ == "__main__":
    fib1, fib2 = recur(), recur()
    assert list(islice(fib1, 8)) == [1, 1, 2, 3, 5, 8, 13, 21]
    assert list(islice(fib1, 8)) == [34, 55, 89, 144, 233, 377, 610, 987]
    assert list(islice(fib2, 15)) == [
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
    ]
    # Successive Lucas numbers, like Fibonacci, have a ratio that
    # converges to the golden ratio, phi (φ ≈ 1.618).
    lucas = recur((2, 1))
    assert list(islice(lucas, 8)) == [2, 1, 3, 4, 7, 11, 18, 29]
