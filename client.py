import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
host = 'localhost'
port = 9090
sock.connect((host, port))

print(f'Successful connection. Host: {host}, port: {port}')
while True:
	msg = input()
	if msg == 'exit':
		break
	sock.send(msg.encode())
	#data = sock.recv(1024)

sock.close()
print('Connection lost.')
#print(data.decode())
