#!/usr/bin/env python3
import os
import sys
try:
    import socket
except:
    sys.exit("Install missing library: pip install sockets")
try:
    import requests
except:
    sys.exit("Install missing library: pip install requests")

if len(sys.argv) !=2:
    print("follow the example: ")
    print("")
    print("%s https://duckduckgo.com"%(sys.argv[0]))
    sys.exit()

try:
    if __name__ == "__main__":
        url = sys.argv[1]
        response = requests.get(url)
        code = response.status_code
        if code in range(100,199):
            print("{} [code {}] information answer".format(url, code))
        elif code in range(200,299):
            print("{} [code {}] success answer".format(url, code))
        elif code in range(300,399):
            print("{} [code {}] redirection".format(url, code))
        elif code in range(400,499):
            print("{} [code {}] client errors".format(url, code))
        elif code in range(500,599):
            print("{} [code {}] server errors".format(url, code))
        else:
            pass
except Exception as error:
    print(error)
    pass
except KeyboardInterrupt:
    sys.exit()

