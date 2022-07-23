
def devisors(n):
    number_of_devisors = 1
    for index in range(1, int(n/2 +1)):
        if n % index == 0:
            number_of_devisors += 1
        
    return number_of_devisors
def main():
    for index in range(1,99999999):
        triangle = index
        for n in range(0, index):
            triangle += n
        print(".")
        if devisors(triangle) > 500:
            print(triangle)
            break
    print("Done")
import math
from time import time
t = time()
def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors +=2
        else:
            continue
    return number_of_factors

x=1
for y in range(2,1000000):
    x += y
    if divisors(x) >= 500:
        print(x)
        break
tt = time()-t
print(tt)