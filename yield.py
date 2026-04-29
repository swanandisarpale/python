def table():

    for i in range(1,11):
        yield i*2

def main():

    for itm in table():
        print(itm)


if __name__ == "__main__":
    main()