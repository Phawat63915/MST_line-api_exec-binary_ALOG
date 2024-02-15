set PATH=%PATH%;C:\Users\Phawat\AppData\Local\Programs\Python\Python310;C:\Users\Phawat\AppData\Local\Programs\Python\Python310\Scripts


python.exe -m pip install requests
python.exe -m pip install nuitka
python.exe -m nuitka --mingw64 hello.py