from itertools import accumulate, islice, repeat, tee

__fib = (
    lambda init: map(
        lambda x: x[0], accumulate(repeat(init), lambda s, _: (s[1], sum(s)))
    )
)((1, 1))


def make_fib():
    global __fib
    __fib, fib = tee(__fib)
    return fib


if __name__ == "__main__":
    print(list(islice(make_fib(), 8)))
    print(list(islice(make_fib(), 15)))
