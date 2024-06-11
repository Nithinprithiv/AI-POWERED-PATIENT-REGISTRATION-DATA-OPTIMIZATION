import kivy
from kivymd.app import MDApp
from kivy.uix.label import Label as L
from kivy.uix.button import Button as B
from kivy.uix.checkbox import CheckBox as C
from kivy.uix.image import Image as I
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
#from html  import html
from datetime import datetime as dt
import datetime as dd
import speech_recognition as sr
from gtts import gTTS
import os
from PIL import Image
import pytesseract
import pyttsx3
import mysql.connector
import sqlite3
import cv2
import time
from threading import Thread
import threading
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import cv2
from cvzone.ClassificationModule import Classifier
from tkinter import filedialog
from tkinter import Tk
import os
import pyautogui as py
class Manager(ScreenManager):
    Builder.load_string("""
<Manager>:
    Screen:
        name:'logo'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/1.png'
        Label:
            text:"AI - AUTOMATED "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 90
            pos_hint:{"center_x":0.5,"center_y":0.9}
        Label:
            text:"Registration"
            color: 1,1,1,1
            font_style:"italic"
            font_size: 50
            pos_hint:{"center_x":0.51,"center_y":0.82}
       
        MDRectangleFlatButton:
            text: "Registration"
            size_hint:.15,.08
            font_size: 30
            pos_hint:{"center_x":0.3,"center_y":0.6}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "green"
            on_press:
                app.c1()
        MDRectangleFlatButton:
            text: "Special Patient"
            size_hint:.15,.08
            font_size: 30
            pos_hint:{"center_x":0.3,"center_y":0.45}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "green"
            on_press:
                app.c3()
        MDRectangleFlatButton:
            text: "Patient Details"
            size_hint:.15,.08
            font_size: 30
            pos_hint:{"center_x":0.3,"center_y":0.3}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "green"
            on_press:
                app.c2()
                        
        Label:
            id:verification
            text:""
            color: 0,1,0,1
            font_style:"italic"
            font_size: 20
            pos_hint:{"center_x":0.51,"center_y":0.15}
        Label:
            id:d1
            text:"Date: "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 25
            pos_hint:{"center_x":0.85,"center_y":0.1}
        Label:
            id:t1
            text:"Time:"
            color: 1,1,1,1
            font_style:"italic"
            font_size: 25
            pos_hint:{"center_x":0.85,"center_y":0.07}
        
    Screen:
        name:'second'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/2.png'
        Label:
            text:"Scan Your Aadhar card : "
            color: 1,1,0,1
            font_style:"italic"
            font_size: 40
            pos_hint:{"center_x":0.3,"center_y":0.8}
        Label:
            id:cc
            text:" "
            color: 0,1,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.55,"center_y":0.55}
                            
        Image:
            id:image
            size_hint:(.15,.18)
            pos_hint:{"center_x":0.8,"center_y":0.70}
        Image:
            id:images
            size_hint:(.15,.18)
            pos_hint:{"center_x":0.8,"center_y":0.45}
        MDRectangleFlatButton:
            id:nn1
            text: "           "
            pos_hint:{"center_x":0.1,"center_y":0.1}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "black"
            on_press:
                root.current='Third'
                app.speech_to_textm()
    Screen:
        name:'Third'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/2.png'
        Image:
            source:'image/mic.png'
            size_hint:(.15,.18)
            pos_hint:{"center_x":0.5,"center_y":0.45}
        Label:
            id:main
            text:"Say your Mobile number / Blood Group and Problem ?"
            color: 0,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.6}
        MDRectangleFlatButton:
            id:m1
            text: "           "
            pos_hint:{"center_x":0.1,"center_y":0.1}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "black"
            on_press:
                root.current='forth'
 
    Screen:
        name:'forth'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/2.png'
        Label:
            text:"Say your Blood Group ..."
            color: 0,1,1,1
            font_style:"italic"
            font_size: 40
            pos_hint:{"center_x":0.5,"center_y":0.5}
        MDRectangleFlatButton:
            id:b11
            text: "           "
            pos_hint:{"center_x":0.1,"center_y":0.1}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "black"
            on_press:
                root.current='fifth'
                
         
        
    Screen:
        name:'fifth'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/2.png'
        Label:
            text:"What's your problem Sir/Mam ? "
            color: 0,1,1,1
            font_style:"italic"
            font_size: 40
            pos_hint:{"center_x":0.5,"center_y":0.5} 
        MDRectangleFlatButton:
            id:p1
            text: "           "
            pos_hint:{"center_x":0.1,"center_y":0.1}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: "black"
            on_press:
                root.current='sixth'           
    Screen:
        name:'sixth'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/2.png'
        Label:
            text:"Patient Details: "
            color: 0,1,1,1
            font_style:"italic"
            font_size: 40
            pos_hint:{"center_x":0.2,"center_y":0.8}
        Label:
            text:"Id : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.7}
        MDTextField:
            id:id2
            mode: "rectangle"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            size_hint:.15,.08
            pos_hint:{"center_x":0.35,"center_y":0.7}
        Label:
            text:"Name : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.6}
        MDTextField:
            id:name
            mode: "rectangle"
            # hint_text: "Name"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            size_hint:.15,.08
            pos_hint:{"center_x":0.35,"center_y":0.6}
        Label:
            text:"Mobile.No : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.5}
        MDTextField:
            id:mobile
            mode: "rectangle"
            # hint_text: "Mobile.No"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.35,"center_y":0.5}
            size_hint:.15,.08
        Label:
            text:"Gender : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.4}
        MDTextField:
            id:gender
            mode: "rectangle"
            # hint_text: "Gender"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.35,"center_y":0.4}
            size_hint:.15,.08
        Label:
            text:"Blood Group : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.3}
        MDTextField:
            id:blood
            mode: "rectangle"
            # hint_text: "Blood Group"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.35,"center_y":0.3}
            size_hint:.15,.08
        Label:
            text:"DOB : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.7}
        MDTextField:
            id:dob
            mode: "rectangle"
            # hint_text: "DOB"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.75,"center_y":0.7}
            size_hint:.15,.08
        Label:
            text:"Problem : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.6}
        MDTextField:
            id:problem
            mode: "rectangle"
            # hint_text: "Problem"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            size_hint:.15,.08
            pos_hint:{"center_x":0.75,"center_y":0.6}
        Label:
            text:"Aadhar No : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.5}
        MDTextField:
            id:aadhar
            mode: "rectangle"
            # hint_text: "Aadhar No"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.75,"center_y":0.5}
            size_hint:.15,.08
        # Label:
        #     text:"Gender : "
        #     color: 1,1,1,1
        #     font_style:"italic"
        #     font_size: 30
        #     pos_hint:{"center_x":0.5,"center_y":0.5}
        # MDTextField:
        #     id:gender
        #     mode: "rectangle"
            hint_text: "Gender"
        #     multiline:False
        #     color_mode: 'custom'
        #     line_color_focus: 1, 1, 1, 1
        #     pos_hint:{"center_x":0.75,"center_y":0.5}
        #     size_hint:.15,.08
        # Label:
        #     text:"Blood Group : "
        #     color: 1,1,1,1
        #     font_style:"italic"
        #     font_size: 30
        #     pos_hint:{"center_x":0.5,"center_y":0.4}
        # MDTextField:
        #     mode: "rectangle"
            # hint_text: "Blood Group"
        #     multiline:False
        #     color_mode: 'custom'
        #     line_color_focus: 1, 1, 1, 1
        #     pos_hint:{"center_x":0.75,"center_y":0.4}
        #     size_hint:.15,.08
        Label:
            text:"Address : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.4}
        MDTextField:
            id:address
            mode: "rectangle"
            # hint_text: "Address"
            multiline:True
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.75,"center_y":0.4}
            size_hint:.15,.08
    Screen:
        name:'seven'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/l.png'
        Label:
            text:"Name : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.7}
        Label:
            id:dname1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.35,"center_y":0.7}
        Label:
            text:"specialist : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.6}
        Label:
            id:dspecialist
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.35,"center_y":0.6}
            
            
    Screen:
        name:'eigth'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/2.png'
        Label:
            text:"Say Patient ID ..."
            color: 0,1,1,1
            font_style:"italic"
            font_size: 40
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Label:
            id:id1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.4}
        
    Screen:
        name:'ninth'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/2.png'
        Label:
            id:id1
            text:""
            color: 1,0,0,1
            font_style:"italic"
            font_size: 40
            pos_hint:{"center_x":0.2,"center_y":0.8}
        Label:
            text:"Name : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.7}
        Label:
            id:name1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.35,"center_y":0.7}
        Label:
            text:"Mobile.No : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.6}
        Label:
            id:mobile1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.35,"center_y":0.6}
            
        Label:
            text:"Gender : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.5}
        Label:
            id:gender1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.35,"center_y":0.5}
            
        Label:
            text:"Blood Group : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.4}
        Label:
            id:blood1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.35,"center_y":0.4}
            
        Label:
            text:"DOB : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.15,"center_y":0.3}
        Label:
            id:dob1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.35,"center_y":0.3}
            
        Label:
            text:"Problem : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.7}
        Label:
            id:problem1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.65,"center_y":0.7}
        Label:
            text:"Aadhar No : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.6}
        Label:
            id:aadhar1
            mode: "rectangle"
            hint_text: "Aadhar No"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.65,"center_y":0.6}
        # Label:
        #     text:"Gender : "
        #     color: 1,1,1,1
        #     font_style:"italic"
        #     font_size: 30
        #     pos_hint:{"center_x":0.5,"center_y":0.5}
        # Label:
        #     id:gender
        #     mode: "rectangle"
        #     hint_text: "Gender"
        #     multiline:False
        #     color_mode: 'custom'
        #     line_color_focus: 1, 1, 1, 1
        #     pos_hint:{"center_x":0.65,"center_y":0.5}
        #     
        # Label:
        #     text:"Blood Group : "
        #     color: 1,1,1,1
        #     font_style:"italic"
        #     font_size: 30
        #     pos_hint:{"center_x":0.5,"center_y":0.4}
        # Label:
        #     mode: "rectangle"
        #     hint_text: "Blood Group"
        #     multiline:False
        #     color_mode: 'custom'
        #     line_color_focus: 1, 1, 1, 1
        #     pos_hint:{"center_x":0.65,"center_y":0.4}
        #        
        # Label:
        #     text:"Gender : "
        #     color: 1,1,1,1
        #     font_style:"italic"
        #     font_size: 30
        #     pos_hint:{"center_x":0.5,"center_y":0.5}
        # Label:
        #     id:gender
        #     mode: "rectangle"
        #     hint_text: "Gender"
        #     multiline:False
        #     color_mode: 'custom'
        #     line_color_focus: 1, 1, 1, 1
        #     pos_hint:{"center_x":0.65,"center_y":0.5}
        #     
        # Label:
        #     text:"Blood Group : "
        #     color: 1,1,1,1
        #     font_style:"italic"
        #     font_size: 30
        #     pos_hint:{"center_x":0.5,"center_y":0.4}
        # Label:
        #     mode: "rectangle"
        #     hint_text: "Blood Group"
        #     multiline:False
        #     color_mode: 'custom'
        #     line_color_focus: 1, 1, 1, 1
        #     pos_hint:{"center_x":0.65,"center_y":0.4}
        #     
        Label:
            text:"Address : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.5}
        Label:
            id:address1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.70,"center_y":0.5}
        Label:
            text:"Date : "
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.5,"center_y":0.4}
        Label:
            id:date1
            text:""
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.65,"center_y":0.4}
    Screen:
        name:'ten'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/2.png'
        Label:
            text:"Patient Details : "
            color: 1,1,0,1
            font_style:"italic"
            font_size: 40
            pos_hint:{"center_x":0.2,"center_y":0.8}
        Label:
            text:"Mobile No : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.4,"center_y":0.7}
        MDTextField:
            id:mob1
            mode: "rectangle"
            # hint_text: "mobile"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            size_hint:.15,.08
            pos_hint:{"center_x":0.55,"center_y":0.7}
        Label:
            text:"Blood group : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.4,"center_y":0.6}
        MDTextField:
            id:blo1
            mode: "rectangle"
            # hint_text: "blo1"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.55,"center_y":0.6}
            size_hint:.15,.08
        Label:
            text:"Problem : "
            color: 1,1,1,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.4,"center_y":0.5}
        MDTextField:
            id:pro1
            mode: "rectangle"
            # hint_text: "problem"
            multiline:False
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            pos_hint:{"center_x":0.55,"center_y":0.5}
            size_hint:.15,.08    
    Screen:
        name:'eleven'
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'image/l.png'
        Label:
            text:"Doctor is not Available.."
            color: 1,0,0,1
            font_style:"italic"
            font_size: 30
            pos_hint:{"center_x":0.35,"center_y":0.6}            
    """)
    pass
