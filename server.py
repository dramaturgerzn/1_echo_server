import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
print(f'Connecton is set. Addres is: {addr}')

while True:
	data = conn.recv(1024)
		#if not data:
		#break
	if data:
		msg = data.decode()
		#conn.send(data)
		print(msg)
	else:
		print('Connection lost. Waiting for connection...')
		sock.listen(1)
		conn, addr = sock.accept()
		print(f'Connecton is set. Addres is: {addr}')

conn.close()

