# hello ji kaise ho -> olleh ij esaiak oh
def rev_sen(sentence:str):

    sentence = sentence.split(" ")
    rev_str = ""

    for i in sentence:
        rev_str += i[-1::-1]+" "

    return rev_str


def main():
    print("enter a sentence")
    k = input()
    print(rev_sen(k))
    
if __name__ == "__main__":
    main()