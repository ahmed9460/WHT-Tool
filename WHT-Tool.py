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
#########################################################################################
E4 = input("please enter password:")
if E4 == 'E4NF':
  time.sleep(5)
  print('done....')
else:
  print("error 404 not found...")
exit()
style_tool = """
                      [1]tool-Termux
"""
print(style_tool)
n_tool = int(input("enter nmber:"))
if n_tool == 1:
  tools = {
  '1':'git clone https://github.com/Gameye98/Lazymux.git'
  '2':'git clone https://github.com/p4kl0nc4t/Spammer-Grab.git'
  '3':'git clone https://github.com/inconshreveable/ngrok.git'
  '4':'git clone https://github.com/cyweb/hammer.git'
  '5':'git clone https://github.com/grafov/hulk.git'
  '6':'git clone https://github.com/derv82/wifite.git'
  '7':'git clone https://github.com/sabri-zaki/EasY_HaCk.git'
  '8':'git clone https://github.com/israelbuitron/wifi-scanner.git'
  '9':'git clone https://github.com/sqlmapproject/sqlmap.git'
  '10':'git clone https://github.com/rajkumardusad/Tool-X.git'
  '11':'git clone https://github.com/emre/fb.py.git'
  '12':'git clone https://github.com/Vairous7x/V7x-Fishing2.git'
  '13':'git clone https://github.com/No-Name-404/N404-Tool.git'
  '14':'git clone https://github.com/beefproject/beef.git'
  }
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
  [14]beef
  """
  import os
  def installer(number):
    try:
      os.system(tools[number])
    except:
      print("unknow...")
    print(style)  
    user = input("enter number tool:")
    installer(user)
