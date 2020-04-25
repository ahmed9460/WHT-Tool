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

                              5-install-metasploit       6-info gathering

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
    "13":"git clone https://github.com/No-Name-404/N404-Tool.git"  
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
    [13]N404-Tool
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
    "3":"git clone https://github.com/Ha3MrX/DDos-Attack.git"
    "4":"git clone https://github.com/jseidl/GoldenEye.git"
  }
  style_d = """
  [1]hammer
  [2]hulk
  [3]DDos-Attack
  [4]ip location
  """
  import os
  installer_dos(numberd):
    try:
      os.system(t_Dos[numberd])
    except:
      ptint("error 404 not found...")
    print(style_d)
    user1 = input("enter number tool: ")
    installer_dos(user1)
######################################################################
#if E4 = 6:
  #t_in = {
    #"1":"git clone https://github.com/nmap/nmap.git"
    #"2":"git clone https://github.com/maldevel/IPGeoLocation.git"
    #"3":"git clone https://github.com/shawarkhanethicalhacker/D-TECT-1.git"
  #}
#######################################################################
elif E4 == 7:
    print(""">>>>>>>>>>>welcome to in my tool<<<<<<<<<<<<<<<

         my name is mohamed Elsayed Abo hassan              

         name code: E4NF                                  

         my channal in Youtup : White Hacker Team       """)

