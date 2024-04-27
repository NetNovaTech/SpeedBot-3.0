# Standardowe importy bibliotek Pythona, uporządkowane alfabetycznie
import os
import random
import re
import sys
import threading
import time
import webbrowser
import winsound

# Importy związane z GUI (tkinter), uporządkowane alfabetycznie
import tkinter
import tkinter.messagebox

# Importy zewnętrznych bibliotek, uporządkowane alfabetycznie
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

# Importy dotyczące konkretnych pakietów OpenAI
import openai
from openai import OpenAI

import imaplib
import email

from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime



duration = 420      # milliseconds - 100
frequency = 4200         # Hz - 1000
# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 1000   # Set Duration To 1000 ms == 1 second


#user = []

dane = None

maile = None

nick = 0
haslo_twit = 0 
token_z_pliku = 0
mail = 0
haslo_mail = 0

suspended = 0
max_suspended = 3





max_prob_logowania = 5

max_prob_nicku = 5 

max_prob_hasla = 5






petla_nr = 0

haslo_twit = ["1","2","3","4"]


nowy_token = 0
nowe_haslo_twit = 0 
link = "https://twitter.com/messages"

token_z_pliku = 0
mail = 0


login_pass = 0
not_logged = 0

capcha_do_zrobienia = 0
zablokowane = 0
dane = 0
mail_password = 0
maile = 0
hasla_do_sprawdzenia = 0
nick = []
mail = []

# petla_nr = 0

# not_logged = 0

# login_pass = 0

# capcha_do_zrobienia = 0

# zablokowane = 0

# mail_password = []  
 
# hasla_do_sprawdzenia = []

### ### ### ### ### 





# MOJ MAIN TOKEN # bdf9ad091eb95e9e4aa63c6091fecc2d5bb1bf04 ################################### MAIN TOKEN ###

######################### LOKALNE #########################

#capcha = 0 ## chuj wi czemu jak to usune to capcha() sie zmienia

komentarz_nr = 0

moje_haslo_mail = "O2haslo933#"

post_url = 0

refferal = 0



token = 0

line = 0

linki_txt = 0

undo_button = 0


######################### IMPORT DANYCH #########################

def setup_dane():
    print("F - Setup")
    global token_z_pliku , dane , haslo_twit , nick , mail , haslo_mail, status
    dane = []

    with open("dane2.txt", "r", encoding="utf-8") as file:
        for line in file:
            dane.append(line.strip()) 

    # token_z_pliku = [(':')[-1] for line in dane]
    token_z_pliku = []
    for line in dane:
        
        variables = line.split(':')
        for variable in variables:
            # Sprawdzanie czy zmienna ma dokładnie 40 znaków i jest alfanumeryczna
            if len(variable) == 40 and variable.isalnum():
                token_z_pliku.append(variable)
                break  # Przerywamy pętlę po znalezieniu pierwszej pasującej zmiennej tokens




    try:
        # nick =[line.split(':')[0] for line in dane] # stary bez usuwania @
        
        nick = [line.split(':')[0].replace('@', '') for line in dane if ':' in line]
    except Exception:
        print (" - nick nie załadowany - ")




    try:
        haslo_twit = []   
        for line in dane:
            czesci = line.split(':')
            if "@" in czesci[1]:
                wybrana_zmienna = czesci[2] if len(czesci) > 2 else None
            else:
                wybrana_zmienna = czesci[1]
            if wybrana_zmienna is not None:
                haslo_twit.append(wybrana_zmienna)
        # Aby wydrukować pierwszy element listy haslo_twit, upewnij się, że lista nie jest pusta
    except Exception:
        print (" - hasło twitter nie załadowane - ")

    try:
        # mail = [line for line in dane if "@" in line and "." in line][0].split(':')[1]
        # mail =[line.split(':')[2] for line in dane]
        mail = []
        for line in dane:
            # Dzielenie linii na potencjalne zmienne
            czesc_mail = line.split(':')  # Możesz zmienić ' ' na inny separator jeśli potrzebujesz
            for czesc_mail in czesc_mail:
                # Sprawdzanie czy zmienna zawiera @ i .
                if "@" in czesc_mail and "." in czesc_mail:
                    mail.append(czesc_mail)
                    break  # Przerywamy pętlę po znalezieniu pierwszej pasującej zmiennej
        # Pobieranie danych z komórki o jedną w prawo od znalezionego adresu e-mail
    except Exception:
        print (" - adres mail nie załadowany - ")

    try:
        # haslo_mail =[line.split(':')[3] for line in dane]
        # zmienna z linii bezpośrednio po emailu.
        haslo_mail = []
        for linia in dane:
            elementy = linia.split(':')
            # Sprawdzamy, czy trzeci element linii zawiera dwa symbole '@' i '.'
            if len(elementy) > 2 and "@" in elementy[2] and "." in elementy[2]:
                # Jeśli tak, to pobieramy czwarty element jako hasło do maila
                if len(elementy) > 3:
                    haslo_mail.append(elementy[3])
                else:
                    # Jeśli nie ma czwartego elementu, możemy dodać wartość None lub kontynuować
                    haslo_mail.append(None)
    except Exception:
        print (" - hasło mail nie załadowane - ")

    
    try:
        nowy_mail = []
        with open('maile.txt', 'r') as plik:
            # Iterujemy przez każdą linię w pliku
            for linia in plik:
                # Usuwamy znaki końca linii i dodajemy linię do listy nowy_mail
                nowy_mail.append(linia.strip())
    except Exception:
        print("Wyjebało pobieranie nowego maila...")


    try:
        # nick =[line.split(':')[0] for line in dane] # stary bez usuwania @
        status = []
        status = [line.split(':')[-1].replace('-', '') for line in dane if ':' in line] # zaimplementowane usuwanie -- ze statusy
    except Exception:
        print (" - Status nie załadowany - ")




    print("Załadowano:")
    print(nick[0])
    print(haslo_twit[0])
    print(token_z_pliku[0]) 
    print(mail[0])
    print(haslo_mail[0])
    print(status[0])





#################################################################################################################

### ### ### ### ### ### ### ### ###

def new_driver(): 
    print("F - new driver\n")
    global driver , mail_password , hasla_do_sprawdzenia , nowy_mail
    service = Service(executable_path=r'C:\geckodriver\geckodriver.exe')
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0")
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("marionette.enabled", True)
 
    driver = webdriver.Firefox(service=service, options=options)
    time.sleep(1)
    #driver.set_window_position(0, 0)                       # C
    driver.set_window_position(-2000, 0)                   # L                                                   ###################################
    #driver.set_window_position(+2950, 0)                  # P                                                   # ZMIANA MIEJSCA OTWIERANIA OKNA #xxx
    #driver.set_window_position(+4250, 0)                   # TV                                                 ###################################
    time.sleep(2)
    # może refresh ??

    # MOJ_MAIN_TOKEN # "bdf9ad091eb95e9e4aa63c6091fecc2d5bb1bf04" #
    ### hasło mail ### 
    mail_password = ["O2haslo933#" , "O2haslo933" ]  
    # hasła twitter 
    hasla_do_sprawdzenia = [haslo_twit[0], "Nigga123123", "Twithas933", "Twithas933#"] ############ tu zmiana
    
### ### ### ### ### ### ### ### ###
    
def login_cookies():
    global driver 
    print("F - login cookies\n")
    #global petla_nr, token_z_pliku
    
    token = token_z_pliku[0] ############ tu zmiana
    print("Pobrany token :", token)
    if not token:
        tkinter.messagebox.showerror("BRAK TOKENÓW !")
        return
    driver.get('https://twitter.com')
    time.sleep(2)                                          ######### tu zmień na czekanie na cos zamiast ts
    try:
        driver.add_cookie({
            'name': 'auth_token',
            'value' : token,
            'domain': '.twitter.com',
            'path': '/',
            'secure': True,
            'httpOnly': True
        })
        print("Cookies załadowane poprawnie")
        mini_export()
        
    except Exception as e:
        print(f"Nie załadowano tokenów: {e}")
  
### ### ### ### ### ### ### ### ###
    
# def wyświetl_token():
#     global driver , token_z_pliku , petla_nr , haslo_twit , nick , mail , haslo_mail , nowe_haslo_twit , nowy_token
#     print("F wyświetl token\n")
#     if token_z_pliku:  # Sprawdza, czy lista tokens zawiera jakiekolwiek elementy            #przerób to na wyswietlanie i sprawdzanie czy jest token ! login nowe_haslo_twit i mail
#         print((f"{nick[petla_nr]} : {haslo_twit[petla_nr]} : {token_z_pliku[petla_nr]} : {mail[petla_nr]} : {haslo_mail[petla_nr]} \n"))
#     else:
#         print("Plik DANE.txt załadowany błędnie")

### ### ### ### ### ### ### ### ###
        
def mini_export():
    global driver
    print("F - mini export\n")
    try:
        with open('OUT-wczytane.txt', 'a',encoding = "utf-8") as file:
            file.write("\n"+f"{nick[0]}"+":"+f"{haslo_twit[0]}"+":"+f"{token_z_pliku[0]}"+":"+f"{mail[0]}"+":"+f"{haslo_mail[0]}"+":"+f"{status[0]}") # +"error" if error =0 -> error = "" 

        print("Użyty TOKEN zapisany poprawnie do pliku backupu")

        with open('dane2.txt', 'r') as file:
            lines = file.readlines()

        # Zapisz, co zostanie usunięte
        removed_line = lines.pop(0)

        with open('dane2.txt', 'w') as file:
            file.writelines(lines)


        print('Linia usunięta:')
        print(removed_line)
    except Exception:
        print("Błąd zapisu użytego tokena")

### ### ### ### ### ### ### ### ###
        
# def wyświetl_dane():
#     global driver , token_z_pliku , petla_nr , haslo_twit  , nick , mail , haslo_mail , nowe_haslo_twit , nowy_token
#     print("F wyświetl dane\n")
#     time.sleep(1)

    # try:
    #     print("próbuje pobrać nowe hasło")
    #     nowe_haslo_twit = logowanie_twitter(driver)
    #     print(f"Nowe hasło to: {nowe_haslo_twit}")
        
    #     print("próbuje pobrać nowy token")
    #     nowy_token = pobierz_token(driver)
    #     print(f"Nowy token to: {nowy_token}")
        
    #     print("Sukces !")

    # except Exception:
    #     print("Nie pobrano danych !!!!!!")

    # try: ########################################## stara wersja dla zmiennych lokalnych - usunąć jak działa
    #     print("próbuje pobrać nowe hasło)")
    #     nowe_haslo_twit = logowanie_twitter(driver) #             nowe_haslo_twit = zapisz_dane()
    #     print("próbuje pobrać nowy token)")
    #     nowy_token = pobierz_token(driver)#             nowy_token = zapisz_dane()
    #     print("Sukces !")
    # except Exception:
    #     print("Nie pobrano danych !!!!!!")



    # try:

    #     with open("DANE.txt", "a", encoding="utf-8") as output:
    #         output.write(f"NICK           : {nick[petla_nr]} \n")

    #         output.write(f"TOKEN Z PLIKU  : {token_z_pliku[petla_nr]} \n")
    #         print("NOWY TOKEN     : ",nowy_token, "\n")           
    #         output.write(f"HASŁO z pliku  : {haslo_twit[petla_nr]} \n")
    #         print("NOWY TOKEN     : ",nowe_haslo_twit, "\n")
    #         output.write(f"EM@IL          : {mail[petla_nr]} \n")
    #         output.write(f"HASŁO @        : {haslo_mail[petla_nr]} \n")



    #     print("Wzór pliku do zapisu:")
    #     print(f"{nick[petla_nr]} : {nowe_haslo_twit} : {nowy_token} : {mail[petla_nr]} : {haslo_mail[petla_nr]}")
        
    # except Exception:
    #     print("Błąd wyświetlania danych")
    #     winsound.Beep(3000, 100)
    #     print("czekam 10....")
    #     time.sleep(10)        # przerwa po błędzie
    # print("-----------------------------------------------")
    # winsound.Beep(420, 100)
    # time.sleep(1)   

### ### ### ### ### ### ### ### ### w zapisie można zrobic rakie wyświetlanie importu jak w wyświetlaniu
    

        
def pobierz_token():
    global driver, nowy_token # token_z_pliku , petla_nr , haslo_twit  , nick , mail , haslo_mail , nowe_haslo_twit
    print("F - pobierz token")
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    
    try:
        cookies = driver.get_cookies() ####### chuj wi co to za funckcja --- 

        print("czyszcze nowy_token")
        nowy_token = 0


        for cookie in cookies:
            if cookie['name'] == 'auth_token':
                nowy_token = cookie['value']
                print("pobrano nowy token !")
                break
                

        if nowy_token:
            print("NOWY TOKEN POBRANY POPRAWINE !")
            print("Token z pliku             :  ",token_z_pliku[0])
            print("Nowy token                :  ", nowy_token)
            # winsound.Beep(420 , 200)
            return
    except Exception:
        print("Błąd pobierania tokena !!!!")
        # winsound.Beep(2500 , 2500)
        # time.sleep(5)

### ### ### ### ### ### ### ### ###

def aktualizuj_token():
    global driver , token_z_pliku
    print("F - aktualizuj token")
    try:        
        print("Zmieniam token...") 
        print("Token z pliku             : ",token_z_pliku[0])
        print("Nowy token                : ",nowy_token)
        time.sleep(2)
        if nowy_token != 0:
            token_z_pliku[0] = nowy_token
        else:
            print("Brak nowego tokenu !")
        print("Sprawdź poprawność danych ! ")
        print("Token z pliku             : ",token_z_pliku[0])
        print("Nowy token                : ",nowy_token)
    except Exception:
        print("błąd aktualizacji tokenu !!")

### ### ### ### ### ### ### ### ###




def zapisz_dane():
    global driver , petla_nr , token_z_pliku , nowy_token , haslo_twit , nowe_haslo_twit , nick , mail , haslo_mail
# Funkcja do odczytania danych z pliku i usunięcia pierwszej linii
    status = "---GIT---"


# Funkcja do dodania nowej linii do pliku
    try:
        # nick = f'nick{petla_nr}'
        # haslo_twit = f'haslo_twit{petla_nr}'
        # token_z_pliku = f'token_z_pliku{petla_nr}'
        # mail = f'mail{petla_nr}'
        # haslo_mail = f'haslo_mail{petla_nr}'

        # new_line = (f"\n{nick}:{haslo_twit}:{token_z_pliku}:{mail}:{haslo_mail}")

        with open('dane2.txt', 'a',encoding = "utf-8") as file:
            file.write("\n"+f"{nick[0]}"+":"+f"{haslo_twit[0]}"+":"+f"{token_z_pliku[0]}"+":"+f"{mail[0]}"+":"+f"{haslo_mail[0]}"+":"+f"{status}") # +"error" if error =0 -> error = ""  ### ???????????????????????????????????????????

        time.sleep(1)
        print('\n\nLinia zapisana:')
        print(f"{nick[0]}"+":"+f"{haslo_twit[0]}"+":"+f"{token_z_pliku[0]}"+":"+f"{mail[0]}"+":"+f"{haslo_mail[0]}"+":"+f"{status}") ### ???????????????????????????????????????????
        print('\n---------------------------------------------------------------------------------------------------------------------\n')
        # with open('dane2.txt', 'r') as file:
        #     lines = file.readlines()

        # # Zapisz, co zostanie usunięte
        # removed_line = lines.pop(0)

        # with open('dane2.txt', 'w') as file:
        #     file.writelines(lines)
    except Exception:
        print("BŁĄD ZAPISU !!!!!!!!!!!!!!!! - prawdopodobnie zrobiło wszystkie i dlatego wyjebało...")
        return

# Główna funkcja skryptu

     # Możesz zmienić tę wartość lub zaimplementować jako argument funkcji

    # Usuń pierwszą linię i dodaj nową


    # print('Linia usunięta:')
    # print(removed_line)
    
    #if removed_line == f"{nick[petla_nr]}"+":"+f"{haslo_twit[petla_nr]}"+":"+f"{token_z_pliku[petla_nr]}"+":"+f"{mail[petla_nr]}"+":"+f"{haslo_mail[petla_nr]}"

    return


    # print("F - zapisz dane")


    # try:
    #     nowy_token = 0 # zeruje po aktualizacji  zeby nie bylo bledow - po aktualizacji oba są takie same !
    #     # nowe_haslo_twit = 0  # J. W.
    #     with open('out.txt', 'w') as file:
    #         for i in range(len(nick)):
    #             line = f"{nick[i]}:{haslo_twit[i]}:{token_z_pliku[i]}:{mail[i]}:{haslo_mail[i]}\n"
    #             file.write(line)

    #     # Wyświetlenie zapisanych danych
    #     with open('out.txt', 'r') as file:
    #         saved_data = file.read()
    #         print(saved_data)
                
    # except Exception:
    #     print("BŁĄD ZAPISU . . . .")
    #     winsound.Beep(5000, 420)
    #     # przerwa po błędzie
    #     time.sleep(1)
    # winsound.Beep(200, 420)
    
    #try:
        #print("próbuje pobrać nowe hasło)")
        #nowe_haslo_twit = logowanie_twitter(driver) #             nowe_haslo_twit = zapisz_dane()
        #print("próbuje pobrać nowy token)")
        #nowy_token = pobierz_token(driver)#             nowy_token = zapisz_dane()
        #print("Sukces !")
    #except Exception:
        #print("Nie pobrano danych !!!!!!")
    # try: 
    #     with open("OUT77-SpeedBot.txt", "a", encoding="utf-8") as output:
    #         time.sleep(1)
    #         # output.write(f"NICK           : {nick[petla_nr]} \n")

    #         output.write(f"{nick[petla_nr]}:{nowe_haslo_twit}:{nowy_token}:{mail[petla_nr]}:{haslo_mail[petla_nr]}")

    #         # linia_do_zapisu = (f"{nick[petla_nr]}:{nowe_haslo_twit}:{nowy_token}:{mail[petla_nr]}:{haslo_mail[petla_nr]}     ")  #tu może \n
    #         # output.write(linia_do_zapisu)
    #         time.sleep(1)



    # try:
    #     with open("OUT77-SpeedBot.txt", "a", encoding="utf-8") as output:
    #         # Prepare the line to be written in the desired format
    #         line_to_write = f"{nick[petla_nr]}:{nowe_haslo_twit}:{nowy_token}:{mail[petla_nr]}:{haslo_mail[petla_nr]}\n"
            
    #         # Write the line to the file
    #         output.write(line_to_write)
            
    #         # Wait for 2 seconds before proceeding
    #         time.sleep(2)
            
    #         print("\nDane zostały przetworzone i zapisane.")
    # except Exception as e:
    #     print(f"BŁAD ZAPISU DANYCH !!!!!\nError: {str(e)}")














    #         print("\nDane zostały przetworzone i zapisane.")
    # except Exception:
    #     print("BŁAD ZAPISU DANYCH !!!!!")

    # winsound.Beep(420, 100)
    # time.sleep(1)
    # return nowy_token , nowe_haslo_twit
    
