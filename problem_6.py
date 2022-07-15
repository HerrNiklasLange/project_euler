def sum_of_first_100_squared():
    total_sum = 0
    for index in range(1,101):
        total_sum += index 
    total_sum = total_sum ** 2 
    return total_sum
def squared_first_100_sum():
    total_squared = 0
    for index in range(1,101):
        total_squared += index ** 2 
    print(total_squared)
    return total_squared
def main():
    square_of_the_sum = sum_of_first_100_squared()
    sum_of_the_squares = squared_first_100_sum()
    print(square_of_the_sum - sum_of_the_squares)
main()