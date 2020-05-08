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
[1]Lazymux           [2]Spammer-Grab

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
