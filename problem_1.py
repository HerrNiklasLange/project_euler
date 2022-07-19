# This finds the sum of all the multiples of 3 or 5 below 1000
from sqlalchemy import false

def multiple_of_3_5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True;
    return False
def main():
    sum = 0
    for index in range(1,1000):
        if multiple_of_3_5(index):
            print(index)
            sum += index
    print(sum)
main()