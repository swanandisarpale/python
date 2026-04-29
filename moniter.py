import keyboard

# static bad words list
bad_words = ["bad", "hate", "stupid", "abuse"]

word = ""

print("Program running... Press Ctrl+C to stop")


while True:
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN:
        key = event.name

        if len(key) == 1 and key.isalpha():
            word += key

        elif key == "space":
            if word.lower() in bad_words:
                file = open("mkl.txt", "a")
                file.write("Bad word detected: " + word + "\n")
                file.close()

            word = ""