def isPrime(n): #checks if the number is a prime number
    # Corner case
    if n <= 1:
        return False
  
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;
  
    return True
def main():
    prime_numbers = [-1] * 10003 #creates a list with 10004 values
    count = 0
    for index in range(1, 99999999):
        if isPrime(index): #calls function that checks prime number
            prime_numbers[count] = (index) #assignes new values to prime number
            count += 1
        if prime_numbers[10000] > 1: #if the 10001 is greater than 1 it stops the loops and prints the 1001 prime number
            print(prime_numbers[10000])
            break
main()