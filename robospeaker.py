import pyttsx3

engine = pyttsx3.init()

# if __name__ == '__main__':
print("Welcome to RoboSpeaker 1.1 for Windows")
    
while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            engine.say("bye bye friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
