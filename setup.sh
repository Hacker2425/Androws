#!/bin/bash
apt update -y
mkdir logs
resize -s 40 70 > /dev/null
#Colors
cyan='\e[0;36m'
lightcyan='\e[96m'
green='\e[0;32m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
blue='\e[1;34m'
Escape="\033";
white="${Escape}[0m";
RedF="${Escape}[31m";
GreenF="${Escape}[32m";
LighGreenF="${Escape}[92m"
YellowF="${Escape}[33m";
BlueF="${Escape}[34m";
CyanF="${Escape}[36m";
Reset="${Escape}[0m";
# Check root
[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo  $red "You must be root to run the script"; echo ; exit 1; }
clear
# check internet 
function checkinternet() 
{
  ping -c 1 google.com > /dev/null 2>&1
  if [[ "$?" != 0 ]]
  then
    echo -e $yellow " Checking For Internet: ${RedF}FAILED"
    echo
    echo -e $red "This Script Needs An Active Internet Connection"
    echo
    echo -e $yellow " ANDROWS Exit"
    echo && sleep 2
    exit
  else
    echo -e $yellow " Checking For Internet: ${LighGreenF}CONNECTED"
  fi
}
checkinternet
sleep 2

echo -e $blue
sudo cat /etc/issue.net
#check dependencies existence
echo -e $blue "" 
echo "® Checking dependencies configuration ®" 
echo "                                       " 
# check if metasploit-framework is installed
which msfconsole > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Metasploit-Framework..............${LighGreenF}[ found ]"
which msfconsole > /dev/null 2>&1
sleep 2
else
echo -e $red "[ X ] Metasploit-Framework  -> ${RedF}not found "
echo -e $yellow "[ ! ] Installing Metasploit-Framework "
sudo apt-get install metasploit-framework -y
echo -e $blue "[ ✔ ] Done installing ...."
which msfconsole > /dev/null 2>&1
sleep 2
fi
echo "METASPLOIT FOUND" > logs/msfconsole.log
#check if xterm is installed
which xterm > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Xterm.............................${LighGreenF}[ found ]"
which xterm > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] xterm -> ${RedF}not found! "
sleep 2
echo -e $yellow "[ ! ] Installing Xterm "
sleep 2
echo -e $green ""
sudo apt-get install xterm -y
clear
echo -e $blue "[ ✔ ] Done installing .... "
which xterm > /dev/null 2>&1
fi
echo "XTERM FOUND" > logs/xterm.log
#check if zenity is installed
which zenity > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Zenity............................${LighGreenF}[ found ]"
which zenity > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Zenity -> ${RedF}not found! "
sleep 2
echo -e $yellow "[ ! ] Installing Zenity "
sleep 2
echo -e $green ""
sudo apt-get install zenity -y
clear
echo -e $blue "[ ✔ ] Done installing .... "
which zenity > /dev/null 2>&1
fi
echo "ZENITY FOUND" > logs/zenity.log
#Check for Android Asset Packaging Tool
which aapt > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Aapt..............................${LighGreenF}[ found ]"
which aapt > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Aapt -> ${RedF}not found! "
sleep 2
echo -e $yellow "[ ! ] Installing Aapt "
sleep 2
echo -e $green ""
sudo apt-get install aapt -y
sudo apt-get install android-framework-res -y
clear
echo -e $blue "[ ✔ ] Done installing .... "
which aapt > /dev/null 2>&1
fi
echo "AAPT FOUND" > logs/aapt.log
#Check for Apktool Reverse Engineering
which apktool > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Apktool...........................${LighGreenF}[ found ]"
which aapt > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Apktool -> ${RedF}not found! "
sleep 2
echo -e $yellow "[ ! ] Installing Apktool "
sleep 2
echo -e $green ""
sudo apt-get install apktool -y
clear
echo -e $blue "[ ✔ ] Done installing .... "
which apktool > /dev/null 2>&1
fi
echo "APKTOOL FOUND" > logs/apktool.log
#check for zipalign
which zipalign > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Zipalign..........................${LighGreenF}[ found ]"
which aapt > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Zipalign -> ${RedF}not found! "
sleep 2
echo -e $yellow "[ ! ] Installing Zipalign "
sleep 2
echo -e $green ""
sudo apt-get install zipalign -y
clear
echo -e $blue "[ ✔ ] Done installing .... "
which zipalign > /dev/null 2>&1
fi
echo "ZIPALIGN FOUND" > logs/zipalign.log
#check if gradle is installed
which gradle > /dev/null 2>&1
if ["$?" -eq "0"]; then
echo -e $green "[ ✔ ]gradle..............${LighGreenF}[ found ]"
which gradle > /dev/null 2>&1
sleep 2
else
echo -e $red "[ X ] gradle  -> ${RedF}not found "
echo -e $yellow "[ ! ] gradle "
sudo apt-get install gradle -y
echo -e $blue "[ ✔ ] Done installing ...."
which gradle > /dev/null 2>&1
sleep 2
fi
echo "GRADLE FOUND" > logs/gradle.log
#check if Jarsigner is installed
which jarsigner > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Jarsigner..............${LighGreenF}[ found ]"
which jarsigner > /dev/null 2>&1
sleep 2
else
echo -e $red "[ X ] Jarsigner -> ${RedF}not found "
echo -e $yellow "[ ! ] Jarsigner "
sudo apt-get install openjdk-11-jdk-headless -y
echo -e $blue "[ ✔ ] Done installing ...."
which jarsigner > /dev/null 2>&1
sleep 2
fi
echo "JARSIGNER FOUND" > logs/jarsigner.log