### ### ### ### ### ### ### ### ### co capchy dolożyć lambda v3 !!       i może od razu zablokowanie konta !!! - przyspieszyć i usunąć wszelkie refreshe @


        
### ### ### ### ### ### ### ### ###  do capchy może jeszcze check czy zalogowano - jak tak to it jak nie to powrót do logowani albo gdzies indzie cos z tą flagą...

##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ## 


# def block():
#     Your account is suspended and is not permitted to perform this action.
#     Sorry, you are rate limited. Please wait a few moments then try again.
#     Pomóż nam zabezpieczyć Twoje konto.




    # Zweryfikuj swoją tożsamość, wprowadzając adres e-mail powiązany z Twoim kontem w serwisie X.
    # @r******.**


def problem_check():
    print("F - problem check - ")
   

    # if driver.current_url == "https://twitter.com/account/access":
    #     print("Jesteśmy na stronie blokady")
    #     time.sleep(1)
    #     capcha()
    # else:
    #     print("To nie strona blokady")


    try:
        print("zaczynam sprawdzać słowa...")
        wait = WebDriverWait(driver, 2)  # Ustawienie maksymalnego czasu oczekiwania
        locators = [
######################################################################################################## SUSPEND
            ("//*[contains(text(), 'Your account is suspended')]", suspend),
            ("//*[contains(text(), 'Your account may not be allowed')]", logowanie_twitter),
            ("//*[contains(text(), 'Chcesz się najpierw zalogować?')]", logowanie_twitter),

######################################################################################################## CAPCHA
            ("//*[contains(text(), 'Authenticate')]", capcha),
            ("//*[contains(text(), 'Your account has been locked')]", capcha),
            # ("//*[contains(text(), 'Authenticate your account')]", capcha),
            ("//*[contains(text(), 'Options')]", capcha),


                                                                                        #### UNLOCK
            # ("//*[contains(text(), 'Thank you for addressing this issue.')]", capcha),
            ("//*[contains(text(), 'Account unlocked.')]", capcha),


######################################################################################################## RELOG
            #("//*[contains(text(), 'Wygląda na to, że taka strona nie istnieje')]", logowanie_twitter),
            ("//*[contains(text(), 'Unlock more on X')]", unlock),


# ######################################################################################################## BAN 3 DNI
#             ("//*[contains(text(), '3 days and 0 hours')]", ban3dni),
            ("//*[contains(text(), 'temporarily limited')]", ban3dni),
#             ("//*[contains(text(), 'Your account appears to be in violation of X's')]", ban3dni),
#             ("//*[contains(text(), 'Your ability to follow, like, and repost will be limited for the following period of time')]", ban3dni),
# ######################################################################################################## WPISZ MAIL
            ("//*[contains(text(), 'Zweryfikuj swoją tożsamość, wprowadzając adres e-mail ')]", wpisz_mail), # tu dać wpisz_mail

# ######################################################################################################## BLOCK 
            ("//*[contains(text(), 'Sprawdź swój e-mail')]", block),
            #("//*[contains(text(), 'Aby chronić Twoje konto przed podejrzanymi')]", block),
#             ("//*[contains(text(), 'blokada konta')]", block),

# ######################################################################################################## BLOCK 
#             ("//*[contains(text(), 'Wygląda na to, że taka strona nie istnieje.')]", refresh),
#             ("//*[contains(text(), 'Spróbuj wyszukać coś innego.')]",  refresh  ),
######################################################################################################## GIT !!
            ("//*[contains(text(), 'Select a message')]", logowanie_twitter),
            ("//*[contains(text(), 'Welcome to your inbox!')]", logowanie_twitter),            
            ("//*[contains(text(), 'Bądź na bieżąco')]",  logowanie_twitter),



        ]

        for xpath, action in locators:
            try:
                element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                print(f"Znaleziono tekst: {element.text}")  # Wyświetlanie znalezionego tekstu
                # time.sleep(1)
                action()
                #time.sleep(60)  # Opcjonalnie, jeśli potrzebujesz opóźnienia
                return
            except TimeoutException:
                continue  # Jeśli element nie został znaleziony, kontynuuj pętlę

        print("Żaden z określonych tekstów nie został znaleziony na stronie.")

    except Exception:
        print("Wywaliło problem check")
    print("Zamykam problem check")





















    #     wait = WebDriverWait(driver, 5)  # Ustawienie maksymalnego czasu oczekiwania na 3 sekundy
    #     locators = [
    #         (By.XPATH, "//*[contains(text(), 'Authenticate')]"),
    #         (By.XPATH, "//*[contains(text(), 'Your account has been locked')]"),


    #         (By.XPATH, "//*[contains(text(), '3 days and 0 hours')]"),
    #         (By.XPATH, "//*[contains(text(), 'We've temporarily limited some of your account features')]"),
    #         (By.XPATH, "//*[contains(text(), 'Your account appears to be in violation of X's')]"),
    #         (By.XPATH, "//*[contains(text(), 'Your ability to follow, like, and repost will be limited for the following period of time')]"),
    #         (By.XPATH, "//*[contains(text(), 'wpisz swój adres emali')]"),
    #         (By.XPATH, "//*[contains(text(), 'brudas zablokował konto')]"),
    #         (By.XPATH, "//*[contains(text(), 'Sprawdź swój e-mail')]"),
    #         (By.XPATH, "//*[contains(text(), 'Aby chronić Twoje konto przed podejrzanymi działaniami, wysłaliśmy kod potwierdzający')]"),
    #         (By.XPATH, "//*[contains(text(), 'blokada konta')]"),

    #         (By.XPATH, "//*[contains(text(), 'Thank you for addressing this issue.')]"),
    #         (By.XPATH, "//*[contains(text(), 'Account unlocked.')]"),
            
            
    #     ]

    #     for locator in locators:
    #         try:
    #             wait.until(lambda d: any(len(d.find_elements(*locator)) > 0 for locator in locators))
    #             if driver.current_url == "https://twitter.com/account/access" or \
    #                 locator[1] == "//*[contains(text(), 'Account unlocked.')]" or \
    #                 locator[1] == "//*[contains(text(), 'Thank you for addressing this issue.')]":
    #                 print("ODPAL CAPCHA !!!")
    #                 time.sleep(60)
    #                 return
                




    #             elif locator[1] == "//*[contains(text(), '3 days and 0 hours')]" or \
    #                 locator[1] == "//*[contains(text(), 'We've temporarily limited some of your account features')]" or \
    #                 locator[1] == "//*[contains(text(), 'Your account appears to be in violation of X's')]" or \
    #                 locator[1] == "//*[contains(text(), 'Your ability to follow, like, and repost will be limited for the following period of time')]":
    #                 time.sleep(60)
    #                 ban3dni()
    #                 return
    #             elif locator[1] == "//*[contains(text(), 'wpisz swój adres emali')]" or \
    #                 locator[1] == "//*[contains(text(), 'brudas zablokował konto')]":
    #                 time.sleep(60)
    #                 wpisz_mail()
    #                 return
    #             elif locator[1] == "//*[contains(text(), 'Sprawdź swój e-mail')]" or \
    #                 locator[1] == "//*[contains(text(), 'Aby chronić Twoje konto przed podejrzanymi działaniami, wysłaliśmy kod potwierdzający')]" or \
    #                 locator[1] == "//*[contains(text(), 'blokada konta')]":
    #                 block()
    #                 return
    #         except TimeoutException:
    #             # Jeśli element nie pojawi się w ciągu 3 sekund, ignoruj i kontynuuj pętlę
    #             continue

    #     print("LAMBDAv5 - Żaden z określonych tekstów nie został znaleziony na stronie.")
    # except Exception:
    #     print("zamykam LAMBDAv5")

def unlock():
        unlock_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div'))
        )
        unlock_button.click()
        time.sleep(1)


def suspend(): ## NA RAZIE ZAMYKAM NA CHAMA / dodać info o perma blocku...
    global driver , suspended , max_suspended
    print("F - suspend")
    try:
        time.sleep(1)
        status = "SUSPEND"
        time.sleep(1)
        with open('dane2.txt', 'a',encoding = "utf-8") as file:
                file.write("\n"+f"{nick[0]}"+":"+f"{haslo_twit[0]}"+":"+f"{token_z_pliku[0]}"+":"+f"{mail[0]}"+":"+f"{haslo_mail[0]}"+":"+f"{status}") # +"erro

        print("ZAMYKAM PRZEGLĄDARKE")
        driver.close()
    except Exception:
        print("Błąd zapisu użytego tokenu dla niewykonanej capchy")
        driver.close()






    
    # try:
    #     print("- - - Szukam SUSPEND - - - ")
    #     suspended = suspended +1
    #     WebDriverWait(driver, 3).until(
    #         lambda d: any(
    #             len(d.find_elements(locator_type, locator)) > 0
    #             for locator_type, locator in [
    #                 #(By.CSS_SELECTOR, 'div#react-root div.css-1rynq56.r-bcqeeo.r-qvutc0'),
    #                 #(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div'),
                    
    #                 (By.XPATH, '//span[contains(text(), "Your account may not be allowed")]'),
    #                 (By.XPATH, '//span[contains(text(), "Your account may not be allowed to perform this action. Please refresh the page and try again")]'),
    #                 #(By.XPATH, '//span[contains(text(), "Wygląda na to, że taka strona nie istnieje.")]'), # TO CHYB GDZIEŚ INDZIEJ ?!
    #                 #(By.XPATH, '//span[contains(text(), "Spróbuj wyszukać coś innego.")]'),                    
    #                 #(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div'),
    #                 #(By.XPATH, '//span[contains(text(), "Sprawdź swój e-mail")]'),                                          #################################### to do kodu z maila
    #                 #(By.XPATH, '//span[contains(text(), "Aby chronić Twoje konto przed podejrzanymi działaniami,")]'),      #################################### to do kodu z maila
    #                 #(By.XPATH, '//span[contains(text(), "wysłaliśmy kod potwierdzający na")]'),                             #################################### to do kodu z maila


                    
                    
    #                 #(By.XPATH, '//div[contains(@class,'r-bcqeeo')]')
    #                 # (By.NAME, 'session[username_or_email]'),
    #                 # (By.NAME, 'session[password]'),
    #             ]
    #         )
    #     )
    #     #funkcja_po_logowaniu()  # Wywołanie funkcji po spełnieniu warunku

    #     print("Znaleziono -SUSPEND- przez lambda v4 !")
    #     time.sleep(1)

    #     if suspended < max_suspended:
    #     # time.sleep(1)
    #         driver.refresh()
    #         time.sleep(5)
    #     #driver.get()
    #     else:
    #         if suspend < max_suspended +1:
    #             driver.get(link)
    #         else:
    #             return   

    #     # print(" - - - Suspend ",suspended, "/  ",max_suspended," - - - " )
    #     # if suspended < max_suspended:

    #     #     time.sleep(2)
    #     #     print("przenosze do logowania")
    #     #     driver.refresh
    #     #     time.sleep(1)
    #     # else: 
    #     #     print("tu nie wiem co else.....")
    #     #     #logowanie_twitter()
    #     #     # driver.quit()

    # except TimeoutException:
    #     print("Nie udało się znaleźć prze lambda v4")






def capcha():
    print("F - capcha")
    global driver , token_z_pliku , petla_nr , haslo_twit  , nick , mail , haslo_mail , nowe_haslo_twit , nowy_token , link
    
    # try:

    #     wait = WebDriverWait(driver, 3)  # Ustawienie maksymalnego czasu oczekiwania
    #     locators = [
    #         (By.XPATH, "//*[contains(text(), 'Authenticate')]"),
    #         (By.XPATH, "//*[contains(text(), 'Your account has been locked')]"),
    #         # (By.XPATH, "//*[contains(text(), 'We found some unusual activity on your account.')]"),
    #         # (By.XPATH, "//*[contains(text(), 'To unlock your account, you must do the following:')]"),
    #         # (By.XPATH, "//*[contains(text(), 'you to confirm your identity before you can continue using X')]"),
    #         # (By.XPATH, "//*[contains(text(), 'Authenticate your account')]"),
    #         # (By.XPATH, "//*[contains(text(), 'We need to make sure that you’re a real person.')]"),

    #         ### UNLOCK ###

    #         (By.XPATH, "//*[contains(text(), 'Account unlocked.')]"),
    #         (By.XPATH, "//*[contains(text(), 'Zaloguj się do serwisu X')]"),
    #         (By.XPATH, "//*[contains(text(), 'Thank you for addressing this issue.')]"),
    #         (By.XPATH, "//*[contains(text(), 'Your account is now available for use.')]"),



    #     ]

    #     for locator in locators:
    #         try:
    #             wait.until(lambda d: any(len(d.find_elements(*locator)) > 0 for locator in locators))
    #             if driver.current_url == "https://twitter.com/account/access":
    #                 print(" - - - - - - - - - CapHa !!! - - - - - - - - -")
    #                 wait = WebDriverWait(driver, 5)

    #                 try:
    #                     # Oczekiwanie na przycisk z określonym XPath
    #                     # Zmien 'tuwklej.div' na faktyczny XPath przycisku
    #                     przycisk_xpath = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/form/input[6]')))
    #                     print("Znaleziono przycisk po XPath.")
    #                     przycisk_xpath.click()
    #                 except:
    #                     print("Nie znaleziono przycisku po XPath, szukam przycisku po tekście.")
    #                     # Jeśli nie uda się znaleźć przycisku po XPath, próbujemy znaleźć przycisk zawierający napis "Continue to X"
    #                     try:
    #                         przycisk_tekst = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continue to X')]")))
    #                         print("Znaleziono przycisk 'Continue to X'.")
    #                         przycisk_tekst.click()
    #                     except:
    #                         print("Nie znaleziono przycisku 'Continue to X'.")

    #                 continue
    #             elif locator[1] == "//*[contains(text(), 'Account unlocked.')]" or \
    #                 locator[1] == "//*[contains(text(), 'Zaloguj się do serwisu X')]" or \
    #                 locator[1] == "//*[contains(text(), 'Thank you for addressing this issue.')]" or \
    #                 locator[1] == "//*[contains(text(), 'Your account is now available for use.')]":
    #                 print("Konto zostało odblokowane. Kontynuuję skrypt.")
    #                 return
                    
                
    #             frequency = 420  # Częstotliwość dźwięku
    #             duration = 420  # Czas trwania dźwięku w ms
    #             winsound.Beep(frequency, duration)
    #             time.sleep(5) 
    #         except TimeoutException:
    #             # Jeśli element nie pojawi się w ciągu 3 sekund, ignoruj i kontynuuj pętlę
    #             continue

    #     print("LAMBDAv5 C - Żaden z określonych tekstów nie został znaleziony na stronie.")
    # except Exception:
    #     print("zamykam LAMBDAv5 - C")
    #     print("Capcha nie wykonana.... ;( ")
          
    #     print("zapisuje aktualny token do pliku OUT-capcha2do.txt")
    #     try:
    #         with open("OUT-capcha2do.txt", "a") as file:
    #             file.write(token_z_pliku[petla_nr]+ "\n")
    #         print("Token zapisany poprawnie")
    #         print("ZAMYKAM PRZEGLĄDARKE")
    #         #spróbować rise
    #         driver.close()
    #     except Exception:
    #         print("Błąd zapisu użytego tokena dla niewykonanej capchy")
    #         print("ZAMYKAM PRZEGLĄDARKE")
    #         #spróbować rise
    #         driver.close()


    # #### v5 ###  




##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ## 

    try:

        if "https://twitter.com/account/access" in driver.current_url:
            print(" - - - - - - CapHa po adresie strony - - - - - - - -")
            try:
                
                


                #time.sleep(1)
                WebDriverWait(driver, 3).until(
                    lambda driver: any([
                        driver.find_elements(By.XPATH, "//*[contains(text(), 'Authenticate')]"),
                        driver.find_elements(By.XPATH, "//*[contains(text(), 'Your account has been locked')]"),
                        #driver.find_elements(By.XPATH, "//*[contains(text(), 'Sprawdź swój e-mail')]"),
                    ]) or "https://twitter.com/account/access" in driver.current_url
                )
                print(" - - - - - - - - - CapHa !!! - - - - - - - - -")
            

            except TimeoutException:
                print("Nie było CapCha !!! \n")


