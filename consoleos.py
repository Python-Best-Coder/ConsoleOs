import os
import keyboard
import time
import requests
import random
import getpass
import ast
import string
import re
import o
import base64

from bs4 import BeautifulSoup


# Function to provide options and handle user input
def Option(question: str, options: list) -> str:
    x = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        print(question)
        for idx, option in enumerate(options):
            if idx == x:
                print('>', option)
            else:
                print(option)

        time.sleep(0.01)
        
        if keyboard.is_pressed('down') and not x + 1 > len(options) - 1:
            x += 1
            time.sleep(0.1)
        elif keyboard.is_pressed('up') and not x - 1 < 0:
            x -= 1
            time.sleep(0.1)
        elif keyboard.is_pressed('shift'):
            time.sleep(0.1)  # Wait briefly to avoid multiple key presses
            while keyboard.is_pressed('shift'):  # Wait until 'shift' is released
                time.sleep(0.01)
            return options[x]

# Function to handle kernel errors
def KernelError():
    return Option("Kernel Error!", ['Restart', 'Shutdown'])

print("Welcome to Console.os.")

import os
isitok = True
apps = ['testingapp','File Manager', 'Settings', 'Shutdown', 'the virus', 'ConsoleBrowse', 'Terminal']
print(os.getcwd())  # prints the current working directory
# adjust the path as needed

# Directory for data storage
data = r'C:/Users/' + getpass.getuser() + r'/ConsoleOs' r'/ConsoleOsData'
datafound = False
datasaved = {'Useless':'','History':[],'Balance':0}
if not os.path.exists(data):
    print("Data not Found. Creating Directory...")

    os.makedirs(data)
# Function to list files in a directory
def list_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        return files
    except FileNotFoundError:
        print("The directory does not exist")
    except PermissionError:
        print("You do not have permission to access this directory")

        # Check if data file exists and load data
for file in list_files_in_directory(data):
    if file == 'donotdelete.txt':
        datafound = True
        print("Reading data...")
        with open(os.path.join(data, 'donotdelete.txt'), 'r') as file:
            read = o.decrypt_string(o.decrypt_string(file.read()))
            print(read)
            # Split the string into key-value pairs
            try:
                datasaved = ast.literal_eval(str(read))

            except Exception:
                datasaved = str(o.encrypt_string("{'Useless':'','History':[],'Balance':0}"))
            print(datasaved)
time.sleep(1)



if not datafound:
    print("Data not found... Writing new file...")
    file_path = os.path.join(data, 'donotdelete.txt')
    with open(file_path, 'w') as file:
        file.write(str(datasaved))
    print(f"File '{file_path}' created.")



