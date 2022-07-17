import random
import requests
import sys

print("-" * 50)
print("Sonic's Zombsroyale UserKeyGen v.1.0")
print("Press Enter to start")
print("-" * 50)
input("")

def gen():
    try:
        while True:
            hash = random.getrandbits(192)
            userKey = "%032x" % hash
            response = requests.head('https://zombsroyale.io/user/{userKey}')
            print(userKey)

            if response.status_code == 200:
                print('Success!')
                with open("foundUserkeys.txt", "a") as o:
                    o.write(userKey)

            elif response.status_code == 401:
                    print('Not Found')
            else:
                print("Connection timed out! (Probably blocked)")
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()


gen()