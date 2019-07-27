def fizzbuzz(n):
    """Fizzin and Buzzin"""
    for i in range(1, n+1):
        val = ''
        if i % 3 == 0:
            val += 'Fizz'
        if i % 5 == 0:
            val += 'Buzz'
        yield val if val else i


if __name__ == '__main__':
    [print(i) for i in fizzbuzz(100)]
