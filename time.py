import time
from functions import _mult

a = open('1.txt')
c = a.readline().split(' ')
f = []
for i in c:
    f.append(int(i))

start = time.perf_counter()
_mult(f)
end = time.perf_counter()
print(end - start)

