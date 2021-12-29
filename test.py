def test(false=True):
    for i in range(1, 11):
        if i % 2 == 0 and false:
            # "Yes, it' still a generator.
            # The return is (almost) equivalent to raising StopIteration."
            pass
            yield i
        elif i == 9 and false is False:
            return i+1


print(*test(False))
