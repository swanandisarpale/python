import multiprocessing
def add(a,b,q):
    result=a+b
    q.put(result) #putting a+b value in queue by using put function
    
def pow(a):
    num=a.get()  # it takes value fron q using get funcn
    print(num**2)
def main():
   q=multiprocessing.Queue()
   p1=multiprocessing.Process(target=add,args=(10,11,q))
   p2=multiprocessing.Process(target=pow,args=(q,))
   p2.start()
   p1.start()
   
   
if __name__=="__main__":
    main()

