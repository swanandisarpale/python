import pandas as pd
import  matplotlib.pyplot as plt

def main():
  df=pd.read_csv("hello.csv")
  line="-"*64
  
  print(line)
  print("first 4 entries")
  print(line)
  print(df.head(4))   #shows first 4 elements

  print(line)
  print("dimensions")
  print(line)
  print(df.info())   #shows dimension and its data  type
 
  print(line)
  print("stastics")
  print(line)
  print(df.describe(include="all",percentiles=[0.25,0.5,0.75])) #shows stastics
  
  dist_group=df.groupby("State Name") #separet the distrit on the basis of states

  states=[]
  state_count=[]

  for i in dist_group:
    # print(i[0]) #will print  state name
    # print(len(i[1])) #it will print sencond value in touple one below one and no. of elements
     
     states.append(i[0])
     state_count.append(len(i[1]))
    
#(n/total numbers)*100
#(i/total data)*100
#(i/779)*100
  state_count_percentage=[]  

  for num in state_count:
     k=(num/779)*100
     state_count_percentage.append(k)

  #print(state_count_percentage)

#drawing pichart
  plt.figure(figsize=(10,10)) #figure is created of size 10*10
  plt.pie(state_count_percentage,labels=states,autopct="%0.1f%%")#creates circular diagram pichart
  plt.show()
    #autopct is a function auto percentage text 
    # "% 0.1f %%" it will show one no. after decimal ex=3.98=4.0

    #drawing bar chart
  plt.figure(figsize=(15,10))
  plt.bar(states,state_count_percentage)
  plt.xticks(rotation=90) #it prints word vertically at 90 degree
  plt.show()
  #draw a bar graph x axis =state name, y axis avg % of that state

if  __name__=="__main__":
    main()