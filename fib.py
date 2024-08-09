from itertools import accumulate, repeat, islice

fib_it = (
    lambda init: map(
        lambda x: x[0], accumulate(repeat(init), lambda s, _: (s[1], s[1] + s[0]))
    )
)((1, 1))

if __name__ == "__main__":
    print(list(islice(fib_it, 10)))
