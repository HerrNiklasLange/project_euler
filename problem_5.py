from sqlalchemy import false


def check(n):
    if n % 2 == 0 and n % 3 == 0 and n % 4 == 0 and n % 5 == 0 and n % 6 == 0 and n % 7 == 0 and n % 8 == 0 and n % 9 == 0 and n % 10 == 0 and n % 11 == 0 and n % 12 == 0 and n % 13 == 0 and n % 14 == 0 and n % 15 == 0 and n % 16 == 0 and n % 17 == 0 and n % 18 == 0 and n % 19 == 0 and n % 20 == 0: 
        print("true")
        return True;
    else:
        return False
    
def main():
    for index in range(20,999999999):
        if check(index):
            print("The smallest number that is equally divisible from 1 to 20 is: ",index)
            break    

main()