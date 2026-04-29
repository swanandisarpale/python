#in dict index no.are not present
def main():
 student= {"name":"sanu","age":19,"roll":18} #dictionary
 number={1,2,3,4,5,6,7,8,9,10} #set-no duplicate value allowed
 
 for elements in student : 
    print (elements)        #print keys
    print(student[elements])# print values
 
 for set in number:
    print(set)

    
 print(number)
if __name__=="__main__":
    main()