################################################################################################################################# 
        czas_na_capcha = 5 #####################################################################################################xxx
#################################################################################################################################
        start_time = time.time()

        end_time = start_time + czas_na_capcha 

      
        print("Startuje timer - CZAS ",czas_na_capcha," sekund !")
        while time.time() < end_time:

            ### tu można dorobić złoty strzał jak pojawi się (1 of 1) to klika przycisk Submit, lub 
            ### /html/body/div/div/div[1]/div/button

            try:
                # Sprawdzanie, czy konto zostało odblokowane
                odblokowano = WebDriverWait(driver, 10).until(
                    lambda driver: driver.find_element(By.XPATH, "//*[contains(text(), 'Account unlocked.')]") #or
                                    #driver.find_element(By.XPATH, "//*[contains(text(), 'Zaloguj się do serwisu X')]") ## nie wiem czy to dobre...
                )
                if odblokowano:
                    print("Konto zostało odblokowane. Kontynuuję skrypt.")
                    break  # Przerywamy pętlę, jeśli konto zostało odblokowane
            except TimeoutException:
                # Jeśli nie wykryto komunikatu o odblokowaniu, generujemy dźwięk
                frequency = 420  # Częstotliwość dźwięku
                duration = 420  # Czas trwania dźwięku w ms
                winsound.Beep(frequency, duration)
                time.sleep(5)  # Odczekujemy 5 sekund przed kolejnym sprawdzeniem


##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  


            #try:
            # time.sleep(3)
        # print("Capcha nie wykonana.... ;( ")
        

                



##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ##  ## 
                    



        wait = WebDriverWait(driver, 5)
    
        try:
            # Oczekiwanie na przycisk z określonym XPath
            # Zmien 'tuwklej.div' na faktyczny XPath przycisku
            przycisk_xpath = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/form/input[6]')))
            print("Znaleziono przycisk po XPath.")
            przycisk_xpath.click()
        except:
            print("Nie znaleziono przycisku po XPath, szukam przycisku po tekście.")
            # Jeśli nie uda się znaleźć przycisku po XPath, próbujemy znaleźć przycisk zawierający napis "Continue to X"
            try:
                przycisk_tekst = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continue to X')]")))
                print("Znaleziono przycisk 'Continue to X'.")
                przycisk_tekst.click()
                print("'Continue to X'. !!!")

            except:
                print("Nie znaleziono przycisku 'Continue to X albo start'.")
                print("zapisuje aktualny token do pliku OUT-capcha2do.txt")
                try:
                    status = "CAPCHA"

                    with open('dane2.txt', 'a',encoding = "utf-8") as file:
                            file.write("\n"+f"{nick[0]}"+":"+f"{haslo_twit[0]}"+":"+f"{token_z_pliku[0]}"+":"+f"{mail[0]}"+":"+f"{haslo_mail[0]}"+":"+f"{status}") # +"erro

                    print("ZAMYKAM PRZEGLĄDARKE")
                    driver.close()
                except Exception:
                    print("Błąd zapisu użytego tokena dla niewykonanej capchy")
                    print("zapisuje dane i zamykam przeglądarke...")
                    
                    
                    driver.close()
        ### dodaje start kurwa !
        try:
            time.sleep(2)
            przycisk_start = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/form/input[6]')))
            przycisk_start.click()
            time.sleep(2)
            print("'START'. !!!")
        except Exception:
            print("Nie kliknięto start")            
        ###
        print("Zamykam CAPCHA !") 
        time.sleep(1)
        driver.get(link)
        return
    except TimeoutException:
        print("Nie znaleziono komunikatu o zablokowaniu konta.")





def wpisz_mail():
    print("F - wpisz mail")
    global driver , mail , petla_nr
    driver.close()
# /html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input - input z firefox

    # try:
    #                         # Wpisz dane do pola tekstowego
    #     pole_input = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    #     # pole_input.clear()  # Czyści pole tekstowe przed wpisaniem nowych danych
    #     print("znaleziono pole na maila...")
    #     time.sleep(1)
    # except Exception:
    #     print("nie znaleziono pola na maila...")


    # try:


    #     print("Wpisuje: ", mail[petla_nr])
    #     time.sleep(1)
    #     pole_input.send_keys(mail[petla_nr])
    #     time.sleep(1)  # Odczekuje 2 sekundy
        
    # except Exception:
    #     print("nie wpisano nicku !!!!")   

    
    # try:
    # #     print("- - - Szukam pola na wpisanie maila - - - ")
        
    # #     pole_maila = WebDriverWait(driver, 3).until(
    # #         EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    # #     )
    # #         # pole_hasla.clear()
    # #     pole_maila.send_keys(mail[petla_nr])
    # #     print("Wpisuje ----> ", mail[petla_nr])
    # #         # Znajdź i kliknij przycisk logowania
    #     przycisk_dalej = WebDriverWait(driver, 3).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span'))
    #     )
    #     print("klikam...")
    #     przycisk_dalej.click()
    #     time.sleep(1)


    # except Exception:
    #     print("Nie kliknięto....")










def ban3dni():
    print("F - ban3dni")
    time.sleep(1)
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        status = now
        time.sleep(1)
        with open('dane2.txt', 'a',encoding = "utf-8") as file:
                file.write("\n"+f"{nick[0]}"+":"+f"{haslo_twit[0]}"+":"+f"{token_z_pliku[0]}"+":"+f"{mail[0]}"+":"+f"{haslo_mail[0]}"+":"+f"{status}") # +"erro

        print("ZAMYKAM PRZEGLĄDARKE")
        driver.close()
    except Exception:
        print("Błąd zapisu ban3dni !!!!!!")
        driver.close()



    # driver.quit()  # Zamykanie przeglądarki
    #raise  # Zakończenie pętli, po znalezieniu pierwszego pasującego tekstu





def block(): ## NA RAZIE ZAMYKAM NA CHAMA / dodać info o perma blocku...
    global driver , suspended , max_suspended
    print("F - block")
    time.sleep(1)
    try:
        time.sleep(1)
        status = "BAN"
        time.sleep(1)
        with open('dane2.txt', 'a',encoding = "utf-8") as file:
                file.write("\n"+f"{nick[0]}"+":"+f"{haslo_twit[0]}"+":"+f"{token_z_pliku[0]}"+":"+f"{mail[0]}"+":"+f"{haslo_mail[0]}"+":"+f"{status}") # +"erro

        print("ZAMYKAM PRZEGLĄDARKE")
        driver.close()
    except Exception:
        print("Błąd zapisu użytego tokenu dla niewykonanej capchy")
        driver.close()



def refresh():
    print("F - Refresh")
    driver.refresh()
    time.sleep(3)
    driver.get(link)
    time.sleep(1)


       
### ### ### ### ### ### ### ### ###

def wpisz_haslo():
    global driver , nowe_haslo_twit  ,  zalogowano , max_prob_hasla , licznik_hasla
    print("F wpisz hasło...")
    
    # haslo_twit[petla_nr] =   tu chyba cos dopisać
    licznik_hasla = 0
    
    
    
    while licznik_hasla  < max_prob_hasla:

        licznik_hasla = licznik_hasla +1
        print("wpisywanie hasła numer: ", licznik_hasla, " / " ,max_prob_hasla, "\n")
        
        
        try:
             
            WebDriverWait(driver, 2).until(
                lambda d: any(
                    len(d.find_elements(locator_type, locator)) > 0
                    for locator_type, locator in [
                        (By.CSS_SELECTOR, 'input[name="session[username_or_email]"]'),
                        (By.CSS_SELECTOR, 'input[name="session[password]"]'),
                        (By.XPATH, '//span[contains(text(), "Select a message")]'),
                        (By.XPATH, '//span[contains(text(), "Welcome to your inbox!")]'),
                        (By.XPATH, "//a[@href='/messages']"),
                        # (By.XPATH, '//div[contains(text(), "Wprowadź swoje hasło")]'),
                        # (By.NAME, 'session[username_or_email]'),
                        # (By.NAME, 'session[password]'),
                    ]
                ) or "https://twitter.com/messages" in driver.current_url
            )
            #funkcja_po_logowaniu()  # Wywołanie funkcji po spełnieniu warunku

            print("Zalogowano poprawnie, nie wpisuje hasła !")
            return
        except TimeoutException:
            print("Nie znaleziono messages...")
            
            print("Ustawiam flage na FALSE !")
            zalogowano = False  # Flaga do śledzenia, czy logowanie się powiodło

            for nowe_haslo_twit in hasla_do_sprawdzenia:
                print("\nWpisuje hasło-----------> ", nowe_haslo_twit , " <-----------")
                
                # Znajdź pole hasła i wpisz hasło
                pole_hasla = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
                )
                # pole_hasla.clear()
                pole_hasla.send_keys(nowe_haslo_twit)
                print("wpisuje...")
                # Znajdź i kliknij przycisk logowania
                przycisk_zaloguj = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'))
                )
                print("klikam...")
                time.sleep(1)
                przycisk_zaloguj.click()
                time.sleep(2 )
               
                try:
                    print("sprawdzam czy zalogowano !") ## NNN nowe słowa do messages !
                    
                    WebDriverWait(driver, 3).until(
                        lambda driver: driver.find_element(By.XPATH, "//*[contains(text(), 'Welcome to your inbox!')]") or
                                    driver.find_element(By.XPATH, "//*[contains(text(), 'Select a message')]") or
                                    driver.find_element(By.XPATH, "//*[contains(text(), 'Choose from your existing conversations, start')]") or
                                    driver.find_element(By.XPATH, "//*[contains(text(), 'Drop a line, share posts and more with private')]")
                                    
                                    
                                    #driver.find_element(By.XPATH, "//a[@href='/messages']") or
                                    # driver.find_element(By.XPATH, "//a[@href='/home']") or
                                    
                                    #driver.find_element(By.XPATH, "//*[contains(text(), 'Messages')]")
                    )
                    print(f"\nZalogowano przy użyciu hasła: ---> {nowe_haslo_twit}\n")
                    zalogowano = True
                    # try:
                    print("\n- - - SPRAWDŹ POPRAWNOŚĆ DANYCH  - - -")
                    time.sleep(1)
                    print("\nHASŁO Z PLIKU : ",haslo_twit[0],)
                    print("\nNOWE HASŁO    : ",nowe_haslo_twit,)
                    print("\nAKTUALIZUJE HASŁO_Z_PLIKU Twitter...")
                    time.sleep(1)
                    haslo_twit[petla_nr] = nowe_haslo_twit
                    time.sleep(1)
                    print("\nHASŁO Z PLIKU : ",haslo_twit[0],)
                    print("\nNOWE HASŁO    : ",nowe_haslo_twit,)
                    # time.sleep(1)
            #     pobierz_token()
            #     time.sleep(1)
            #     aktualizuj_token
            #     time.sleep(1)
            #     print('WSZYSTKIE DANE ZAKTUALIZOWANE POPRAWNIE !!!')
            #     print('Zapisuje do plik...')
            #     zapisz_dane()
            #     time.sleep(1)
                    print("\n - - - ZAKTUALIZOWANO - - - ! \n")
                    # break
                    return True
                # except Exception:
                #     print("WYJEBAŁO AKTUALIZACJEDANYCH !!!")
            # Wyjście z pętli po udanym logowaniu
                except:
                    print("\nNie zalogowano hasłem: ", nowe_haslo_twit)
                    problem_check()
    # return        
    # if not zalogowano:
    #     print("Błąd logowania, sprawdź dane wejściowe !!!!!")
    #     with open('OUT-niezalogowane-hasłem.txt', 'a') as file:
    #         file.write(token_z_pliku[petla_nr]+ "\n")  # Zapisanie tokenu do pliku
    #     time.sleep(2)
    #     driver.close()
    #     return
    # else:
        # return
### ### ### ### ### ### ### ### ###
        
def wpisz_nick():
    global driver , max_prob_nicku , licznik_nicku
    print("F Wpisz nick ")
    time.sleep(1) 

    
    licznik_nicku = 0
    
    # licznik_nicku = 0



    
 # Maksymalna liczba prób logowania
    while licznik_nicku  < max_prob_nicku:
        
        licznik_nicku = licznik_nicku+1
        
        print("wpisywanie nicku numer: ", licznik_nicku, " / " ,max_prob_nicku, "\n")


        try:
            # problem_check()
            WebDriverWait(driver, 1).until(
                lambda d: any(
                    len(d.find_elements(locator_type, locator)) > 0
                    for locator_type, locator in [
                        #(By.CSS_SELECTOR, 'input[name="session[username_or_email]"]'),
                        #(By.CSS_SELECTOR, 'input[name="session[password]"]'),
                        (By.XPATH, '//span[contains(text(), "Select a message")]'),
                        (By.XPATH, '//span[contains(text(), "Welcome to your inbox!")]'),
                        #(By.XPATH, "//a[@href='/messages']"),
                        # (By.XPATH, '//div[contains(text(), "Wprowadź swoje hasło")]'),
                        # (By.NAME, 'session[username_or_email]'),
                        # (By.NAME, 'session[password]'),
                    ]
                ) or "https://twitter.com/messages" in driver.current_url
            )
            #funkcja_po_logowaniu()  # Wywołanie funkcji po spełnieniu warunku

            print("Nie wpisuje nicku, Twitter zalogowany")
            
            return
        except TimeoutException:
            print("Zaczynam wpisywanie nicku")



        try:
            WebDriverWait(driver, 2).until(
                lambda d: any(
                    len(d.find_elements(locator_type, locator)) > 0
                    for locator_type, locator in [
                        # Używamy bardziej ogólnych selektorów i unikamy bezpośrednich ścieżek
                        (By.CSS_SELECTOR, 'input[name="session[username_or_email]"]'),  # Pole nazwy użytkownika/emaila
                        (By.CSS_SELECTOR, 'input[name="session[password]"]'),  # Pole hasła
                        (By.XPATH, '//span[contains(text(), "Zaloguj się")]'),  # Przycisk logowania
                        (By.XPATH, '//span[contains(text(), "Nie pamiętasz hasła?")]'),  # Link do resetowania hasła
                        (By.XPATH, '//input[@aria-label="Phone, email, or username"]'),  # Alternatywne pole do wprowadzenia danych
                        (By.XPATH, '//div[contains(text(), "Wprowadź swoje hasło")]'),  # Tekst zachęcający do wprowadzenia hasła
                        (By.NAME, 'session[username_or_email]'),  # Alternatywny selektor dla nazwy użytkownika/emaila
                        (By.NAME, 'session[password]'),  # Alternatywny selektor dla hasła
                    ]
                ) or "https://twitter.com/i/flow/login?redirect_after_login=%2Fmessages" in driver.current_url
            )

            print("Znaleziono stronę do wpisania nicku")  # The element was found within the timeout period.
        except TimeoutException:
            print("NIE znaleziono strony do nicku !!!!")
            time.sleep(1)
            driver.get("https://twitter.com/messages")
            time.sleep(1)
            problem_check()
            return





        try:
                                # Wpisz dane do pola tekstowego
            pole_input = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            # pole_input.clear()  # Czyści pole tekstowe przed wpisaniem nowych danych
            print("znaleziono pole na nick...")
            pole_input.send_keys(nick[0])
            time.sleep(2)  # Odczekuje 2 sekundy
            print("Wpisano: ", nick[0])
        except Exception:
            print("nie wpisano nicku !!!!")   


    # try:        # Kliknij przycisk na podstawie XPath lub tekstu na przycisku
        try:
            przycisk_xpath = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
            print("kliknięto xpath")
            przycisk_xpath.click()
        except:
            przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'Dalej')]")
            print("kliknięto slowo Dalej")
            przycisk_tekst.click()

        WebDriverWait(driver, 3).until(
            lambda d: any([
                len(d.find_elements(By.XPATH, "//*[contains(text(), 'Wprowadź swoje hasło')]")) > 0,
                len(d.find_elements(By.XPATH, "//*[contains(text(), 'Nie pamiętasz hasła?')]")) > 0,
                len(d.find_elements(By.XPATH, f"//*[contains(text(), '{nick[0]}')]")) > 0
            ])
        )
        print("Znaleziono wprowadź hasło zamykam f NICK ")
        break

    print("NICK wpisany i zatwierdzony... \n")
    
    return
    # time.sleep(1)    
    # wpisz_haslo()
    # time.sleep(1)

### ### ### ### ### ### ### ### ###

