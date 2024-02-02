import requests
import random
import string
import time
from termcolor import colored

banner = '''
.__                __                                      
|__| ____   ______/  |______    ________________    _____  
|  |/    \ /  ___|   __\__  \  / ___\_  __ \__  \  /     \ 
|  |   |  \\___ \ |  |  / __ \/ /_/  >  | \// __ \|  Y Y  \
|__|___|  /____  >|__| (____  |___  /|__|  (____  /__|_|  /
        \/     \/           \/_____/   _____    \/      \/ 
 __ __  ______ ___________            /  |  |              
|  |  \/  ___// __ \_  __ \  ______  /   |  |_             
|  |  /\___ \\  ___/|  | \/ /_____/ /    ^   /             
|____//____  >\___  >__|            \____   |              
           \/     \/                     |__|                            
'''

print(colored(banner, 'red'))

def generate_random_username():
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(3))
    username += str(random.randint(0, 9)) 
    return username

def check_instagram_username(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Username '{username}' is already taken.")
    elif response.status_code == 404:
        print(colored(f"Username '{username}' GET [+]", 'green'))
    else:
        print(f"Failed to check username '{username}'. Status code: {response.status_code}")

while True:
    username = generate_random_username()
    check_instagram_username(username)
    time.sleep(0.1)  
