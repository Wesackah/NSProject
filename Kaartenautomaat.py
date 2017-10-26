from tkinter import *
import requests
import xmltodict

#returnt een lijst met alle vertrektijden als strings
def vertrekTijd(code):
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + code
    response = requests.get(api_url, auth=inlogGegevens)
    vertrekXML = xmltodict.parse(response.text)
    vertrekList = []
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        str = vertrek['EindBestemming'] + ';'
        str += vertrek['VertrekTijd'][11:16] + ';'
        str += vertrek['TreinSoort'] + ';'
        #er is niet altijd een spoor bekend bij het XML bestand van de NS. daarom gebruiken we hier een try/except
        try:
            str += vertrek['VertrekSpoor']['#text']
        except:
            str += 'onbekend'
        vertrekList.append(str)
    return vertrekList

#returnt een lijst met alle vertrektijden als strings
def storingen(code):
    api_url = 'http://webservices.ns.nl/ns-api-storingen?station=' + code
    response = requests.get(api_url, auth=inlogGegevens)
    storingXML = xmltodict.parse(response.text)
    storingList = []
    if storingXML['Storingen']['Gepland'] != None:
        storingList.append('Geplande storingen')
        for storing in storingXML['Storingen']['Gepland']['Storing']:
            storingList.append(storing['Traject'] + ' ' + storing['Periode'])

    if storingXML['Storingen']['Ongepland'] != None:
        storingList.append('')
        storingList.append('Ongeplande storingen')
        if type(storingXML['Storingen']['Ongepland']['Storing']) == list:
            x = storingXML['Storingen']['Ongepland']['Storing'][0]
            storingList.append(x['Traject'] + ' ' + x['Reden'])
        else:
            x = storingXML['Storingen']['Ongepland']['Storing']
            storingList.append(x['Traject'] + ' ' + x['Reden'])

    return storingList

#opent een window met de reisinformatie van het huidige station
def reisInformatie(code):
    infoFrame = Frame(width=1280,
                      height=720,
                      bg="Yellow")
    listBox = Listbox(infoFrame,
                      height= 25,
                      width= 128,
                      font=('Consolas',14),
                      bg='yellow')
    # for loop die de juiste tijden ophaalt via vertrekTijd() en ze daarna in de ListBox zet met de juiste opmaak via makeString()
    for tijd in vertrekTijd(code):
        listBox.insert(END, makeString(tijd))
    listBox.insert(END,'')
    # het zelfde voor de storingen
    for storing in storingen(code):
        listBox.insert(END, storing)
    listBox.place(x=0,y=25)
    infoLabel = Label(master= infoFrame,
                      text=makeString('Bestemming;Tijd;Type;Spoor'),
                      font=('Consolas',14,'bold'),
                      bg='yellow',
                      width=108)
    infoLabel.place(x=0,y=0)
    # back button om terug te gaan naar het hoofdmenu
    back = Button(master=infoFrame,
                  text='terug',
                  bg="Blue",
                  fg="White",
                  activebackground="Blue",
                  activeforeground="White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2,
                  command= infoFrame.destroy)
    back.place(x=1000, y=610)
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
            melding = Label(master=selectFrame,
                            text='geen geldig station, bedoelde je:',
                            bg="yellow",
                            fg="red",
                            font=('Helvetica', 20),
                            width=30,
                            height=1)
            melding.place(x=50,y=110)
            listBox = Listbox(master=selectFrame,
                              height=10,
                              width=30,
                              selectborderwidth= 0,
                              fg= 'red',
                              font=('Helvetica', 20),
                              bg='yellow')
            for naam in stationDict:
                if textInvoer.get() in naam:
                    listBox.insert(END,naam)
            listBox.place(x=500,y=110)
        else:
            reisInformatie(stationDict[found])
            selectFrame.destroy()

    #maakt het frame aan met de textinvoer en de buttons
    selectFrame = Frame(width=1280,
                        height=720,
                        bg="Yellow")
    textInvoer = Entry(master=selectFrame,
                       font=('Helvetica', 34))
    textInvoer.place(x=50,y=50)
    goButton = Button(master=selectFrame, text='>',
                  bg="Blue",
                  fg="White",
                  activebackground="Blue",
                  activeforeground="White",
                  font=('Helvetica', 19, 'bold'),
                  width=7,
                  height=1,
                  command=checkStation)
    goButton.place(x=550,y=50)
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


#inloggegevens om bij de NS api te kunnen
inlogGegevens = ('wesackah@gmail.com', 'aw17-v2gaEXQp1zWCvHXPW-M7lmVFrj1wr05rbTgmyPN0PF7-HDsJg')
response = requests.get('http://webservices.ns.nl/ns-api-stations-v2', auth=inlogGegevens)

#zet alle stationsnamen en de bijhoorende codes in een dictionary
stationDict = {}
for station in xmltodict.parse(response.text)['Stations']['Station']:
    stationDict[station['Namen']['Lang']] = station['Code']

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
                  text='Ik wil naar \nAmsterdam',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold'),
                  width= 14,
                  height= 2)
button01.place(x=60,y=400)
button02 = Button(master= root,
                  text='Kopen \nlos kaartje',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2)
button02.place(x=260,y=400)
button03 = Button(master= root,
                  text='Kopen \nOV-Chipkaart',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold'),
                  width=14,
                  height=2)
button03.place(x=460,y=400)
button04 = Button(master= root,
                  text='ik wil naar \nhet buitenland',
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
                  text='Reisinformatie \nUtrecht',
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
                  text='Reisinformatie \nander station',
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