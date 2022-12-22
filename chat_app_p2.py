#Chat Application
from datetime import datetime as dt

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["what's the date","date","date please","tell me date"]
timeIntent = ["what's the time","time","time please","tell me time"]


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
    elif msg == "bye":
        print("Bye...")
        chat = False
    else:
        print("I don't understand...")

