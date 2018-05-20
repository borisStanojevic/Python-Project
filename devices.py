from formats import *
from transactions import *
import os

#Vraca listu svih uredjaja cija je kolicina veca od nule.
def getAvailableDevices() -> list:
	devicesList = []
	with open("devices.txt","r") as devicesFile:
		line = devicesFile.readline()
		while line != "":
			lineElements = line.split("|")
			if int(lineElements[4].rstrip("\n")) > 0:
				device = {"ID":lineElements[0],
				"NAME":lineElements[1],
				"MANUFACTURER":lineElements[2],
				"DESCRIPTION":lineElements[3],
				"AVAILABLE":lineElements[4].rstrip("\n")}
				devicesList.append(device)
			line = devicesFile.readline()
	return devicesList


"""U zavisnosti od parametra, prikazuje listu SVIH uredjaja ili samo onih sa kolicinom vecom od 0.
Ako proslijedimo getDevices() metodu kao parametar,vratice listu uredjaja sa kolicinom vecom od nule.
Ako proslijedimo getAllDevices() metodu kao parametar,vratice listu svih uredjaja."""
def showDevices(devicesList):
	printHeader()
	for device in devicesList:
		print (formatID(device["ID"])
		+formatNAME(device["NAME"])
		+formatMANUFACTURER(device["MANUFACTURER"])
		+formatDESCRIPTION(device["DESCRIPTION"])
		+formatAVAILABLE(device["AVAILABLE"]))
			

#Vraca listu SVIH uredjaja, ukljucujuci one cija je kolicina 0.
def getAllDevices() -> list:
	devicesList = []
	with open("devices.txt","r") as devicesFile:
		line = devicesFile.readline()
		while line != "":
			lineElements = line.split("|")	
			device = {"ID":lineElements[0],
			"NAME":lineElements[1],
			"MANUFACTURER":lineElements[2],
			"DESCRIPTION":lineElements[3],
			"AVAILABLE":lineElements[4].rstrip("\n")}
			devicesList.append(device)
			line = devicesFile.readline()
	return devicesList


#Sortira uredjaje po odredjenom kljucu(parametar) i printa sortiranu listu.
def sortDevices(key):
	sortedList = sorted(getAvailableDevices(), key = lambda device: device[key])
	printHeader()
	for device in sortedList:
		print (formatID(device["ID"]) 
		+ formatNAME(device["NAME"]) 
		+ formatMANUFACTURER(device["MANUFACTURER"]) 
		+ formatDESCRIPTION(device["DESCRIPTION"]) 
		+ formatAVAILABLE(device["AVAILABLE"]))


#Trazi uredjaje (ukljucujuci one sa kolicinom 0), po odredjenom kljucu(parametar) i kljucnoj rijeci koju korisnik unese.
#Za lakse pronalazenje uredjaja, input i vrijednost pod kljucem koji proslijedimo kao parametar konvertujemo u mala slova.
def searchDevices(key):
	devicesList = getAllDevices()
	keyword = input("Keyword or a phrase : ").lower()
	if keyword == "":
		print ("Invalid input.")
		keyword = input ("Keyword or a phrase : ").lower
	devices_found = 0
	os.system("cls")
	printHeader()
	for device in devicesList:
		if keyword in device[key].lower():
			print (formatID(device["ID"]) 
			+ formatNAME(device["NAME"]) 
			+ formatMANUFACTURER(device["MANUFACTURER"]) 
			+ formatDESCRIPTION(device["DESCRIPTION"]) 
			+ formatAVAILABLE(device["AVAILABLE"]))
			devices_found += 1
	if devices_found == 0:
		print ("No devices found.\n")


#Provjerava da li uredjaj sa odredjenim ID-om postoji. Vraca True ako postoji, False ako ne.
def deviceExists(device_id) -> bool:
	device_exists = False
	devicesList = getAllDevices()
	for device in devicesList:
		if device_id == device["ID"]:
			device_exists = True
			break
	return device_exists