def logowanie_twitter():
    global driver , token_z_pliku ,  haslo_twit  , nowe_haslo_twit , nowy_token , login_pass , zalogowano , licznik_prob_logowania , max_prob_logowania
    print("\nROZPOCZYNAM LOGOWANIE DO TWITTERA...\n")
    link = "https://twitter.com/messages"
    licznik_prob_logowania = 0
        
    # licznik_prob_logowania = 0
    try:
        cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]')
        cookies.click()
        print("zamknięto cookies")
    except Exception:
        print("Nie kliknięto zamknij cookies...")


    try:                                                                                                       # Maksymalna liczba prób logowania
        while licznik_prob_logowania < max_prob_logowania:
            licznik_prob_logowania = licznik_prob_logowania +1
            print("Logowanie numer", licznik_prob_logowania, " / " ,max_prob_logowania, "\n")  
            
            driver.get(link)  # Wejdź na stronę Twitter
            time.sleep(1) 

               
            WebDriverWait(driver, 1).until(
                lambda driver: driver.find_element(By.XPATH, "//*[contains(text(), 'Welcome to your inbox!')]") or
                            driver.find_element(By.XPATH, "//*[contains(text(), 'Select a message')]") #or
                            
                            #driver.find_element(By.XPATH, "//a[@href='/messages']") or
                            # driver.find_element(By.XPATH, "//a[@href='/home']") or
                            
                            #driver.find_element(By.XPATH, "//*[contains(text(), 'Messages')]")
            )
            # time.sleep(1)
            print("\nL - Zalogowano tokenem (przeszło na wiadomości/home) !!! ")
            #login_pass = login_pass + 1
            
            # try:        
            #     print("Token z pliku                    : ",token_z_pliku[0])
            #     print("Nowy token (powinno byc 0)       : ",nowy_token)
            #     # pobierz_token()
            # except Exception:
            #     print("L - Błąd wyświetlania tokenu !?")
            login_pass = login_pass +1
            zalogowano = True
            return
            ###
            ###
            ###

            


            

        # login_pass = login_pass +1
        # zalogowano = True
        # return  # Zakończenie funkcji po zalogowaniu tokenem
    except:
            # Wywołanie funkcji wpisz (zakładam, że wpisuje nick/login)
        time.sleep(1)
        print("L - nie zalogowało tokenem....")
        driver.refresh()
        time.sleep(1)


        try:
            print("L - przechodzę do wpisywania nicku")
            wpisz_nick()
            # time.sleep(1)
        except Exception:
            print("L - nie przeszło wpisywania nicku !")
            problem_check()



        try:
            print("L - przechodzę do wpisywania hasła")  
            wpisz_haslo()
            # time.sleep(1)
        except Exception:
            print("L - nie przeszło do wpisywania hasła !")#dupa
            problem_check()



        try:
            #driver.get('https://twitter.com/messages')
            time.sleep(1)
            # Sprawdź, czy udało się zalogować po wpisaniu loginu i hasła
            # WebDriverWait(driver, 5).until(
            #     lambda driver: driver.find_element(By.XPATH, "//*[contains(text(), 'Welcome to your inbox!')]") or
            #                 driver.find_element(By.XPATH, "//*[contains(text(), 'Select a message')]") or
            #                 driver.find_element(By.XPATH, "//*[contains(text(), 'Choose from your existing')]")
                            
            #                 #driver.find_element(By.XPATH, "//a[@href='/messages']") or
            #                 # driver.find_element(By.XPATH, "//a[@href='/home']") or
                            
            #                 #driver.find_element(By.XPATH, "//*[contains(text(), 'Messages')]")
            # )
            
            print("\nL - zalogowano poprawnie loginem - - - > ",nick[0] ," - - - hasłem - - - > ",nowe_haslo_twit) ############ tu przypisac wartość hasła !
            #nowe_haslo_twit = wpisz_haslo()

            # print("aktualizuje hasło")
            # login_cookies()
            # time.sleep(1) 
            # pobierz_token()
            # time.sleep(1) 
            

            #wyświetl_dane()  ## zapisujemy token / nie mamy dostępu do noweo hasła .
            
            # zapisz_dane() 
            


            login_pass = login_pass +1
            zalogowano = True
            return  # Zakończenie funkcji po zalogowaniu loginem i hasłem
        except:
            print("TWITTER NIEZALOGOWANY !!!!")                                                                                 ### DODAĆ ZAPIS NIEZALOGOWANYCH TWITTERÓW !
            
            licznik_prob_logowania = licznik_prob_logowania +1  # Zwiększenie licznika prób
            time.sleep(3)  # Krótka przerwa przed kolejną próbą
        problem_check()    
        not_logged = not_logged + 1
        print("Przekroczono maksymalną liczbę prób logowania.")
        try:
            status = "Niezalogowane!"

            with open('dane2.txt', 'a',encoding = "utf-8") as file:
                    file.write("\n"+f"{nick[0]}"+":"+f"{haslo_twit[0]}"+":"+f"{token_z_pliku[0]}"+":"+f"{mail[0]}"+":"+f"{haslo_mail[0]}"+":"+f"{status}") # +"erro

            time.sleep(1)
            driver.close()
            return
        except Exception:
            print("błąd zapisu - logowanie !!!")

### ### ### ### ### ### ### ### ###

def follow_twit():
    global driver , token_z_pliku , petla_nr , haslo_twit  , nick , mail , haslo_mail , nowe_haslo_twit , nowy_token
    time.sleep(1)
    driver.get("https://twitter.com/Bartosz416782")
    time.sleep(2)
    try:
        # Czekanie na przycisk "Follow" i jego kliknięcie
        follow_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div'))
        )
        follow_button.click()
        print("Przycisk 'Follow' został kliknięty.")
        # suspend()
        # capcha()
        # problem_check()
    except Exception as e:
        print("Nie udało się kliknąć przycisku 'Follow':", e)

    # Oczekiwanie na jakieś dodatkowe ładowanie strony itp.
    time.sleep(2)

### ### ### ### ### ### ### ### ###

def tweet_farmer(linki_txt='linki.txt'):
    global driver, token_z_pliku, petla_nr, haslo_twit, nick, mail, haslo_mail, nowe_haslo_twit, nowy_token , link , nr_posta
    time.sleep(1)
    # actions = ActionChains(driver)
        # Maksymalizacja okna przeglądarki
    driver.maximize_window()
    time.sleep(2)
    
    try:

        print("Sprawdzam linki.txt...")
        with open(linki_txt, 'r') as file:
            linki = [line.strip() for line in file.readlines()]
        
        time.sleep(1)
    except Exception:
        print(" - - - - - - - - - - - - - - - - KONIEC LINKÓW - - - - - - - - - - - - - - - - ")    

    match=0

    for index, link in enumerate(linki):
        #driver.get(link)

        print("\nZaładowano---> ", link, "\n")




        match = re.search(r'/(\d+)$', link)
        if match:
            nr_posta = match.group(1)
            print("Numer posta: ", nr_posta, "\n")
        else:
            print("Nie znaleziono numeru posta w URL.")



        #if zalogowano:
        try:
            mixer()
            tweet_post()
            driver.refresh()
            time.sleep(1)
            problem_check()

            
            # problem_check()

            tweet_retweet()

            tweet_like()
            # problem_check()
            
            # try:
            #     print("PC1in")
            #     problem_check()  ##############
            #     # capcha()
            #     time.sleep(1)
            # except Exception:
            #     print("PC1out")

            
            

            # try:
            #     print("PC2in")
            #     problem_check()  ##############
            #     # capcha()
            #     time.sleep(2)
            # except Exception:
            #     print("PC2out")



            # time.sleep(1)
            # problem_check()
            # #follower()
            # time.sleep(1)
        except:
            print("wyjebało farmera !!!!!!!!!!!!!!!!!")
            time.sleep(1)
            # logowanie_twitter()

            # else:
            #     print("bark flagi zalogowano - przechodzę do logowania")
        # Odczekaj między działaniami, ale nie zamykaj przeglądarki, dopóki nie jesteś na ostatnim linku.
        time.sleep(2)
        if index == len(linki) - 1:  # Jeśli to ostatni link, zamknij przeglądarkę.
            time.sleep(3)
            # # Opcjonalne czekanie między akcjami
            break
        time.sleep(3)
### ### ### ### ### ### ### ### ###

def tweet_like():  # Dodajemy argument 'link', który powinien być typu string (ciągiem znaków)
    global driver , token_z_pliku , petla_nr , haslo_twit  , nick , mail , haslo_mail , nowe_haslo_twit , nowy_token , link
    time.sleep(1)


    try:
        link = f"https://twitter.com/intent/like?tweet_id={nr_posta}"

        driver.get(link)

        time.sleep(1)
        # problem_check()
        # Wysyłanie kombinacji klawiszy CTRL+ENTER
        okienko = ActionChains(driver)
        #okienko = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]') ##
        okienko.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform() # 
        # time.sleep(2)

        return


    except Exception:
        print("Wyjebało LIKE v2")
        problem_check()
















################################# WERSJA ZE SCROLLEM !! ###########################################################################################################################################################


    # driver.get(link)  # Wchodzimy na stronę używając adresu URL przekazanego w zmiennej 'link'
    # time.sleep(2)


    # locators = [
    #     (By.XPATH, '//div[@data-testid="like"]'),
    #     (By.XPATH, '//svg[@class="r-4qtqp9 r-yyyyoo r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-50lct3 r-1srniue"]'),
    #     (By.XPATH, '//*[@id="id__98xb3q40vz8"]/div[3]/div/div'), ### XPATH DO POSTA Z X nie twitter
    #     (By.CSS_SELECTOR, 'div[data-testid="like"]'),
    #     (By.XPATH, '//*[@id="id__po31jdkjlyg"]/div[3]/div/div'),
    #     #(By.XPATH, '//div[contains(@class, "r-1niwhzg r-sdzlij r-xf4iuw r-o7ynqc")]/div')
    #     (By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[2]/div/div/article/div/div/div[3]/div[5]/div/div/div[3]/div/div')
    # ]
    
    # for locator in locators:
    #     try:
    #         like_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locator))

    #         like_button.click()
    #         print("Kliknięto Like !")                                                                   #### tu można dodać sprawdzanie numeru , i licznik like !!
    #         return True
    #     except:
    #         try:
    #             start_time = time.time()
    #             end_time = start_time + 3  # Ustaw końcowy czas na 3 sekundy później

    #             # Scrolluj stronę w dół do znalezienia przycisku "like" lub do upływu 3 sekund
    #             while time.time() < end_time:
    #                 driver.execute_script("window.scrollBy(0, 50)")  # Przewija stronę o 200 pikseli w dół
    #                 time.sleep(0.1)  # Krótka przerwa, aby uniknąć zbyt szybkiego przewijania
    #                 # Sprawdź, czy przycisk "like" jest obecny
    #                 if driver.find_elements_by_css_selector(like_button):
    #                     print("Znaleziono przycisk 'like' kończe scrollowanie !")
    #                     break

    #             # Opcjonalnie, jeśli chcesz kliknąć znaleziony przycisk
    #             like_buttons = driver.find_elements_by_css_selector(like_button)
    #             if like_buttons:
    #                 like_buttons[0].click()  # Kliknij pierwszy znaleziony przycisk "like"
    #                 return True
    #         except Exception:
    #             print("scrolluje......")
    #         continue  # If current locator doesn't work, try the next one

    # print("NIE ZNALEZIONO LIKE !!")
    # return False



###################################################

### ### ### ### ### ### ### ### ###

def tweet_retweet():  # przekazanie drivera jako argumentu


    global driver , token_z_pliku , petla_nr , haslo_twit  , nick , mail , haslo_mail , nowe_haslo_twit , nowy_token , link
    print("Dodaje retweet...")

    #capcha()  # zakładając, że jest to wcześniej zdefiniowana funkcja


    try:
        link = f"https://twitter.com/intent/retweet?tweet_id={nr_posta}"

        driver.get(link)

        time.sleep(1)
        # problem_check()
        # Wysyłanie kombinacji klawiszy CTRL+ENTER
        okienko = ActionChains(driver)
        #okienko = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]') ##
        okienko.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform() # 
        # time.sleep(2)

        return


    except Exception:
        print("Wyjebało REPOST v2")
        problem_check()






    # try:
    #     time.sleep(1)
    #     retweet_buttons = driver.find_elements(By.CSS_SELECTOR, '[data-testid="retweet"]')
    #     if retweet_buttons:
    #         retweet_buttons[0].click()
    #         time.sleep(1)  # Czekaj na otwarcie okna retweet
    #         driver.find_element(By.CSS_SELECTOR, '[data-testid="retweetConfirm"]').click()  # Potwierdź retweet
    #         print("Retweet zrobiony!")
    #     else:
    #         print("Nie znaleziono przycisku retweet.")













    # #     try:
    # #     # Kliknięcie przycisku (przykładowy XPath)
    # #         repost_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/div/div')
    # #         repost_button.click()
    # #         print("Retweet 1 naciśnięty !")
    # #         time.sleep(1) 
    # #         # Oczekiwanie 3 sekundy na pojawienie się napisu "Undo repost"
    # #         # time.sleep(3)
    # #         # 
    # #     except Exception:
    # #         print("Wyjebało dodawanie reposta !")
    # #         # Jeśli napis "Undo repost" się nie pojawił, naciska inny przycisk
    # #         # if not undo_elements:
       
       
    # #     try:
    # #         time.sleep(3) 
    # #         repost2_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div')   ### jakby nie działało na dole inne xpathy
    # #         repost2_button.click()
    # #         print("Dodano po xpath !!!")                  
    # #     except:
    # #         time.sleep(1)
    # #         repost3_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/span')
    # #         repost3_button.click()
    # #         print("Dodano po xpath 2 !!!") 
    # #         return  
    # except ExceptionGroup:
    #     print("wyjebało repost ")
    #     return
    
