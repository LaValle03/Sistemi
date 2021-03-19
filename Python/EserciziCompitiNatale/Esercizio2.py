import random
import string

def genera_mac():
    mac = ""
    for k in range (6):
        mac = mac + ''.join(random.choice(string.hexdigits) for i in range(2)) + ":"
    mac = mac[:-1]
    print(mac.upper())


genera_mac()
