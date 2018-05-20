from storekeepers import *
from formats import printLoginHeader

#Preko ove metode pokusavamo da se logujemo,kroz tri pokusaja, pozivajuci i provjeravajuci storekeeperExists() metodu.
#U trenutku kad storekeeperExists() vrati True, onda se mijenja logged_in u True i vraca se ta vrijednost.(Logovanje je uspjesno.)
def logIn() -> bool:
	logged_in = False
	login_attempt = 0
	printLoginHeader()
	while login_attempt < 3:
		if storekeeperExists() :
			logged_in = True
			break
		print ("\nIncorrect username/password.\n")
		login_attempt += 1
	return logged_in
