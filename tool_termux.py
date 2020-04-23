def termux():
    style_tools= """                         1-Lazymux                         2-v7x-Tool

                             3-spammer grap                    4-ngrok

                             5-v7xstyle                        6-hammer

                             7-hulk                            8-wifite

                             9-Easy Hack                       10-wifi-scanner

                             11-sqlmap                         12-Tool-x

                             13-fb                             14-v7x-fishing

                                              15-back"""
    tools = {
    "1":"git clone https://github.com/Gameye98/Lazymux.git"
    "2":"git clone https://github.com/Vairous7x/V7x-Tool.git"
    "3":"git clone https://github.com/p4kl0nc4t/Spammer-Grab.git"
    "4":"git clone https://github.com/inconshreveable/ngrok.git"
    "5":"git clone"
    "6":"git clone https://github.com/cyweb/hammer.git"
    "7":"git clone https://github.com/grafov/hulk.git"
    "8":"git clone https://github.com/derv82/wifite.git"
    "9":"git clone https://github.com/sabri-zaki/EasY_HaCk.git"
    "10":"git clone https://github.com/israelbuitron/wifi-scanner.git"
    "11":"git clone https://github.com/sqlmapproject/sqlmap.git"
    "12":"git clone https://github.com/rajkumardusad/Tool-X.git"
    "13":"git clone https://github.com/emre/fb.py.git"  
    "14":"git clone https://github.com/Vairous7x/V7x-Fishing2.git"
    }
import os
def installer(number):
    try:
        os.system(tools[number])
    except:
        print("error not found...")
def print1():        
    print(style_tools)
    user = input("enter number: ")
installer(user)
termux()
print1()


