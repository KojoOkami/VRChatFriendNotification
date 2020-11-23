from vrcpy.errors import IncorrectLoginError
from vrcpy.wss import WSSClient
import atexit
import sys
import time
from playsound import playsound
from datetime import datetime

username, password = '', ''

if len(sys.argv) >= 3:
    username = sys.argv[1]
    password = sys.argv[2]
else:
    print("Not provided with Username and Password in Sys args, please provide User and Pass.")
    username = input("Username: ")
    password = input("Password: ")


# Logs in the user and authorizes the API
# Initialise vrcpy wrapper client and login with username + password
client = WSSClient()
try:
    client.login(username, password)
    print('Login Successful')
except IncorrectLoginError:
    print('Login Failed: Incorrect Username or Password.')
#client.verify2fa("123456")

# Runs when friend goes online
@client.event
def on_friend_online(friend):
    current_time = datetime.now().strftime("[%H:%M:%S] ")
    try:
        playsound('notification.mp3')
    except:
        pass
    print(current_time + "{} is now online.".format(friend.displayName))

# Runs when friend goes offline
@client.event
def on_friend_offline(friend):
    current_time = datetime.now().strftime("[%H:%M:%S] ")
    print(current_time + "{} is now offline.".format(friend.displayName))


# Logs out the user and ceases connection with API
# Runs on program exit
def logout():
    # Close client session, invalidate auth cookie
    client.logout()


# Registers logout() to run on exit
atexit.register(logout)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    client.logout()
