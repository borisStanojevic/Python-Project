from datetime import date

#Vraca listu svih transakcija koje se nalaze u transactions.txt fajlu.
def getTransactions() -> list:
    transactionsList = []
    with open ("transactions.txt","r") as transactionsFile:
        transactionsList = transactionsFile.readlines()
    return transactionsList


#Vraca broj koji predstavlja ID transakcije.
#Vraca 1 ako nema transakcija,tj. ako je fajl prazan.Vraca ID poslednje transakcije + 1 u slucaju da ima prethodnih transakcija.
def getTransactionID() -> int:
    transactionsList = getTransactions()
    last_transaction_id = 0
    
    if len(transactionsList) == 0:
        return last_transaction_id + 1
    else:
        last_transaction_id = transactionsList[len(transactionsList)-1].split("|")[0] 
        return int(last_transaction_id) + 1


#Kreira transakciju. Kao parametre proslijedjujemo ID transakcije(getTransactionID(), ID uredjaja, kolicinu prometa(koliko smo uredjaja dodali ili izdali),
#,tip transakcije(DODATO,IZDATO) i korisnicko ime magacionera.
def createTransaction(transaction_id,device_id,transaction_quantity,transaction_type,storekeeper_username):
    transaction_date = date.today().strftime("%d-%m-%Y")
    with open("transactions.txt","a") as transactionsFile:
        delimiter = "|"
        transactionsFile.write(str(transaction_id) + delimiter 
        + device_id + delimiter 
        + str(transaction_quantity) + delimiter 
        + transaction_type + delimiter 
        + transaction_date + delimiter 
        + storekeeper_username + "\n" )




