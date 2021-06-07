# THIS REPOSITORY IS VERY OLD AND IS FULL OF MISTAKES
# I WILL UPDATE THIS SOON

'''imports'''
import zipfile # make sure to install this module 
import sys
import os
from datetime import datetime

# This is ascii color codes
class colors():
    R = '\u001b[31m'
    G = '\u001b[32m'
    Y = '\u001b[33m'
    M = '\u001b[35m'
    RESET = '\u001b[0m'


if os.name == 'nt': # if your on windows 
    clear = 'cls'
else: # if your on linux or mac
    clear = 'clear'


try:
    os.system(clear)
    print(colors.M + '''
     ███████╗██╗██████╗ ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
     ╚══███╔╝██║██╔══██╗████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
       ███╔╝ ██║██████╔╝██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
      ███╔╝  ██║██╔═══╝ ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
     ███████╗██║██║     ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
     ╚══════╝╚═╝╚═╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝''' + colors.RESET)
    print(colors.Y + "                             By: ToastedWaffless" + colors.RESET)
    wordfile = input("WORDFILE: ")
    lockedzip = input("LOCKED ZIP-FILE: ")
    t1 = datetime.now() # gets the time when it starts to brute-force 
    count = 1
    num_words = len(list(open(wordfile, "rb"))) # gets the amount of words in your wordfile
    with open(wordfile,'rb') as text:
        for entry in text.readlines(): # reads all the lines in your wordfile
            password = entry.strip()
            try:
                # tries to unzip the folder with the words in your wordfile
                with zipfile.ZipFile(lockedzip,'r') as zf:
                    zf.extractall(pwd=password) # extracts the folder
                    data = zf.namelist()[0] # Whats in the folder
                    data_size = zf.getinfo(data).file_size #how big the folder is
                    t2 = datetime.now() # ending time
                    total_time = t2 - t1 # gets the time it took
                    print(f"{colors.G}\n\n****************************************\n ~ PASSWORD CRACKED! [WORD: {number}/{num_words}]\n ~ CRACKED PASSWORD: {password.decode('utf8')}\n ~ CONTENTS: {data}\n ~ SIZE: {data_size} bytes\n ~ TIME TOOK: {total_time}\n****************************************{colors.RESET}")
                    break
            # if the word is incorrect

            except:

                # if you want to not say what word was wrong comment or delete the line below                                             
                print(colors.R + "[+] ~ INCORRECT PASSWORD : " + password.decode("utf8"))
                number = count
                count += 1
                pass

# if you hit ctrl + c it wont throw an error
except KeyboardInterrupt:
    print(colors.R + "\n\nGoodbye...")
    sys.exit(0)


