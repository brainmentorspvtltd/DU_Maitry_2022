import streamlit as st
from datetime import datetime as dt
import os, random
import gtts
from playsound import playsound
import urllib.request as url
import json
from geopy.geocoders import Nominatim
import bs4

st.title("Chat Application")

greetIntent = ["hi", "hello", "hey", "hi there", "hello there", "hey there"]
dateIntent = ["what's the date","date","date please","tell me date"]
timeIntent = ["what's the time","time","time please","tell me time"]
musicIntent = ["play song", "play music"]
weatherIntent = ["weather","tell me weather","how's the weather outisde", "temperature outside", "temperature"]
productIntent = ["search product","product"]

geolocator = Nominatim(user_agent="App_1")

form = st.form(key="chat_app")
msg = form.text_input(label="Enter your message")

if msg in weatherIntent:
    location = form.text_input(label="Enter location")
    coords = geolocator.geocode(location)
elif msg in productIntent:
    productName = form.text_input(label="Enter product")
    productName = productName.replace(" ","+")

submitBtn = form.form_submit_button(label="Send Message...")

# user has clicked on submit button
if submitBtn:
    if msg == "":
        st.write("Please Enter a Message...")
    else:
        st.write("User : " + msg)
        msg = msg.lower()
        if msg in greetIntent:
            st.write("CPU : Hello User")
        elif msg in dateIntent:
            d = dt.now().date()
            st.write(d.strftime("%d %b,%Y, %A"))
        elif msg in timeIntent:
            t = dt.now().time()
            st.write(t.strftime("%I:%M:%S, %p"))
        elif msg in musicIntent:
            path = "D:/Batches/Songs/Users"
            os.chdir(path)
            songs = os.listdir()
            song = random.choice(songs)
            os.startfile(song)
        elif msg in weatherIntent:
            c = 0
            if not location:
                st.write("")
            else:
                coords = geolocator.geocode(location)
                lat = coords.latitude
                lon = coords.longitude
                path = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=83e01e3dce5d28839bb5a177cb51af12"
                response = url.urlopen(path)
                data = json.load(response)
                k = data['main']['temp']
                c = k - 273.15
                st.write(f"Temp in {location} is {c:.2f}")
        elif msg in productIntent:
            if not productName:
                st.write("")
            else:
                path = f"https://www.flipkart.com/search?q={productName}"
                response = url.urlopen(path)   # Making HTTPRequest to Flipkart...
                page = bs4.BeautifulSoup(response)
                titleList = page.find_all('div', {'class' : '_4rR01T'})
                priceList = page.find_all('div', {'class' : '_30jeq3 _1_WHN1'})
                ratingsList = page.find_all('span', {'class' : '_2_R_DZ'})
                for i in range(len(titleList)):
                    st.write("Title : " + titleList[i].text)
                    st.write("Price : " + priceList[i].text)
                    st.write("Reviews : " + ratingsList[i].text)
                    st.write("*" * 40)

        elif msg == "bye":
            st.write("Bye...")
        else:
            st.write("I don't understand...")

        tts = gtts.gTTS("You said " + msg)
        tts.save(f"{msg}.mp3")
        playsound(f"{msg}.mp3")
        os.remove(f"{msg}.mp3")

