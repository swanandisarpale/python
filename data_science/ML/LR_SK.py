#linear regression scikit learn(LR_SK)

import pandas as pd
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error     # it gives mean square of output error

def main():
 #step1-load data  set
 df=pd.read_csv("multifeature.csv") # df=data frame

 #step2-split into dependent/y/ans and independent/x/feature/question

 x=df[["x1","x2"]] #when you want to put two col then use arr inside arr its 2d data
 y=df["ans"] # 1[] cause ans column is 1

#step3-split into traning and testing data set

 x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4) #0.4 is 40% for testing
                                                         # train_test_split split and shuffle the data in random way
 print("x for training:",x_train)
 print("x for test:",x_test)
 print("y for training:",y_train)
 print("y for testing:",x_test)

#step4- train your model

 model=LinearRegression()
 model.fit(x_train,y_train)   # fit is used for starting training with these variable

#comparing actual data and predicted
 y_predi=model.predict(x_test)
 print("actual ans :",y_test)
 print("predicted ans",y_predi)

#error
 MSE=mean_squared_error(y_test,y_predi)
 print(" the error is:",MSE)

if __name__=="__main__":
    main()