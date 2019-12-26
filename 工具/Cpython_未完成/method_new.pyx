cpdef double test(int x):
    cdef double y = 0
    cdef double i
    for i in range(x):
        y = y + i
    return y

# 與method_old.py一模一樣
def prime1(givenNumber):
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        isPrime = 1
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = 0
        if isPrime:
            primes.append(possiblePrime)
    return primes

# 有加入宣告
cpdef list prime2(int givenNumber):
    cdef list primes = []
    cdef unsigned int possiblePrime
    cdef unsigned int num
    cdef int isPrime
    for possiblePrime in range(2, givenNumber + 1):
        isPrime = 1
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = 0
        if isPrime:
            primes.append(possiblePrime)
    return primes
