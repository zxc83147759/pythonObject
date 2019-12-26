import method_old as old
import method_new as new
import time

print(old.test(50000000))
print(new.test(50000000))

start = time.time()
old.prime(50000)
print('Old:', '%.2f' % (time.time() - start), 'sec')

start = time.time()
old.prime(50000)
print('Cython1:', '%.2f' % (time.time() - start), 'sec')

start = time.time()
old.prime(50000)
print('Cython2:', '%.2f' % (time.time() - start), 'sec')
