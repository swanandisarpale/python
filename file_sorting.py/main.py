from pathlib import Path
import schedule
import os
import time

folder="C:\\Users\\HP\\Desktop" 

def file_sort():
       path=Path(folder)                          #will give you file names on desktop
       for file in path.iterdir():                #iterdir is a function returns values in yield form (iterating dictionary)=iterdir(used to itrate over files or folders)
                                               #print(file) print file names
           
           ext=str(file).split(".")
           file_name=str(file).split("\\")                                
                                                           #  print (ext[-1]) prints extensions  
           if len(ext)>1:
             if not os.path.exists(folder+"\\"+ext[-1]):
               os.makedirs(folder+"\\"+ext[-1])
               new_location=folder+"\\"+ext[-1]+"\\"+file_name[-1]
               
               print("old location of file :",str(file))
               print("new loctaion of file:", new_location)
             
             else:
                 new_location=folder+"\\"+ext[-1]+"\\"+file_name[-1]
                 print("old location of file :",str(file))
                 print("new loctaion of file:", new_location+"\n")

                 os.rename(str(file),new_location) #rename moves or changes file location
             
               

                                          

def main():
    schedule.every(1).minute.do(file_sort)
    
    while(True):
        schedule.run_pending() #scheduler has come before or not tells the run_pending fucn
        time.sleep(1)     #sleeps for 1 seconds

                
if __name__=="__main__":
  main()


  #we use pip for installing package in python pip installs packages
