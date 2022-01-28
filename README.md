# cyber_patriots_ubuntu
```
  #delete media files
  import os
          #install and remove packages
          os.system("sudo apt-get update && sudo apt-get upgrade")
          purge = ["netcat","nmap","zemap","john","johntheripper","hydra","metasploit"]
          install = ["rkhunter", "ssh", "ufw", "firefox", "iptables", "Gufw", "lightdm", "bum"]
          for i in install:
                  os.system("sudo apt-get install --assume-yes "+i)

          #install lippam cracklib
          os.system("sudo apt-get update -y")
          os.system("sudo apt-get install -y libpam-cracklib")
          os.system("sudo ufw enable")
          for i in purge:
                  os.system("apt-get purge --assume-yes "+i)

          #update packages
          os.system("sudo apt-get update && sudo apt-get upgrade")

          #show what is running on the computer
          os.system("ps aux > running.txt")
  else:
          print("do the questions")
```
**delete media files**
```
import os
media = ["'*.mp3'","'*.mp4'","'*.wav'"]
for i in media:
  os.system("sudo find $dir -name " +i+ " -delete")
```
**install and remove packages**
```
#install and remove packages
os.system("sudo apt-get update && sudo apt-get upgrade")
purge = ["netcat","nmap","zemap","john","johntheripper","hydra","metasploit"]
install = ["rkhunter", "ssh", "ufw", "firefox", "iptables", "Gufw", "lightdm", "bum"]
for i in install:
  os.system("sudo apt-get install --assume-yes "+i)

#install lippam cracklib
os.system("sudo apt-get update -y")
os.system("sudo apt-get install -y libpam-cracklib")
os.system("sudo ufw enable")
for i in purge:
  os.system("apt-get purge --assume-yes "+i)
```
