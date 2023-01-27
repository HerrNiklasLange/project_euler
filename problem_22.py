# opening the file in read mode
my_file = open("projectEuler.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
#for index in range(0, ):
data_into_list = data.replace('"', '').split(",")
  
# printing the data
#print(data_into_list)
my_file.close()

def bubbleSort(list):
    n = len(list)
    swapped = True
    while swapped == True and n > 0:
        swapped = False
        for i in range(0, n-1):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                swapped = True
        n -= 1
    #print(list)
    #print(len(list))
    return list
def character_counter(list):
    total = 0
    for index in range (0, len(list)):
        x = ','.join(list[index])
        splitUp = x.split(",")
        chr_counter = 0
        for i in range(0, len(splitUp)):
            print(splitUp[i])
            chr_counter +=   ord(splitUp[i])-64
        total += chr_counter * (index + 1)

    print(total)
list = bubbleSort(data_into_list)
x = ["AB", "BC"]
character_counter(list)


