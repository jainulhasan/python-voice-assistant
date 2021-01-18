import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os 
import pyjokes  
import psutil

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
print (voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("catty at your service, Please tell me how can i help you?")

#command by user function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 2
        r.energy_threshold=4000
        audio = r.listen(source)
        

    try:
        print("Recognizing...")
        query = r.recognize(audio)
    except:
        # print(e)
        speak("Say that again please...")

        return "None"

    return query

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def personal():
    speak(
        "I am Jainul's personal AI assistent...,CATTY, .. I am developed by jainul hasan on 30 july 2020 in Bareily Uttar pradesh INDIA"
    )
    speak("Now i hope you know me")

def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")

def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")

def wishme_end():
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 16):
        speak("thank you sir take care of yourself i am signing off, have a good day")
    elif (hour >= 18 and hour < 20):
        speak("thank you sir take care of yourself i am signing off, have a good eve")
    else:
        speak("thank you sir take care of yourself i am signing off, Goodnight.. Sweet dreams")
    quit()

#main
if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

#wikipedia'

        if ('wikipedia' in query or 'what' in query or 'who' in query or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

#time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()

#personal info
        elif ("tell me about yourself" in query):
            personal()
        
# open website
        elif("open youtube" in query):
            wb.open("www.youtube.com")
        elif("open netflix" in query):
            wb.open("www.netflix.com")
        elif("open amazon" in query):
            wb.open("www.amazon.com")
        elif("open flipkart" in query):
            wb.open("wwww.flipkart.com")
        elif ( "open website" in query):
            speak("Which websit should i search or open?")
            web = takeCommand().lower()
            wb.open(web + '.com')

#open music

        elif('play music' in query):
            music_dir ='D:\\MUSIC'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
#changing voice
        elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = takeCommand()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)            
           
#reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())
           
#jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("jarvis", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

#CATTY features
        elif ("tell me your powers" in query or "help" in query
              or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can shut down or restart your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search things on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)

#sysytem logout/ shut down etc

        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shutdown" in query):
            os.system("shutdown /s /t 1")
            
#cpu and battery usage
        elif ("cpu usage" in query or "battery" in query
              or "cpu" in query):
            cpu()

#exit function
        elif ('i am done' in query or 'bye bye CATTY' in query or 'go offline CATTY' in query or 'bye' in query or 'nothing' in query):
            wishme_end()
        