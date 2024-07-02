import os
import keyboard
import time
import requests
import shutil
import random
import getpass
import ast
import re
import base64

from time import sleep

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
        print('\n')
        time.sleep(0.01)

        if keyboard.is_pressed('down') and not x + 1 > len(options) - 1:
            x += 1
            time.sleep(0.1)
        elif keyboard.is_pressed('up') and not x - 1 < 0:
            x -= 1
            time.sleep(0.1)
        elif keyboard.is_pressed('shift') or keyboard.is_pressed('enter'):
            # delVar = 0
            # while (delVar<1000000): delVar+=1
            if (keyboard.is_pressed('shift') or keyboard.is_pressed('enter')):
                # time.sleep(0.2)  # Wait briefly to avoid multiple key presses
                while keyboard.is_pressed('shift') or keyboard.is_pressed('enter'):  # Wait until 'shift' is released
                    time.sleep(0.01)
                delVar = 0
                while (delVar<1000000): delVar+=1
                return options[x]
            else:
                continue
        elif keyboard.is_pressed('esc'): return False

# Function to handle kernel errors
def KernelError():
    return Option("Kernel Error!", ['Restart', 'Shutdown'])


print("Welcome to Console.os.")

import os

isitok = True
apps = ['testingapp', 'File Manager', 'Settings', 'Shutdown', 'the virus', 'ConsoleBrowse', 'Terminal']
print(os.getcwd())  # prints the current working directory
# adjust the path as needed

# Directory for data storage
data = r'C:/Users/' + getpass.getuser() + r'/ConsoleOsData'
datafound = False
datasaved = {'Useless': '', 'History': []}
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

for file in list_files_in_directory(data):
    if file == 'donotdelete.txt':
        datafound = True
        print("Reading data...")
        with open(os.path.join(data, 'donotdelete.txt'), 'r') as file:
            read = file.read()
            # Split the string into key-value pairs
            datasaved = ast.literal_eval(read)
            print(datasaved)

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
            a = Option("WHY ARE YOU HERE", ['a', 'b'])
            if a == 'b':
                x = input("Write to data... > ")
                datasaved['Useless'] = x
            else:
                Option(datasaved['Useless'], ['GET OUT!'])

        if app == 'Settings':
            setting = Option('Settings', ['BuildModule'])
            if setting == 'BuildModule':
                Option("BuildModule: 0.0.2", ['Exit'])
        elif app == 'Terminal':
            os.system('cls')
            inp = input("> ")
            install = re.search(r'\$sudo inst \;(.+)', inp)
            if install:
                appsincloud = ['appstore']
                appinstalling = install.group(1)
                if appinstalling in appsincloud and not appinstalling in apps:
                    for i in range(1, 100):
                        print("Installing...")
                        print('[', '#' * i, '0' * (100 - i), ']')
                        os.system('cls')
                        time.sleep(random.uniform(0.01, 0.1))
                    apps.append(appinstalling)
            else:
                print("Failed to install app: app not found")
                time.sleep(3)

        elif app == 'File Manager':
            filemanage = Option("File Manager", ['Write File', 'Open File','ls'])
            time.sleep(0.4)
            if filemanage == 'Open File':
                input()
                input()
                name = input("Enter file name >")


                if not name == '>':
                    if name.startswith('"') and name.endswith('"'):
                        name = name[1:-1]
                    try:
                        with open(name, 'r') as file:
                            text = file.read()
                            Option(text, ['Exit'])
                    except Exception as e:
                        time.sleep(1)
                        Option(
                            "There was a error that happened when opening the file. so we saved you from getting a console error.",
                            ['Exit'])
                else:
                    Option("...", ['Haha'])
                    Option("Its not funny lil bro", ['and?'])
                    if not Option("Do you want your death?", ['What you gonna do?', 'im sorry..']) == 'im sorry..':
                        print("ALRIGHT FINE.")
                        time.sleep(3)
                        KernelError()
                    else:
                        print("Its not ok.")
                        time.sleep(4)
                        datasaved['Useless'] = 'ITS NOT OK ' * 1000
                        isitok = False

            elif filemanage == 'Write File':
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
                file.write(str(datasaved))
            print("Shutting down")
            print("Goodbye!")
            break

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
            x = Option("Install App:", ['base64 translator'])
            if x == 'base64 translator':
                for i in range(1, 100):
                    print("Installing...")
                    print('[', '#' * i, '0' * (100 - i), ']')
                    os.system('cls')
                    time.sleep(random.uniform(0.01, 0.1))
                    if not x in apps:
                        apps.append(x)
        elif app == 'base64 translator':
            inp = input("> ")
            x = bytes(inp, 'utf-8')
            Option(f"Base64: {str(base64.b64encode(x))}", ['exit'])

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
                Option("YOU CANT GET AWAY. " * 20, ['alright thats it'])
                Option("OHHH MY GOOOOOo- THIS IS IMPOSSIBLE.", ['noob'])
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
    text = text.replace('\n', ' ')  # Remove newlines
    return text


# Start the console OS system
System()