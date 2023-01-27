n = 1
for index in range(2, 101):
    n *= index

#print(n)

def getSum(n):
    
    sum = 0
    for digit in str(n): 
        #print(int(digit))
        sum += int(digit)      
    return sum
   
print(getSum(n))