class AI_Register(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.time_remaining = 0  # Initial time in seconds
        self.is_running = False
        
        # if True:
        #     thread7 = threading.Thread(target=self.c1)
        #     thread7.start() 
        mydb = mysql.connector.connect(

			host = "localhost", 
			user = "root",
			passwd = "",
			database = "second1_db"
			)
        c = mydb.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS second1_db")
        c.execute("""CREATE TABLE if not exists patient_main1 (Id  VARCHAR(5),name  VARCHAR(15),mobile_NO VARCHAR(20),Gender VARCHAR(5),Blood_group VARCHAR(10),DOB VARCHAR(20),problem VARCHAR(20),Aadhar_no VARCHAR(20),Address VARCHAR(100),Date VARCHAR(10))""")
        mydb.commit()
        mydb.close()
        return Manager()    
    
    def human_face(self):
        if True:
            human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            cap = cv2.VideoCapture(0)
            m=1
            while True:
                ret, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                for (x, y, w, h) in humans:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imshow("Human Detection", frame)
                # print(m//10)
                if m>=50 and frame.all()==True:
                    time.sleep(2)
                    py.hotkey('alt'+'f4')
                    py.typewrite('q')
                    now=dt.now()
                    cv2.imwrite("out/"+(str(dd.date.today()))+str(m)+'.jpg',frame)
                    m=0
                    
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                m=m+1
            
            cap.release()
            now=dt.now()
            self.root.ids.t1.text = 'Time : '+str(now.strftime("%H:%M:%S"))
            self.root.ids.d1.text = 'Date : '+str(dd.date.today())
            cv2.destroyAllWindows()
            text='Human face successfully dectected'
            self.text_to_speech(text)
    def speech_to_textpp(self,say):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print(say)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            self.show(text)
            self.root.ids.id1.text=text
        except sr.UnknownValueError:
            print("Could not understand audio")
            # self.root.ids.mobile.text='ghfygf'
            self.speech_to_textpp(say)
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            # self.speech_to_textm(say)
    count = 0        
    def c3(self):
        # Start the clock
            # clock=Clock()
            Clock.schedule_interval(self.Callback_Clock3, 1)
    now=dt.now()
    global tn
    tn =int(now.strftime("%H"))
    # if tn>12:
    #     global tn
    #     tn=tn-12
    def Callback_Clock3(self, dt):
            # now=dt.now()
            self.count = self.count + 1
            count=self.count
            print(count)
            if self.count==1:
                for i in range (1,3):  
                    self.face_cap(i)
            elif self.count==2:
                self.root.current='ten'  
                 
            elif self.count==20:
                c=[]
                for i in range (1000,4000):
                    c.append(i)   
                ch=random.choice(c)
                self.root.ids.id2.text=str(ch)
                self.root.ids.mobile.text=self.root.ids.mob1.text
                self.root.ids.blood.text=self.root.ids.blo1.text
                self.root.ids.problem.text=self.root.ids.pro1.text
                self.detail()
            elif self.count==21:
                self.root.current='sixth'
            elif self.count==31:
                
                d=['fever,cold,head ache,body pain,injury,fire injury,stomach pain','leg facher,hand facher,finger facher,hip_bone facher,back_bone facher','left leg nerve,right leg nerve,neck nerve,right hand nerve,left hand nerve','heart problem']
                for i in (d):
                    if str(self.root.ids.pro1.text).casefold() in i.casefold():
                        mydb = mysql.connector.connect(
                                    host = "localhost", 
                                    user = "root",
                                    passwd = "",
                                    database = "second1_db"
                        )
                        c = mydb.cursor() 
                        c.execute(f"SELECT  Work_time FROM doctor_details WHERE Treatment='{i}'")
                        d = c.fetchall()
                        # print(d)
                        ww= str(d[0]).removeprefix("('").removesuffix("',)")
                        wf=int(ww[0])
                        wl=int(ww[-1])
                        t=[]
                        for j in range(int(wf)):
                            t.append(wf)
                            wf+=1
                            # if wf>12:
                            #     wf=1
                        # now=dt.now()
                        
                        if int(tn) in t:
                            self.d_show(i)
                            self.add()
                            self.root.current='seven'
                            # self.new()
                            t.clear()
                        else:
                            self.new()
                            self.root.current='eleven'  
                        mydb.commit()
                        mydb.close() 
            elif self.count==37:
                # self.root.current='sixth'
                self.new()
            elif self.count==38: 
                Clock.unschedule(self.Callback_Clock3)
                self.count =0
                self.root.current='logo'   
                        
    count = 0        
    def c2(self):
        # Start the clock
            # clock=Clock()
            Clock.schedule_interval(self.Callback_Clock2, 1)
    def Callback_Clock2(self, dt):
            self.count = self.count + 1
            count=self.count
            print(count)
            if self.count==1:
                self.root.current='eigth'  
            elif self.count==2:
                say='Say Patient Id Number... '
                self.speech_to_textpp(say)  
                 
            elif self.count==3:   
                self.root.current='ninth' 
            elif self.count==13:
                Clock.unschedule(self.Callback_Clock2)
                self.count =0
                self.root.current='logo'  
    count = 0        
    def c1(self):
        # Start the clock
            # clock=Clock()
            Clock.schedule_interval(self.Callback_Clock1, 1)
    def Callback_Clock1(self, dt):
            self.count = self.count + 1
            count=self.count
            print(count)
            if self.count==2:
                self.human_face()
            elif self.count==3:
                self.root.current='second'  
            elif self.count==4:
                text='Scan Your Aadhar card '
                self.text_to_speech(text)
            elif self.count==5:
                for i in range (1,3):  
                    self.face_cap(i)
                # text='Say your Mobile number Blood Group and Problem '
                # self.text_to_speech(text)
                
            elif self.count==6:
                self.root.current='Third'
            elif self.count==8: 
                # self.root.current='Third'
                say="Say your Mobile number: "
                self.speech_to_textm(say)  
                # self.root.ids.mobile.text='ghfygf'
                # self.root.current='forth'
            elif self.count==10:
                say="Say your Blood Group: "
                # text=say
                # self.text_to_speech(text)
                self.speech_to_textb(say) 
                # self.root.current='felifth'  
            elif self.count==12:
                say="What is your problem Sir/Mam ?"
                # text=say
                # self.text_to_speech(text)
                self.speech_to_textp(say)
                # self.root.ids.name.text='ghfygf' 
                c=[]
                for i in range (1000,4000):
                    c.append(i)   
                ch=random.choice(c)
                self.root.ids.id2.text=str(ch)
                self.detail()
                self.root.current='sixth'  
            elif self.count==22:
                # self.add()
                d=['fever,cold,head ache,body pain,injury,fire injury,stomach pain','leg facher,hand facher,finger facher,hip_bone facher,back_bone facher','left leg nerve,right leg nerve,neck nerve,right hand nerve,left hand nerve','heart problem']
                # d=['fever,cold,head ache,body pain,injury,fire injury,stomach pain','leg facher,hand facher,finger facher,hip_bone facher,back_bone facher','left leg,right leg,neck,right hand,left hand','heart problem']
                for i in (d):
                    if str(self.root.ids.problem.text).casefold() in i.casefold():
                        mydb = mysql.connector.connect(
                        host = "localhost", 
                        user = "root",
                        passwd = "",
                        database = "second1_db"
                        )
                        c = mydb.cursor() 
                        c.execute(f"SELECT  Work_time FROM doctor_details WHERE Treatment='{i}'")
                        d = c.fetchall()
                        ww= str(d[0]).removeprefix("('").removesuffix("',)")
                        wf=int(ww[0])
                        wl=int(ww[-1])
                        t=[]
                        for j in range(int(wf)):
                            t.append(wf)
                            wf+=1
                            # if wf>12:
                            #     wf=1
                        # now=dt.now()
        
                        if int(tn) in t:
                            self.d_show(i)
                            self.add()
                            self.root.current='seven'
                            t.clear()
                        else:
                            self.root.current='eleven'  
                        mydb.commit()
                        mydb.close()  
                
            elif self.count==25:
                Clock.unschedule(self.Callback_Clock1)
                self.count =0
                self.new()
                self.root.current='logo'
                
    def speech_to_textm(self,say):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print(say)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            self.root.ids.mobile.text=str(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
            # self.root.ids.mobile.text='ghfygf'
            self.speech_to_textm(say)
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            # self.speech_to_textm(say) 
    def speech_to_textb(self,say):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print(say)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            self.root.ids.blood.text=str(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
            # self.root.ids.blood.text = 'ghfygf'
            self.speech_to_textb(say)
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            # self.speech_to_textb(say)
    def speech_to_textp(self,say):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print(say)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            self.root.ids.problem.text=str(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
            # self.root.ids.name.text = 'ghf'
            self.speech_to_textb(say)
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            # self.speech_to_textb(say)

    def face_cap(self,i):
            if True:
                # Clock.unschedule(self.Callback_Clock2)
                l=[]
                # self.c3()
                cap = cv2.VideoCapture(0)
                m=0
                n=150
                while True:
                    
                    ret, frame = cap.read()
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("scan for aadhar",frame)            
                    if n==1:
                        now=dt.now()
                        cv2.imwrite("Aadhar/"+(str(dd.date.today()))+str(n+i)+'.jpg',frame)
                        if i==1:
                            self.root.ids.image.source="Aadhar/"+(str(dd.date.today()))+str(n+i)+'.jpg'
                        else:
                            self.root.ids.images.source="Aadhar/"+(str(dd.date.today()))+str(n+i)+'.jpg'
                    print(n)
                    if n==0:
                        py.hotkey('alt'+'f4')
                        py.typewrite('q')
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    n=n-1
                # self.root.ids.cc.text = 'Scan Back side '   
                            
            cap.release()
            cv2.destroyAllWindows()
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
          
    def extract_information_from_image(self,image_path):
        # Open the image file
        img = Image.open(image_path)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

        # Process the extracted text to find relevant information
        lines = text.split('\n')

        for line in lines:
            if lines[1] in line:
                name = line.split(":")[-1].strip()
                self.root.ids.name.text=str(name)
            elif "DOB" in line:
                dob = line.split(":")[-1].strip()
                self.root.ids.dob.text=str(dob)
            elif "Male" in line:
                sex = line.split("/")[-1].strip()
                self.root.ids.gender.text=str(sex)
            elif lines[10] in line:
                aadhar_number = line.split(":")[-1].strip()
                self.root.ids.aadhar.text=str(aadhar_number)
    def extract_information_from_image1(self,image_path):
        # Open the image file
        img = Image.open(image_path)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

        # Process the extracted text to find relevant information
        lines = text.split('\n')

        for line in lines:
            if 'Address' in line:
                a = line.split(":")[-1].strip()
                
            if lines[40] in line:
                d = line.split(":")[-1].strip()
        address=(a+d) 
        self.root.ids.address.text=str(address)       
    def detail(self):
        self.extract_information_from_image('Aadhar/2024-01-3051.jpg')
        self.extract_information_from_image1('Aadhar/2024-01-3052.jpg')  
    def add(self):
        mydb = mysql.connector.connect(
                        host = "localhost", 
                        user = "root",
                        passwd = "",
                        database = "second1_db"
                        )
        c = mydb.cursor() 
        sq=("INSERT INTO patient_main1 (Id,name,mobile_No,Gender,Blood_group,DOB,problem,Aadhar_no,Address,Date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        r=[(self.root.ids.id2.text,self.root.ids.name.text,self.root.ids.mobile.text,self.root.ids.gender.text,self.root.ids.blood.text,self.root.ids.dob.text,
            self.root.ids.problem.text,self.root.ids.aadhar.text,self.root.ids.address.text,str(dd.date.today()),
                        )]
        c.executemany(sq,r)	
        mydb.commit()
        mydb.close() 
    def show(self,text):
        mydb = mysql.connector.connect(
                        host = "localhost", 
                        user = "root",
                        passwd = "",
                        database = "second1_db"
                        )
        c = mydb.cursor() 
        c.execute("SELECT  name FROM patient_main1 WHERE Id="+str(text))
        a = c.fetchall()
        self.root.ids.name1.text = str(a[0]).removeprefix("('").removesuffix("',)")
        c.execute("SELECT  mobile_No FROM patient_main1 WHERE Id="+str(text))
        b = c.fetchall()
        self.root.ids.mobile1.text = str(b[0]).removeprefix("('").removesuffix("',)")
        c.execute("SELECT  Gender FROM patient_main1 WHERE Id="+str(text))
        d = c.fetchall()
        self.root.ids.gender1.text = str(d[0]).removeprefix("('").removesuffix("',)")
        c.execute("SELECT Blood_group  FROM patient_main1 WHERE Id="+str(text))
        e = c.fetchall()
        self.root.ids.blood1.text = str(e[0]).removeprefix("('").removesuffix("',)")
        c.execute("SELECT  DOB FROM patient_main1 WHERE Id="+str(text))
        f = c.fetchall()
        self.root.ids.dob1.text = str(f[0]).removeprefix("('").removesuffix("',)")
        c.execute("SELECT  problem FROM patient_main1 WHERE Id="+str(text))
        g = c.fetchall()
        self.root.ids.problem1.text = str(g[0]).removeprefix("('").removesuffix("',)")
        c.execute("SELECT  Aadhar_no FROM patient_main1 WHERE Id="+str(text))
        h = c.fetchall()
        self.root.ids.aadhar1.text = str(h[0]).removeprefix("('").removesuffix("',)")
        c.execute("SELECT  Address FROM patient_main1 WHERE Id="+str(text))
        i = c.fetchall()
        self.root.ids.address1.text = str(i[0]).removeprefix("('").removesuffix("',)")
        c.execute("SELECT  Date FROM patient_main1 WHERE Id="+str(text))
        j = c.fetchall()
        self.root.ids.date1.text = str(j[0]).removeprefix("('").removesuffix("',)")
        mydb.commit()
        mydb.close() 
    def d_show(self,i):
        # d=['fever,cold,head ache,body pain,injury,fire injury,stomach pain','leg facher,hand facher,finger facher,hip_bone facher,back_bone facher','left leg,right leg,neck,right hand,left hand','heart problem']
        mydb = mysql.connector.connect(
                        host = "localhost", 
                        user = "root",
                        passwd = "",
                        database = "second1_db"
                        )
        c = mydb.cursor() 
        c.execute(f"SELECT  Name FROM doctor_details WHERE Treatment='{i}'")
        a = c.fetchall()
        self.root.ids.dname1.text = str(a[0]).removeprefix("('").removesuffix("',)")
        c.execute(f"SELECT  Specialist FROM doctor_details WHERE Treatment='{i}'")
        b = c.fetchall()
        self.root.ids.dspecialist.text = str(b[0]).removeprefix("('").removesuffix("',)")
        mydb.commit()
        mydb.close()  
    def new(self):
        self.root.ids.name.text=''
        self.root.ids.mobile.text=''
        self.root.ids.gender.text=''
        self.root.ids.blood.text=''
        self.root.ids.dob.text=''
        self.root.ids.problem.text=''
        self.root.ids.aadhar.text=''
        self.root.ids.address.text=''
    def text_to_speech(self,text):
        self.root.ids.verification.text = 'Human face successfully dectected'
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    def text_to_speech1(self,text):    
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    

if __name__ == '__main__':
    AI_Register().run()