# Function to handle system operations
def System():
    
    while True:
        app = Option('Choose an app:', apps)
        print(f"Opening {app}..")
        if app == 'testingapp':
            a = Option("WHY ARE YOU HERE",['a','b'])
            if a == 'b':
                x = input("Write to data... > ")
                datasaved['Useless'] = x
            else:
                Option(datasaved['Useless'],['GET OUT!'])
            
        if app == 'Settings':
            setting = Option('Settings', ['BuildModule'])
            if setting == 'BuildModule':
                Option("BuildModule: 0.0.2", ['Exit'])
        elif app == 'Terminal':
            os.system('cls')
            inp = input("> ")
            install = re.search(r'\$sudo inst \;(.+)',inp)
            package = re.search(r'\$sudo instpackage \;(.+)',inp)
            hELL = re.search(r'\$sudo HELP \;useful',inp)
            if hELL:
                for i in range(1,100):
                    print("Installing..")
                    print('[','#'*i,'0'*(100-i),']')
                    time.sleep(random.uniform(0.01,0.1))
                    os.system('cls')
                apps.append('really useful')
            if install:
                
                
                appsincloud = ['appstore','10110','$sudo', 'THEPACKAGE']
                appinstalling = install.group(1)
                if appinstalling in appsincloud and not appinstalling in apps:
                    for i in range(1,100):
                        print("Installing..")
                        print('[','#'*i,'0'*(100-i),']')
                        time.sleep(random.uniform(0.01,0.1))
                        os.system('cls')
                    apps.append(appinstalling)
            elif package:
                appsincloud = ['consoleoscoder']
                appinstalling = package.group(1)
                if appinstalling in appsincloud and not appinstalling in apps:
                    for i in range(1,100):
                        print("Installing Package..")
                        print("this may take long.")
                        print('[','#'*i,'0'*(100-i),']')
                        time.sleep(random.uniform(0.01,0.2))
                        os.system('cls')
                    apps.append(appinstalling)

            else:
                print("Failed to install app: app not found")
                time.sleep(3)
        elif app == '$sudo':
            x = 0
            while True:
                os.system('cls')
                x += 1
                nameer = string.ascii_letters
                randomname = ''
                for _ in range(4):
                    randomname += random.choice(nameer)
                
                print(f'$sudo inst ;{randomname}')
                time.sleep(1)
                if x == 30:
                    Option("Paitience.",[''])
                    break
            if not 'Paitience' in apps:
                apps.append('Paitience')
        elif app == 'really useful':
            x = 1
            while True:
                print("Installing..")
                print('[','#'*x,'0'*(100-x),']')
                time.sleep(random.uniform(0.01,0.1))
                os.system('cls')
                if random.randint(1,4) != 4:
                    x += 1
                else:
                    y = random.randint(1,10)
                    if x > y:
                        os.system('cls')
                        for i in range(y):
                            x -= 1
                            print("Installing..")

                            print('[','#'*x,'0'*(100-x),']')
                            time.sleep(0.1)
                            os.system('cls')
                if x >= 99:
                    os.system('cls')
                    print("the leakrs saved you again.. pretty lucky..")
                    Option('oh..',['>'])
                    

        elif app == 'THEPACKAGE':
            alphabet = 'λß©∂€ҒḡҺ!jкℓм∩оρq®ƨ†μνωχ¥z'
            alpha = {
                'a': 'λ',
                'b': 'ß',
                'c': '©',
                'd': '∂',
                'e': '€',
                'f': 'Ғ',
                'g': 'ḡ',
                'h': 'Һ',
                'i': '!',
                'j': 'j',
                'k': 'к',
                'l': 'ℓ',
                'm': 'м',
                'n': '∩',
                'o': 'о',
                'p': 'ρ',
                'q': 'q',
                'r': '®',
                's': 'ƨ',
                't': '†',
                'u': 'μ',
                'v': 'ν',
                'w': 'ω',
                'x': 'χ',
                'y': '¥',
                'z': 'z'
            }
            e = input('import a string of txt for only using letters in the alphabet.')
            strtoprint = ''
            for letter in e:
                if letter in alpha:
                    strtoprint += f'{alpha[letter]}'
                else:
                    strtoprint += letter
            Option(strtoprint,['Exit'])
        elif app == 'Paitience':
            x = 600
            while x > 0:
                os.system('cls')
                print(f"Just wait for {x} more seconds. you'll be fine.")
                time.sleep(1)
                x -= 1
        elif app == 'File Manager':
            filemanage = Option("File Manager", ['Write File','Open File'])
            time.sleep(0.4)
            if filemanage == 'Open File':
                name = input('Filepath > ')
                if not name == '>':
                    if name.startswith('"') and name.endswith('"'):
                        name = name[1:-1]
                    try:
                        with open(name, 'r') as file:
                            text = file.read()
                            Option(text,['Exit'])
                    except Exception as e:
                        Option("There was a error that happened when opening the file. so we saved you from getting a console error.",['Exit'])

                else:
                    Option("...",['Haha'])
                    Option("Its not funny lil bro",['and?'])
                    if not Option("Do you want your death?",['What you gonna do?','im sorry..']) == 'im sorry..':
                        print("ALRIGHT FINE.")
                        time.sleep(3)
                        KernelError()
                    else:
                        print("Its not ok.")
                        time.sleep(4)
                        datasaved['Useless'] = 'ITS NOT OK '*1000
                        isitok = False

               
            if filemanage == 'Write File':
                name = input("Name > ")
                text = input("Text > ")
                file_path = os.path.join(data, name + '.txt')
                
                # Write text to file
                with open(file_path, 'w') as file:
                    file.write(text)
                
                print(f"File '{name}.txt' saved to '{data}'")
                
        elif app == 'Shutdown':
            print("Saving data...")
            file_path = os.path.join(data, 'donotdelete.txt')
            with open(file_path, 'w') as file:
                pass
            with open(file_path, 'w') as file:
                file.write(str(o.encrypt_string(datasaved)))
            print("Shutting down")
            print("Goodbye!")
            break
        elif app == '10110':
            Option("01010111 01001000 01011001 00100000 01000100 01001001 01000100 00100000 01011001 01001111 01010101 00100000 01000100 01001111 00100000 01010100 01001000 01001001 01010011",['winwin'])
            Option("im removing all your ram.",['nooo'])
            x = 100
            while True:
                if not x == 0:
                    Option("THE LEAKRS ARE COMING",[f'NO PLS! ILL GIVE YOU {x} COOKIES!'])
                else:
                    Option("the gods has savd u from the leakrs!",['what?'])
                    break
                x -= 1
        
        elif app == 'the virus':
            print("SYSTEMOS has stopped responding.")
            time.sleep(1)
            kernel = KernelError()
            if kernel == 'Shutdown':
                print('FORCE SHUTDOWN')
                break
            else:
                print("FORCE RESTART..")
                time.sleep(2)
                continue
        elif app == 'appstore':
            x = Option("Install App:",['base64 translator','Lottery!'])
            
            if x == 'base64 translator':
                for i in range(1,100):
                    print("Installing...")
                    print('[','#'*i,'0'*(100-i),']')
                    os.system('cls')
                    time.sleep(random.uniform(0.01,0.1))
                    if not x in apps:
                        apps.append(x)
            elif x == 'Lottery!':
                for i in range(1,100):
                    print("Installing...")
                    print('[','#'*i,'0'*(100-i),']')
                    
                    time.sleep(random.uniform(0.01,0.1))
                    os.system('cls')
                    if not x in apps:
                        apps.append(x)
        elif app == 'base64 translator':
            inp = input("> ")
            x = bytes(inp,'utf-8')
            Option(f"Base64: {str(base64.b64encode(x))}",['exit'])




        elif app == 'Lottery!':
            while True:
                try:
                    inp = int(input("Bet: "))
                    break
                except Exception as e:
                    print("error.")

            turn = 1
            symbols = ['$','%','&']
            x = '$'
            y = '$'
            z = '$'
            os.system('cls')
            for _ in range(3):
                lastsymbol = ''
                for _ in range(random.randint(10,100)):
                    print(f'{x}|{y}|{z}')
                    while True:
                        if turn == 1:
                            x = random.choice(symbols)
                        elif turn == 2:
                            y = random.choice(symbols)
                        else:
                            z = random.choice(symbols)
                        if turn == 1:
                            if not x == lastsymbol:
                                break
                        if turn == 2:
                            if not y == lastsymbol:
                                break
                        if turn == 3:
                            if not z == lastsymbol:
                                break
                    time.sleep(0.1)
                    os.system('cls')
                turn += 1
            print(f'{x}|{y}|{z}')
            time.sleep(1)
            os.system('cls')
                    

            if x == y and y == z:
                Option("You win!",['yay'])
                datasaved['Balance'] += inp
            else:
                Option("You lose!",['Ya- wait, what?!'])
                datasaved["Balance"] -= inp






        elif app == 'ConsoleBrowse':
            if isitok:
                print("History")
                historiesprinted = 0
                for x in datasaved['History']:
                    if historiesprinted <= 10:
                        print(x)
                        historiesprinted += 1
                    else:
                        break

                
                browse = input("Website >")
                url = browse.strip()

                
                if not url.startswith("http://") and not url.startswith('https://'):
                    url = 'https://' + url
                
                # Replace ':' with '.' before storing in history

                
                response = fetch_webpage(url)
                if response:
                    parsed_content = parse_html(response)
                    print(parsed_content)
                    datasaved['History'].append(url)
                
                input("Press Enter to continue...")
                continue
            else:
                Option("YOU CANT GET AWAY. "*20,['alright thats it'])
                Option("OHHH MY GOOOOOo- THIS IS IMPOSSIBLE.",['noob'])
                isitok = True


# Function to fetch a web page using requests
def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Function to parse HTML content using BeautifulSoup
def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    text = text.replace('\n',' ')  # Remove newlines
    return text

# Start the console OS system
System()

