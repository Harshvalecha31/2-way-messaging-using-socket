import socket
hostname = socket.getservername()
ipaddr = socket.gethostbyname()
port = 12345
# create a socket 
s = socket.socket()
s.bind((ipaddr,port))
# for keep on listening
s.listen()
# when thecliet connects
conn,clientaddr = s.accept()
print('We got it connected!!')
print('This is the connection Object:',conn,'This is the address:',clientaddr)
# keep on running the server and it automatically breaks when the client connection is broken
while True:
    # first recieving the content from the client
    clientmsg = conn.recv(1024)
    if not clientmsg:
        break
    print('Client Message:',clientmsg.decode())
    servermsg = input('Enter the message for server:')
    conn.send(servermsg.encode())

# atlast when the loop breaks connection is closed
conn.close


