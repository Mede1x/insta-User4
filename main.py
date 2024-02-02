import requests
import random
import string
import time
from termcolor import colored

banner = '''
 ____  ____   _____ ______   ____   ____  ____    ____  ___ ___ 
|    ||    \ / ___/|      | /    | /    ||    \  /    ||   |   |
 |  | |  _  (   \_ |      ||  o  ||   __||  D  )|  o  || _   _ |
 |  | |  |  |\__  ||_|  |_||     ||  |  ||    / |     ||  \_/  |
 |  | |  |  |/  \ |  |  |  |  _  ||  |_ ||    \ |  _  ||   |   |
 |  | |  |  |\    |  |  |  |  |  ||     ||  .  \|  |  ||   |   |
|____||__|__| \___|  |__|  |__|__||___,_||__|\_||__|__||___|___|
                                                                
 __ __  _____   ___  ____                  _____                
|  |  |/ ___/  /  _]|    \                |     |               CODED BY MEED
|  |  (   \_  /  [_ |  D  )     _____     |__/  |                  ENJOY ;)
|  |  |\__  ||    _]|    /     |     |    |   __|               
|  :  |/  \ ||   [_ |    \     |_____|    |  /  |               
|     |\    ||     ||  .  \               |     |        TELEGRAM : Meed_Man       
 \__,_| \___||_____||__|\_|               |_____|               
                                                                                          
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
