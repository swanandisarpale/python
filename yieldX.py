def char_count(string:str):

    A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for ch in string:
        if ch.upper() in A:
            yield "index of "+ch +" is "+str(A.index(ch.upper())+1)

def main():
    print("Enter a string")
    text = input()

    for i in char_count(text):
        print(i)

if __name__ == "__main__":
    main()