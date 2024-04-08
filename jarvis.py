import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak('Food Afternoon!')
        
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis Sir. Please tell me how Ihelp you")
    
def takeCommand():
    #it takes
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print("user said:", query)
        
    except Exception as e:
        print(e)
        
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',535)  
    #server.ehlo()
    server.starttls()
    server.login('mandloipooja2002@gmail.com', 'Poojamsi1234')
    server.sendmail('mandloipooja2002@gmail.com', to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
      query = takeCommand().lower()
       
      if 'wikipedia' in query:
          speak('Searching wikipedia...')
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=2)
          speak("According to wikipedia")
          print(results)
          speak(results)
          
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
        
      elif 'open google' in query:
          webbrowser.open("google.com")
          
      elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")
               
      elif 'play music' in query:
          music_dir = 'C:\\Users\\mandl\\Downloads'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))
          
      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          print(strTime)
          speak(f"Sir, the time is{strTime}")
      elif 'open code' in query:
          codePath = "C:\\Users\\mandl\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
          os.startfile(codePath)
          
      elif 'email to pooja' in query:
          try:
              speak("what shoud I say")   
              content = takeCommand()
              to = "mandloipooja2002@gmail.com"  
              sendEmail(to, content)
              speak("Email has been sent!")
          except Exception as e:
              print(e)
              speak("Sorry my friend Pooja , I am not able to send this email")
            
      elif "exit" in query:
            speak("Goodbye!")
            exit()