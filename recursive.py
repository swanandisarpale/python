num = 0

def counter():
    global num
    num = num+1
    print(num)
    return counter()

def main():
    counter()

if __name__ == "__main__":
    main()