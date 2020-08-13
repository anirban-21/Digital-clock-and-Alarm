import pylint
import pyttsx3
import speech_recognition as sr 
import datetime
import os
import subprocess
import time
from tkinter import *
import calendar
import winsound

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

def takeCommand():
       #It takes voice input from user using a mic and returns string output
       r=sr.Recognizer()
       with sr.Microphone() as source:
              print("Listening....")
              r.pause_threshold=1
              audio = r.listen(source)

       try:

              print("Recognizing...")
              query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
              print(f"User said: {query}\n")  #User query will be printed.
    
       except Exception as e:  #exception
              print(e)
              print("Could you please repeat that...")   #"Could you please repeat that..." will be printed in case of improper voice input
              return "None" #None string will be returned
       return query                

def speak(audio):
       engine.say(audio)
       engine.runAndWait() #Without this command, speech will not be audible to us.

def showclock():
    root=Tk()
    root.title("DIGITAL CLOCK")
    root.geometry("1380x716+0+0")
    root.config(bg="#081923")

    def clock():
        h=str(time.strftime("%H"))
        m=str(time.strftime("%M"))
        s=str(time.strftime("%S"))
    
        dd=str(time.strftime("%d"))
        mm=int(time.strftime("%m"))
        mm=calendar.month_name[mm]
        yy=datetime.datetime.now()

        lbl_date.config(text=dd)
        lbl_month.config(text=str(mm))
        lbl_year.config(text=str(yy.year))

        if int(h)>12 and int(m)>0:
            lbl_noon.config(text="PM")
        elif int(h)>12:
            h=str((int(h)-12))
        lbl_hr.config(text=h)
        lbl_min.config(text=m)
        lbl_sec.config(text=s)
    
        lbl_hr.after(200,clock)

    lbl_hr=Label(root,text="12",font=("times new roman",50,"bold"),bg="#087587",fg="white",cursor="pirate")
    lbl_hr.place(x=350,y=200,width=150,height=150)

    lbl_hr2=Label(root,text="HOURS",font=("times new roman",20,"bold"),bg="#087587",fg="white",cursor="pirate")
    lbl_hr2.place(x=350,y=360,width=150,height=50)

    lbl_date=Label(root,text="DATE",font=("times new roman",20,"bold"),bg="#087587",fg="white",cursor="pirate")
    lbl_date.place(x=350,y=420,width=150,height=50)
  
    lbl_min=Label(root,text="12",font=("times new roman",50,"bold"),bg="#DF002A",fg="white",cursor="pirate")
    lbl_min.place(x=520,y=200,width=150,height=150)

    lbl_min2=Label(root,text="MINUTES",font=("times new roman",20,"bold"),bg="#DF002A",fg="white",cursor="pirate")
    lbl_min2.place(x=520,y=360,width=150,height=50)

    lbl_month=Label(root,text="MONTH",font=("times new roman",20,"bold"),bg="#DF002A",fg="white",cursor="pirate")
    lbl_month.place(x=520,y=420,width=150,height=50)

    lbl_sec=Label(root,text="12",font=("times new roman",50,"bold"),bg="#087587",fg="white",cursor="pirate")
    lbl_sec.place(x=690,y=200,width=150,height=150)

    lbl_sec2=Label(root,text="SECONDS",font=("times new roman",20,"bold"),bg="#087587",fg="white",cursor="pirate")
    lbl_sec2.place(x=690,y=360,width=150,height=50)

    lbl_year=Label(root,text="YEAR",font=("times new roman",20,"bold"),bg="#087587",fg="white",cursor="pirate")
    lbl_year.place(x=690,y=420,width=150,height=50)

    lbl_noon=Label(root,text="12",font=("times new roman",50,"bold"),bg="#DF002A",fg="white",cursor="pirate")
    lbl_noon.place(x=860,y=200,width=150,height=210)

    lbl_cdate=Label(root,text="DATE",font=("times new roman",20,"bold"),bg="#DF002A",fg="white",cursor="pirate")
    lbl_cdate.place(x=860,y=420,width=150,height=50)

    clock()
    root.mainloop()

def setalarm():
    speak("User asked to set alarm ...")
    alarmHour=int(input("Hour : "))
    alarmMinute=int(input("Minute : "))
    ampm=str(input("AM or PM : "))

    if (ampm == "pm"):
        alarmHour=alarmHour+12
    while True:
        if (alarmHour==datetime.datetime.now().hour and alarmMinute==datetime.datetime.now().minute):
            winsound.Beep(1200,500)
            winsound.Beep(1200,500)
            winsound.Beep(1200,500)
            showclock()
            break

if __name__=="__main__" :
    while True:

        query = takeCommand().lower() #Converting user query into lower case
        #query=str(input("Query : "))

        if 'hello' in query:  
            speak("Hello sir") 

        elif 'set an alarm' in query or 'set alarm' in query or 'alarm' in query or 'set the alarm' in query:
            setalarm()
        
        elif 'bye' in query:
            speak("Have a good day Sir!")
            exit()

            



        