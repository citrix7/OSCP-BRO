
def Document_Metadata():
    #

    options = [
    '1-exiftool',
    '2-strings']

    for i in options: print(i)

    exiftool = '''git clone https://github.com/exiftool/exiftool.git \ncd exiftool\nchmod +x exiftool\n./exiftool t/ d.png'''

    strings = "strings + target"
    cho = input("put your optuions :")
    if cho == "1":
        print(exiftool)
def anoynomus():

    proxychain='''nano /etc/proxychains.conf
    https://umbrella.cisco.com/

    uncheck #  Proxy DNS requests - no leak for DNS data

    service tor start

    #################
    dns change
    > cat /etc/resolv.conf
    > nano /etc/dhcp/dhclient.conf
    > delet 127.0.0.1 on an uncheck it  #prepend domain-name-servers 127.0.0.1;
    # prepend domain-name-servers 208.67.222.222,208.67.220.220;
    > service network-manager restart
    '''
    mac='''macchanger -s wlan0

    if you use wifi its wlan0
    sudo ifconfig wlan0 down

    macchanger -r wlan0

    '''
    anonsurf='''git clone https://github.com/Und3rf10w/kali-anonsurf
        cd kali-anonsurf/
        ./installer.sh
        anonsurf start

        to change the node >anonsurf change'''
    options=['1-proxychain',"2-mac","3-anonsurf"]
    for i in options:    print(i)

    x=input ("put choicec :")
    if x=="1":
        print(proxychain)
    elif x=="2":
            print(mac)
    elif x=="3":
        print(anonsurf)
        
    else:
        print("try again")
