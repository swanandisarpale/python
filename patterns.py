def main():
    letter= input("Enter a letter betwwn a-c: ")

    for i in range(5):
        for j in range(5):
            if letter == "A":
                if j == 0 or j == 4 or i == 2 or (i == 0 and j > 0 and j < 4):
                    print("*", end="")
                else:
                    print(" ", end="")

            elif letter == "B":
                if j == 0 or i == 0 or i == 2 or i == 4 or j == 4:
                    print("*", end="")
                else:
                    print(" ", end="")

            elif letter == "C":
                if i == 0 or i == 4 or j == 0:
                    print("*", end="")
                else:
                    print(" ", end="")

            else:
                print("Pattern not available")
                return
        print()

if __name__ == "__main__":
    main()