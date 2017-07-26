# RaspberryPi

To install Rasbian OS on Raspberry Pi - 

1. Download Noobs from here - https://www.raspberrypi.org/documentation/installation/noobs.md
2. Unzip
3. Copy contents into MS-FAT formated clean SD card
4. Put SD card on Board
5. Connect to display and turn on
6. Select Raspbian OS from On Screen menu
7. Done


While doing SSH, if you get following error - 
Nishants-MacBook-Pro:~ nishant$ ssh pi@10.0.0.210
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:J+PhehcCoa+n2zjj0F7gaz2F3MPhFTL+MxZ2wy+7kko.
Please contact your system administrator.
Add correct host key in /Users/nishant/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /Users/nishant/.ssh/known_hosts:5
ECDSA host key for 10.0.0.210 has changed and you have requested strict checking.
Host key verification failed.
Nishants-MacBook-Pro:~ nishant$ ssh-keygen -R 10.0.0.210
#Host 10.0.0.210 found: line 5
/Users/nishant/.ssh/known_hosts updated.
Original contents retained as /Users/nishant/.ssh/known_hosts.old

Then run following command on your mac. This message will go away.
ssh-keygen -R <10.0.0.210>   <raspi ip>



Setup for RFID Reader - 

Assumes that you have installed the Raspbian OS already.

1. Run the command sudo raspi-config and enter the config
2. Go to Interfacing Options
3. Enable SPI
4. Restart Board
5. sudo apt-get update
6. sudo apt-get install python2.7-dev
7. git clone https://github.com/lthiery/SPI-Py.git
8. cd SPI-Py
9. sudo python setup.py install
10 cd ~
11. git clone https://github.com/mxgxw/MFRC522-python.git 
12. cd MFRC522-python 
13. sudo python Read.py

