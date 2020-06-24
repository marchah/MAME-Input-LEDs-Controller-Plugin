import sys
import json
import requests
from constants import SERVER_IP, DEBUG

if (len(sys.argv) < 3):
    print("Error startQuery: missing arguments")
else:
    try:
        f = open("./" + sys.argv[2], "r", encoding="utf-8-sig")
        config = json.load(f)
        f.close()

        inputs = []
        for key in config["inputs"]:
            inputs.append(key)

        nbPlayers = int(config["inputs"][0])

        r = requests.post("http://" + SERVER_IP + '/game/' +
                          sys.argv[1], json={"inputs": inputs, "nbPlayers": nbPlayers})
        if (DEBUG):
            print(r.text)
    except Exception as e:
        print("An error occcured: " + str(e))