# 
# '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/div/div'




        #     global driver , token_z_pliku , petla_nr , haslo_twit  , nick , mail , haslo_mail , nowe_haslo_twit , nowy_token , link , undo_button , repost_button , undo_repost
        #     print("Dodaje retweet...")
        #     #capcha()  # zakładając, że jest to wcześniej zdefiniowana funkcja
        #     try:
                



        #         #### Może tu dodać driver.get(link)



        # ########## LAMBDAAAAAAAAAAA 

        #         try:
        #             WebDriverWait(driver, 10).until(
        #                 lambda d: any(
        #                     len(d.find_elements(locator_type, locator)) > 0
                    
        #                         for locator_type, locator in [
        #                             # (By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]'),
        #                             # (By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label'),
        #                             # (By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'),
        #                             # (By.CSS_SELECTOR, 'input.r-30o5oe[type="login"]'),
        #                             # (By.CSS_SELECTOR, 'input[type="login"]'),
        #                             # (By.XPATH, '//input[@aria-label="Login"]'),
        #                             # (By.NAME, 'login'),
        #                             (By.XPATH, "//*[contains(text(), 'Undo repost')]"),
        #                             #(By.XPATH, "//*[contains(text(), 'Wprowadź swoje hasło')]"),
        #                             #(By.XPATH, f"//*[contains(text(), '{nick[petla_nr]}')]"),
        #                             #(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        #                         ]
        #                     )




        #                 )
        #         except Exception:
        #             print ("nie znaleziono")



        #     ##########################

        #         try:
        #             time.sleep(1)
        #             print("1")
        #             # Kliknięcie przycisku (przykładowy XPath)
        #             repost_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/div/div')
        #         except Exception:

        #             time.sleep(1)

        #         try:
        #             print("2")
        #             # Kliknięcie przycisku (przykładowy XPath)
        #             repost_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[2]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/div/div/div[1]/div')
        #         except Exception:

        #             time.sleep(1)

        #         try:
        #             print("3")
        #             # Kliknięcie przycisku (przykładowy XPath)
        #             repost_button = driver.find_element(By.CSS_SELECTOR,'#id__bi0w0qmqk9a > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        #         except Exception:

        #             time.sleep(1)

        #         try:
        #             print("4")
        #             # Kliknięcie przycisku (przykładowy XPath)
        #             repost_button = driver.find_element(By.CSS_SELECTOR,'html body div#react-root div.css-175oi2r.r-13awgt0.r-12vffkv ... div.css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-1awozwy.r-6koalj.r-1h0z5md.r-o7ynqc.r-clp7b1.r-3s2u2q div.css-175oi2r.r-xoduu5')
        #         except Exception:
        #             print("nie znaleziono.")  
        #             time.sleep(1)









        #         #     print("Znaleziono przez lambda v3  undo repost !!!")  # The element was found within the timeout period.
        #         # except TimeoutException:
        #         #     print("NIE znaleziono przez lambda v3  undo repost!!!")



        # ################################################# RETWEET 222222222222 #########################





        #         try:
        #             time.sleep(1)
        #             print("1")
        #             # Kliknięcie przycisku (przykładowy XPath)
        #             repost_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div')
        #         except Exception:

        #             time.sleep(1)

        #         try:
        #             print("2")
        #             # Kliknięcie przycisku (przykładowy XPath)
        #             repost_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/div/div')
        #         except Exception:

        #             time.sleep(1)

        #         try:
        #             print("3")
        #             # Kliknięcie przycisku (przykładowy XPath)
        #             repost_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div')
        #         except Exception:

        #             time.sleep(1)

        #         try:
        #             print("4")
        #             # Kliknięcie przycisku (przykładowy XPath)
        #             repost_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div')
        #         except Exception:
        #             print("nie znaleziono.")  

        #             time.sleep(1)

        #         try:
        #             print("5")
        #             # Kliknięcie przycisku (przykładowy XPath)
        #             repost_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div/div[1]')
        #         except Exception:
        #             print("nie znaleziono.")  

        #             time.sleep(1)







        # # #############################################
        # #     except Exception:
        # #         print("NIE ZNALEZIONO 1 RETWEETA !!!!")  
        # #         time.sleep(1)




        #             # start_time = time.time()
        #             # end_time = start_time + 7
                
        #             # while time.time() < end_time:

        #             #     ### tu można dorobić złoty strzał jak pojawi się (1 of 1) to klika przycisk Submit, lub 
        #             #     ### /html/body/div/div/div[1]/div/button

        #             #     try:
        #             #         # Sprawdzanie, czy konto zostało odblokowane
        #             #         odblokowano = WebDriverWait(driver, 3).until(
        #             #             lambda driver: driver.find_element(By.XPATH, "//*[contains(text(), 'Undo repost')]") or
        #             #                             driver.find_element(By.XPATH, "//*[contains(text(), 'Zaloguj się do serwisu X')]") ## nie wiem czy to dobre...
        #             #         )
        #             #         if odblokowano:

        #             #             # odblokowano.click()





        #     except Exception:
        #         print("Wyjebałe RT !")













                        #         print("JUŻ REPOSTOWANO !")
                        #         break  # Przerywamy pętlę, jeśli konto zostało odb
                        # except Exception:
                        #     print("Nie było undo repost !")















            #     print("klikam...")
            #     time.sleep(1)
            #     repost_button.click()
            #     print("KLIKNIĘTE ! jebać Elona")
            #     # Oczekiwanie 3 sekundy na pojawienie się napisu "Undo repost"
            #     time.sleep(2)
            # except Exception:
            #     print("Nie kliknięte...")
            #     time.sleep(2)











            # wait = WebDriverWait(driver, 5) # Ustawienie maksymalnego czasu oczekiwania na 3 sekund
            # try:
            #     # Użyj WebDriverWait aby poczekać na element z tekstem "Undo repost".
            #     undo_repost = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Undo repost')]")))
            #     print("Element 'Undo repost' został znaleziony, wyjście z funkcji.")
            #     return
            # except TimeoutException:
            #     print("Element 'Undo repost' nie został znaleziony w ciągu 3 sekund.")
                
            # try:
            #     # Spróbuj znaleźć i kliknąć przycisk "Repost".
            #     repost_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Repost')]")))
            #     repost_button.click()
            #     print("Kliknięto przycisk 'Repost'.")
            # except TimeoutException:
            #     print("Przycisk 'Repost' nie został znaleziony, próba kliknięcia przycisku przez XPATH.")
                
            # # Poczekaj 2 sekundy
            #     time.sleep(2)
                
                # try:
                #     # Jeśli przycisk "Repost" nie był klikalny, użyj podanego XPATH.
                #     driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/div/div').click()
                #     print("Kliknięto pierwszy przycisk przez XPATH.")
                #     # Poczekaj 2 sekundy przed kliknięciem następnego przycisku.
                #     time.sleep(2)
                #     driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div').click()
                #     print("Kliknięto drugi przycisk przez XPATH.")
                # except NoSuchElementException:
                #     print("Nie udało się kliknąć przycisków przez XPATH.")










            # for xpath in xpaths:
            #     try:
            #         element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            #         driver.execute_script("arguments[0].scrollIntoView(true);", element)
            #         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            #         element.click()
            #         print(f"Kliknięto element XPATH: {xpath}")
            #     except ElementClickInterceptedException:
            #         driver.execute_script("arguments[0].click();", element)
            #         print(f"Kliknięto element XPATH za pomocą JavaScript: {xpath}")
            #     except (NoSuchElementException, TimeoutException):
            #         print(f"Element XPATH nie znaleziony lub przekroczono czas oczekiwania: {xpath}")
            
            # # Szukanie elementu zawierającego tekst
            # try:
            #     element_with_text = WebDriverWait(driver, 10).until(
            #         EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
            #     )
            #     element_with_text.click()
            #     print(f"Kliknięto element zawierający tekst: {text}")
            # except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            #     print(f"Nie udało się znaleźć lub kliknąć elementu z tekstem: {text}")
            
            # # Szukanie elementu z selektorem CSS
            # try:
            #     element_with_css = WebDriverWait(driver, 10).until(
            #         EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            #     )
            #     element_with_css.click()
            #     print(f"Kliknięto element CSS SELECTOR: {css_selector}")
            # except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            #     print(f"Nie udało się znaleźć lub kliknąć elementu CSS SELECTOR: {css_selector}")

        # Przykład użycia
        # driver = webdriver.Chrome('path_to_your_webdriver')
        # driver.get('URL_strony_do_sprawdzenia')

        # xpaths = [
        #     "XPATH1",
        #     "XPATH2",
        #     "XPATH3"
        # ]
        # text_to_find = "testowy tekst"
        # css_selector_to_find = "12345"
















                # undo_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'Undo repost')]")

                # # Jeśli napis "Undo repost" się nie pojawił, naciska inny przycisk
                # if not undo_elements:

                #     try:
                #         undo_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/span')
                                                    
                #         undo_button.click()   ################# to klika repost !!!!!!!!!!!
                #     except Exception:
                #         print("Nie znaleziono po xpath")
                #         try:
                #             undo_button = driver.find_element(By.XPATH, "//div[@contenteditable='Undo repost']")
                                                        
                #             undo_button.click()
                #         except Exception:
                #             print("Nie znaleziono po treści...")


                # print("klikam...")
                # time.sleep(1)
                # repost_button.click()
                # print("KLIKNIĘTE ! jebać Elona")
                # # Oczekiwanie 3 sekundy na pojawienie się napisu "Undo repost"
                # time.sleep(2)


                            










        ################################################################
            #     print("Retweet dodany !")                        
            # except Exception:
            #     print("Retweet juz dodany NIE klikam drugi raz !!")
            #     try:
            #         time.sleep(2)
            #         undo_button.send_keys(Keys.ESC)
            #         time.sleep(2)
            #         print("naciśnięto ESCAPE")
            #     except Exception:
            #         print("nie naciśnięto ESCAPE")
        ##############################################################
























        # button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[2]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/div/div')
        # button.click()

        # button = driver.find_element_by_css_selector('#id__smgvfmgaeq > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
        # button.click()


        # complex_css_selector = "html body div#react-root div.css-175oi2r.r-13awgt0.r-12vffkv ... r-1ny4l3l div.css-1rynq56.r-bcqeeo.r-qvutc0"
        # button = driver.find_element_by_css_selector(complex_css_selector)
        # button.click()





            # finally:
            #     tweet_post()  # Wywołanie funkcji odpowiedzialnej za dodanie komentarza

        ### ### ### ### ### ### ### ### ###



