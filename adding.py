from devices import *
from formats import *
from transactions import *
from logging import *
from storekeepers import *


"""Metod dodaje uredjaje u sistem.
Posle svakog inputa provjerava je li validan format inputa. Ako nije trazi input ponovo."""
def addDevice():
	print ("Adding  : \n")

	#Provjeravamo i zahtijevamo ispravan format ID-a.
	device_id = input ("ID : ").upper()
	while not formatValidID(device_id):
		print ("Device ID format not valid.")
		device_id = input ("ID : ").upper()

	#Kad dobijemo ID ispravnog formata, provjeravamo da li uredjaj sa tim ID-om postoji.
	#Ako postoji trazimo unos za koliko zelimo da povecamo kolicinu uredjaja na stanju i rewrite-ujemo fajl sa novim stanjem.
	#Ako ne postoji idemo na else blok.
	if deviceExists(device_id):
		print ("\nAdding existing device : ")
		devices_to_add = input ("\nDevices to add : ")
		while not formatValidAVAILABLE(devices_to_add):
			print ("Device quantity format not valid.")
			devices_to_add = input ("Devices to add : ")
		
		devicesList = getAllDevices()

		for device in devicesList:
			if device_id == device["ID"]:
				device["AVAILABLE"] = int (device["AVAILABLE"]) + int(devices_to_add)
				#Pozivamo metod za kreiranje transakcije i proslijedjujemo mu ID transakcije, ID uredjaja, kolicinu transakcije, tip i korisnika.
				createTransaction(getTransactionID(),device_id,devices_to_add,"ADDED",getActiveStorekeeper())

		with open ("devices.txt","w") as devicesFile:
			for device in devicesList:
				delimiter = "|"
				devicesFile.write(device["ID"] + delimiter 
				+ device["NAME"] + delimiter 
				+ device["MANUFACTURER"] + delimiter 
				+ device["DESCRIPTION"] + delimiter 
				+ str(device["AVAILABLE"]) + "\n")

	#Ako uredjaj sa datim ID-om ne postoji, zahtijevamo unose imena,proizvodjaca,opisa i kolicine uredjaja u ispravnom formatu.
	#Nakon unosa svega navedenog, dodajemo uredjaj u fajl.
	else:
		print ("\nAdding new device.\n")
		name = input ("NAME : ").lower().title()
		while not formatValidNAME(name):
			print ("Device name format not valid.")
			name = input ("NAME : ").lower().title()

		manufacturer = input ("MANUFACTURER : ").lower().title()
		while not formatValidMANUFACTURER(manufacturer):
			print ("Device manufacturer format not valid.")
			manufacturer = input ("MANUFACTURER : ").lower().title()

		description = input ("DESCRIPTION : ").lower().capitalize()
		while not formatValidDESCRIPTION(description):
			print ("Device description format not valid.")
			description = input ("DESCRIPTION : ").lower().capitalize()

		left_available = input ("AVAILABLE : ")
		while not formatValidAVAILABLE(left_available):
			print ("Device quantity format not valid.")
			left_available = input ("AVAILABLE : ")
		
		device = {"ID":device_id,"NAME":name,"MANUFACTURER":manufacturer,"DESCRIPTION":description,"AVAILABLE":left_available}
	
		with open("devices.txt","a") as devicesFile:
			delimiter = "|"
			devicesFile.write(device["ID"] + delimiter 
			+ device["NAME"] + delimiter 
			+ device["MANUFACTURER"] + delimiter 
			+ device["DESCRIPTION"] + delimiter 
			+ str(device["AVAILABLE"]) + "\n")

		createTransaction(getTransactionID(),device_id,left_available,"ADDED",getActiveStorekeeper())

