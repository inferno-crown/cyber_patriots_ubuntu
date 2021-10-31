#delete media files
import os
media = ["'*.mp3'","'*.mp4'","'*.wav'"]
for i in media:
        os.system(f"sudo find $dir -name {i} -delete")

import os
media = ["'*.mp3'","'*.mp4'","'*.wav'"]
for i in media:
        os.system("sudo find $dir -name " +i+ " -delete")

#install and remove packages
import os
purge = []
install = []ls
os.system("sudo apt-get install --assume-yes rkhunter ssh ufw firefox iptables")
os.system("sudo sudo ufw enable")
os.system("apt-get purge --assume-yes netcat nmap zemap john johntheripper hydra nmap matasploit")


#update packages
import os
os.system("sudo apt-get update")
