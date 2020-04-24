tools = {
"1:"git clone https://github.com/Gameye98/Lazymux.git"
"2":"git clone https://github.com/Vairous7x/V7x-Tool.git"
"3":"git clone https://github.com/p4kl0nc4t/Spammer-Grab.git"
"4":"git clone https://github.com/inconshreveable/ngrok.git"
"5":"git clone https://github.com/cyweb/hammer.git"
"6":"git clone https://github.com/grafov/hulk.git"
"7":"git clone https://github.com/derv82/wifite.git"
"8":"git clone https://github.com/sabri-zaki/EasY_HaCk.git"
"9":"git clone https://github.com/israelbuitron/wifi-scanner.git"
"10":"git clone https://github.com/sqlmapproject/sqlmap.git"
"11":"git clone https://github.com/rajkumardusad/Tool-X.git"
"12":"git clone https://github.com/emre/fb.py.git"  
"13":"git clone https://github.com/Vairous7x/V7x-Fishing2.git"
}
#######################################################################
style ="""
[1]Lazymux
[2]V7x-Tool
[3]Spammer-Grab
[4]ngrok
[5]hammer
[6]hulk
[7]wifite
[8]EasY_HaCk
[9]wifi-scanner
[10]sqlmap
[11]Tool-X
[12]fb
[13]V7x-Fishing2
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
            
