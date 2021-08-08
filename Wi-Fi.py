# -*- coding: utf-8 -*-
"""
Assignment 4:
Write a python class that is able to find three available WiFi networks with the strongest signal
and connect to the one where the password is provided.
Expected output:
$ python wifi.py
> Your available wifi networks are:
> [1] Wifi_network 1
> [2] Wifi_network 2
> [3] Wifi_network 3
> Your choice? 3
> Password: *******
> connected!
"""

import subprocess
import os
import platform
import getpass



class WiFi:
    def __init__(self, ssid_name=None, password=None):
        self.name=ssid_name
        self.password=password
        
    def AvailableWifiNetwork(self):
        devices=subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
        devices=devices.decode('ascii')
        devices=devices.replace("\r", "")
        ssid=devices.split("\n")
        ssid=ssid[4:]
        
        options={}
        i=1
        x=0
        while x<len(ssid):
            if x%5==0:
                options[i]=ssid[x]
                i+=1
            x+=1
            if i==3:    #for top 3 only on the basic of strength
                break
        
        #print(options) 
        print("Your available wifi networks are: ")  
        for i in range(1, len(options)+1):          #We may need to modify here to show more than three Wi-Fi etc.
            print("[{}] {}".format(i, options[i]))
            
        return options


    def createNewConnection(self):
        name=self.name
        SSID=self.name
        key=self.password
        config = """<?xml version=\"1.0\"?>
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
            <name>"""+name+"""</name>
            <SSIDConfig>
                <SSID>
                    <name>"""+SSID+"""</name>
                </SSID>
            </SSIDConfig>
            <connectionType>ESS</connectionType>
            <connectionMode>auto</connectionMode>
            <MSM>
                <security>
                    <authEncryption>
                        <authentication>WPA2PSK</authentication>
                        <encryption>AES</encryption>
                        <useOneX>false</useOneX>
                    </authEncryption>
                    <sharedKey>
                        <keyType>passPhrase</keyType>
                        <protected>false</protected>
                        <keyMaterial>"""+key+"""</keyMaterial>
                    </sharedKey>
                </security>
            </MSM>
        </WLANProfile>"""
        if platform.system() == "Windows":
            command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
            with open(name+".xml", 'w') as file:
                file.write(config)
        elif platform.system() == "Linux":
            command = "nmcli dev wifi connect '"+SSID+"' password '"+key+"'"
        os.system(command)
        if platform.system() == "Windows":
            os.remove(name+".xml")

    def connect(self):
        name=self.name
        SSID=self.name
        if platform.system() == "Windows":
            command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
        elif platform.system() == "Linux":
            command = "nmcli con up "+SSID
        os.system(command)





if __name__=="__main__":
    options=WiFi().AvailableWifiNetwork()
    choice=int(input("Your choice?: "))
    ssid_name=options[choice]
    #Connecting
    try:
        key = getpass.getpass("Password: ")
        WiFi(ssid_name[9:], key).createNewConnection()
        WiFi(ssid_name[9:], key).connect()
        print("Connected!")
    except Exception:
        print("Try again!")
