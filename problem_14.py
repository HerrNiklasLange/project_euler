from sympy import N


def odd(n):
    n = 3*n + 1
    return n
def even(n):
    n = n/2
    return n

def main():
    longest_chain = 0
    longest_chain_starting = 0
    for index in range(2,1000001):
        n = index
        chain = 0
        print(n)
        while n != 1:
            if n % 2 ==0:
                n = even(n)
                chain += 1
            else:
                n = odd(n)
                chain += 1
        if longest_chain < chain:
            longest_chain = chain
            longest_chain_starting = index
    print("the chain starts at ", longest_chain_starting, " and ends at ", chain)
main()