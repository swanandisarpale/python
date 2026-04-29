import pandas as pd
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
def main():
  line="*"*70
  df=pd.read_csv("salary_pred.csv")
  print(line)
  print("first five data")
  print(df.head())
  print(line)

  print(line)
  print("dimensions of data set")
  print(df.info())
  print(line)

  print(line)
  print("statstics of data set")
  print(df.describe())
  print(line)

#map({}) will replace the values in csv with your value or data
  df["EducationLevel"]=df["EducationLevel"].map({
     "Bachelors":0,
     "Masters":1,
     "PhD":2
  })
  print(df.head())

  x=df[["YearsExperience","EducationLevel"]]
  y=df["Salary"]

  x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42) 
  #train_test_split shuffle data
  #randon_state shuffle data in 42 random state

  model=LinearRegression()
  model.fit(x_train,y_train) #fit tells what to load

  Y_pred=model.predict(x_test)

  for i,j in zip(y_test,Y_pred):    #zip is like for each loop runs loop in one line
     print(f"actual value:{i} predicted value:{j}")

  error=mean_absolute_error(y_test,Y_pred)
  print(error)
if __name__=="__main__":
    main()