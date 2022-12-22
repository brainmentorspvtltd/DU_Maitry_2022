#Chat Application

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg == "hi" or msg == "hello" or msg == "hey" or msg == "hi there":
        print("Hello User")
    elif msg == "bye":
        print("Bye...")
        chat = False
    else:
        print("I don't understand...")

