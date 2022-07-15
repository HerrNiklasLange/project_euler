def sum_of_first_100_squared(): # calculates the sum of all real numbers between 1 and 100 and adds them up and then squares them
    total_sum = 0
    for index in range(1,101):
        total_sum += index 
    total_sum = total_sum ** 2 
    return total_sum
def squared_first_100_sum(): # squares all the real numbers from 1 to 100 and then adds them up 
    total_squared = 0
    for index in range(1,101):
        total_squared += index ** 2 
    print(total_squared)
    return total_squared
def main(): #the sum from 1 to 100 that was squared is subtracted by the real numbers from 1 to 100 that where squared
    square_of_the_sum = sum_of_first_100_squared()
    sum_of_the_squares = squared_first_100_sum()
    print(square_of_the_sum - sum_of_the_squares)
main()