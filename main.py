
import argparse

parser=argparse.ArgumentParser(
         description="""\033[33m i gift this script to my freind GEO for his stronge and beautiful sprit \nthis script its main funcation as sheat sheat for white hat hackers \n this tool based on the great course in youtube for  Hassan Saad
 \nhttps://www.youtube.com/channel/UClzCbf-F0BnOydXAtVQ9n7A
 feal free to check any bugs in it 
https://www.facebook.com/BADBON77
         """
         )
args=parser.parse_args()








# Console colors
bg ='' # '\033[44m'  # gray
W = bg+'\033[0m'  # white (normal)
R = bg+'\033[31m'  # red
G = bg+'\033[32m'  # green
O = bg+'\033[33m'  # orange
B = bg+'\033[34m'  # blue
P = bg+'\033[35m'  # purple
C = bg+'\033[36m'  # cyan
GR = bg+'\033[37m'  # gray
Y="\033[33m"

logo=Y+'''


          _______  _______  _______                _______           _______  _        _______ __________________
|\     /|(  ___  )(  ____ )(  ____ )|\     /|     (  ____ \|\     /|(  ____ )( \      (  ___  )\__   __/\__   __/
| )   ( || (   ) || (    )|| (    )|( \   / )     | (    \/( \   / )| (    )|| (      | (   ) |   ) (      ) (   
| (___) || (___) || (____)|| (____)| \ (_) /_____ | (__     \ (_) / | (____)|| |      | |   | |   | |      | |   
|  ___  ||  ___  ||  _____)|  _____)  \   /(_____)|  __)     ) _ (  |  _____)| |      | |   | |   | |      | |   
| (   ) || (   ) || (      | (         ) (        | (       / ( ) \ | (      | |      | |   | |   | |      | |   
| )   ( || )   ( || )      | )         | |        | (____/\( /   \ )| )      | (____/\| (___) |___) (___   | |   
|/     \||/     \||/       |/          \_/        (_______/|/     \||/       (_______/(_______)\_______/   )_(   
                                                                                                                 




'''+C

print(logo)
print("created by A_naser   v1.1 \n")

from   EXPLOIT  import *
from OSINT import *
from  Scanning  import *
if __name__ == '__main__':
	line="\033[0;35m_____________________________________________ "

	options=['\033[34m1-OSINT',line,'\033[33m2-SCANING',line,'\033[35m3-EXPLOIT',line,"\033[36m4-exit [*]"]
	for i in options:    print(i)

	try:
		#
		opt=input (R+"put your option pls :"+G) 
		if opt == "1":

			osint()
		elif opt=="2":
			scans()
		elif opt=="3":
			exploit()
		elif opt=="*":
			exit()
			


	except Exception as s:
		print(s)
