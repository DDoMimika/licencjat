# licencjat

Œcie¿ki plików znajduj¹ siê w pliku "paths.py"

dane wejœciowe:
plik powinien znajdowaæ siê w tym samym folderze co programy
plik "test.txt" z s³owami do przetestowania, po jednym w jednej linii

dane wyjœciowe:
plik "result.txt" z s³owami zbilanoswanymi, po jednym w jednej linii
plik powinien znajdowaæ siê w tym samym folderze co programy

Opis dzia³ania main.py
1.start
2.wczytujemy wszytkie s³owa z pliku
3.dla s³ow z pliku
	3.1 sprawdzamy czy jest zbilanoswane
		jeœli tak to zapisujemy je w pliku z wynikiem
4.koniec

Opis dzia³ania if_balanced.py
1. start
2. dla wszystkich liter w s³ownie
	2.1 sprawdzamy czy litera znajduje siê ju¿ w s³owniku ilosci wystepowania litery
		Jeœli nie to dodajemy j¹ i ustawiamy jej iloœæ na zero
3. Dla d³ugoœci od 2 do d³ugoœci s³owa-1
	3.1. Tworzymy s³ownik liter wystêpuj¹cych w s³owie ustawiaj¹c min iloœæ wystêpowania
	na  d³ugoœæ s³woa i max iloœæ wystêpowania na zero
	3.2 Dla wszytkich mo¿liwych indeksów rozpoczynaj¹cych pod³owo o danej d³ugoœci(iteruj¹c od zera)
		3.2.1 zerujemy s³ownik liter, który zawiera iloœæ wyst¹pieñ danej litery
		3.2.2 dla wszystkich liter ze s³owa od litery zaczynaj¹cej podci¹g do indeksu+d³ugoœæ s³owa
			3.2.2.1 Dodajemy dodajemy 1 do iloœci wystêpowania litery jak na ni¹ trafimy
		3.2.3 dla liter wystêpuj¹cych w s³owie:
			3.2.3.1 sprawdzamy czy iloœæ jej wystêpowania jest wiêksza ni¿ obecne maksimum wystêpowania:
				jeœli tak to nowe maximum to iloœæ wtstêpowania
			3.2.3.2 sprawdzamy czy iloœæ jej wystêpowania jest mniejsza ni¿ obecne minimum wystêpowania:
				jeœli tak to nowe minimum to iloœæ wtstêpowania
	3.3 Dla wszystkich liter w s³owie sprawdzamy czy ich max-min wystêpowania jest wiêksze ni¿ 1
		jeœli tak koñczymy przeszukiwaæ s³owo, zwracamy informacjê i¿ s³owo nie jest zbilansowane
4. zwracamy informacjê i¿ s³owo jest zbilansowane
5.koniec