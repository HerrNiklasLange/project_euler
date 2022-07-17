#Find the sum of all the primes below two million.
from sympy import isprime
def isPrime(n):
  
    # Corner case
    if n <= 1:
        return False
  
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;
  
    return True

def main():
    sum = 0
    for index in range(1,2000001):
        if isprime(index):
            sum += index
    print(sum)
main()