def find_a_b_c():
    sum = 1000
    for a in range(1, int(sum/3)):
        for b in range(a, int(sum/2)):
            c = sum - a - b
            if a*a + b*b == c*c:
                print("a = ", a , ", b = ", b, ", c = ", c)
                print(a * b * c)
                
find_a_b_c()
 