def osint():
	#
	import socket

	G = '\x1b[1;32m'
	R = '\x1b[31m'
	V="\033[33m"
	B ='\033[34m' 

	host=input (G+"put your host  :") or "127.0.0.1"
	ip   = socket.gethostbyname(host)


	dig="""
	hint : nano /etc/resolv.conf # 208.67.222.222|208.67.220.220

	------------------------
	dig +noall +answer {0} A
	dig +noall +answer {0} NS
	dig +noall +answer {0} MX
	dig +noall +answer {0} ANY
	dig +noall +answer @8.8.8.8 {0} ANY
	dig +noall +answer +norecurse {0} A
	dig +noall +answer @8.8.8.8 {0} AXFR
	-----------------
	zone transfer
	--------------
	dig +noall +answer {0} NS
	dig +noall +answer @8.8.8.8 {0} AXFR
	dig +noall +answer -x {1} #YOUR IP

	""".format(host,ip)

	dnsrecon='''
	
	dnsrecon -d {0}
	dnsrecon -d {0} -n “8.8.8.8 | 8.8.4.4”

	#get all dns and try all one by one 
	-----------------
	zone transfer
	--------------
	dnsrecon -d {0} -t axfr
	___________________________
	dnsrecon -r 127.0.0.1-{1} 
	dnsrecon -r {1}/16

	DNSRecon
	dnsrecon -t brt -d {0} -D /usr/share/dnsrecon/namelist.txt


	'''.format(host,ip)

	####################

	TheHarvester='''
	FindSubDomains
	----------------
	theharvester -d {0} -b google,bing,yahoo,netcraft,virustotal

	Find Emails
	----------------
	theharvester -d {0} -b hunter > result.txt

	Get Hunter API Key
	https://hunter.io/api_keys
	nano /usr/share/theharvester/discovery/huntersearch.py

	Find Users
	----------------
	theharvester -d {0} -b linkedin
	theharvester -d {0} -b twitter

	'''.format(host)


	sites='''
	curl ipinfo.io/{0}
	----------------
	https://findsubdomains.com/subdomains-of/microsoft.com

	rawojo3693@fft-mail.com
	rawojo3693@fft-mail.com
	----------------------------------------
	Get Network Ranges

	http://whois.domaintools.com
	----------------------------
	https://findsubdomains.com/subdomains-of/{0}

	--------------------------
    fierce = fierce -dns {0}
	'''.format(host)


	Google_Dorks  ='''
	site:{0} -www.{0}
	intitle:index.of passwd
	-------
	inurl:"linkedin.com/in/" "{0}"

	-------
	Find Sub-Domains
	****************
	site:{0} -www.{0}
	--------
	Collect Files
	--------
	site:{0} filetype:pdf
	------
	Search For Specific Word
	______________________

	site:{0} "hackers"
	-----
	Search For Specific Files
	__________________________

	site:{0} intitle:"index of"
	-------
	site:{0} inurl:phpinfo
	----
	site:{0} intext:password
	----
	Google Dorks (Collect Files)
	_____________________________
	site:{0} filetype:pdf

	Search For Company Users
	-------------------------
	inurl:"linkedin.com/in/" "{0}"
	'''.format(host)


	Recon_NG ='''
	recon-ng
	--------
	
	1-install marketplace
	---------------------

	marketplace install all
	marketplace search who

	2- creat your workspaces
	-----------------------

	workspaces list

	workspaces  install


	3-modules
	--------------
	modules search

	modules loads  .......

	options set SOURCE #you site xxxxxxx


	4- api
	--------

	keys add  #your api name xxxxx ...

	Show keys


	5-db
	----------
	db schema
	db delet hosts 40

	db quary select ip_adress from hosts 

	-------------------
	 web interfaec
	-------------
	#type this and you can use gui

	recon-web

	---------
	workspaces creat   xxxx naser

	workspaces select  xxxx naser

	###############################


	work space location in your pc

	cd /root/.recon-ng/workspaces/# your work space name xxxxx

	ls -alh

	-------------------
	*******************
	sub domains _Modules:
	********************
	-------------------
	recon/domains-hosts/bing_domain_web
	recon/domains-hosts/findsubdomains
	recon/domains-hosts/google_site_web
	recon/domains-hosts/netcraft
	recon/domains-hosts/bing_domain_api

	#########################################

	------------------------
	Recon-NG BRUTE FORCE
	---------------------
	recon/domains-hosts/brute_hosts

	Resolve and Extract Sub-Domains

	_____________________________________
	Recon-NG (Find Antivirus Programs) 
	_____________________________________

	discovery/info_disclosure/cache_snoop

	______________________________________
	------host to ip -----
	_______________________________
	recon/hosts-hosts/resolve


	----------------
	reporting/list


	Recon-NG EXAMPLE
	----------------------

	show modules
	use recon/domains-hosts/findsubdomains
	show info
	set source {0}
	run
	show hosts
	back
	###############

	https://github.com/lanmaster53/recon-ng-marketplace/wiki/API-Keys

	'''.format(host)


	ipinfo='''curl ipinfo.io/{0}'''.format(host)

	##########

	Metagoofil='''
	apt-get install metagoofil
	metagoofil -d {0} -t pdf,doc,xls,ppt -l 100 -n 10 -o metapdf -f result.html'''.format(host)

	hint='''
	# Generated by NetworkManager
	nameserver 208.67.222.222
	nameserver 208.67.220.220
	nameserver 8.8.8.8
	'''
	shodan='''sudo apt-get install python-setuptools ;pip install shodan'''
	#strings="strings  + name of any file (txt,jpg,exe,..)"
	user_recon = ''' git clone https://github.com/thelinuxchoice/userrecon'''
	linux_smart_enumeration = "https://github.com/diego-treitos/linux-smart-enumeration"
	enum4 = ''' https://labs.portcullis.co.uk/tools/enum4linux/\r\nenum4linux -a 127.0.0.1'''

	lists='''all lists : /usr/share/wordlists
				dirb > /usr/share/wordlists/dirb
				dirb > /usr/share/wordlists/dirb/small.txt'''
				    
	crunch ='''crunch 1 5 ahmed -o /root/Desktop/pass.txt

				 -p  WILL MAKE THE LIST NO THING IN IT REPEATED
				 
				crunch [min] [max] [characters]-t[pattern]-o[filename]

				crunch 6 8 123abc$ -o wordlist -t a@@@@b'''
	onlinelists='''https://wordlists.capsop.com'''
	wpscan='''wpscan --url https://brainfuck.htb --disable-tls-checks
		    wpscan --url https://www.certstars.com -e u vp
			wpscan --url http://www.certstars.com -e u -- wordlist /usr/share/wordlists/dirb/small.txt
			wget -mk http://www.certstars.com/
			gem install wpscan'''
	red_hook_enum = ''' git clone https://github.com/Tuhinshubhra/RED_HAWK
    cd RED_HAWK
    php rhawk.php'''

	options=['1-dig','2-dnsrecon','3-TheHarvester',"4-sites",'5-Google_Dorks','6-Recon_NG',"7-ipinfo","8-hint","9-shodan",
	"10-user_recon","11-linux_smart_enumeration","12-enum4","13-\x1b[36manoynomus","\x1b[1;32m14-lists","15-crunch","16-onlinelists","17-wpscan","18-red_hook_enum"]



	for i in options:    print(i)


	while 1:
		opt=input (R+"put your option pls :"+G) ;
		if opt == "1":
			print(dig)
		elif opt=="2":
			print(dnsrecon)
		elif opt=="3":
			print(TheHarvester)
		elif opt=="4":
			print(sites)
		elif opt=="5":
			print(Google_Dorks)
		elif opt=="6":
			print(Recon_NG)
		elif opt=="7":
			print(ipinfo)
		elif opt=="8":
			print(hint)
		elif opt=="9":
			print(shodan)
		elif opt=="10":
			print(user_recon)
		elif opt=="11":
			print(linux_smart_enumeration)
		elif opt=="12":
			print(enum4)

		elif opt=="13":
			anoynomus()

		elif opt=="14":
			print(lists)
		
		elif opt=="15":
			print(crunch)
		elif opt=="16":
			print(onlinelists)
		elif opt=="17":
			print(wpscan)
		elif opt=="18":
			print(red_hook_enum)
		elif opt=="*":
			exit()
				#######
	
		

