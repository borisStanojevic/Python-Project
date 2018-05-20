import re


def printLoginHeader():
    print ("#================================#".center(108))
    print ("|    Login (Case sensitive)      |".center(108))
    print (" #================================#\n".center(108))

def printMenu():
    print ()
    print ("MAIN MENU".center(108))
    print ("#===========================#".center(108))
    print ("| 1) Show available devices |".center(108))
    print ("| 2) Search devices         |".center(108))
    print ("| 3) Issue devices          |".center(108))
    print ("| 4) Add devices            |".center(108))
    print ("| 5) Show report            |".center(108))
    print ("| X) Quit                   |".center(108))
    print ("#===========================#".center(108))

def printSortMenu():
    print ()
    print ("#=========================#")
    print ("| 1) Sort by ID           |")
    print ("| 2) Sort by NAME         |")
    print ("| 3) Sort by MANUFACTURER |")
    print ("#=========================#")
    
def printSearchMenu():
    print ()
    print ("#===========================#")
    print ("| 1) Search by ID           |")
    print ("| 2) Search by NAME         |")
    print ("| 3) Search by MANUFACTURER |")
    print ("#===========================#")

def printReportsMenu():
    print()
    print ("#==============================================#")
    print ("| 1) Transactions in date range                |")
    print ("| 2) Transactions in date range/for device     |")
    print ("| 3) Transactions in date range/by storekeeper |")
    print ("#==============================================#")

def printHeader():
    print()
    print ("ID".ljust(5),end="\t")
    print ("NAME".ljust(20),end="\t")
    print ("MANUFACTURER".ljust(20),end="\t")
    print ("DESCRIPTION".ljust(30),end="\t")
    print ("AVAILABLE".rjust(9))
    print ("-------------------------------------------------------------------------------------------------")

def printTransactionHeader():
    print()
    print ("ID".ljust(5),end = "\t")
    print ("DEVICE ID".ljust(8),end = "\t")
    print ("QUANTITY".ljust(8),end = "\t")
    print ("TYPE".ljust(6),end = "\t")
    print ("DATE".ljust(10),end = "\t")
    print ("STOREKEEPER".rjust(20))
    print ("------------------------------------------------------------------------------------")

def printStorekeeperHeader():
    print()
    print ("USERNAME".ljust(30) + "\t" + "NAME".ljust(20) + "\t" + "LAST NAME".ljust(20))
    print ("-----------------------------------------------------------------")


def formatStorekeeperUSERNAME(storekeeper_username) -> str:
    if len(storekeeper_username) > 30:
        return (storekeeper_username[:27] + "...").ljust(30) + "\t"
    else:
        return storekeeper_username.ljust(30) + "\t"

def formatStorekeeperNAME(storekeeper_name) -> str:
    if len(storekeeper_name) > 20:
        return (storekeeper_name[:17] + "...").ljust(20) + "\t"
    else:
        return storekeeper_name.ljust(20) + "\t"

def formatStorekeeperLASTNAME(storekeeper_lastname) -> str:
    if len(storekeeper_lastname) > 20:
        return (storekeeper_lastname[:17] + "...").ljust(20) + "\t"
    else:
        return storekeeper_lastname.ljust(20) + "\t"

def formatTransactionID(transaction_id) -> str:
    return transaction_id.ljust(5) + "\t"

def formatDeviceID(device_id) -> str:
    return device_id.rjust(8) + "\t"

def formatTransactionQUANTITY(transaction_quantity) -> str:
    return transaction_quantity.rjust(8) + "\t"

def formatTransactionTYPE(transaction_type) -> str:
    return transaction_type.ljust(6) + "\t"

def formatTransactionDATE(transaction_date) -> str:
    return transaction_date.ljust(10) + "\t"

def formatSTOREKEEPER(storekeeper_username) -> str:
    if len(storekeeper_username) > 20:
        return (storekeeper_username[:17] + "...").rjust(20) + "\t"
    else:
        return (storekeeper_username.rjust(20) + "\t")

def formatID(device_id) -> str:
    return device_id.ljust(5) + "\t"

def formatNAME(name) -> str:
	if len(name)>20:
		return (name[:17] + "...").ljust(20) + "\t"
	else:
		return name.ljust(20) + "\t"

def formatMANUFACTURER(manufacturer) -> str:
	if len(manufacturer)>20:
		return (manufacturer[:17] + "...").ljust(20) + "\t"
	else:
		return manufacturer.ljust(20) + "\t"

def formatDESCRIPTION(description) -> str:
    if len(description) > 30:
        return (description[:27]+"...").ljust(30) + "\t"
    else:
        return description.ljust(30) + "\t"

def formatAVAILABLE(left_available) -> str:
    return str(left_available).rstrip("\n").rjust(9)

#Provjerava validnost formata.
#Format ID-a uredjaja treba da je : 2 slova potom 3 cifre.
def formatValidID(device_id) -> bool:
    is_valid = False
    id_pattern = re.compile("^[A-Z]{2}[0-9]{3}$")
    if re.fullmatch(id_pattern,device_id):
        is_valid = True
    return is_valid

#Provjerava validnost formata imena. Nema posebnih zahtjeva, samo da je unos manji ili jednak 25 i veci od 5 karaktera.
#Isto vrijedi i za proizvodjaca.
def formatValidNAME(name) -> bool:
    is_valid = False
    if len(name) <= 25 and name != "":
        is_valid = True
    return is_valid


def formatValidMANUFACTURER(manufacturer) -> bool:
    is_valid = False
    if len(manufacturer) <= 25 and manufacturer != "":
        is_valid = True
    return is_valid

#Isto kao i ime i proizvodjac samo unos mora biti manji ili jednak 50 karaktera.
def formatValidDESCRIPTION(description) -> bool:
    is_valid = False
    if len(description) <= 50 and len(description) > 10:
        is_valid = True
    return is_valid

#Provjerava je li unijeta kolicina ispravnog formata. Kolicina treba da je najvise trocifren pozitivan broj razlicit od nule.
def formatValidAVAILABLE(left_available) -> bool:
    is_valid = False
    left_available_pattern = re.compile("^[1-9]\d{,3}$")
    if re.fullmatch(left_available_pattern,left_available):
        is_valid = True
    return is_valid

#Provjerava je li unijeti datum u ispravnom formatu, 'dan-mjesec-godina'
def formatValidDATE(date) -> bool:
    is_valid = False
    date_pattern = re.compile("^(0?[1-9]|[12][0-9]|3[01])\-(0?[1-9]|1[012])\-\d{4}$")
    if re.fullmatch(date_pattern,date):
        is_valid = True
    return is_valid

