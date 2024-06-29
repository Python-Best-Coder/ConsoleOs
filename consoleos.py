import os
import keyboard
import time
import requests
import shutil
import getpass
import os
import ast

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
print(os.getcwd())  # prints the current working directory
# adjust the path as needed

# Directory for data storage
data = r'C:/Users/' + getpass.getuser() + r'/ConsoleOsData'
datafound = False
datasaved = {'Useless':'','History':[]}
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

time.sleep(3)

# Function to handle system operations
def System():
    while True:
        app = Option('Choose an app:', ['testingapp','File Manager', 'Settings', 'Shutdown', 'the virus', 'ConsoleBrowse'])
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
                
        elif app == 'File Manager':
            filemanage = Option("File Manager", ['Write File','Open File'])
            time.sleep(0.4)
            if filemanage == 'Open File':
                name = input('Filepath > ')
                if name.startswith('"') and name.endswith('"'):
                    name = name[1:-1]
                try:
                    with open(name, 'r') as file:
                        text = file.read()
                        Option(text,['Exit'])
                except Exception as e:
                    print("There was a error that happened when opening the file. so we saved you from getting a console error.")

               
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
        
        elif app == 'ConsoleBrowse':
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
