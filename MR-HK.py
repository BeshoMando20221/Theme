from getpass import getpass

import os

import time

def menu():

      while True:

           print("")

           os.system("clear")

           print('\033[1;36;40m<────────────────[MR-HK]────────────────>')

           print("\033[91m_________________________________________\033[0m")

           print("\033[92m")

           print(" ██╗      ██████╗  ██████╗ ██╗███╗   ██╗")

           print(" ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║")

           print(" ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║")

           print(" ██║     ██║   ██║██║   ██║██║██║╚██╗██║")

           print(" ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║")

           print(" ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝")

           print("\033[91m_________________________________________\033[0m")

           print("\033[91m_________________________________________\033[0m")

           print("")

           print("\033[92m 👇 Ragister your username & password 👇\033[0m")

           print("\033[91m_________________________________________\033[0m")

           print('The mountains are not made in a short time ')

           print("\033[1;93m")

           print("\033[1;92m            ♥️ i love termux ♥️ ")

           print("\033[1;93m")

           print("<─────────────────(^.^)──────────────────>")

           print("")

           try:

                x = str(input('\033[1;92mUsername \033[1;93m: '))

                print("")

                e = getpass('\033[1;92mPassword \033[1;93m: ')

                print ("")

                if x=="1" and e=="1":

                   print('wait...')

                   time.sleep(1)

                   os.system('clear')

                   break

                else:

                      print("")

                      print("")

                      print("")

                      print("")

                      print("\033[1;91m     Wrong Password")

                      time.sleep(0.1)

                      print("")

           except Exception:

                      print("")

                      print("")

                      print("")

                      print("")

                      print("")

                      print("\033[1;91m     Wrong Password")

                      time.sleep(0.1)

           except KeyboardInterrupt:

                      print("")

                      os.system('killall -9 com.termux')

                      print("")

                      print("")

                      print("")

                      print("")

                      print("\033[1;91m     Wrong Password")

                      time.sleep(0.1)

menu()
