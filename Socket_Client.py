import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#ip = socket.gethostbyname(socket.gethostname())
#print("ur ip is: "+ip)

# replace "xxx.xxx.x.x" with your ip , any port number u choose
client.connect(("xxx.xxx.x.x",5000))
print("--------------------------------")
#while True:
msg = str(input("Please enter the msg u wanna send: ")) 
encode_msg = msg.encode("UTF-8")
client.send(encode_msg)
print("--------------------------------")
raw_data = client.recv(1024)
print("Server is sending this msg {}".format(raw_data.decode("UTF-8")))
client.close()
