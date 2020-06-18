import sys
import json
import requests
from constants import SERVER_IP, DEBUG

if (len(sys.argv) < 2):
    print("Error endQuery: missing arguments")
else:
    try:
        r = requests.delete("http://" + SERVER_IP + '/game/' + sys.argv[1])
        if (DEBUG):
            print(r.text)
    except Exception as e:
        print("An error occcured: " + str(e))
