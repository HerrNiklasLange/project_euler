# What is the sum of the digits of the number 2 ** 1000?

# Function to get sum of digits 
def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = 2 ** 1000
print(getSum(n))