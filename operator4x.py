def main():
    print("enter first no.")
    no1=input()
    no1=int(no1)

    print("enter second number")
    no2=input()
    no2=int(no2)
    
    print("what do you want addition,sub,mul,div,remainder")
    
    operator=input()
    if operator=="addition":
        print("addition is",no1+no2)

    elif operator=="sub":
        print(no1-no2)

    elif operator=="mul":
        print(no1*no2)
     
    elif operator=="div":
        print(no1/no2)

    

if __name__ == '__main__':
    main()