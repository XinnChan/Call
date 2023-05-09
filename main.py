# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2023-05-08 11:08:46.822916
import os, sys, time
from time import sleep
from requests.exceptions import ConnectionError
def jalan(xnxx):
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();time.sleep(0.01)
		
###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
###---[ Banner2 ]--------###
def banner2():
	jalan(f'''\t
\33[36;1m╦  \33[37;1m┌─┐┌─┐┬┌┐┌ 
\33[36;1m║  \33[37;1m│ ││ ┬││││ \33[31;1m> \33[37;1mCreator \33[31;1m: \33[1;33m𝚅𝙸𝙽𝙳𝚁𝙰-𝚇𝙳
\33[36;1m╩═╝\33[37;1m└─┘└─┘┴┘└┘ \33[31;1m> \33[37;1mFacebook\33[31;1m: \33[1;33mVindra Doang

 \33[31;1m> \33[37;1mKetik\33[32;1m BOT\33[37;1m Untuk Cara Mendapatkan Password sc Ini
 \33[31;1m> \33[37;1mDownload Dulu Passwordnya
 \33[31;1m> \33[37;1mLink \33[31;1m: [ \33[32;1mhttps://khaddavi.net/3jSFIwNbTA \33[31;1m]
 \033[1;97m>─────────────────────────────────────────────────<\n''')
#-----------( Bang give alok bang hahahahahhhaha )-----------------
y = "AbgGhLkJOLmkldcVblpoinalsbsbjhsjsj"

def login():
	clear_layar();	banner2();
	p = input("\33[31;1m# \33[37;1mPassword \33[31;1m: \33[30m")
	if p == y:
		print ("\n\33[31;1m> \33[37;1mLogin Succes \33[32;1m√\n")
		time.sleep(3)
		subrek()
	if p in ['BOT','Bot','bot']:
		os.system('xdg-open https://youtu.be/62YQzzYiD34')
		login()
	else :
		print ("\n\33[31;1m> \33[37;1mPassword Salah \33[31;1mX\n")
		os.system("clear")
		login()
###---------[ subrek ]----------###
def subrek():
	clear_layar();
	print(f'\033[1;35m•\033[1;32m Script\033[1;37m Sudah Di\033[1;32m Hapus Lihat Video Terbaru ')
	os.system('xdg-open https://github.com/Dra-ID')
	time.sleep(3)
	exit()
#-------- Crack Fb -----------##
if __name__ == "__main__":
	try:
		login()
	except  ConnectionError:
		exit(f"\n\33[31;1m  !\33[37;1m Tidak ada koneksi internet\n")
	except  KeyboardInterrupt:
		exit(f'{putih}[{R}!{putih}] Eror Login Ulang {R}!{putih}')
		
