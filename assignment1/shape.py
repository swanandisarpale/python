def main():
    n = 4
    width = 2*n - 1
    center = n

    for i in range(1, n+1):#4rows
        for j in range(1, width+1): #width =8
            if center-(i-1) <= j <= center+(i-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    print("next pattern")
    for i in range(1,8):
       for j in range(1,8):
         if i==j :
          print("*",end="")
         else:
            print(" ",end="")
       print("") 

if __name__ == "__main__":
    main()