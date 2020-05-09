import datetime , time , os
os.system("clear")
c1 = "\033[0;31m" #red
c2 = "\033[0;32m" #green
c3 = "\033[0;33m" #yellow
c4 = "\033[0;36m" #cyan
print(c2+">>>>>>>25%")
time.sleep(1)
print(c1+">>>>>>>>>>>>>50%")
time.sleep(1)
print(c2+">>>>>>>>>>>>>>>>>>>>75%")
time.sleep(1)
print(c1+">>>>>>>>>>>>>>>>>>>>>>>>>>>100%")
time.sleep(1)
print(c2+">>>>>>>>>>>>>>>>>>>>>>>>>>>welcome to in my tool<<<<<<<<<<<<<<<<<<<<<<<<")
time.sleep(1)
print(c1+" _          __  _   _   _____        _____   _   _   __   _   _____")  
print(c1+"| |        / / | | | | |_   _|      | ____| | | | | |  \ | | |  ___|") 
print(c1+"| |  __   / /  | |_| |   | |        | |__   | |_| | |   \| | | |__")   
print(c1+"| | /  | / /   |  _  |   | |        |  __|  \___  | | |\   | |  __|")  
print(c1+"| |/   |/ /    | | | |   | |        | |___      | | | | \  | | |")     
print(c1+"|___/|___/     |_| |_|   |_|        |_____|     |_| |_|  \_| |_|")
print("                                                                           ")
password = input("please enter password..: ")
if password == "E4NF":
    time.sleep(3)
    print("                               ")
    print(c3+"done.....")
else:
    print("password not found....")
    exit()
#########################################################################
style_tool = """
[1]Termux-Tool                    [2]scaning

[3]info gathering                 [4]install metasploit

[5]Dos attack                     [6]about me

                  [7]exit WHT-Tool

"""
os.system("clear")
print(style_tool)
E4 = input("enter number: ")
if E4 == "7":
    exit()
if E4 == "1":
    os.system("clear")
    tools_termux = {
    "1":"git clone https://github.com/Gameye98/Lazymux.git",
    "2":"git clone ttps://github.com/p4kl0nc4t/Spammer-Grab.git",
    "3":"git clone https://github.com/inconshreveable/ngrok.git",
    "4":"git clone https://github.com/cyweb/hammer.git",
    "5":"git clone https://github.com/grafov/hulk.git",
    "6":"git clone https://github.com/derv82/wifite.git",
    "7":"git clone https://github.com/sabri-zaki/EasY_HaCk.git",
    "8":"git clone https://github.com/israelbuitron/wifi-scanner.git",
    "9":"git clone https://github.com/sqlmapproject/sqlmap.git",
    "10":"git clone https://github.com/rajkumardusad/Tool-X.git",
    "11":"git clone https://github.com/emre/fb.py.git",
    "12":"git clone https://github.com/Vairous7x/V7x-Tool.git",
    "13":"git clone https://github.com/Vairous7x/V7x-Fishing2.git",
    "14":"git clone https://github.com/No-Name-404/N404-Tool.git"
    }

    style_termux = """
    [1]Lazymux            [2]Spammer-Grab

    [3]ngrok              [4]hammer

    [5]hulk               [6]wifite

    [7]EasY_HaCk          [8]wifi-scanner

    [9]sqlmap             [10]Tool-X

    [11]fb                [12]V7x-Tool

    [13]V7x-Fishing2      [14]N404-Tool


"""

    def installer1(number):
        try:
            os.system(tools_termux[number])
        except:
            print("error not found....")
    print(style_termux)
    user = input("enter number tool: ")
    installer1(user)
    back = input("enter 99 to back: ")
    if back == "99":
        os.system("python WHT-Tool.py")

###############################################################################
if E4 == "2":
    os.system("clear")
    tools_scan = {
    "1":"git clone https://github.com/nmap/nmap.git",
    "2":"git clone https://github.com/threat9/routersploit.git",
    "3":"git clone https://github.com/sqlmapproject/sqlmap.git",
    "4":"git clone https://github.com/Dionach/CMSmap.git"
    }
    style_scan = """
    [1]Nmap scan             [2]RouterSploit scan

    [3]Sqlmap scan           [4]Cmsmap scan
    """
    def installer2(number_scan):
        try:
            os.system(tools_scan[number_scan])
        except:
            print("error not found....")
    print(style_scan)
    user1 = input("enter number tool: ")
    installer2(user1)
    back1 = input("enter 99 to back: ")
    if back1 == "99":
        os.system("python WHT-Tool.py")
############################################################################
if E4 == "3":
    os.system("clear")
    tools_info = {
    "1":"git clone https://github.com/Richienb/iplocation.git",
    "2":"git clone https://github.com/UndeadSec/EvilURL.git",
    "3":"git clone https://github.com/shawarkhanethicalhacker/D-TECT-1.git",
    "4":"git clone https://github.com/thelinuxchoice/thechoice.git",

    }
    style_info = """
    [1]ip location             [2]Evil URL

    [3]D-TECT                  [4]The CHOICE
    """
    def installer3(number_info):
        try:
            os.system(tools_info[number_info])
        except:
            print("error not found....")
    print(style_info)
    user2 = input("enter number tool: ")
    installer3(user2)
    back2 = input("enter 99 to back: ")
    if back2 == "99":
        os.system("python WHT-Tool.py")
############################################################################
if E4 == "4":
    os.system("clear")
    tool_meta = {
    "1":"git clone https://github.com/rapid7/metasploit-framework.git"
    }
    style_meta = """
                     [1]metasploit
    """
    def installer4(number_meta):
        try:
            os.system(tool_meta[number_meta])
        except:
            print("error not found....")
    print(style_meta)
    user3 = input("enter number tool: ")
    installer4(user3)
    back3 = input("enter 99 to back : ")
    if back3 == "99":
        os.system("python WHT-Tool.py")
############################################################################
if E4 == "5":
    os.system("clear")
    tool_dos = {
    "1":"git clone https://github.com/cyweb/hammer.git",
    "2":"git clone https://github.com/grafov/hulk.git",
    "3":"git clone https://github.com/XCHADXFAQ77X/XERXES.git",
    "4":"git clone https://github.com/jseidl/GoldenEye.git"
    }
    style_dos = """
    [1]H.A.M.M.E.R            [2]H.U.L.K

    [3]X.E.R.X.E.S            [4]Golden E.Y.E
    """
    def installer5(number_dos):
        try:
            os.system(tool_dos[number_dos])
        except:
            print("error not found....")
    print(style_dos)
    user4 = input("enter number tool: ")
    installer5(user4)
    back4 = input("enter 99 to back: ")
    if back4 == "99":
        os.system("python WHT-Tool.py")
###########################################################################
if E4 == "6":
    print("""
    my name : mohamed elsayed abo hassan
    my channal in youtup : https://www.youtube.com/channel/UC59cjUqBqiNmvDHF_XORrTA
    """) 
    back5 = input("enter 99 to back:")
    if back5 == "99":
        os.system("python WHT-Tool.py")

#############################################################################
