
def parent(name):
    def hello():
       return "hello "+name
    
    def gm():
        return "good morning "+name
    
    def gn():
        return "good night "+name
    
    return gm,gn,hello              # if you use ,,, then it returns in touple format

def main():
    a,b,c=parent("sanu")                               #or in touple print(parent("sanu")) will give in one line
    print(a())
    print(b())
    print(c())
if __name__=="__main__":
    main()