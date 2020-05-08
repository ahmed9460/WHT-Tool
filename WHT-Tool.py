import datetime , time , os
os.system("clear")
c1 = "\033[0;31m" #red
c2 = "\033[0;32m" #green
c3 = "\033[0;33m" #yellow
c4 = "\033[0;36m" #cyan
print(c2+">>>>>>>25%")
time.sleep(3)
print(c1+">>>>>>>>>>>>>50%")
time.sleep(3)
print(c2+">>>>>>>>>>>>>>>>>>>>75%")
time.sleep(3)
print(c1+">>>>>>>>>>>>>>>>>>>>>>>>>>>100%")
time.sleep(3)
print(c2+">>>>>>>>>>>>>>>>>>>>>>>>>>>welcome to in my tool<<<<<<<<<<<<<<<<<<<<<<<<")
time.sleep(3)
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
#######################################################################33
style_tool = """
[1]Termux-Tool                    [2]scaning

[2]info gathering                 [4]install metasploit

[5]Dos attack                     [6]Hash Anything

[7]about me                       [8]exit 
"""
print(style_tool)

E4 = input("enter number: ")
if E4 == "1":
    tools_temux = {
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
    import os 
    def installer1(number):
        try:
            os.system(tools_termux[number])
        except:
            print("error not found....")
    print(style_termux)
    user = input("enter number tool: ")
    installer1(user)

