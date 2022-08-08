#this will find the sum of letters from a range e.g 1-1000
# dashes and spaces won't be count

def one_to_nine(n1):
    count = 0
    if n1 == 1 or n1 == 2 or n1 == 6:
        count += 3
    elif n1 == 4 or n1 == 5 or n1 == 9:
        count += 4
    elif n1 == 7 or n1 == 8 or n1 ==  3:
        count += 5
    elif n1 == 0:
        count += 0
    return count

def ten_to_nineteen(n1):
    count = 0
    if n1 == 1:
        count += 3
    elif n1 == 1 or n1 == 2:
        count += 6
    elif n1 == 6 or n1 == 5:
        count += 7
    elif n1 == 7:
        count += 9
    else:
        count += 8
    return count

def tweenty_ninety(n2):
    count = 0
    if n2 == 4 or n2 == 5 or n2 == 6:
        count += 5
    elif n2 == 7:
        count += 7
    elif n2 == 1:
        count += 0
    else:
        count += 6
    return count

def main():
    word_count = 0
    for n3 in range(0,10):
        for n2 in range(0,10):
            for n1 in range(0,10):
                if n2 == 1:
                    word_count += int(ten_to_nineteen(n1))
                else:
                    word_count += int(one_to_nine(n1))
                    if n2 != 0:
                        print(n3,n2,n1)
                        word_count += int(tweenty_ninety(n2))
                    
                if n3 != 0:
                    word_count += int(one_to_nine(n3)) + 7 + 3
                
    word_count += 3 + 8     
    print(word_count)
#print(int(one_to_nine(9)) + 7, int(tweenty_ninety(9)) + 3, int(one_to_nine(9)))

main()