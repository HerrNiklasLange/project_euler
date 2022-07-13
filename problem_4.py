def ispalindrome(n, first_num, second_num):
    num = n
    # Assigning variables
    reversed_num = 0
    #Reversing the number
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    reversed_num = int(reversed_num)
    #cheking if number is a palindrome
    if n == reversed_num:
        return True;
    else:
        return False


def main():
    largest_num = 0
    for index1 in range(0, 899):
        first_num = 999 - index1
        print(first_num)
        for index2 in range(0, 899):
            second_num = 999 - index2
            print(index2)
            multplication = first_num * second_num
            if ispalindrome(multplication, first_num, second_num):
                if largest_num < multplication:
                    #saves the largest palindrom
                    largest_num = multplication
    print("The greates 3 digit palindrom is:  ", largest_num)

main()