def tweet_post():
    global driver, token_z_pliku, petla_nr, haslo_twit, nick, mail, haslo_mail, nowe_haslo_twit, nowy_token, link
    print("Dodaje komentarz....")
    # link = 
    time.sleep(1)
    driver.get(link)
    time.sleep(1)
    #     driver.get(link)
    # except Exception:
    #     print("Tp - nie było capcha !")
    # time.sleep(1)
    
    
    # # Wczytanie losowego komentarza z pliku
    # with open("komentarze.txt", "r", encoding="utf-8") as plik:
    #     komentarze = plik.readlines()
    #     losowy_komentarz = random.choice(komentarze).strip()
    #     print("\nWylosowałem: ", losowy_komentarz, "\n")

    locators = [


        #(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[1]")
        (By.XPATH, "//input[@aria-label='Dodaj komentarz']"),
        (By.XPATH, "//div[@contenteditable='true']"),
        (By.XPATH, "//div[@data-testid='replyInput']"),
        (By.XPATH, "//input[placeholder='Napisz coś...']"),
        (By.XPATH, "//div[.//text()='Napisz coś...']"),
        (By.CSS_SELECTOR, "[role='textbox'][placeholder='Napisz coś...']"),
        (By.CSS_SELECTOR, ".klasa-pola-komentarza"),
        #(By.XPATH, "//input[@name='comment']")


        (By.XPATH, "//div[contains(text(), 'Co się dzieje')]"),
        (By.XPATH, "//div[contains(text(), 'Post your reply')]"),
        (By.XPATH, "//div[@aria-label='Dodaj komentarz']"),
        (By.CSS_SELECTOR, "div[aria-label='Dodaj komentarz']"),


        (By.XPATH, '//div[@data-testid="reply"]'),
        (By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/div/div'),
        (By.XPATH, "//span[contains(text(), 'Post your replay')]"),
        (By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div'),
        (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')






    ]

    
    comment_field = None

        
    for locator in locators:
        try:
            comment_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
            if comment_field:

                break #  zmienić na return jakby nie działało !!!!
        except:
            try:
                start_time = time.time()
                end_time = start_time + 2  # Ustaw końcowy czas na 3 sekundy później

                # Scrolluj stronę w dół do znalezienia przycisku "like" lub do upływu 3 sekund
                while time.time() < end_time:
                    driver.execute_script("window.scrollBy(0, 50)")  # Przewija stronę o 200 pikseli w dół
                    time.sleep(0.1)  # Krótka przerwa, aby uniknąć zbyt szybkiego przewijania
                    # Sprawdź, czy przycisk "like" jest obecny
                    if driver.find_elements_by_css_selector(comment_field):
                        print("Znaleziono przycisk 'like' kończe scrollowanie !")
                        break
            except Exception:
                print("Nie znaleziono pola komentarza !")
                
    try:
        print("dodaje..", mix_kom,)
        time.sleep(1)
        comment_field.click()  # Click the comment field
        time.sleep(2)  # Wait for 2 seconds
        comment_field.send_keys(mix_kom)
            # # Press the ENTER key
            # comment_field.send_keys(Keys.ENTER).key_up(Keys.CONTROL)
        time.sleep(2)
        comment_field = ActionChains(driver)
        comment_field.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        time.sleep(2)
        print("\nDODANO ---> ", mix_kom, " <---\n")
        #print("DODANO ---> ", losowy_komentarz, " <---")
                          
    except Exception:
        print("nie dodano komentarza !!!!")   
        winsound.Beep(4000 , 420)




    
    print("zamykam dodawanie posta")
    # problem_check()
# except Exception:
#     print("Nie znaleziono pola komentarza !")

#             continue
#     print("NIE ZNALEZIONO POLA KOMENTARZA !!")
#     return False

# except Exception:
#     print("WYJEBAŁO dodawanie posta...")


                    #continue  # If current locator doesn't work, try the next one

            #if not comment_field:
                # start_time = time.time()
                # end_time = start_time + 3  # Ustaw końcowy czas na 3 sekundy później
                #     # Scrolluj stronę w dół do znalezienia przycisku "like" lub do upływu 3 sekund
                # while time.time() < end_time:
                #     driver.execute_script("window.scrollBy(0, 200)")  # Przewija stronę o 200 pikseli w dół
                #     time.sleep(0.1)  # Krótka przerwa, aby uniknąć zbyt szybkiego przewijania
                #     # Sprawdź, czy przycisk "like" jest obecny
                #     if driver.presence_of_element_located(comment_field):
                #         comment_field.click()  # Click the comment field
                #         time.sleep(2)  # Wait for 2 seconds
                #         print("Znaleziono pole komentarza")
                #         #break







                # raise Exception("The comment field was not found.")
            


        



        # print("dodaje..", mix_kom,)
        # time.sleep(2)  # Wait for 2 seconds
        # comment_field.click()  # Click the comment field
        # time.sleep(2)  # Wait for 2 seconds
        
        # Paste the random comment
        #comment_field.send_keys(losowy_komentarz)


        # comment_field.send_keys(mix_kom)






        #     # # Press the ENTER key
        #     # comment_field.send_keys(Keys.ENTER).key_up(Keys.CONTROL)
            


        # time.sleep(2)

        # comment_field = ActionChains(driver)
        # comment_field.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()


        # time.sleep(2)


        # print("DODANO ---> ", mix_kom, " <---")
        # #print("DODANO ---> ", losowy_komentarz, " <---")
        # time.sleep(1)

        # # for _ in range(5):
        # #     winsound.Beep(5000,420)
        # #     time.sleep(0,5)
    
        # print("DODANO KOMENTARZ ! ! ! ! ! ! ! ! ! ! !")



        # except Exception:
        #     print("zamykam dodawanie posta...")
    # except Exception:
    #     print("WYJEBAŁO dodawanie posta...")



    # try:
    #     # Czekaj aż jeden z trzech elementów będzie dostępny
    #     pole_komentarza = WebDriverWait(driver, 10).until(

            # try:
            #     print("szukam przycisku dodania posta")




        #         send_button_locator = WebDriverWait(driver, 10).until(
        #             lambda d: d.find_element(By.XPATH, '//button[contains(text(), "Reply")]') 
        #                     if d.find_elements(By.XPATH, '//button[contains(text(), "Reply")]') else None
        #         )
        #         if send_button_locator:
        #             send_button_locator.click()
        #             print("Kliknięto przycisk.")
        #     except Exception as e:
        #         print("Wystąpił problem:", e)

        #     if send_button_locator:
        #         send_button_locator.click()
        #         print("DODAJE POST !!")
        #     else:
        #         print("Nie znaleziono przycisku wysłania posta.")
        #     time.sleep(3)
            
        # except Exception as e:
        #     print("Nie udało się dodać komentarza !", str(e))
        # finally:
        #     print("Dodawanie posta zakończone !")







        # try:
        #     print("szukam przycisku dodania posta")



        #     locators = [
        #         # Looking for buttons with text that exactly matches "Reply" or "Odpowiedz"
        #         (By.XPATH, '//button[text()="Reply"]'),
        #         (By.XPATH, '//button[text()="Odpowiedz"]'),
                
        #         # Using contains() for flexibility with additional text or spaces
        #         (By.XPATH, '//button[contains(., "Reply")]'),
        #         (By.XPATH, '//button[contains(., "Odpowiedz")]'),
                
        #         # Targets input fields or editable divs with specific placeholders or roles for replying
        #         (By.XPATH, '//input[@placeholder="Post your reply"]'),
        #         (By.XPATH, '//div[@role="textbox"][@placeholder="Post your reply"]'),
                
        #         # Using data-testid attributes, which are often used in React apps like Twitter for testing
        #         (By.XPATH, '//div[@data-testid="reply"]'),
                
        #         # Fallback to broad matches that might be useful if the structure is known but text varies
        #         (By.XPATH, '//div[contains(@aria-label, "Reply")]'),
                
        #         # Avoiding absolute XPaths, which are brittle and likely to break if the structure changes
        #     ]


        #     POST = None
    
        #     for locator in locators:
        #         try:
        #             POST = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
        #             if POST:
        #                 break
        #         except:
        #             continue  # If current locator doesn't work, try the next one

        #     if not POST:
        #         raise Exception("The comment field was not found.")

        #     time.sleep(2)  # Wait for 2 seconds
        #     POST.click()  # Click the comment field
        #     time.sleep(2)  # Wai



        #     try:
        #         print("Druga próba Replay....")
                


        #     except Exception:
        #         print("nieudane.. !")





                
                

        #     print("DODANO !")
        # except Exception:
        #     print("NIE KLIKNIĘTO !!!!!")


    #     print("ZAKOŃCZONO !")
    # except Exception:
    #     print("NIE DODANO !!!!!!!!!!!!!!")




    #############################################################################################################


        # time.sleep(4)

        # try:
        #     try:
        #         # Próba kliknięcia za pomocą XPath
        #         driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]').click()
        #         print("Kliknięto przycisk za pomocą XPath.")
        #     except NoSuchElementException:


        #         try:
        #             time.sleep(1)
        #             # Próba kliknięcia za pomocą CSS
        #             driver.find_element(By.CSS_SELECTOR, 'div.r-1moyyf3:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)').click()
        #             print("Kliknięto przycisk za pomocą CSS.")
        #         except NoSuchElementException:


        #             try:
        #                 time.sleep(1)
        #                 # Próba kliknięcia po napisie na przycisku
        #                 driver.find_element(By.XPATH, '//button[text()="Replay"]').click()
        #                 print("Kliknięto przycisk 'Replay'.")
        #             except NoSuchElementException:


        #                 try:
        #                     time.sleep(1)
        #                     # Próba kliknięcia po napisie "Odpowiedz"
        #                     driver.find_element(By.XPATH, '//button[text()="Odpowiedz"]').click()
        #                     print("Kliknięto przycisk 'Odpowiedz'.")
        #                 except NoSuchElementException:
                            
                            

        #                     try:
        #                         time.sleep(1)
        #                         # Próba kliknięcia po napisie "Odpowiedz"
        #                         driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]').click()
        #                         print("Kliknięto przycisk 'Odpowiedz'.")
        #                     except NoSuchElementException:
        #                         print("Nie znaleziono przycisków !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.")







        #     print("zakończono szukanie")
        # except Exception:
        #     print("NIE KLIKNIĘTO !!!!!")












        #     )

            #     print("Komentarz---> ", losowy_komentarz, " <--- dodany poprawnie !!")         ________________ TO SKOMENTOWAŁEM !!!!
            # except Exception:
            #     print ("NIE DODANO KOMENTARZA !!!!!!!")

        # Przewiń do elementu
            # time.sleep(5)
        # driver.execute_script("arguments[0].scrollIntoView(true);", pole_komentarza)  #############################  SCROLL  TO #############################
        # time.sleep(5)

        # try:
        #     print("wpisuje komentasz..")
        #     pole_komentarza.click()
        #     time.sleep(10)
        #     # Wpisywanie komentarza
        #     pole_komentarza.send_keys(losowy_komentarz)
        #     print ("Komentarz wpisany !!")
        # except Exception:
        #     print("Nie wpisano komentarza !!!!!!!!")


        # time.sleep(4)  # Krótkie opóźnienie, aby upewnić się, że komentarz został wprowadzony
        # #pole_komentarza.send_keys(Keys.ENTER)
        # # Oczekuj na dostępność przycisku odpowiedzi i kliknij go


            # try:
                
            #     print("Klikam przycisk dodawania posta....")


            #     locators2 = [
            #         (By.XPATH, "/html/body/div[1]/div[1]/div[1]/section/div[3]/form/button"),
            #         (By.XPATH, "//*[@id='react-root']//div[contains(@aria-label, 'Reply') and @role='button']"),
            #         (By.CSS_SELECTOR, "div[aria-label='Reply'][role='button']"),
            #         (By.XPATH, "//div[@role='button'][contains(@aria-label, 'Reply')]"),
            #         (By.XPATH, "//span[contains(text(), 'Reply')]"),
            #         (By.CSS_SELECTOR, ".css-1dbjc4n.r-18u37iz.r-1h0z5md"),
            #         (By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]"),
            #         # Inne metody znajdowania przycisku, przykładowo:
            #         (By.XPATH, "//div[@data-testid='reply']"),  # Założenie, że Twitter używa atrybutu `data-testid` dla przycisku odpowiedzi
            #         (By.CSS_SELECTOR, "button.reply"),  # Przykładowa klasa CSS
            #         (By.ARIA_LABEL, "Odpowiedz"),  # Przykładowy atrybut ARIA Label
            #         # Dalsze selektory w zależności od dostępnych atrybutów
            #         (By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]'),
            #         (By.XPATH, '//div[@data-testid="Reply"]')
            #         #     EC.element_to_be_clickable() 
            #    ]
                


            #     post_field = None
            #     try:
            #         for locator2 in locators2:
            #             try:
            #                 post_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator2))
            #                 if post_field:
            #                     print("znaleziono !!!!! ")
            #                     break
            #             except:
            #                 continue  # If current locator doesn't work, try the next one

            #         if not post_field:
            #             raise Exception("The comment field was not found.")

            #         time.sleep(2)  # Wait for 2 seconds
            #         post_field.click()  # Click the comment field
            #         time.sleep(2)  # Wait for 2 seconds


            #         print("DODANO !!!!!!!")
            #     except Exception:

            #         print("Nie dodano !!!!!!")














            #     time.sleep(3)


            #     print("ZAMYKAM DODAWANIE POSTA\n")
            #     time.sleep(5)
            # except Exception:
            #     print("Nie dodano komentarza !!!!!!!!!!")
            # print("post dodany !")
            # time.sleep(60)

def follower():
    # https://twitter.com/intent/follow?screen_name=henry_ethlas
    global driver , follow_buttons
    # time.sleep(1)
    # driver.get(link)
    time.sleep(1)
    
    try:
        follow_buttons = driver.find_elements(By.XPATH, "//span[text()='Follow']/ancestor::div[contains(@role, 'button')]")
    except Exception:
        print(" 1 nie klknięte...")

    try:
        follow_buttons = driver.find_elements(By.XPATH, "//span[text()='Follow']")
    except Exception:
            print("2...")

    # try:
    #     follow_buttons = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/aside/div[2]/div[1]/div/div[2]/div[1]/div[2]/div")
    # except Exception:
    #     print("3")

    # try:
    #     follow_buttons = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/aside")
    # except Exception:
    #     print("4")

        
    # Kliknij trzy pierwsze przyciski
    for button in follow_buttons[:2]:  # Pobierz tylko trzy pierwsze elementy
        try:
            button.click()
            time.sleep(1)
        except ElementClickInterceptedException:
            print("Nie można kliknąć przycisku 'Follow', być może jest on zasłonięty.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")




    # locators = [
    #     (By.XPATH, "//span[text()='Follow']"),
    #     (By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/aside/div[2]/div[1]/div/div[2]/div[1]/div[2]/div"),
    #     (By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/aside")
    #     # Możesz dodać więcej XPATHs lub selektorów CSS jeśli są dostępne
    # ]
    
    # # Przejdź przez listę lokatorów i spróbuj znaleźć przycisk "Follow"
    # for locator in locators:
    #     elements = driver.find_elements(locator[0], locator[1])
    #     if elements:
    #         for element in elements:
    #             if element.is_displayed() and element.is_enabled():
    #                 return element

    # return None


def mixer():
    global driver, mix_kom
    # Otwórz plik komentarze.txt i przeczytaj linie
    with open("komentarze.txt", "r", encoding="utf-8") as file:
        lines = file.read().split('\n\n')
    
    # Znajdź sekcje oddzielone pustymi liniami
    sections = [section.splitlines() for section in lines if section.strip()]
    
    # Wybierz losową linijkę z pierwszej sekcji
    kom_1 = random.choice(sections[0]).strip() if sections and sections[0] else ""
    
    # Wybierz losową linijkę z drugiej sekcji, jeśli istnieje
    kom_2 = random.choice(sections[1]).strip() if len(sections) > 1 else ""

    kom_3 = random.choice(sections[2]).strip() if len(sections) > 2 else ""

    kom_4 = random.choice(sections[3]).strip() if len(sections) > 3 else ""
    
    # Połącz linie w jedną zmienną mix_kom
    mix_kom = f"{kom_1} {kom_2} {kom_3} {kom_4}" if kom_1 or kom_2 or kom_3 or kom_4 else ""
    
    print("--Wylosowałem--")
    print(mix_kom)
    time.sleep(1)
    return
    
    # return mix_kom

### ### ### ### ### ### ### ### ###
###      Melodia startowa       ###
def muzyczka(frequency, duration):
    global driver
    winsound.Beep(frequency, duration)
start = [
    (440, 200),  # częstotliwość 440Hz, długość 200ms
    (554, 200),
    (659, 200),
    (880, 400),
    (659, 200),
    (880, 800),
]
    # Odtworzenie melodii
    # for note in start:
    #     muzyczka(*note)
    #     time.sleep(0.1)  # krótka przerwa między tonami

################################  M A I L E ##################################

##############################################################################
def get_o2_code():
    # global  petla_nr , token_z_pliku, haslo_twit, nick, dane, mail_password, maile

    #SET API AND SWITCH AFTER 10 ++
    
        
    imap_host = 'poczta.o2.pl'  # Zastąp odpowiednim serwerem IMAP
    imap_user = maile[0]
    imap_pass = moje_haslo_mail
    
    #GO INSIDE
    time.sleep(2)
    
    try:
        mail = imaplib.IMAP4_SSL(imap_host)
        mail.login(imap_user, imap_pass)
        mail.select('inbox')
    except Exception as e:
        print(f"Błąd połączenia z serwerem IMAP: {e}")
        return None
    
    time.sleep(25)
    
    #SEARCH MAILBOX FOR INFO@X.COM
    
    status, messages = mail.search(None, '(FROM "info@x.com")')
    if status != 'OK':
        print("Nie znaleziono wiadomości od info@x.com")
        return None
    print(status, messages)

    
    time.sleep(10)

    #GO INSIDE MESSAGE
    try:
        messages = messages[0].split()
        latest_email_id = messages[-1]
        status, data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
    except Exception as e:
        print(f"Błąd podczas wyszukiwania lub pobierania wiadomości: {e}")
        return None
    time.sleep(5)
    print(f"Petla_nr przed inkrementacja: {petla_nr}")
    try:
        status, messages = mail.search(None, '(FROM "info@x.com")')
        if status != 'OK':
            print("Nie znaleziono wiadomości od info@x.com")
            return None
        for num in reversed(messages[0].split()):
            typ, data = mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
            match = re.search(r'\b\d{6}\b', subject)
            print("match:", match)
            if match:
                # petla_nr = petla_nr + 1
                return match.group(0)
    except Exception as e:
        # petla_nr = petla_nr + 1
        print(f"Błąd podczas wyszukiwania lub przetwarzania wiadomości: {e}")

    return "Kod weryfikacyjny nie został znaleziony."

##############################  change_mail() ################################

def change_mail():
    #global petla_nr, token_z_pliku, haslo_twit, nick, dane, haslo_mail
    try:
        # GO TO MAIL UPDATE LINK
        time.sleep(5)
        driver.get("https://twitter.com/settings/your_twitter_data/account")
        time.sleep(5)
    except Exception as e:
        print("Problem z przejściem do ustawień konta:", e)

    try:
        # TYPE PASSWORD TO CONTINUE
        password_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/label/div/div[2]/div/input')
        password_input.send_keys(haslo_twit[0])
        time.sleep(3)
        confirm_password = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[4]/div')
        confirm_password.click()
        time.sleep(5)
    except Exception as e:
        print("Problem z wprowadzeniem hasła:", e)

    try:
        # UPDATE EMAIL
        driver.get("https://twitter.com/i/flow/add_email")
        time.sleep(5)
    except Exception as e:
        print("Problem z aktualizacją e-maila:", e)

    try:
        verify_password_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')
        verify_password_input.send_keys(haslo_twit[0])
        time.sleep(3)
        next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        next_button.click()
        time.sleep(3)
    except Exception as e:
        print("Problem z weryfikacją hasła:", e)

    try:
        email_adress_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
        email_adress_input.send_keys(nowy_mail[0])
        time.sleep(5)
        next2_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        next2_button.click()
        time.sleep(5)
    except Exception as e:
        print("Problem z wprowadzeniem adresu e-mail:", e)

    try:
        # GET MAIL FROM O2.PL IMAP
        time.sleep(15)
        code_from_o2 = get_o2_code()
        time.sleep(5)
    except Exception as e:
        print("Problem z pobraniem kodu z O2:", e)

    try:
        verification_code_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        verification_code_input.send_keys(code_from_o2)
        time.sleep(5)
        verify_button2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        verify_button2.click()
        time.sleep(5)
    except Exception as e:
        print("Problem z wprowadzeniem kodu weryfikacyjnego:", e)

##############################  change_auth() ################################

def change_auth():
        
        #global petla_nr, token_z_pliku, haslo_twit, nick, dane, haslo_mail
        try:
            time.sleep(5)
            driver.get("https://twitter.com/settings/account/login_verification")
            time.sleep(5)
            
            try:
                authenticator_app = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/div/div/label/div/div[2]/input')
                authenticator_app.click()
            except NoSuchElementException:
                print("Authenticator app option not found.")
                

            time.sleep(5)
            
            try:
                password3_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')
                password3_input.send_keys(haslo_mail[0])  
            except NoSuchElementException:
                print("Password input field not found.")
                

            time.sleep(3)

            try:
                confirm2_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
                confirm2_button.click()
            except NoSuchElementException:
                print("Confirm button not found.")
                

            time.sleep(3)

            try:
                turn_off_auth = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div')
                turn_off_auth.click()
                time.sleep(5)
            except NoSuchElementException:
                print("Turn off authentication option not found.")
                
        except WebDriverException as e:
            print(f"Web driver error: {e}")

            time.sleep(3)

##############################  change_pass() ################################

def change_pass():
    #global petla_nr, token_z_pliku, haslo_twit, nick, dane, haslo_mail, maile, driver

    new_password = "Nigga123123"  

    try:
        time.sleep(5)
        driver.get("https://twitter.com/settings/password")
        time.sleep(5)
        
        try:
            current_password_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div[1]/label/div/div[2]/div/input')
            current_password_input.send_keys(haslo_twit[0])
        except NoSuchElementException:
            print("Current password input not found.")
            

        time.sleep(2)
        
        try:
            pinput1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div[3]/label/div/div[2]/div/input')
            pinput1.send_keys(new_password)
        except NoSuchElementException:
            print("New password input field 1 not found.")
            

        time.sleep(2)
        
        try:
            pinput2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div[4]/label/div/div[2]/div/input')
            pinput2.send_keys(new_password)
        except NoSuchElementException:
            print("New password input field 2 not found.")
            

        time.sleep(2)
        
        try:
            save_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/div')
            save_button.click()
        except NoSuchElementException:
            print("Save button not found.")
            

        time.sleep(5)

        #GET NEW TOKEN
        
        #new_token = get_new_token()  
        new_token = 0 # dodaje zeby nie bylo bledow , bylo to z góry 
        if(token_z_pliku[0] != nowy_token):
            # OUTPUT
            with open("capture_output.txt", "a", encoding="utf-8") as output:
                try:
                    print((f"Nick:{nick[0]} | Token: {new_token} | nowe_haslo_twit: {new_password} | Mail: {mail[0]} \n"))
                    output.write(f"Nick:{nick[0]} | Token: {new_token} | nowe_haslo_twit: {new_password} | Mail: {mail[0]} \n")
                except Exception as ee:
                    print("koniec")
                    return
        else:
            with open("tessametokeny.txt", "a", encoding="utf-8") as output:
                try:
                    print((f"Nick:{nick[0]} | Token: {new_token} | nowe_haslo_twit: {new_password} | Mail: {mail[0]} \n"))
                    output.write(f"Nick:{nick[0]} | Token: {new_token} | nowe_haslo_twit: {new_password} | Mail: {mail[0]} \n")
                except Exception as ee:
                    print("koniec")
                    return
                
    except WebDriverException as e:
 
       print(f"Web driver error: {e}")

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###
 ###                                                                       ###
  ###                              AIRDROPY                               ###
 ###                                                                       ###
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###

def sidequest():
    global driver
    link = "https://sidequest.rcade.game/quests"
    driver.get(link)
    
    refferal = "Bartosz416782"       ###### REFERAL CODE !!!!!!!!!!

     
                            # CONNECT X
    # try:        # Kliknij przycisk na podstawie XPath lub tekstu na przycisku
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/button[1]')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'CONNECT X')]")
    #         przycisk_tekst.click()
    #         time.sleep(5)
    #     print("connect kliknięty")        
    # except Exception:
    #     print("Nie udało się kliknąć connect to x")

    try:
        # Czekanie na przycisk "Follow" i jego kliknięcie
        connect_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Connect X')]")) or
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/button[1]'))
        )
        connect_button.click()
        print("Przycisk 'connect to x' został kliknięty.")
        # suspend()
        # capcha()
        # problem_check()
    except Exception as e:
        print("Nie udało się kliknąć przycisku connect", e)






                            # authorize app
        
    # try:
    #     # Oczekiwanie na element i jego kliknięcie
    #     time.sleep(3)
    #     # element = WebDriverWait(driver, 3).until(
    #     #     lambda driver: 
    #     #         driver.find_element(By.XPATH, "//*[contains(text(), 'Authorize Side Quest to access')]") or
    #     #         driver.find_element(By.XPATH, "//*[contains(text(), 'Authorize Side Quest to access your account?')]"))
        



    #     try:
    #         przycisk_xpath = driver.find_element(By.ID, "allow")
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, '//*[@id="allow"]')
    #         przycisk_tekst.click()
    #         time.sleep(2)  # Odczekuje 2 sekundy
    # except Exception as e:
    #     print("Nie udało się kliknąć AUTHORIZE", e)



    try:
        # Czekanie na przycisk "allow" i jego kliknięcie
        auth_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "allow")) or
            EC.element_to_be_clickable((By.XPATH, '//*[@id="allow"]'))
        )
        auth_button.click()
        print("Przycisk 'allow' został kliknięty.")
        # suspend()
        # capcha()
        # problem_check()
    except Exception as e:
        print("Nie udało się kliknąć przycisku allow", e)
















        

                    #   wpisz refa
    
    try:
        time.sleep(3)
                             # Wpisz dane do pola tekstowego
        pole_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[3]/div[2]/div/div[3]/input')
        # pole_input.clear()  # Czyści pole tekstowe przed wpisaniem nowych danych
        time.sleep(2)  # Odczekuje 2 sekundy
        pole_input.send_keys(refferal)
        time.sleep(2)  # Odczekuje 2 sekundy
        print("WPISANO !")
    except Exception:
        print("REF NIE WPISANY.....")   
        #return





    # try:
    #     # Czekanie na przycisk "allow" i jego kliknięcie
    #     pole_refa = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/input'))
    #         #EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/input'))
    #     )

    #     pole_refa.click()
    #     time.sleep(1)
    #     pole_refa.send_keys(refferal)
    #     print("Ref wpisany !")
    #     # suspend()
    #     # capcha()
    #     # problem_check()
    # except Exception as e:
    #     print("Nie udało się wpisać refa... !", e)
    #     return








            ######## zatwierdzenie reffa

    # try:
    #     time.sleep(2)  # Odczekuje 2 sekundy        
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[3]/div/div/button')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'ENTER')]")
    #         przycisk_tekst.click()
    #         time.sleep(2)
    # except Exception:
    #     print("Nie udało się kliknąć przycisku ok")


    try:
        # XPath - Twój oryginalny selektor
        enter_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/button'))
        )
        enter_button.click()
        print("Przycisk 'ENTER' (XPath) został kliknięty.")
        time.sleep(2)

    except Exception as e_xpath:
        print("Nie udało się kliknąć przycisku 'ENTER' (XPath):", e_xpath)

        # try:
        #     # CSS Selector - bezpośredni ścieżka
        #     enter_button_css = WebDriverWait(driver, 3).until(
        #         EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div > div > div.main > div.content > div.inner-content > div > div.referral-code > button'))
        #     )
        #     enter_button_css.click()
        #     print("Przycisk 'ENTER' (CSS Selector - bezpośredni) został kliknięty.")
            

        # except Exception as e_css_direct:
        #     print("Nie udało się kliknąć przycisku 'ENTER' (CSS Selector - bezpośredni):", e_css_direct)

        #     try:
        #         # CSS Selector - uproszczony
        #         enter_button_css_simplified = WebDriverWait(driver, 3).until(
        #             EC.element_to_be_clickable((By.CSS_SELECTOR, '.main .content .inner-content .referral-code > button'))
        #         )
        #         enter_button_css_simplified.click()
        #         print("Przycisk 'ENTER' (CSS Selector - uproszczony) został kliknięty.")
                

        #     except Exception as e_css_simplified:
        #         print("Nie udało się kliknąć przycisku 'ENTER' (CSS Selector - uproszczony):", e_css_simplified)

        #     # Tutaj możesz kontynuować dodając więcej metod, jeśli są dostępne
        #     print("Nie udało się znaleźć przycisku używając żadnej z metod.")











