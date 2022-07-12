from sympy import factor, isprime

def isPrime(n):
  
    # Corner case
    if n <= 1:
        return False
  
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;
  
    return True
def find_factor(number):
    x = 0
    num = 0
    tracker = 0 
    count = 0
    factors = []
    end = False

    for index in range(number):
        x = 1 + x
        index += 1
        if (number % x) == 0:
            num = int(number/x)
            factors.append(num)
            if isprime(factors[tracker]):
                print("prime number is ", factors[tracker])
                end = True
                break
            print(factors[tracker])
            tracker += 1   
            
    #while end == False:
     #   if isprime(factors[count]):
      #      print("prime number is ", factors[count])
       #     end = True
        #count += 1

find_factor(600851475143)
