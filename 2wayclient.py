import socket
# getting the clients details
hostname = socket.gethostname()
ipaddr = socket.gethostbyname()
port = 12345
# Here the client connection is made using connect
#create the socket object
s = socket.socket()
s.connect((ipaddr,port))
print('Client connected to the socket!!')
# input the message
clientmsg = input('Enter the message:')
while clientmsg!='exit':
    #for sending the client message
    s.send(clientmsg.encode())
    # for recieving the server message
    servermessage = s.recv(1024)
    print('Server Message:',servermessage.decode())
    # Now Again fetching client message
    clientmsg = input('Enter the message:')
# for closing the connection!!
s.close()

