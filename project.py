from re import T
from time import strftime
from turtle import back, color, width
from click import command
from tkinter import *
from PIL import Image,ImageTk
from cv2 import waitKey
from tkinter import filedialog
import os 
import subprocess
from datetime import datetime
from numpy import diag
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

####################################################################################################################################################333

def fEncode(pic):
    encodedList = []
    for i in pic:
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(i)[0]
        encodedList.append(encode)
    return encodedList
print('Encoding Complete')

def clear():
    with open('Attendance.csv','w') as f:
        f.close()

def register(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


#################################################################################################################################################3





def grow(raw):
    global datename

    p=Toplevel()
    f=open('log.txt','r')
    r=f.readline()
    c=r.split('  ||  ')
    for i in range(len(c)):
        l=c[i].split(',')
        if l[0]==raw:
            for j in range(len(l)):
                Label(p,text=l[j]).pack()
            

def home2():
    global homebutton
    global datename
    global askbutton

    global buad
    global bude
    global buen

    homebutton.grid_forget()
    datename.grid_forget()
    askbutton.grid_forget()

    buad=Button(root,text='Attendence',command=attend)#this for attendence
    buen=Button(root,text='enter new',command=neww)#this for new entry
    bude=Button(root,text='Get Attndence',command=display)#this is for delete any rec

    buad.grid(row=0,column=0)
    buen.grid(row=1,column=0)
    bude.grid(row=2,column=0)




def display():
    global buad
    global buen
    global bude

    global homebutton
    global datename
    global askbutton
    global raw

    raw=StringVar()

    buad.grid_forget()
    bude.grid_forget()
    buen.grid_forget()

    homebutton=Button(root,text='back',command=home2)
    homebutton.grid(row=0,column=0)

    datename=Entry(root,width='50')
    datename.grid(row=1,column=1)

    askbutton=Button(root,text='Get attendence',command=lambda: grow(datename.get()))
    askbutton.grid(row=1,column=2)

    raw=datename.get()

    

def saves(m):
    f=open('log.txt','a+')
    d1=strftime("%d/%m/%y")
    f.write(d1+',')
    for i in range(len(m)-1):
        f.write(m[i+1]+',')
    f.write('  ||  ')
    p.quit()



def attend():
    global p

    global buad
    global bude
    global buen
    global harr_cascade

    ####################################################################################################################################

    pic = []
    names = []
    List = os.listdir("ImagesAttendence")
    #print(List)
    for i in List:
        temp = cv2.imread(f'{"ImagesAttendence"}/{i}')
        pic.append(temp)
        names.append(os.path.splitext(i)[0])
    #print(names)

    encodedList = fEncode(pic)

    clear()

    vid = cv2.VideoCapture(0)

    while True:
        check, frame = vid.read()
        img = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        curpic = face_recognition.face_locations(img)
        cdcurpic = face_recognition.face_encodings(img, curpic)

        for encode, fl in zip(cdcurpic, curpic):
            same = face_recognition.compare_faces(encodedList, encode)
            fd = face_recognition.face_distance(encodedList, encode)
            pos = np.argmin(fd)

            if same[pos]:
                n = names[pos].upper()
                y1, x2, y2, x1 = fl
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (255, 0, 0), cv2.FILLED)
                cv2.putText(frame, n, (x1 + 4, y2 - 4), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                register(n)
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

    vid.release()
    cv2.destroyAllWindows()

    #####################################################################################################################################################################33


    namesa=[]
    with open('Attendance.csv','r+') as f:
        p=f.readlines()
        for i in p:
            c=i.split(',')
            namesa.append(c[0])
    global p
    
    p=Toplevel()
    for i in namesa:
        Label(p,text=i).pack()
    Button(p,text='Save',command=lambda: saves(namesa)).pack()
    



    
    


def store():#pass parameters
    #to store data, Enter your code here:

    global entroll
    global entname
    global gender
    global d
    global mo
    global ye

    roll=entroll.get()
    name=entname.get()
    gender=gender.get()
    dob=str(d)+'/'+str(mo)+'/'+str(ye)

    f=open('info.txt','a+')

    rite=roll+','+name+','+dob+','+gender+' || '

    f.write(rite)
    f.close()

    home1()#this is to go back to home page

def train():

    tell=[]
    #openCV code here:
    global myimg
    global entroll
    global img
    
    os.rename(myimg,'ImagesAttendence/'+entroll.get()+'.jpg')



    store()#this is to save other data

def picshow():
    global piclab
    global myimg
    global img

    piclab.grid_forget()

    myimg=filedialog.askopenfilename(title='Select Picture Of Student')
    img=ImageTk.PhotoImage(Image.open(myimg))
    piclab=Label(image=img)

    piclab.grid(row=6,column=1,columnspan=3)

def home1():
    global lab1
    global lab2
    global lab3
    global lab4
    global buback

    global buad
    global bude
    global buen

    global entname
    global entroll

    global gender


    global genradfemale
    global genradmale

    global da
    global m
    global y

    global bupic
    global piclab

    global submit
    
    bupic.grid_forget()
    piclab.grid_forget()

    y.grid_forget()
    m.grid_forget()
    da.grid_forget()

    lab1.grid_forget()
    lab2.grid_forget()
    lab3.grid_forget()
    lab4.grid_forget()
    buback.grid_forget()

    entname.grid_forget()
    entroll.grid_forget()

    genradmale.grid_forget()
    genradfemale.grid_forget()

    submit.grid_forget()

    buad=Button(root,text='Attendence',command=attend)#this for attendence
    buen=Button(root,text='enter new',command=neww)#this for new entry
    bude=Button(root,text='Get Attendence',command=display)#this is for delete any rec

    buad.grid(row=0,column=0)
    buen.grid(row=1,column=0)
    bude.grid(row=2,column=0)


def neww():
    global lab1
    global lab2
    global lab3
    global lab4
    global buback

    global buad
    global bude
    global buen

    global entname
    global entroll

    global gender

    global genradfemale
    global genradmale

    global d
    global mo
    global ye
    global da
    global m
    global y

    global bupic
    global piclab
    global myimg
    global img

    global submit

    gender.set('empty')

    d=IntVar()
    mo=IntVar()
    ye=IntVar()


    buen.grid_forget()
    bude.grid_forget()
    buad.grid_forget()

    year=[]
    for i in range(2000,2023):
        year.append(i)
    month=[1,2,3,4,5,6,7,8,9,10,11,12]
    day=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

    lab1=Label(root,text='Name: ')
    lab2=Label(root,text='Roll: ')
    lab3=Label(root,text='DOB: ')
    lab4=Label(root,text='Gender')
    buback=Button(root,text='Home',command=home1)

    entname=Entry(root)
    entroll=Entry(root)

    genradmale=Radiobutton(root,text='Male',variable=gender,value='male')
    genradfemale=Radiobutton(root,text='Female',variable=gender,value='female')
    genempty=Radiobutton(root,text='',variable=gender,value='empty')

    da=OptionMenu(root,d,*day)
    m=OptionMenu(root,mo,*month)
    y=OptionMenu(root,ye,*year,)

    myimg=ImageTk.PhotoImage(Image.open('photo/any.jpg'))
    piclab=Label(root,image=myimg)
    bupic=Button(root,text='Select a Picture',command=picshow)
    
    submit=Button(root,text='Submit',command=train)

    da.grid(row=4,column=2)
    m.grid(row=4,column=3)
    y.grid(row=4,column=4)

    lab1.grid(row=1,column=1)
    lab2.grid(row=2,column=1)
    lab3.grid(row=4,column=1)
    lab4.grid(row=3,column=1)
    buback.grid(row=0,column=0)

    entname.grid(row=1,column=2,columnspan=3)
    entroll.grid(row=2,column=2,columnspan=3)

    genradfemale.grid(row=3,column=3)
    genradmale.grid(row=3,column=2)

    bupic.grid(row=5,column=1,columnspan=3)
    piclab.grid(row=6,column=1,columnspan=3)

    submit.grid(row=7,column=1,columnspan=3)

root = Tk()

gender=StringVar()#this for gender
buad=Button(root,text='Attendence',command=attend)#this for attendence
buen=Button(root,text='enter new',command=neww)#this for new entry
bude=Button(root,text='Get Attendence',command=display)#this is for delete any rec


buad.grid(row=0,column=0)
buen.grid(row=1,column=0)
bude.grid(row=2,column=0)



root.mainloop()

