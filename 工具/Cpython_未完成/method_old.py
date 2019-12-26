def test(x):
    y = 0
    for i in range(x):
        y += i
    return y


def prime(givenNumber):
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        isPrime = 1
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = 0
        if isPrime:
            prime.append(possiblePrime)
    return primes
