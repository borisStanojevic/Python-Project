from devices import *
from formats import *
from transactions import *
from logging import *
import os


#Metod izdavanja uredjaja.
def issueDevice():
	print ("Issuing : \n")
	device_id = input ("Device ID : ").upper()
	while not formatValidID(device_id) or deviceExists(device_id) == False:
		print ("Device ID format not valid or device does not exist.")
		device_id = input ("Device ID : ").upper()

	devices_to_issue = input ("Devices to issue : ")
	while not formatValidAVAILABLE(devices_to_issue):
		print ("Device quantity format not valid.")
		devices_to_issue = input("Devices to issue : ")

	devicesList = getAllDevices()

	#Prolazak kroz listu uredjaja, kad nadjemo onaj za koji smo unijeli ID, promijenimo mu left_available(kolicinu dostupnih uredjaja) i kreiramo transakciju.
	for device in devicesList:
		if device_id == device["ID"]:
			if int(device["AVAILABLE"]) < int(devices_to_issue):
				os.system("cls")
				print ("There are not enough devices to issue.")
			else:
				device["AVAILABLE"] = int(device["AVAILABLE"]) - int(devices_to_issue)
				createTransaction(getTransactionID(),device_id,devices_to_issue,"ISSUED",getActiveStorekeeper())

	#Prolazak kroz listu kojoj smo prethodno jednom uredjaju promijenili left_available i re-write-ovanje novog stanja u fajl.
	with open ("devices.txt","w") as devicesFile:
		for device in devicesList:
			delimiter = "|"
			devicesFile.write(device["ID"] + delimiter 
			+ device["NAME"] + delimiter 
			+ device["MANUFACTURER"] + delimiter 
			+ device["DESCRIPTION"] + delimiter 
			+ str(device["AVAILABLE"]) + "\n")