################# kliknij proced to quests   ---------- to chyba na góre 

    # try:
    #     time.sleep(2)  # Odczekuje 2 sekundy        # Kliknij przycisk na podstawie XPath lub tekstu na przycisku
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[3]/div/button')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'PROCEED TO QUESTS')]")
    #         przycisk_tekst.click()
    # except Exception:
    #     print("Nie udało się kliknąć przycisku proceed")






    # try:        # SPIN !!!
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/button')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'SPIN')]")
    #         przycisk_tekst.click()
    #         time.sleep(3)
    #     print("----SPIN !-----")        
    # except Exception:
    #     print("Nie udało się kliknąć przycisku SPIN")


    # try:
    #     # Czekanie na przycisk "allow" i jego kliknięcie
    #     spin_button = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/button')) or
    #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[1]/div/button'))
    #     )
    #     spin_button.click()
    #     print("Przycisk 'ENTER' został kliknięty.")
    #     time.sleep(2)
    #     return
    #     # suspend()
    #     # capcha()
    #     # problem_check()
    # except Exception as e:
    #     print("Nie udało się kliknąć przycisku enter", e)
    #     return








    #                            # SPIN 2 !!!

    #     new_func() 

    # def new_func():
    #     try:       
    #         try:
    #             przycisk_xpath = driver.find_element(By.XPATH, '//*[@id="radix-:r0:"]/div/div[2]/div[2]/button')
    #             przycisk_xpath.click()
    #         except:
    #             przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'SPIN')]")
    #             przycisk_tekst.click()
    #             time.sleep(5)
    #         print("----SPIN 2 ! ! -----") 
    #     except Exception:
    #         print("Nie udało się kliknąć przycisku 4")


    # ##################### ODBIERANIE NAGRODY ##########################
    #     try:
    #         element = WebDriverWait(driver, 30).until(
    #             lambda driver: driver.find_element(By.XPATH, "//*[contains(text(), 'Congrats!')]") or
    #                                    driver.find_element(By.XPATH, "//*[contains(text(), 'SHARE ON X')]")
    #             )
    #     except ExceptionGroup:
    #         print("Nie kliknięto Congrats")  
    #     print("Kliknięto Congrats !!!")    
        # try:
        #     time.sleep(5)
        #     przycisk_xpath = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/button')
        #     przycisk_xpath.click()
        #     print("Przycisk został kliknięty.")

        # except Exception as e:
        #     print("Wystąpił problem: ", e)

def mon():
    time.sleep(1)
    link = "https://app.monprotocol.ai/questing/missions"
    driver.get(link)
    
    refferal = "Bartosz416782"       ###### REFERAL CODE !!!!!!!!!!
    
    time.sleep(2) 
                            # CONNECT X
    try:        # Kliknij przycisk na podstawie XPath lub tekstu na przycisku
        try:
            przycisk_xpath = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div[3]/div[2]/button[1]/span')
            przycisk_xpath.click()
        except:
            przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'CONNECT X')]")
            przycisk_tekst.click()
            time.sleep(5)
        print("connect kliknięty")        
    except Exception:
        print("Nie udało się kliknąć connect to x")

## jak sie pojawi Zaloguj się do serwisu X --> logowanie twitt

                            # authorize app
        
    try:
        print("Oczekiwanie na element i jego kliknięcie")
        time.sleep(1)
        element = WebDriverWait(driver, 3).until(
            lambda driver: 
                driver.find_element(By.XPATH, "//*[contains(text(), 'Authorize app')]") or
                driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div'))
        



        try:
            przycisk_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/span/span")
            przycisk_xpath.click()
        except:
            przycisk_tekst = driver.find_element(By.XPATH, '//*[@id="allow"]')
            przycisk_tekst.click()
            time.sleep(2)  # Odczekuje 2 sekundy
    except Exception as e:
        print("Nie udało się kliknąć AUTHORIZE", e)
        problem_check()

#                       wpisz refa
    
    try:
        time.sleep(5)
                             # Wpisz dane do pola tekstowego
        pole_input = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[3]/div/div/div/input')
        # pole_input.clear()  # Czyści pole tekstowe przed wpisaniem nowych danych
        time.sleep(1)  # Odczekuje 2 sekundy
        pole_input.send_keys(refferal)
        print
    except Exception:
            


        print("Element do wpisania refa nie znaleziony na stronie.")   
        return
    try:
        enter_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div/div/div[3]/div/div/button')) or
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'ENTER')]"))
        )
        enter_button.click()
        time.sleep(2)
        return










        # time.sleep(3)
        # przycisk_xpath = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[3]/div/div/button')
        # przycisk_xpath.click()
    except Exception:
        print("nie kliknięto !")
        return      
            

       
            ######## zatwierdzenie reffa

    # try:
    #     time.sleep(7)  # Odczekuje 5 sekund        
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[3]/div/div/button')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'PROCEED TO MISSIONS')]")
    #         przycisk_tekst.click()
    #         time.sleep(3)
    # except Exception:
    #     print("Nie udało się kliknąć przycisku 3")

################# kliknij proced to quests   ---------- to chyba na góre 

    #     try:
    #         time.sleep(2)  # Odczekuje 2 sekundy        # Kliknij przycisk na podstawie XPath lub tekstu na przycisku
    #         try:
    #             przycisk_xpath = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[3]/div[2]/div/button')
    #             przycisk_xpath.click()
    #         except:
    #             przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'PROCEED TO QUESTS')]")
    #             przycisk_tekst.click()
    #     except Exception:
    #         print("Nie udało się kliknąć przycisku 4")






    # try:        # SPIN !!!
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div[2]/div/div[1]/div/button')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'SPIN')]")
    #         przycisk_tekst.click()
    #         time.sleep(5)
    #     print("----SPIN !-----")        
    # except Exception:
    #     print("Nie udało się kliknąć przycisku SPIN")
    #     return
    
    # return                      # SPIN 2 !!!

    # try:       
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/button[2]')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'SPIN')]")
    #         przycisk_tekst.click()
    #         time.sleep(5)
    #     print("----SPIN 2 ! ! -----") 
    # except Exception:
    #     print("Nie udało się kliknąć przycisku 4")


    ##################### ODBIERANIE NAGRODY ##########################
            
        # element = WebDriverWait(driver, 12).until(
        #     lambda driver: driver.find_element(By.XPATH, "//*[contains(text(), 'Congratulations!')]") or
        #                                driver.find_element(By.XPATH, "//*[contains(text(), 'SHARE ON X')]")
        # )

def pump():
    time.sleep(1)
    link = "https://pump.markets/"
    driver.get(link)
    
    refferal = "21146026"       ###### REFERAL CODE !!!!!!!!!!
    
    time.sleep(2) 
                            # CONNECT X
    # try:        # Kliknij przycisk na podstawie XPath lub tekstu na przycisku
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div[3]/div[2]/button[1]/span')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'CONNECT X')]")
    #         przycisk_tekst.click()
    #         time.sleep(5)
    #     print("connect kliknięty")        
    # except Exception:
    #     print("Nie udało się kliknąć connect to x")

## jak sie pojawi Zaloguj się do serwisu X --> logowanie twitt

                            # authorize app
        
    # try:
    #     print("Oczekiwanie na element i jego kliknięcie")
    #     time.sleep(1)
    #     element = WebDriverWait(driver, 3).until(
    #         lambda driver: 
    #             driver.find_element(By.XPATH, "//*[contains(text(), 'Authorize app')]") or
    #             driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div'))
        



    #     try:
    #         przycisk_xpath = driver.find_element(By.ID, "allow")
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, '//*[@id="allow"]')
    #         przycisk_tekst.click()
    #         time.sleep(2)  # Odczekuje 2 sekundy
    # except Exception as e:
    #     print("Nie udało się kliknąć AUTHORIZE", e)
        

###################################################################### wpisz refa

 
    try:
        time.sleep(2)
                             # Wpisz dane do pola tekstowego
        pole_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/div/section[1]/div/div/div[2]/div/input')
        # pole_input.clear()  # Czyści pole tekstowe przed wpisaniem nowych danych
        time.sleep(1)  # Odczekuje 2 sekundy
        pole_input.send_keys(refferal)
        print
    except Exception:
        print("Element nie został znaleziony na stronie.")   




            ######## zatwierdzenie reffa

    try:
        # Czekanie na przycisk "Follow" i jego kliknięcie
        connect_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/section[2]/div/div/button[1]/div[1]/div')) or
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Connect')]"))
        )
        connect_button.click()
        print("Przycisk 'connect to x' został kliknięty.")
        # suspend()
        # capcha()
        # problem_check()
    except Exception as e:
        print("Nie udało się kliknąć przycisku connect", e)





    # try:
    #     time.sleep(5)  # Odczekuje 2 sekundy        
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/div/section[2]/div/div/button[1]/div[1]/div')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'Connect')]")
    #         przycisk_tekst.click()
            
    # except Exception:
    #     print("Nie udało się kliknąć przycisku refa")

################# authorize

    try:
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[-1])  
        time.sleep(2)
        
   
            



        try:
            print("klikam jebane authorize...")
            przycisk_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]')
            przycisk_xpath.click()
        except:
            przycisk_tekst = driver.find_element(By.XPATH, '//*[@id="allow"]')
            przycisk_tekst.click()
        time.sleep(10)  # tu czekanie na przeładowanie okienka !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0]) 
    except Exception as e:
        print("Nie udało się kliknąć AUTHORIZE", e)
        time.sleep(1)
        # problem_check()
        # # driver.close()
        # time.sleep(2)
        driver.switch_to.window(driver.window_handles[0]) 
        print("karta zamknięta poprawnie")
    # except Exception:
    #         print("błąd logowania w okienku")
    #         time.sleep(10)
    #         driver.close()






    # try:
    #     time.sleep(1)  
    #     # Pobranie uchwytów do wszystkich otwartych kart (okien)
    #     handles = driver.window_handles

    #         # Przełączanie na nowo otwartą kartę (zakładamy, że to ostatnia karta)
    #     driver.switch_to.window(handles[-1])
    #     time.sleep(5)
    #         # Zamknięcie nowo otwartej karty
      
    #     try:
    #         przycisk_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div')
    #         przycisk_xpath.click()
    #     except:
    #         przycisk_tekst = driver.find_element(By.XPATH, "//button[contains(text(), 'Authorize app')]")
    #         przycisk_tekst.click()
        
            
    #         # Powrót do pierwotnej karty (zakładamy, że to pierwsza otwarta karta)
    #     driver.switch_to.window(handles[0])
    #     time.sleep(7)
    # except Exception:
    #     print("Nie udało się kliknąć AUTHORIZE")

    #     time.sleep(20)




########### LIKE AND RT
    try:
        # Czekanie na przycisk "Follow" i jego kliknięcie
        like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/section[2]/div/div/button[2]'))
            
        )



        # tu zamknięcie
        like_button.click()
        print("Przycisk LiR został kliknięty.")
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1]) 
        time.sleep(1)

        try:
            locators = [
                (By.XPATH, '//div[@data-testid="like"]'),
                (By.XPATH, '//svg[@class="r-4qtqp9 r-yyyyoo r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-50lct3 r-1srniue"]'),
                (By.XPATH, '//*[@id="id__98xb3q40vz8"]/div[3]/div/div'), ### XPATH DO POSTA Z X nie twitter
                (By.CSS_SELECTOR, 'div[data-testid="like"]'),
                (By.XPATH, '//*[@id="id__po31jdkjlyg"]/div[3]/div/div'),
                #(By.XPATH, '//div[contains(@class, "r-1niwhzg r-sdzlij r-xf4iuw r-o7ynqc")]/div')
                (By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[2]/div/div/article/div/div/div[3]/div[5]/div/div/div[3]/div/div')
            ]
        
            for locator in locators:
                try:
                    like_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locator))

                    like_button.click()
                    print("Kliknięto Like !")    
                    time.sleep(1) 
                except Exception:
                    print("Nie kliknięto like !")
        except Exception:
            print("wyjebało całe like !")
        try:
            repost_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/div/div')
            repost_button.click() 
            time.sleep(3)
            undo_elements = driver.find_elements(By.XPATH, "//span[contains(text(), 'Undo repost')]")

            # Jeśli napis "Undo repost" się nie pojawił, naciska inny przycisk
            if not undo_elements:
                undo_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/span')
                undo_button.click()
            print("Dodano !!!")        
        except Exception:
            print("wyjebało całe RT !")
        # tweet_like()
        # time.sleep(1)
        # tweet_retweet
        # time.sleep(1)
        driver.close()
        
        # tweet_like()
        # tweet_retweet()
        # time.sleep(1)
        # driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0]) 
        time.sleep(1)
 
        return





        # suspend()
        # capcha()
        # problem_check()
    except Exception as e:
        print("Nie udało się kliknąć przycisku LiR", e)
        driver.close()
        return
    



######### INVITE

    # try:
    #     # Czekanie na przycisk "Follow" i jego kliknięcie
    #     auth_button = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/section[2]/div/div/button[3]'))
            
    #     )
    #     auth_button.click()
    #     print("Przycisk invite kliknięty.")
    #     # suspend()
    #     # capcha()
    #     # problem_check()
    # except Exception as e:
    #     print("Nie udało się kliknąć przycisku invite", e)










# /html/body/div[1]/div/div[2]/main/div/section[2]/div/div/button[1]/div[1]/div
#         try:
#             przycisk_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/div/section[2]/div/div/button[1]')
#             przycisk_xpath.click()
#         except:
#             print("nie nacisnięto connect")
# # like and RT
#         try:
#             przycisk_xpath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/div/section[2]/div/div/button[2]/div[1]')
#             przycisk_xpath.click()
#         except:
#             print("nie kliknięto likr RT")

#         try:
#             print("zamykam karte")



#         except:
#             print("nie kliknięto likr RT")
        
        
#         try:
#             time.sleep(5)
            

#             # Pobranie uchwytów do wszystkich otwartych kart (okien)
#             handles = driver.window_handles

#             # Przełączanie na nowo otwartą kartę (zakładamy, że to ostatnia karta)
#             driver.switch_to.window(handles[-1])
#             time.sleep(2)
#             # Zamknięcie nowo otwartej karty
#             driver.close()
            
#             # Powrót do pierwotnej karty (zakładamy, że to pierwsza otwarta karta)
#             driver.switch_to.window(handles[0])
#             time.sleep(2)
#         except Exception:
#             print("wyjebało zamykanie karty")

#         try:
#             przycisk_xpath = driver.find_element
#             przycisk_xpath.click()
#         except:
#             print("błąd tweet your invite kod")
#         time.sleep(5)




#(By.XPATH, '/html/body/div[1]/div/div[2]/main/div/section[2]/div/div/button[3]/div[1]')





        # try:
        #     element = WebDriverWait(driver, 30).until(
        #         lambda driver: driver.find_element(By.XPATH, "//*[contains(text(), 'Congratulations!')]") or
        #                             driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/div[2]/a")
        #         )
        # except ExceptionGroup:
        #     print("Nie kliknięto Congrats")  











# def battle():
#     driver.get("https://battleshowdown.com")

#     try:
#         # Oczekiwanie na przycisk "Connect with" i kliknięcie go
#         connect_with_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[1]/div/div/div/div[1]/div[2]"))
#         )
#         connect_with_button.click()
        
#         # Oczekiwanie na drugi element do kliknięcia i kliknięcie go
#         # Uwaga: Poniższy XPath może nie być aktualny, ponieważ wygląda na specyficzny dla Twittera
#         # i może wymagać zaktualizowania na podstawie aktualnej struktury strony
#         second_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/span/span"))
#         )
#         second_button.click()

#     except Exception as e:
#         print(f"Wystąpił błąd: {e}")









# def battle():
#     driver.get("https://battleshowdown.com")
#     global driver , refferal
#     refferal = "ip6zia"

#     try:
#         # Oczekiwanie na przycisk "Connect with" i kliknięcie go
#         connect_with_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[1]/div/div/div/div[1]/div[2]"))
#         )
#         connect_with_button.click()
        
#         # Oczekiwanie na drugi element do kliknięcia i kliknięcie go
#         # Uwaga: Poniższy XPath może nie być aktualny, ponieważ wygląda na specyficzny dla Twittera
#         # i może wymagać zaktualizowania na podstawie aktualnej struktury strony
#         second_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div/div/span/span"))
#         )
#         second_button.click()

#     except Exception as e:
#         print(f"Wystąpił błąd: {e}")








#     try:
#         # Oczekiwanie na pojawienie się okienka modalnego
#         modal = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//*[@id='modal-root']/div/div[2]"))
#         )
#         print("Okienko modalne zostało wykryte.")

#         # Oczekiwanie na przycisk wewnątrz okienka modalnego i kliknięcie go
#         button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//*[@id='modal-root']/div/div[2]/div[2]/div[4]"))
#         )
#         button.click()
#         print("Przycisk wewnątrz okienka modalnego został kliknięty.")

#     except Exception as e:
#         print(f"Wystąpił błąd: {e}")







#     try:
#         # Kliknięcie w przycisk "Referals"
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Referals") or @xpath="/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[2]"]'))
#         ).click()

#         # Definiowanie XPaths pól input
#         input_fields_xpath = [
#             '/html/body/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div[1]/div[1]/input',
#             '//*[@id="__next"]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div[1]/div[2]/input',
#             '//*[@id="__next"]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div[1]/div[3]/input',
#             '//*[@id="__next"]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div[1]/div[4]/input',
#             '//*[@id="__next"]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div[1]/div[5]/input',
#             '//*[@id="__next"]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div[1]/div[6]/input'
#         ]

