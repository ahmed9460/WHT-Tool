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
    import Tool_Termux

