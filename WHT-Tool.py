import datetime , time
c1 = "\033[0;31m"
c2 = "\033[0;33m"
c3 = "\033[1;35m"
print(c1+"*****%25")
time.sleep(5)
print(c2+"************%50")
time.sleep(5)
print("******************%75")
time.sleep(5)
print("***************************%100")
time.sleep(5)
print(">>>>>>>>>>>>>>>>>>>>> done.............")
time.sleep(5)
print(c3+'>>>>>>>>>>>>>>>>>>>>>welcome to in my TooL...<<<<<<<<<<<<<<<<<<<<<')
time.sleep(5)
print(c1+'_____   _   _   __   _   _____        _          __  _   _   _____  ')
print(c1+'| ____| | | | | |  \ | | |  ___|      | |        / / | | | | |_   _|') 
print(c1+'| |__   | |_| | |   \| | | |__        | |  __   / /  | |_| |   | |')   
print(c1+'|  __|  \___  | | |\   | |  __|       | | /  | / /   |  _  |   | |')   
print(c1+'| |___      | | | | \  | | |          | |/   |/ /    | | | |   | |')   
print(c1+'|_____|     |_| |_|  \_| |_|          |___/|___/     |_| |_|   |_|')
print('                                                                     ')

import enter_user
############################################################################3
style_tool= """                              1-Tool-Termux              2-Dos attack

                              3-fishing                  4-scaning

                              5-install-metasploit       6-info gathring

                              7-about me                 8-exit"""
print(style_tool)
############################################################################
E4 = int(input("enter number:"))
time.sleep(3)
if E4 == 1:
    time.sleep(3)
    tools = {
    "1":"git clone https://github.com/Gameye98/Lazymux.git"
    "2":"git clone https://github.com/p4kl0nc4t/Spammer-Grab.git"
    "3":"git clone https://github.com/inconshreveable/ngrok.git"
    "4":"git clone https://github.com/cyweb/hammer.git"
    "5":"git clone https://github.com/grafov/hulk.git"
    "6":"git clone https://github.com/derv82/wifite.git"
    "7":"git clone https://github.com/sabri-zaki/EasY_HaCk.git"
    "8":"git clone https://github.com/israelbuitron/wifi-scanner.git"
    "9":"git clone https://github.com/sqlmapproject/sqlmap.git"
    "10":"git clone https://github.com/rajkumardusad/Tool-X.git"
    "11":"git clone https://github.com/emre/fb.py.git"  
    "12":"git clone https://github.com/Vairous7x/V7x-Fishing2.git"
    }
    #######################################################################
    style ="""
    [1]Lazymux
    [2]Spammer-Grab
    [3]ngrok
    [4]hammer
    [5]hulk
    [6]wifite
    [7]EasY_HaCk
    [8]wifi-scanner
    [9]sqlmap
    [10]Tool-X
    [11]fb
    [12]V7x-Fishing2
    """
    #######################################################################
    import os
    def installer(number):
        try:
            os.system(tools[number])
        except:
            print('error 404 not found..')
    print(style)
    user = input("enter number tool: ")
    installer(user)
######################################################################    
if E4 == 2:
  t_Dos = {
    "1":"git clone https://github.com/cyweb/hammer.git"
    "2":"git clone https://github.com/grafov/hulk.git"
    "3":""
    "4":""
    "5":""
    "6":""
  }
######################################################################
elif E4 == 7:
    print(""">>>>>>>>>>>welcome to in my tool<<<<<<<<<<<<<<<

         my name is mohamed Elsayed Abo hassan              

         name code: E4NF                                  

         my channal in Youtup : White Hacker Team       """)

