from transactions import *
from datetime import *
from formats import *
from storekeepers import *

#Transakcije izvrsene za dati uredjaj u datom vremenskom opsegu.
#Od korisnika trazimo unos i ako je u validnom formatu, iz unosa parsiramo datum u formatu 'dan-mjesec-godina'.
#Prolazimo kroz listu transakcija, iz svake linije uzimamo i parsiramo datum.
#Ako je taj datum u zadatom opsegu, 'kacimo' ga u filteredListu-u...
def printTransactionsReport():
    transactionsList = getTransactions()
    filteredList = []

    #Prvo provjeravamo validnost inputa datuma i trazimo unos sve dok ne unesemo ispravno.
    #Potom moramo iz unosa (koji je string) da parsiramo datum, da bismo dobili date objekat, koji cemo moci porediti sa <,> da vidimo je li datum u opsegu.
    date_start = input("Date range start : ")
    while not formatValidDATE(date_start):
        print ("Invalid date format.")
        date_start = input("Date range start : ")
    date_start = datetime.strptime(date_start,"%d-%m-%Y")

    date_end = input("Date range end : ")
    while not formatValidDATE(date_end):
        print ("Invalid date format")
        date_end = input("Date range end : ")
    date_end = datetime.strptime(date_end,"%d-%m-%Y")

    print()
    
    for transaction in transactionsList:
        transactionDate = datetime.strptime(transaction.split("|")[4],"%d-%m-%Y")
        if date_start <= transactionDate <= date_end:
            filteredList.append(transaction)
    printTransactionHeader()
    if len(filteredList) == 0:
        print ("There are no transactions in desired date range.")
    else:
        for transaction in filteredList:
            print (formatTransactionID(transaction.split("|")[0])
            + formatDeviceID(transaction.split("|")[1])
            + formatTransactionQUANTITY(transaction.split("|")[2])
            + formatTransactionTYPE(transaction.split("|")[3])
            + formatTransactionDATE(transaction.split("|")[4])
            + formatSTOREKEEPER(transaction.split("|")[5].rstrip("\n"))
            )


#Print svih transakcija odredjenog uredjaja u datom vremenskom opsegu.
def printTransactionsReport_2(device_id):
    device_id = device_id.upper()
    while not formatValidID(device_id):
        print("Device ID format not valid.")
        device_id = input ("Device ID : ").upper()
    transactionsList = getTransactions()
    filteredList = []

    date_start = input("Date range start : ")
    while not formatValidDATE(date_start):
        print ("Invalid date format.")
        date_start = input("Date range start : ")
    date_start = datetime.strptime(date_start,"%d-%m-%Y")
    
    date_end = input("Date range end : ")
    while not formatValidDATE(date_end):
        print ("Invalid date format.")
        date_start = input("Date range end : ")
    date_end = datetime.strptime(date_end,"%d-%m-%Y")

    print()

    for transaction in transactionsList:
        transactionDate = datetime.strptime(transaction.split("|")[4],"%d-%m-%Y")
        if date_start <= transactionDate <= date_end and device_id == transaction.split("|")[1]:
            filteredList.append(transaction)

    printTransactionHeader()
    if len(filteredList) == 0:
        print ("There are no transactions for desired device in desired date range.")
    else:
        for transaction in filteredList:
            print (formatTransactionID(transaction.split("|")[0])
            + formatDeviceID(transaction.split("|")[1])
            + formatTransactionQUANTITY(transaction.split("|")[2])
            + formatTransactionTYPE(transaction.split("|")[3])
            + formatTransactionDATE(transaction.split("|")[4])
            + formatSTOREKEEPER(transaction.split("|")[5].rstrip("\n"))
            )

#Print svih transakcija koje je napravio odredjeni magacioner u datom vremenskom opsegu.
def printTransactionsReport_3(storekeeper_username):
    transactionsList = getTransactions()
    filteredList = []
    storekeepersList = getStorekeepers()

    date_start = input("Date range start : ")
    while not formatValidDATE(date_start):
        print ("Invalid date format.")
        date_start = input("Date range start : ")
    date_start = datetime.strptime(date_start,"%d-%m-%Y")
    
    date_end = input("Date range end : ")
    while not formatValidDATE(date_end):
        print ("Invalid date format.")
        date_start = input("Date range end : ")
    date_end = datetime.strptime(date_end,"%d-%m-%Y")

    print()

    for transaction in transactionsList:
        transactionDate = datetime.strptime(transaction.split("|")[4],"%d-%m-%Y")
        if date_start <= transactionDate <= date_end and storekeeper_username in storekeepersList:
            filteredList.append(transaction)

    printTransactionHeader()
    if len(filteredList) == 0:
        print ("There are no transactions for desired device in desired date range.")
    else:
        for transaction in filteredList:
            print (formatTransactionID(transaction.split("|")[0])
            + formatDeviceID(transaction.split("|")[1])
            + formatTransactionQUANTITY(transaction.split("|")[2])
            + formatTransactionTYPE(transaction.split("|")[3])
            + formatTransactionDATE(transaction.split("|")[4])
            + formatSTOREKEEPER(transaction.split("|")[5].rstrip("\n"))
            )
