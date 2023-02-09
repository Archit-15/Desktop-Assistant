import datetime         #Used for gettin date and time
import pyttsx3          #This is a text to speech recognition library
import speech_recognition as sr     #This is used for taking audio as input
import wikipedia
import webbrowser           #This is inbuilt library
import os

engine = pyttsx3.init('sapi5')      # Speach API used for speach recognition
voices = engine.getProperty('voices')       #Getting the voices and other properties from our system
# print(voices)   This will print the voices that are present in our system
# print(voices[1].id) This will present the 2nd voice
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)           #This function will speak whatever is present in string
    engine.runAndWait()         #This function will make the speech audible in the system,
    #it is absolutely necessary

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning!")
    elif hour>12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    
    speak("I am Jarvis sir, How may I help you")

#This function takes microphone input from user and returns string output    
def takecommand():
    r = sr.Recognizer()             #Recognizer is a class, helps us in recognizing audio
    with sr.Microphone() as source:   #The source of our audio input will be microphone
        #r.energy_threshold = 300
        print("Listening.....")
        r.pause_threshold = 1      # Seconds of non speaking audio before the listenig is over
        audio = r.listen(source)     #Records a single phrase from the source ("Audio source")
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language = 'en-in') #This will access the google speach API
        #and convert audio into text
        print(f"User said {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"   #Just a string not the python none
    return query


if __name__ == "__main__":
    #speak("Archit is stupid")
    wishme()
    while True:
        querry = takecommand().lower()       #Turns the string into lowercase
        
        #logic for executing tasks based on querry
        if 'wikipedia' in querry:
            speak("Searching Wikipedia....")
            querry.replace("wikipedia","")
            results = wikipedia.summary(querry,sentences = 2)    #This will search whatever is 
            #writen inside querry on wikipedia and will only show 2 sentences
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in querry:  
            webbrowser.open("youtube.com")    #This will use the web browser file and it will open
            # the url gievn as parameter

        elif 'open google' in querry:  
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in querry:  
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in querry:
            music_dir = "C:\\Users\\KIIT\\Music"
            songs = os.listdir(music_dir)            #Will list all the files present in a directory
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))
            #os.path.join -> concatinates 2 paths together so from music dir we will get the
            #folder directory and with song[0] we will get the song name which together will
            #be the path of that file and os.start file will start it
        
        elif 'the time' in querry:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            #This returns the current time in ohurs,minutes and seconds
            print(strtime)
            speak(strtime)

        # We can simmilarly open many applications 
        elif 'open code' in querry:
            codepath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'opera' in querry: 
            codepath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            os.startfile(codepath)

        elif 'exit' in querry:
            speak("Thanks for using me ,i am now closing myself")
            print("Exitting")
            exit()