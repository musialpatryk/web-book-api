# web-book-api

Przygotowanie środowiska:
- utwórz folder dla projektu
- w folderze wykonaj komendę python -m venv venv (python/py - w zależności od zmiennych środowiskowych)
- aktywuj venv (Linux: source venv/bin/activate; Windows: ./venv/bin/activate) <br>
  (po poprawnej aktywacji powinien pojawić się napis "venv" na początku lini komend)
- zainstaluj django - pip install django
- zainstaluj rest'a - pip install djangorestframework
- pobierz projekt z gita w miejscu utworzonego folderu
- file -> settings -> Python Interpreter - wybierz odpowiedni interpreter
- w zakładce "Edit configuration" w polu Script path ustaw ściężkę na plik manage.py a w Parameters "runserver"
<br>
- gdyby coś wam się przypomniało to dodajcie, bo nie pamiętam czy używaliśmy jeszcze jakiś komend
<br>
<br>
W przypadku nowego projektu: <br>
- python manage.py migrate - tworzenie migracji, tworzy nowe tabele w bazie<br>
- python manage.py createsuperuser - tworzy nowego użytkownika
<br>
<br>
Obecnie stworzony user: admin / admin
