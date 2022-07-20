from calendar import c
from sqlalchemy import false

#work in progress
def even_numbers(n):
    if n % 2 == 0:
        return True;
    return False
def main():
    over_2million = False
    sum = 0
    a = 1
    b = 1
    c = 1
    while over_2million == False:
        a = b + c
        d = b
        b = a
        c = d
        
        if even_numbers(a):
            sum += a
            print(a, ", ", sum)
        print(a)
        print(c)
        if a > 4000000:
            print(sum)
            break

main()