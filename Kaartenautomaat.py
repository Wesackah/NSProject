from tkinter import *
import requests
import xmltodict

auth_details = ('wesackah@gmail.com', 'aw17-v2gaEXQp1zWCvHXPW-M7lmVFrj1wr05rbTgmyPN0PF7-HDsJg')
#returnt een lijst met alle vertrektijden als strings
def vertrekTijd(code):
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + code
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)
    vertrekLijst = []
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        str = ''
        str += vertrek['EindBestemming'] + ';'
        vertrekTijd = vertrek['VertrekTijd'] + ';' # 2016-09-27T18:36:00+0200
        str += vertrekTijd[11:16] + ';' # 18:36
        str += vertrek['TreinSoort'] + ';'
        try:
            str += vertrek['VertrekSpoor']['#text']
        except:
            str += 'onbekend'
        # if spoor['@wijziging'] == "True":
        #     str += ' spoorweiziging'
        vertrekLijst.append(str)
    return vertrekLijst

#opent een window met de reisinformatie van het huidige station
def reisInformatie(code):
    infoFrame = Frame(width=1280, height=720, bg="Yellow")
    scrollbar = Scrollbar(master=infoFrame,)
    listBox = Listbox(infoFrame, yscrollcommand=scrollbar.set, height= 25,width= 116,font=('Consolas',14),bg='yellow')
    for tijd in vertrekTijd(code):
        listBox.insert(END, makeString(tijd))
    listBox.place(x=0,y=0)
    scrollbar.config(command=listBox.yview)
    scrollbar.place(x=1260, y=0)

    back = Button(master=infoFrame,text='terug',
                  bg="Blue",
                  fg="White",
                  activebackground="Blue",
                  activeforeground="White",
                  font=('Helvetica', 14, 'bold italic'),
                  width=14,
                  height=2,
                  command= infoFrame.destroy)
    back.place(x=1000, y=600)
    infoFrame.place(x=0, y=0)

def reisInfoUtrecht():
    reisInformatie('ut')

def reisInfoAnder():
    code = ''

    reisInformatie(code)

#maakt de string geordend door er spaties tussen te zetten
def makeString(inputString):
    outputString = ''
    for word in inputString.split(';'):
        while len(word) < 27:
            word += ' '
        outputString += word
    return outputString

#stel het TK window in met de goede afmetingen en de buttons en labels van het startscherm
root = Tk()
root.geometry("1280x720")
root.configure(background='yellow')

title = Label(master= root,
              text='Welkom bij NS',
              bg= "yellow",
              fg= "blue",
              font=('Helvetica', 72, 'bold italic'),
              width= 14,
              height= 3)
title.pack()
button01 = Button(master= root,
                  text='Ik wil naar \n Amsterdam',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold italic'),
                  width= 14,
                  height= 2)
button01.place(x=60,y=400)
button02 = Button(master= root,
                  text='Kopen \n los kaartje',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold italic'),
                  width=14,
                  height=2)
button02.place(x=260,y=400)
button03 = Button(master= root,
                  text='Kopen \n OV-Chipkaart',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold italic'),
                  width=14,
                  height=2)
button03.place(x=460,y=400)
button04 = Button(master= root,
                  text='ik wil naar \n het buitenland',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold italic'),
                  width=14,
                  height=2)
button04.place(x=660,y=400)
button05 = Button(master= root,
                  text='Actuele \n reisinformatie',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold italic'),
                  width=14,
                  height=2,
                  command=reisInfoUtrecht)
button05.place(x=860,y=400)
button06 = Button(master= root,
                  text='Reisinformatie \n ander station',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold italic'),
                  width=14,
                  height=2,
                  command=reisInfoAnder)
button06.place(x=1060,y=400)
root.mainloop()