from tkinter import *

#opent een window met de reisinformatie van het huidige station
def reisinformatie():
    infoframe = Frame(width=1280, height=720, bg="Yellow")
    scrollbar = Scrollbar(master=infoframe)
    listbox = Listbox(infoframe, yscrollcommand=scrollbar.set, height= 25,width= 114,font=('Helvetica',14),bg='yellow')
    for line in range(100):
        listbox.insert(END, "This is line number " + str(line))
    listbox.place(x=0,y=0)
    scrollbar.config(command=listbox.yview)
    scrollbar.place(x=1260, y=0)

    back = Button(master=infoframe,
                  text='terug',
                  bg="Blue",
                  fg="White",
                  activebackground="Blue",
                  activeforeground="White",
                  font=('Helvetica', 14, 'bold italic'),
                  width=14,
                  height=2,
                  command= infoframe.destroy)
    back.place(x=1000, y=600)
    infoframe.place(x=0, y=0)


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
                  command=reisinformatie)
button05.place(x=860,y=400)
button06 = Button(master= root,
                  text='Reisinformatie \n ander station',
                  bg="Blue",
                  fg= "White",
                  activebackground= "Blue",
                  activeforeground= "White",
                  font=('Helvetica', 14, 'bold italic'),
                  width=14,
                  height=2)
button06.place(x=1060,y=400)
root.mainloop()