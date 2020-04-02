n = int(input("How many triangular numbers do you want to print? "))

for _ in range(1,n+1):
    tri_n = (_ * (_ + 1)) / 2
    print(_, "\t", int(tri_n))
