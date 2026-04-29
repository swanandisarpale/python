#formulae
#line of regression: y= mx+c
#m=sum((x-mean(x)))(y-mean(y)) / (x-x_bar)**2
#c=mean(y)-m*mean(x)

import pandas as pd
import numpy as np  

def main():
    
    line ="-"*64
    df=pd.read_csv("./bike_price.csv")
    print("below are first five entries of data")
    print(df.head()) #it will print fist five data
    print(line)

    print("below are dimensions of data")
    print(df.info())
    print(line)

    print("below are statistics of data")
    print(df.describe())
    print(line)

#-----------------------------------------------------------------------------
#               LINEAR REGRESSION (SELF-DEFINED)
#------------------------------------------------------------------------------
    
    #separate features and snswers from dataset
    feature = df["Bike_Power_CC"]
    answer = df["Bike_Price_INR"]
    
    #split into training and testing of data set
    x_train=[]
    y_train=[]

    for data in range(0,6):
        x_train.append(feature[data])
        y_train.append(answer[data])       #for x,y in zip(feature,answer) 
                                           #using zip you can run multiple loop

    # data for testing
    x_test=[]
    y_test=[]
    for data in range(6,10):
        y_test.append(answer[data])
        x_test.append(feature[data])

    print(line)
    print("these are features of training:",x_train)
    print("these are y foe training",y_train)    
    print(line)
    
    print(line)
    print("these are features of testing:",x_test)
    print("these are y foe testing",y_test)    
    print(line)

    x_=np.mean(x_train)
    print("mean of training feature(x)",x_)

    y_=np.mean(y_train)
    print("mean of training y:",y_)
    print(line)
     
     #x-mean(x) and y-mean(y)
    x_sub_xbar=[]
    y_sub_ybar=[]
    for data in range (0,6):
        x_sub_xbar.append(x_train[data]-x_)
        y_sub_ybar.append(y_train[data]-y_)
    print(line)
    print("x-mean(x):",x_sub_xbar)
    print("y-mean(y)",y_sub_ybar)
    print(line)

# (x-mean(x)*(y-mean(y))
    x_sub_xbar_y_sub_ybar=[]

    for data in range(0,6):
        x_sub_xbar_y_sub_ybar.append(x_sub_xbar[data] * y_sub_ybar[data])
    print(line)
    print("(x-mean(x)*(y-mean(y)):",x_sub_xbar_y_sub_ybar) #xbar or y bar is mean of x and y
    print(line)

 #(x-mean(x))**2
    x_sub_xbar2=[]
    for data in range(0,6):
        x_sub_xbar2.append(x_sub_xbar[data]**2)

    print(line)
    print("(x-mean(x))^2:",x_sub_xbar2) 
    print(line)

    #summation of (x-xbar)*(y-ybar)
    sum_x_sub_xbar_y_sub_ybar=0
    sum_x_sub_xbar2=0
    for data in range (0,6):
        sum_x_sub_xbar2 = x_sub_xbar + x_sub_xbar2[data]
        sum_x_sub_xbar_y_sub_ybar += x_sub_xbar_y_sub_ybar[data]
    print(line)

# calculating mean (m)
    m=sum_x_sub_xbar_y_sub_ybar / sum_x_sub_xbar2

    print("value of m",m)
    print(line)


# calculating c
    c=y_-(m*x_)
    print("value of c",c)
    print(line)
    
#testing
    err=0
    for data in range(0,4):
      y_hat= (m*(x_test[data]))+c
      err=y_test[data]-y_hat
      err+=err

    error=err/4
    print(line)
    print("error is ",error)
    print(line)                                                                                                                                                                                         

if __name__=="__main__":
    main()
