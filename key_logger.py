
import keyboard
def main():
    badwords=["apple","orange","banana","pineapple","guava","cherry"]
    pressedkey=input()
    
    if pressedkey==badwords:
        print("bad word is getting pressed")
        keyboard.play("recorded bad word")
    else:
        print("no bad word")

    if pressedkey=="exit":
        exit()
        
keyboard.start_recording()
keyboard.wait("esc")
keyboard.add_abbreviation('@@', 'my.long.email@mail.com')
         



if __name__=="__main__":
    main()