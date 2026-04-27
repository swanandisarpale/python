def main(): 

    question_set_1 = {"Who is National Animal ? ":["Kutra","Manjar","Wagh","Hatti",2],
                    "Which is National Anthem ? ":["Sukh karta","Hanuman Chalisa","Samay samzaega","Jana gan man",3],
                    "Fingers in one hand ? ":["5","8","7","4",0],
                    "National Flower ? ":["Rose","Lotus","Hibiscus","Iris",1],
                    "Native Language of UP ? ":["Marathi","Sanskrit","Urdu","Braj",3]}

    question_set_2 = {"Who is National crush ? ":["me","you","rahmika","virat",2],
                    "Which is National tree ? ":["pipal","mango","neem","coconut",3],
                    "Fingers in one lag? ":["5","8","7","4",0],
                    "National hero ? ":["vijay","vickey","ranverr","ritik",1],
                    "Native Language of marathwada? ":["Marathi","Sanskrit","Urdu","Braj",0]}
    
    question_set_3 = {"Who is our pm  ? ":["rahul ji","mamta ji","modi ji","thakre ji",2],
                    "who are you? ":["human","robaot","dev","student",3],
                    "ring shape? ":["round","square","rectangle","oval",0],
                    "colour of anger ? ":["blue","red","pink","violet",1],
                    "ancient language ":["Marathi","Sanskrit","Urdu","Braj",1]}
    
    question_set_4 = {"who is strong ? ":["wood","copper","metal","plastic",2],
                    "covid year? ":["2005","2008","2021","2023",3],
                    "we live on? ":["earth","jupiter","venus","saturn",0],
                    "symol of water ? ":["co","h2o","co2","o2",1],
                    "city in america ? ":["new york","texas","swizerland","washingtone",3]}

    question_sets= [question_set_1, question_set_2, question_set_3, question_set_4]
    Terminator = True

    print("Message : For more details type help")
    option = 0

    while(Terminator):

        cmd = input(">>> ")
        if cmd == "exit":
            exit()
        
        elif cmd == "help":
           print("""
            To start the game just say "start"
            If you want to stop just say "exit"
            If you want to chose different Topic for quiz just say "options"
            To add your own quiz just say "add-quiz"
            """)
        
        elif cmd == "options":
           
           print("""
            type 1 for : MYTHOLOGICAL QUESTIONS
            type 2 for : GK QUESTIONS
            type 3 for : SCINTIFIC QUESTIONS
            type 4 for : HISTORY QUESYTIONS
            type 5 for : COMPUTER QUESTIONS
            """)
           
           option = int(input(">>> "))
        
        elif cmd == "start":
            point = 0
            for questions in question_sets[option]:
                print(questions+"\n")

                for ops in range(0,4):
                    print("\t",ops+1, question_sets[option][questions][ops])

                # ans = int(input())-1

                ans = input()

                if ans.isdigit():
                   ans = int(ans)-1

                elif ans == "exit":
                    print(f"You score {point}/5")
                    exit()
                
                if question_sets[option][questions][-1] == ans:
                   point += 1

            print(f"You score {point}/5")
         
        elif cmd == "add-quiz":
            quiz = {}
            

            print("Eter Quiz Title")
            title = input()

            for question in range(1,6):
                options=[]
                print(f"Enter Question no.{question}")
                key = input()

                for val in range(0,5):

                    if val == 4:
                        value = int(input("Enter an answer of this question : "))    
                    else:
                        value = input(f"Enter option {val} : ")

                    options.append(value) 
                
                quiz[key] = options
            
            question_sets.append(quiz)
            option = -1
            print(question_sets)

if __name__=="__main__":
 main()