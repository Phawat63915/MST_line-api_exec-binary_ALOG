"C:\Users\Phawat\AppData\Local\Programs\Python\Python311\Scripts\pyinstaller.exe" --onefile linecall.py
@REM copy /Y dist\hello.exe %~dp0\hello.exe
copy /Y config.ini dist\config.ini
copy /Y msg.toml dist\msg.toml