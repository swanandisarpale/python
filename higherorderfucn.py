def cal(a):
     return a(10,11)

def add(a,b):
   return a+b

def main():
 ret=  cal(add)
 print(ret)

if __name__=="__main__":
     main()