import socket
s=socket.socket()
print("Socket is created")
s.bind(('localhost',9999))
s.listen(3)
print("Waiting for the connection")
while True:
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print("Connected with the client",addr,name)
    c.send(bytes('Hi I am server, You are welcome on server','utf-8'))
    c.close()
