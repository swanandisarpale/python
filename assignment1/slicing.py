def print_series():
    n = int(input("Enter value of n: "))
    lists=[]
    ans=[]
    for a in range(1,n+1):
        lists.append(a)
    for i in range(0,n+1):
       if i + i + 1 <= len(lists): 
        # starts from i goes till i elements stops if there are not enough elements 
        print(*lists[i:i+i+1:], sep="",end="") # sep="" removes space between list elements

def main():
    print_series()

if __name__ == "__main__":
    main()