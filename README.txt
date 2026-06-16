#До сборки
pip install wxPython

#Сборка
pip install pyinstaller
cd целевая папка 
pyinstaller --onefile --noconsole --add-data="image.png:." --add-data="menu.txt:." test.py

версия Питона 3.14
скачать можно тут:
https://www.python.org/downloads/release/python-3143/