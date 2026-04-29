import pandas
def main():
    data=pandas.read_csv("hw.csv")
    print(data)

    print(data["HEIGHT"])
    p=data["HEIGHT"].mean() #mean is function for giving mean value
    
    data["HEIGHT"] = data["HEIGHT"].fillna(p)   

    q=data["WEIGHT"].mean() 
    
    data["WEIGHT"]=data["WEIGHT"].fillna(q) 
    print(data)

if __name__=="__main__":
  main()