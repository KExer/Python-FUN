import requests
import threading
from time import sleep

URL = "http://counter5.01counter.com/private/contadorvisitasgratis.php?c=cc752f03e9eb758405927ce708942ebf"

threads_count = 200
requests_count = 0

def requestPage(URL, threadNumber):
    global requests_count
    while True:
        r = requests.get(URL)
        if r.status_code == 200:
            requests_count += 1
            print(requests_count)

for i in range(threads_count):
    x = threading.Thread(target=requestPage, args=(URL, i,))
    x.start()

print("Threads STARTED")
