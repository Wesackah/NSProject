import requests
import xmltodict

auth_details = ('wesackah@gmail.com', 'aw17-v2gaEXQp1zWCvHXPW-M7lmVFrj1wr05rbTgmyPN0PF7-HDsJg')

def vertrekTijd():
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)
    vertreklijst = []
    print('Dit zijn de vertrekkende treinen:')
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        str = ''
        str += vertrek['EindBestemming'] + ' '
        # str += vertrek['VertrekVertragingTekst'] + ' '
        vertrektijd = vertrek['VertrekTijd'] + ' ' # 2016-09-27T18:36:00+0200
        str += vertrektijd[11:16] + ' ' # 18:36
        str += vertrek['TreinSoort'] + ' '
        spoor = vertrek['VertrekSpoor']
        str += spoor['@wijziging'] + ' '
        str += spoor['#text']
        vertreklijst.append(str)
    print(vertreklijst)
    # print(vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein'])

def Storing():
    api_url = 'http://webservices.ns.nl/ns-api-storingen?station=ut'
    response = requests.get(api_url, auth=auth_details)
    storingXML = xmltodict.parse(response.text)
    storingOngeplandlst = []
    storingGeplandlst = []
    for storing in storingXML['Storingen']['Gepland']['Storing']:
        str = ''
        str += storing['Traject']
        str += storing['Periode']
        storingGeplandlst.append(str)

    if storingXML['Storingen']['Ongepland'] != None:
        for storing in storingXML['Storingen']['Ongepland']['Storing']:
            str = ''
            str += storing['Traject']
            str += storing['Periode']
            storingOngeplandlst.append(str)


    print(storingGeplandlst)
    print(storingOngeplandlst)


vertrekTijd()