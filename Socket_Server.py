import socket
        #internet protocol: IPv4, type : TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         

#ip = socket.gethostbyname(socket.gethostname())
#print("ur ip is: "+ip)

# replace "xxx.xxx.x.x" with your ip , any port number u choose
s.bind(("xxx.xxx.x.x",5000))  
s.listen(1)          #listen for number of clients

while True:
    #accept() returns -> client instance , address
    client, address = s.accept()   # wait till client connect
    print("Client address is: {}".format(address))
    rawdata = client.recv(1024)    # wait till client sends
    print("{} is sending to you this message {} ".format(address,rawdata.decode("UTF-8")))
    print("--------------------------------------------")
    msg = str(input("Please enter the msg u wanna send: ")) 
    encoded_msg = msg.encode("UTF-8")
    client.send(encoded_msg)
    client.close()