#         # Wklejanie po jednym znaku ze zmiennej referral do każdego pola
#         for i, field_xpath in enumerate(input_fields_xpath):
#             if i < len(refferal):  # Aby uniknąć wyjścia poza zakres stringa referral
#                 input_field = WebDriverWait(driver, 10).until(
#                     EC.visibility_of_element_located((By.XPATH, field_xpath))
#                 )
#                 input_field.send_keys(refferal[i])
#                 time.sleep(0.5)  # Mała pauza, aby upewnić się, że strona zdąży zarejestrować wpisany znak

#         # Kliknięcie w przycisk "Claim"
#         claim_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Claim") or @xpath="//*[@id=\'__next\']/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div[2]/button"]'))
#         )
#         claim_button.click()

#     except Exception as e:
#         print(f"Wystąpił błąd: {e}")
#################################################################################### OSY

def battle():
    
    time.sleep(2)
    #SITE LOGIN
    link = "https://battleshowdown.com/"
    wait = WebDriverWait(driver, 5)
    referalcode = "jm84hj"
    try:
        driver.get(link)
        time.sleep(3)
        connect_x = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]')))
        connect_x.click()
    except Exception as er:
        print("Unable to load site or click connect:", er)
 
    try:
        authorize = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div/div[1]/div[3]/div')))
        authorize.click()
    except Exception as e:
        print(e)
 
    try:
        bonus = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[4]')))
        bonus.click()
    except Exception as e:
        driver.refresh()
        # time.sleep(10)
        print(e)
 
    # REFERAL CODE
    try:
        referaltab = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[2]')))
        referaltab.click()
    except Exception as e:
        print(e)
 
    try:
        referal_input = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div[1]/div[1]/input')))
        referal_input.send_keys(referalcode)
    except Exception as e:
        print("brak imputu do refa...")
 
    try:
        claim_referal = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/div[3]/div/div/div[2]/button')))
        claim_referal.click()
    except Exception as e:
        print("ref nie kliknięty...")
 
    try:
        back_to_farm = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[1]')))
        back_to_farm.click()
    except Exception as e:
        print(e)
        
        
    print("Black man on white man's farm starting doing free tasks... [+]")
    # time.sleep(6)
    # tasks_done = 0
    windows = driver.window_handles
    quest_nr = 0



############################################################# #QUESTY



    try:
        while True:
            # driver.get(link)
            time.sleep(1)
            lista = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]')
            lista.click()
            time.sleep(1)  # Czekanie między kliknięciami
            try:
                # Sprawdzenie, czy pojawił się przycisk "Add"
                button2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]')
                button2.click()
            except Exception:
                print("pierwszy niekliknięty...")
                return
            try:
                button2ipol = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]')
                button2ipol.click()
               
            except Exception:
                print("Nie kliknięto read albo join")
                
                




            time.sleep(2) 
            windows = driver.window_handles
            driver.switch_to.window(windows[-1])




            time.sleep(1)
            # Wysyłanie kombinacji klawiszy CTRL+ENTER
            okienko = ActionChains(driver)
            #okienko = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]') ##
            okienko.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform() # 
            time.sleep(1)
            # Zamknięcie karty


#####################################################


            try:
                print("zaczynam sprawdzać słowa...")
                wait = WebDriverWait(driver, 1)  # Ustawienie maksymalnego czasu oczekiwania
                locators = [
        ######################################################################################################## SUSPEND
                    ("//*[contains(text(), 'Edit profile')]", zmiana_nazwy),
                    #("//*[contains(text(), 'Your account may not be allowed')]", logowanie_twitter),
                    #("//*[contains(text(), 'Zaloguj się do serwisu X')]", logowanie_twitter),

                ]

                for xpath, action in locators:
                    try:
                        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                        print(f"Znaleziono tekst: {element.text}")  # Wyświetlanie znalezionego tekstu
                        time.sleep(1)
                        try:
                            problem_check()
                        except Exception:
                            print("nie było problemu")

                        action()
                        #time.sleep(60)  # Opcjonalnie, jeśli potrzebujesz opóźnienia
                        continue
                    except TimeoutException:
                        continue  # Jeśli element nie został znaleziony, kontynuuj pętlę

                print("to nie zmiana nazwy !")

            except Exception:
                print("Wywaliło !!!!!!!!!!!!")
            print("Zamykam szukanie zmiany nazwy")





            try:
                time.sleep(1)
                driver.close()
                time.sleep(1)
                # Powrót do karty 0
                driver.switch_to.window(windows[0])
                time.sleep(3)  # Odczekanie 3 sekundy
            except Exception:
                print(" Nie zamknięto katy !!")


            try:
                xpaths = [
                    '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[2]',
                    '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]',
                    '/html/body/div[2]/div/div[2]/div[*]/div[1]/div[3]/div[*]',
                    "//div[contains(@class, 'btn-primary')][contains(text(), 'Claim')]"
                ]

                for xpath in xpaths:
                    try:
                        # Sprawdzanie, czy element jest klikalny
                        claim = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                        if claim:
                            claim.click()  # Kliknięcie pierwszego dostępnego elementu
                            print("Kliknięto element:", xpath)
                            break  # Przerwanie pętli po kliknięciu
                    except:
                        # Przechwycenie wyjątku, gdy element nie jest dostępny lub czas oczekiwania minął
                        print(f"Element dla XPath {xpath} nie jest dostępny lub czas oczekiwania minął.")
                print("Przycisk CLAIM został kliknięty.")
            except Exception:
                print("Nie kliknięto CLAIM !!!")
            time.sleep(2)
            try:
                done = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[4]')) or
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'DONE')]"))
                )
                done.click()
                print("Przycisk DONE został kliknięty.")
            except Exception:
                print("nie było done")

            time.sleep(1)

            quest_nr = quest_nr +1
            print("\nQUEST NR --> ", quest_nr, " <--- \n")
            continue # /html/body/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[2]



    except KeyboardInterrupt:
        print("Zakończono działanie skryptu.")

    try:
        driver.get(link)
        time.sleep(3)
        points = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div/div/div[1]/div[2]/div[4]/div/div[9]/span')
        print(points)   
    except Exception as e:
        print(e)


def zmiana_nazwy():
    try:
               
        nick_input = driver.find_element(By.CSS_SELECTOR, '[name="displayName"]')
        nick_input.click()
        nick_input.send_keys(" $ELS")
        time.sleep(3)
        save = driver.find_element(By.CSS_SELECTOR, '[data-testid="Profile_Save_Button"]')
        save.click()
        time.sleep(5)
        
    except Exception:
        print("nazwa nie zmieniona")
        





    ############################# OSY -->
    
    # try:
    #     driver.refresh()
    #     time.sleep(10)
    #     a = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]')
    #     a.click()
    #     time.sleep(7)
    #     a1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]')
    #     a1.click()
    #     time.sleep(7)
    #     windows = driver.window_handles
    #     driver.switch_to.window(windows[-1])
    #     time.sleep(3)
    #     driver.close()
    #     time.sleep(3)
    #     driver.switch_to.window(windows[0])
    #     time.sleep(7)
        
    #     a2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[2]')
    #     a2.click()
    #     time.sleep(7)

    #     a3 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[4]')
    #     a3.click()
    #     tasks_done = tasks_done + 1
    #     print("Total tasks done", tasks_done)
    #     time.sleep(7)
    # except Exception as e:
    #     print("Quest 1 not done", e)
        
    # #2
    # try:
    #     driver.refresh()
    #     time.sleep(10)
    #     a = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]')
    #     a.click()
    #     time.sleep(7)
    #     a1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]')
    #     a1.click()
    #     time.sleep(7)
    #     windows = driver.window_handles
    #     driver.switch_to.window(windows[-1])
    #     time.sleep(3)



    #     # TU CTRL ENTER 





    #     driver.close()
    #     time.sleep(3)
    #     driver.switch_to.window(windows[0])
    #     time.sleep(7)
    #     a2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[2]')
    #     a2.click()
    #     time.sleep(7)
    #     a3 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[4]')
    #     a3.click()
    #     tasks_done = tasks_done + 1
    #     print("Total tasks done", tasks_done)
    #     time.sleep(7)
    # except Exception as e:
    #     print("Quest 2 not done", e)
        
    # #3
    # try:
    #     driver.refresh()
    #     time.sleep(10)
    #     a = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]')
    #     a.click()
    #     time.sleep(7)
    #     a1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]')
    #     a1.click()
    #     time.sleep(7)
    #     windows = driver.window_handles
    #     driver.switch_to.window(windows[-1])
    #     time.sleep(3)
    #     driver.close()
    #     time.sleep(3)
    #     driver.switch_to.window(windows[0])
    #     time.sleep(7)
    #     a2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[2]')
    #     a2.click()
    #     time.sleep(7)
    #     a3 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[4]')
    #     a3.click()
    #     tasks_done = tasks_done + 1
    #     print("Total tasks done", tasks_done)
    #     time.sleep(7)
    # except Exception as e:
    #     print("Quest 3 not done", e)
      
    # #4  
    # try:
    #     driver.refresh()
    #     time.sleep(10)
    #     a = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]')
    #     a.click()
    #     time.sleep(7)
    #     a1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]')
    #     a1.click()
    #     time.sleep(7)
    #     windows = driver.window_handles
    #     driver.switch_to.window(windows[-1])
    #     time.sleep(5)
        
    #     nick_input = driver.find_element(By.CSS_SELECTOR, '[name="displayName"]')
    #     nick_input.click()
    #     nick_input.send_keys(" $ELS")
    #     time.sleep(3)
    #     save = driver.find_element(By.CSS_SELECTOR, '[data-testid="Profile_Save_Button"]')
    #     save.click()
    #     time.sleep(5)
    #     driver.close()
    #     time.sleep(3)
    #     driver.switch_to.window(windows[0])
    #     time.sleep(15)
    #     a2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[2]')
    #     a2.click()
    #     time.sleep(7)
    #     a3 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[4]')
    #     a3.click()
    #     tasks_done = tasks_done + 1
    #     print("Total tasks done", tasks_done)
    #     time.sleep(7)    
    # except Exception as e:
    #     print("Failed to change nickname, do it manually", e)
    #     #save()
        
        
       
    # #30 tasks task_element == 2
    # for i in range(30):
    #     try:
    #         driver.refresh()
    #         time.sleep(10)
    #         a = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]')
    #         a.click()
    #         time.sleep(7)
    #         a1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[2]')
    #         a1.click()
    #         time.sleep(7)
    #         windows = driver.window_handles
    #         driver.switch_to.window(windows[-1])
    #         time.sleep(3)
    #         driver.close()
    #         time.sleep(3)
    #         driver.switch_to.window(windows[0])
    #         time.sleep(7)
    #         a2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[1]/div[4]/div[2]')
    #         a2.click()
    #         time.sleep(7)
    #         a3 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[4]')
    #         a3.click()
    #         tasks_done = tasks_done + 1
    #         print("Total tasks done", tasks_done)
    #         time.sleep(7)
    #     except Exception as e:
    #         print(f"Quest {i} not done", e)
        
        
            
    # with open("output.txt", "a", encoding="utf-8") as output:
    #     output.write(f"Token: {actual_token} Total tasks: {tasks_done} Points: {text}000 ")








#####################################################################################





def beyond():
    max_try = 3
    tryB = 0
    print("zaczynam BEYOND")
    
    time.sleep(3)
    global driver , token, token_z_pliku
    
    options = webdriver.FirefoxOptions()
    options.add_argument("--disable-site-isolation-trials")
    options.add_argument("--profile-directory=YourProfile")
   

    while tryB < max_try:


        tryB = tryB +1
        link = "https://beyondblitz.app/dashboard"
        try:
            referallcode = "KCHVK04T"
            driver.get(link)
            time.sleep(3) #### 
            button1 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="login-wrapper"]/div[2]/div[1]/div/button')) or
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]"))
            )
            button1.click()

            time.sleep(3)
            try:
                auth_button1 = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="allow"]')) or
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Authorize')]"))
                )
                auth_button1.click()
                # time.sleep(10)
            except Exception:
                print("nie kliknięto authorize!")

            time.sleep(3)

            try:

                request = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/button/div[2]/div[2]/span')) or
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Request')]"))
                )
                request.click()

            except Exception:
                print("nie kliknięte...")
                time.sleep(3)
                
                

            try:
                time.sleep(2)
                referal_input=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/div/input')
                referal_input.send_keys(referallcode)
                time.sleep(1)
            except Exception:
                    
                    print("nie wpisano..")
                    continue
                    # driver.get(link)
                    
            try:
                time.sleep(3)
                continue_button = WebDriverWait(driver, 5).until( #/html/body/div[1]/div/div[2]/div[1]/form/div/button/div[2]/div[2] - xpath z firefox
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div[1]/form/div/button')) or
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]"))
                )
                continue_button.click()
            except Exception:
                time.sleep(1)
                print("nie kliknięto CONTINUE")
                    # driver.get(link)


            time.sleep(3)
            print('REF DODANY POPRAWNIE !!')
            return # return # ??
        except Exception:
            print("wryjebało beyond")
            time.sleep(2)
            
    # else:
    #     return





# def pixel():

#     link = "https://hub.pixelpix.com/inv/3OADIU"
#     try:
        
#         driver.get(link)
#         time.sleep(1) #### 
#         button1 = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/button'))  or
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'GO')]"))
#         )
#         button1.click()

#         time.sleep(5)

#         auth_button1 = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[3]/div/div/div/div/div[4]/button[3]')) 
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'X LOGIN')]"))
#         )
#         auth_button1.click()
#         time.sleep(10)
#     except Exception:
#         print("wyjebało...")



#         driver.get(link)
#         time.sleep(1) #### 
#         button1 = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="allow"]'))  or
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Authorize')]"))
#         )
#         button1.click()



def trip():
    global driver , link

    link = "https://app.overtrip.com/auth/inv/QUZ48H"
    try:
        
        driver.get(link)
        time.sleep(2) #### 
        button1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div/app-auth/div/app-login-email/div/div/div[2]/app-login-twitter/button')) or
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'LOGIN WITH X')]"))
        )
        button1.click()

        time.sleep(3)

        auth_button1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="allow"]')) or
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Authorize App')]"))
        )
        auth_button1.click()
        time.sleep(5)
    except Exception:
        print("wyjebało...")



#         driver.get(link)
#         time.sleep(1) #### 
#         button1 = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//*[@id="allow"]'))  or
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Authorize')]"))
#         )
#         button1.click()









################################################################################################
    # print("------------------ G I T -----------------------")  #################################
    # time.sleep(2)  ############################################################################






    



    
    

    # for _ in range(180 // 5):
    #     winsound.Beep(420, 1000)  # 440 Hz przez 1000 ms
    #     time.sleep(   4   -1) #   -1 nie usuwać albo suma x1000 większ od ms !!

##############################################################################

##############################################################################

##############################################################################

print("- - - - - - - - - - - -  Startuje SpeedBota - - - - - - - - - - - -  \n\n")


with open('dane2.txt', 'r', encoding='utf-8') as plik:
    wiersze = plik.readlines()
# Uzyskujemy liczbę wierszy
liczba_wierszy = len(wiersze)

# Teraz tworzymy pętlę, która wykonuje się tyle razy, ile jest wierszy
for i in range(liczba_wierszy):
    # Tutaj umieść kod, który ma być wykonany dla każdego wiersza
    print("                       Liczba tokenów w maszynce: ",liczba_wierszy)

# for i in range(10): 

#############################
#          MAIN             #
############################# 
    try:
        setup_dane()

        new_driver()

        login_cookies()
            
        logowanie_twitter()

        pobierz_token()

        aktualizuj_token()

        zapisz_dane()

        time.sleep(2)

    except:        
        print("SPEED BOT - - - WYJEBAŁO MAIN !")
        petla_nr = petla_nr +1
        time.sleep(2)
        driver.quit()
        time.sleep(2) 
        continue
#############################
#          MAILE            #
#############################

    # change_mail()
    # change_auth()
    # change_pass()


#############################
#         TWITTER           #
#############################
    # try:

        
    #     tweet_farmer('linki.txt')
    #     # problem_check()

    #     follow_twit()

    # except:        
    #     print("SPEED BOT - - - WYJEBAŁO FARME TWITTER !")
    #     petla_nr = petla_nr +1
    #     time.sleep(2)
    #     #driver.quit()
    #     time.sleep(2)
    #     continue

#############################
#         AIRDRY            #
#############################
    try:
        #trip()

        #battle()

        #beyond()
        
        #sidequest()

        #mon()

        pump()

    except:        
        print("SPEED BOT - - - WYJEBAŁO AIRDROPY !")
        petla_nr = petla_nr +1
        time.sleep(2)
        driver.quit()
        time.sleep(2)
        continue


#############################
#           QUIT            #
#############################


    petla_nr = petla_nr +1

    driver.quit()

    print(f"- - - - - SpeedBot - - - - - Pętla {petla_nr}  / tokenów {liczba_wierszy} ! \n"       )
    
    print(f"- - - - - SpeedBot - - - - - Zalogowanych  poprawnie  {login_pass}  /   {petla_nr}\n")

    print(f"- - - - - SpeedBot - - - - - Niezalogowanych {not_logged} , zakończony token: {petla_nr-1}\n")  

    print ("nowy_token: " ,nowy_token ,"\n")

    print("token_z_pliku: " ,token_z_pliku[petla_nr],"\n")

    print("Pętle numer: " ,petla_nr,"")

    print("Do pliku dodano - - ",capcha_do_zrobienia," - - CapChy do zrobienia\n")

    print("Do pliku dodano - - ", zablokowane," - - zablokowanych kont\n")

    print("------------------- KONIEC ------------------- \n\n\n ")

    time.sleep(3)