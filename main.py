from vrcpy.wss import WSSClient
import atexit
import sys
import time

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
client.login(username, password)
#client.verify2fa("123456")


# Runs when friend goes online
@client.event
def on_friend_online(friend):
    print("{} is now online.".format(friend.displayName))


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
