# licencjat

�cie�ki plik�w znajduj� si� w pliku "paths.py"

dane wej�ciowe:
plik powinien znajdowa� si� w tym samym folderze co programy
plik "test.txt" z s�owami do przetestowania, po jednym w jednej linii

dane wyj�ciowe:
plik "result.txt" z s�owami zbilanoswanymi, po jednym w jednej linii
plik powinien znajdowa� si� w tym samym folderze co programy

Opis dzia�ania main.py
1.start
2.wczytujemy wszytkie s�owa z pliku
3.dla s�ow z pliku
	3.1 sprawdzamy czy jest zbilanoswane
		je�li tak to zapisujemy je w pliku z wynikiem
4.koniec

Opis dzia�ania if_balanced.py
1. start
2. dla wszystkich liter w s�ownie
	2.1 sprawdzamy czy litera znajduje si� ju� w s�owniku ilosci wystepowania litery
		Je�li nie to dodajemy j� i ustawiamy jej ilo�� na zero
3. Dla d�ugo�ci od 2 do d�ugo�ci s�owa-1
	3.1. Tworzymy s�ownik liter wyst�puj�cych w s�owie ustawiaj�c min ilo�� wyst�powania
	na  d�ugo�� s�woa i max ilo�� wyst�powania na zero
	3.2 Dla wszytkich mo�liwych indeks�w rozpoczynaj�cych pod�owo o danej d�ugo�ci(iteruj�c od zera)
		3.2.1 zerujemy s�ownik liter, kt�ry zawiera ilo�� wyst�pie� danej litery
		3.2.2 dla wszystkich liter ze s�owa od litery zaczynaj�cej podci�g do indeksu+d�ugo�� s�owa
			3.2.2.1 Dodajemy dodajemy 1 do ilo�ci wyst�powania litery jak na ni� trafimy
		3.2.3 dla liter wyst�puj�cych w s�owie:
			3.2.3.1 sprawdzamy czy ilo�� jej wyst�powania jest wi�ksza ni� obecne maksimum wyst�powania:
				je�li tak to nowe maximum to ilo�� wtst�powania
			3.2.3.2 sprawdzamy czy ilo�� jej wyst�powania jest mniejsza ni� obecne minimum wyst�powania:
				je�li tak to nowe minimum to ilo�� wtst�powania
	3.3 Dla wszystkich liter w s�owie sprawdzamy czy ich max-min wyst�powania jest wi�ksze ni� 1
		je�li tak ko�czymy przeszukiwa� s�owo, zwracamy informacj� i� s�owo nie jest zbilansowane
4. zwracamy informacj� i� s�owo jest zbilansowane
5.koniec