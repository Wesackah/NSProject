from tkinter import *
import requests
import xmltodict

#inloggegevens om bij de NS api te kunnen
inlogGegevens = ('wesackah@gmail.com', 'aw17-v2gaEXQp1zWCvHXPW-M7lmVFrj1wr05rbTgmyPN0PF7-HDsJg')
response = requests.get('http://webservices.ns.nl/ns-api-stations-v2', auth=inlogGegevens)

#zet alle stationsnamen en de bijhoorende codes in een dictionary
stationDict = {}
for station in xmltodict.parse(response.text)['Stations']['Station']:
    stationDict[station['Namen']['Lang']] = station['Code']

#returnt een lijst met alle vertrektijden als strings
def vertrekTijd(code):
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + code
    response = requests.get(api_url, auth=inlogGegevens)
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
        vertrekLijst.append(str)
    return vertrekLijst

def storingen(code):
    api_url = 'http://webservices.ns.nl/ns-api-storingen?station=' + code
    response = requests.get(api_url, auth=inlogGegevens)
    storingXML = xmltodict.parse(response.text)

    if storingXML['Storingen']['Gepland'] != None:
        storingList = ['Geplande Storingen']
        for storing in storingXML['Storingen']['Gepland']['Storing']:
            str = ''
            str += storing['Traject'] + ' '
            str += storing['Periode']
            storingList.append(str)

    # if storingXML['Storingen']['Ongepland'] != None:
    #     storingList.append('Ongeplande Storingen')
    #     for storing in storingXML['Storingen']['Ongepland']['Storing']:
    #         storingList.append(storing['Traject'])

    return storingList

#opent een window met de reisinformatie van het huidige station
def reisInformatie(code):
    infoFrame = Frame(width=1280, height=720, bg="Yellow")
    scrollbar = Scrollbar(master=infoFrame) #scrollbar om door de lijst te kunnen scrollen
    listBox = Listbox(infoFrame, yscrollcommand=scrollbar.set, height= 25,width= 128,font=('Consolas',14),bg='yellow')
    for tijd in vertrekTijd(code): #for loop die de juiste tijden ophaalt via vertrekTijd() en ze daarna in de ListBox zet met de juiste opmaak via makeString()
        listBox.insert(END, makeString(tijd))
    listBox.insert(END,'')
    for storing in storingen(code): #het zelfde voor de storingen
        listBox.insert(END, storing)
    listBox.place(x=0,y=25)
    scrollbar.config(command=listBox.yview)
    scrollbar.place(x=1260, y=25)
    infoLabel = Label(text=makeString('Bestemming;Tijd;Type;Spoor'),font=('Consolas',14,'bold'),bg='yellow',width=108)
    infoLabel.place(x=0,y=0)
    back = Button(master=infoFrame,text='terug', #back button om terug te gaan naar het hoofdmenu
                  bg="Blue",
                  fg="White",
                  activebackground="Blue",
                  activeforeground="White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2,
                  command= infoFrame.destroy)
    back.place(x=1000, y=600)
    infoFrame.place(x=0, y=0)

#roept reisInformatie() aan met de code van Utrecht
def reisInfoUtrecht():
    reisInformatie('ut')

#opent een frame om een stationsnaam in te voeren
def reisInfoAnder():
    #deze functie kijkt of de invoer juist is. zo ja sluit ie zijn eigen frame en roept reisInformatie() aan met de bijhoorende code
    def checkStation():
        found = ''
        for naam in stationDict:
            if naam == textInvoer.get():
                found = naam
                break
        if found == '':
            print('foute invoer')
        else:
            reisInformatie(stationDict[found])
            selectFrame.destroy()

    #maakt het frame aan met de textinvoer en de buttons
    selectFrame = Frame(width=1280, height=720, bg="Yellow")
    textInvoer = Entry(master=selectFrame,font=('Helvetica', 34))
    textInvoer.place(x=300,y=300)
    goButton = Button(master=selectFrame, text='>',
                  bg="Blue",
                  fg="White",
                  activebackground="Blue",
                  activeforeground="White",
                  font=('Helvetica', 19, 'bold'),
                  width=7,
                  height=1,
                  command=checkStation)
    goButton.place(x=800,y=300)
    back = Button(master=selectFrame, text='terug',
                  bg="Blue",
                  fg="White",
                  activebackground="Blue",
                  activeforeground="White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2,
                  command=selectFrame.destroy)
    back.place(x=1000, y=600)
    selectFrame.place(x=0,y=0)

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

#welkom bij NS titel
title = Label(master= root,
              text='Welkom bij NS',
              bg= "yellow",
              fg= "blue",
              font=('Helvetica', 72, 'bold'),
              width= 14,
              height= 3)
title.pack()
#alle buttons die geen functie hebben
button01 = Button(master= root,
                  text='Ik wil naar \n Amsterdam',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold'),
                  width= 14,
                  height= 2)
button01.place(x=60,y=400)
button02 = Button(master= root,
                  text='Kopen \n los kaartje',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2)
button02.place(x=260,y=400)
button03 = Button(master= root,
                  text='Kopen \n OV-Chipkaart',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2)
button03.place(x=460,y=400)
button04 = Button(master= root,
                  text='ik wil naar \n het buitenland',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2)
button04.place(x=660,y=400)

#button om de reisinformatie voor Utrecht te laten zien
button05 = Button(master= root,
                  text='Actuele \n reisinformatie',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2,
                  command=reisInfoUtrecht)
button05.place(x=860,y=400)

#button die een window opent om een Station in te voeren
button06 = Button(master= root,
                  text='Reisinformatie \n ander station',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2,
                  command=reisInfoAnder)
button06.place(x=1060,y=400)

#start de mainloop van TKinter
root.mainloop()