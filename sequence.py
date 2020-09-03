n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1 = 0
n2 = 1
n3 = 0

for i in range(n):
    nsum = n1 + n2 + n3
    n1 = n2
    n2 = n3
    n3 = nsum
    print(nsum)
