from calendar import c
from sqlalchemy import false


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
            print(sum)
        if a > 2000001:
            print(sum)
            break

main()