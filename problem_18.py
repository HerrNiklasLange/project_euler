# 0
def table():
    piramid = [(95,64),(17,47,82),(18,35,87,10),(20,4,82,47,65),(19,1,23,75,3,34),(88,2,77,73,7,63,67),(99,65,4,28,6,16,70,92)]
        #41 41 26 56 83 40 80 70 33
        #41 48 72 33 47 32 37 16 94 29
        #53 71 44 65 25 43 91 52 97 51 14
        #70 11 33 28 77 73 17 78 39 68 17 57
        #91 71 52 38 17 14 91 43 58 50 27 29 48
        #63 66 04 68 89 53 67 30 73 16 69 87 40 31
        #04 62 98 27 23 09 70 98 73 93 38 53 60 04 23)]
    return piramid
def main():
    piramid = table()
    x = piramid[1]
    position_sum = 0
    sum = 0 
    for index in range(0,7):
        x = piramid[index]
        if x[index] == x[0]:
            if x[0] > x[1]:
                position_sum += .5
                sum += x[0]
            else:
                position_sum -= .5
                sum += x[1]
        elif len(x) % 2 != 0:
            if x[position_sum + .5] > x[position_sum - .5]:
                x
            
#main()
