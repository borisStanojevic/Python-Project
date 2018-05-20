from formats import *
import os

#Logika za prijavu. Provjerava da li se uneseni username/password poklapa sa nekim username/passwordom u storekeepers.txt fajlu.
#Vraca True ako nadje poklapanje,False ako ne.
def storekeeperExists() -> bool:
	storekeeper_exists = False
	storekeepersList = []
	with open("storekeepers.txt","r") as storekeepersFile:
		storekeepersList = storekeepersFile.readlines()
	username = input ("Username : ")
	password = input ("Password : ")
	for storekeeper in storekeepersList:
		if username == storekeeper.split("|")[0] and password == storekeeper.split("|")[1]:
			storekeeper_exists = True
			#Ako program pronadje magacionera, uzimamo korisnicko ime magacionera i upisujemo ga u active.txt fajl.
			#Na taj nacin sistem "pamti" koji je trenutno logovani magacioner.
			storekeeper_username = storekeeper.split("|")[0]
			with open ("active.txt","w") as activeStorekeeper:
				activeStorekeeper.write(storekeeper_username)
			os.system("cls")
			print ("Login successful.")
			print ("Welcome {0} {1}.".format(storekeeper.split("|")[2].capitalize(),storekeeper.split("|")[3].rstrip("\n").capitalize()))
			break
	return storekeeper_exists


#Ova metoda vraca listu magacionera(korisnickih imena).
def getStorekeepers() -> list:
    storekeepersList = []
    with open("storekeepers.txt","r") as storekeepersFile:
        storekeeperLine = storekeepersFile.readline()
        while storekeeperLine != "":
            storekeepersList.append(storekeeperLine.split("|")[0])
            storekeeperLine = storekeepersFile.readline()
    return storekeepersList


def printStorekeepers():
    storekeepersList = getStorekeepers()
    printStorekeeperHeader()
    with open("storekeepers.txt","r") as storekeepersFile:
        storekeeperLine = storekeepersFile.readline()
        while storekeeperLine != "":
            print (formatStorekeeperUSERNAME(storekeeperLine.split("|")[0])
            + formatStorekeeperNAME(storekeeperLine.split("|")[2])
            + formatStorekeeperLASTNAME(storekeeperLine.split("|")[3].rstrip("\n"))
            )
            storekeeperLine = storekeepersFile.readline()



#Metoda vraca trenutno aktivnog magacionera citajuci prethodno upisano magacionerovo korisnicko ime u active.txt fajl. 
def getActiveStorekeeper() -> str:
	with open ("active.txt","r") as activeStorekeeper:
		return activeStorekeeper.readline().rstrip("\n")


