from logging import *
from devices import *
from adding import *
from issuing import *
from formats import *
from reports import *
import os


def menuInteract():
	#Ako logIn() uspije(vrati True) printamo meni i trazimo unos komande.
	#Sve dok komanda nije 1,2,3,4,5, ili x ponovo trazimo unos iste.
	os.system("cls")
	if logIn():
		printMenu()
		command = input ("\nChoose option : ").upper()
		while command not in ("1","2","3","4","5","X"):
			os.system("cls")
			print ("Invalid option.")
			printMenu()
			command = input ("\nChoose option : ").upper()

		#U trenutku kad je komanda validna I NIJE X izvrsavamo logiku za odabir i izvrsavanje opcija.	
		while command != "X": 

			if command == "1":
				os.system("cls")
				printSortMenu()
				command = input ("\nChoose option : ").upper()
				while command not in ("1","2","3","X"):
					os.system("cls")
					print("Invalid option.")
					printSortMenu()
					command = input ("\nChoose option : ").upper()
				while command != "X":
					if command == "1":
						os.system("cls")
						sortDevices("ID")
						print()
						break
					elif command == "2":
						os.system("cls")
						sortDevices("NAME")
						print()
						break
					elif command == "3":
						os.system("cls")
						sortDevices("MANUFACTURER")
						print()
						break
				if command == "X":
					os.system("cls")
					

			elif command == "2":
				os.system("cls")
				printSearchMenu()
				command = input ("\nChoose option : ").upper()
				while command not in ("1","2","3","X"):
					os.system("cls")
					print ("Invalid option.")
					printSearchMenu()
					command = input ("\nChoose option : ").upper()
				while command != "X":
					if command == "1":
						os.system("cls")
						searchDevices("ID")
						print()
						break
					elif command == "2":
						os.system("cls")
						searchDevices("NAME")
						print()
						break
					elif command == "3":
						os.system("cls")
						searchDevices("MANUFACTURER")
						print()
						break
				if command == "X":
					os.system("cls")
				

			elif command == "3":
				os.system("cls")
				issueDevice()
				os.system("cls")
				

			elif command == "4":
				os.system("cls")
				addDevice()
				os.system("cls")

			elif command == "5":
				os.system("cls")
				printReportsMenu()
				command = input ("\nChoose option : ").upper()
				while command not in ("1","2","3","X"):
					os.system("cls")
					print ("Invalid option.\n")
					printReportsMenu()
					command = input ("\nChoose option : ").upper()
				while command != "X":
					if command == "1":
						os.system("cls")
						printTransactionsReport()
						print ()
						break
					elif command == "2":
						os.system("cls")
						printTransactionsReport_2(input("Device ID : "))
						print ()
						break
					elif command == "3":
						os.system("cls")
						printTransactionsReport_3(input("Storekeeper USERNAME : "))
						print ()
						break
						
				if command == "X":
					os.system("cls")
					
			printMenu()
			command = input ("\nChoose option : ").upper()
					
		os.system("cls")
		print ("Goodbye!")


menuInteract()
