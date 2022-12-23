#Chat Application
from datetime import datetime as dt
import os, random
import gtts
from playsound import playsound

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["what's the date","date","date please","tell me date"]
timeIntent = ["what's the time","time","time please","tell me time"]
musicIntent = ["play song", "play music"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    # Membership operator - in, not in
    if msg in greetIntent:
        print("Hello User")
    elif msg in dateIntent:
        d = dt.now().date()
        print(d.strftime("%d %b,%Y, %A"))
    elif msg in timeIntent:
        t = dt.now().time()
        print(t.strftime("%I:%M:%S, %p"))
    elif msg in musicIntent:
        path = "D:/Batches/Songs/Users"
        os.chdir(path)
        songs = os.listdir()
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "bye":
        print("Bye...")
        chat = False
    else:
        print("I don't understand...")

    tts = gtts.gTTS("You said " + msg)
    tts.save(f"{msg}.mp3")
    playsound(f"{msg}.mp3")
    os.remove(f"{msg}.mp3")
