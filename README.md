Read Me NS applicatie

Dit is de Read Me die de opzet van de NS applicatie uitlegt.
Het eerste scherm wat de gebruiker voor zich krijgt is het Startscherm, waarmee de gebruiker verschillende opties krijgt om zijn reis te plannen. Voor cosmetische doeleinden krijgt de gebruiker de optie om direct een kaartje naar Amsterdam te kopen en kan de gebruiker kiezen om een los of OV chipkaart te kopen met aparte knoppen. Tot slot kan de gebruiker een reis plannen naar het buitenland. 
Verder zijn er daadwerkelijke werkende opties om actuele reisinformatie te verkrijgen en de reisinformatie van andere station.

Actuele reisinformatie functie 

Met de optie actuele reisinformatie functie krijgt de gebruiker een nieuw scherm voor zich met de actuele reistijden naar verschillende eindstations. Dit scherm kan worden afgedrukt.
De reis informatie haalt de informatie door middel van het ophalen van een lijst uit de vertrektijden, en zet deze om in TKinter Listbox en print deze op het scherm.

Reisinfo ander station functie

Met de optie reisinfo ander station krijgt de gebruiker een nieuwe scherm voor zich met de reisinformatie van een ander station.
De reisinfo ander station functie haalt de informatie door middel van het ophalen van een lijst uit de vertrektijden, en zet deze om in TKinter Listbox en print deze op het scherm.
Met de back knop kan er worden teruggekeerd naar het startscherm.

Vertrektijd()

De functie Vertrektijd word gebruikt door de reisinformatie functies om de vertrektijden op te halen die relevant zijn de opgevraagde informatie. De vertrektijd functie haalt API data van een NS url. Hij maakt hiervan een string van XML data, plaatst deze in een lijst en geeft de lijst door aan de reisinformatie functie.

Storing()

De functie Storing word gebruikt om aan te geven of er storingen plaatsvinden om de trajecten wanneer er een reis gepland word. De storing functie haalt API data van een NS url om te kijken of er storingen zijn, en zet deze in een string en plaatst deze in een lijst en geeft de lijst door aan de reisinformatie functie.

StationDic()

De functie StationDic word gebruikt om alle stationsnamen uit de NS XML te halen en deze in een dictionary waarbij de lange naam de key is en de code de value.

