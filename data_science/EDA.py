#EDA= explolatery data analysis
#step1 -load data set
#step 2- show first five entries of data
#step 3-show dimensions of data set
#step 4-show the statistics of dataset
#step 5-split data into dependent and independant

import pandas as pd  # we imported pandas but  we  will use it as pd or anything inofront of as
def main():
    line="-"*64                    # will print - 64 time just  for formatting
    df= pd.read_csv("./salary.csv") #step1 df is variable  as data frame 
    print(line)
    print("first five entries")
    print(line)

    print(df.head())      #step2 head is function is pandas which shows  first 5 entries
    #print(df.size)      # size is variable shows no. of entries
    print(df.info())    # step3 info() is a function which gives dimensions

    print (line)
    print("data set  statistics")
    print(line)
    print(df.describe()) # step4  describe is a function shows statistics

    features=[df["Experience"],
              df["Education_Level"],
              df["Age"]]
    
    answer=[df["Salary"]]
    print(answer)

if __name__=="__main__":
    main()

