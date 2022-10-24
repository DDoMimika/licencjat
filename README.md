# licencjat

<p>&#347cie&#380ki plik&#243w znajduj&#261 si&#281 w pliku "paths.py"</p>

<p>dane wej&#347ciowe:
plik powinien znajdowa&#263 si&#281 w tym samym folderze co programy
plik "test.txt" z s&#322owami do przetestowania, po jednym w jednej linii</p>

<p>dane wyj&#347ciowe:
plik "result.txt" z s&#322owami zbilanoswanymi, po jednym w jednej linii
plik powinien znajdowa&#263 si&#281 w tym samym folderze co programy</p>

<p>Opis dzia&#322ania main.py
<ul>
<li>start</li>
<li>wczytujemy wszytkie s&#322owa z pliku</li>
<li>dla s&#322ow z pliku
<ul><li> sprawdzamy czy jest zbilanoswane, je&#347li tak to zapisujemy je w pliku z wynikiem</li></ul>
</li><li>koniec</p>
</ul>
<p>Opis dzia&#322ania if_balanced.py
<ul><li> start</li>
<li> dla wszystkich liter w s&#322ownie
	<ul><li> sprawdzamy czy litera znajduje si&#281 ju&#380 w s&#322owniku ilosci wystepowania litery
	<space><space>Je&#347li nie to dodajemy j&#261 i ustawiamy jej ilo&#347&#263 na zero</li></ul>
</li><li> Dla d&#322ugo&#347ci od 2 do d&#322ugo&#347ci s&#322owa-1
	<ul><li> Tworzymy s&#322ownik liter wyst&#281puj&#261cych w s&#322owie ustawiaj&#261c min ilo&#347&#263 wyst&#281powania na d&#322ugo&#347&#263 s&#322owa i max ilo&#347&#263 wyst&#281powania na zero</li>
	<li> Dla wszytkich mo&#380liwych indeks&#243w rozpoczynaj&#261cych pod&#322owo o danej d&#322ugo&#347ci(iteruj&#261c od zera)
		<ul><li> zerujemy s&#322ownik liter, kt&#243ry zawiera ilo&#347&#263 wyst&#261pie&#324 danej litery</li>
		<li> dla wszystkich liter ze s&#322owa od litery zaczynaj&#261cej podci&#261g do indeksu+d&#322ugo&#347&#263 s&#322owa
			<ul><li> Dodajemy dodajemy 1 do ilo&#347ci wyst&#281powania litery jak na ni&#261 trafimy</li></ul></li>
		<li> dla liter wyst&#281puj&#261cych w s&#322owie:
			<ul><li> sprawdzamy czy ilo&#347&#263 jej wyst&#281powania jest wi&#281ksza ni&#380 obecne maksimum wyst&#281powania:</li><br>
			je&#347li tak to nowe maximum to ilo&#347&#263 wtst&#281powania
			<li> sprawdzamy czy ilo&#347&#263 jej wyst&#281powania jest mniejsza ni&#380 obecne minimum wyst&#281powania:<br>
			je&#347li tak to nowe minimum to ilo&#347&#263 wtst&#281powania</li></ul></li></ul>
	<li> Dla wszystkich liter w s&#322owie 
		<ul><li>sprawdzamy czy ich max-min wyst&#281powania jest wi&#281ksze ni&#380 1<br>
		je&#347li tak ko&#324czymy przeszukiwa&#263 s&#322owo, zwracamy informacj&#281 i&#380 s&#322owo nie jest zbilansowane</li></ul></li></ul>
<li> zwracamy informacj&#281 i&#380 s&#322owo jest zbilansowane</li>
<li>koniec</li></ul></p>
