#!usr/bin/python3
import   socket

target_ip = '192.168.29.1'
print(f"[*] Commencing Advanced scan on : {target_ip}")
for port in range (1,1025):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target_ip, port))
    if  result == 0:
        try :
            # if the door is open, listen for upto 1024 bytes of the data
            banner = s.recv(1024).decode('utf-8').strip()
            print(f"[+] Port {port} is  OPEN | Service : {banner}")
        except  :
           #if the service didn't send the banner just print it's open
            print(f"[+] Port {port} isOPEN| (no banner recieved)")

