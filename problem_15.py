# not solved
def create_grid(n):
    grid = []
    for y in range(0,n + 1):
        y =  y 
        for x in range(0, n +1):
            x = x * 10 + y
            grid.append(x)
    return grid


def main(n):
    grid = create_grid(n)
    print(grid)
    x = 10
    y = 1
    path = 0
    # the goal is to find all the ways to grid 22
    # we can move + 10 (x) or + 1 (y)
    for row1 in range(0, n +1):
        holder = 0
        holder += row1 * x
        holder += y
        print(holder)
        if not holder > 22:
            for row2 in range(0, n +1):
                holder += row2 * x
                holder += y
                print(holder)
                if not holder > 22:
                    for row3 in range(0, n +1):
                        holder += row3 * x
                        holder += y
                        print(holder)
                        if holder == 22:
                            path += 1
    print(path)
main(2)