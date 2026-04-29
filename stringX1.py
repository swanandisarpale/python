# *
# **
# ***
# ****

def main():
    print("Enter a number ")
    num = int(input())

    for line in range(1,num+1):
        for star in range(0,line):
            print("*",end="")

        print()

if __name__ == "__main__":
    main()
