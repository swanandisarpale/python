

def oddnum(end):
    for num in range(0,end):
        if num & 1!=0: # or 1==1 for even no.
            yield num #returns one thing with multiple parameter

def main():
    
    for itm in oddnum(100):
        print(itm)

if __name__=="__main__":
    main()