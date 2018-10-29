#!/usr/bin/python
#Coded by ERIC
import os
import time
import getpass
from time import sleep
from io import open
systemos = input('Select your operating system (winxx,mac,linux): ')
if systemos not in ('winxx','mac','linux'):
   os.system('')
elif systemos == 'winxx':
   os.system('cls')
   operating = 'winxx'
   def winxx(script):
      ii = 0 
      winxxbatD = open('open_dorks.bat','w')
      winxxDest = winxxbatD.write('@echo off\n')
      winxxbatD.close()
      while ii < int(quest):
        winxxbat = open('open_dorks.bat','a')
        writeWinxx = winxxbat.write(script[ii]+'\n')
        winxxbat.seek(len(script[ii]))
        winxxbat.close()
        ii += 1
      if ii == int(quest):
           os.system('@echo off')
           os.system('open_dorks.bat')
elif systemos == 'linux':
   operating = 'linux'
   os.system('clear')
elif systemos == 'mac':
   opperating = 'mac'
   os.system('')
def banner():
    print("""\033[1;33m
    DD     OOO  RRRR   KK  KK HHHHHHH
    D  D  \033[1;31mO   O R    R  K K      H
    D   D \033[1;31mO   O R   R   KK       H
    D   D \033[1;31mO   O RRRR    K KK     H
    DD D   \033[1;31mOOO  R  RR   K   KK   H
       ,-----------------.
        \033[1;33mCoded By Eric\033[1;31m    |
       ,-----------------.\n""")
def sales(keys,ii,append):
    salesA = list(','*int(quest))
    salesA[ii] = keys
    append.append('inurl:products/'+salesA[ii])
    print(append)
def documents(keys,ii,append):
    documentsA = list(','*int(quest))
    documentsA[ii] = keys
    append.append('inurl:library/'+documentsA[ii])
    append.append('intitle:[PDF] '+documentsA[ii])
    print(append)
def socialN(keys,ii,append):
    socialNA = list(','*int(quest))
    socialNA[ii] = keys
    append.append('intitle:Profile: '+socialNA[ii])
    append.append('inurl:login.php?sessId='+socialNA[ii])
def email(keys,ii,append):
    emailA = list(','*int(quest))
    emailA[ii] = keys
    append.append('inurl:mail-box/'+emailA[ii])
def sqli(keys,ii,append):
    sqliA = list(','*int(quest))
    sqliA[ii] = keys
    append.append('inurl:/'+sqliA[ii]+'.php?id=')
def terminal():
    banner()
    print('''
            Funcs:
                |
                |
              <_}
              |
              |_> banner()
              |     |
              |     |_> Example : Term$  banner()
              |
              |_> sales(keys,ii,append)
              |     |
              |     |_> Example : Term$  sales('nisan','2',appender)
              |                   Term$  sales('ford','2',appender)
              |
              |_> documents(keys,ii,append)
              |     |
              |     |_> Example : Term$  documents('trump','1',appender)
              |
              |_> socialN(keys,ii,append)
              |     |
              |     |_> Example : Term$  socialN('friends','3',appender)
              |                   Term$  socialN('groups','3',appender)
              |                   Term$  socialN('relationships','3',appender)
              |_> email(keys,ii,append)
                    |
                    |_> Example : Term$ email('asociation','1',appender)

       ''')
    while True:
       term = input(green+'Term$ -  '+yellow)
       exec(term)
       if term == 'exit':
          print('exiting...')
          break
banner()
a = 0
red    = "\033[1;31m"
green  = "\033[1;32m"
yellow = "\033[1;33m"
blue   = "\033[1;34m"
print(green)
quest = input('how many keywords will be?  '+yellow)
if quest == '69':
   terminal()
print(green)
type = input('Which type of page do you want?\n\n '+red+'[1]'+blue+'Sales  '+red+'[2]'+blue+'Documents  '+red+'[3]'+blue+'Social Network\n '+red+'[4]'+blue+'Email  '+red+'[5]'+blue+'SQLi'+green+'                         :  '+yellow)
warning = red+'[!]'
info = blue+'[*]'
dorks = []
appender = []
create_list = ','*int(quest)
winxxScript = []
while a < int(quest):
    keywords = input(green+"\nEnter You Keyword\'s: "+yellow)
    if type not in ('1','2','3','4','5'):
       print(warning+yellow+'Select a correct page number.')
       break
    elif type == '1':
       sales(keywords,a,appender)
    elif type == '2':
       documents(keywords,a,appender)
    elif type == '3':
       socialN(keywords,a,appender)
    elif type == '4':
       email(keywords,a,appender)
    elif type == '5':
       sqli(keywords,a,appender)
    winxxScript.append('Start https://google.com/search?q='+appender[a])
    if int(quest)-1 == a:
       s = 0
       print('%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/\n')
       while s < int(quest):
          print('      ',appender[s].replace(' ','+'))
          s += 1
       print(yellow+'\n%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/%/')
       winxx(winxxScript)
       print(info+yellow+' Opening browser to search the dorks.')
    a += 1
