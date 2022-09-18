import socket
import datetime as dt
import sys

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
sock.settimeout(30)

logs = open('logs.txt', 'a')
print('Waiting for connection. 30 sec to join...')
logs.write(f'{dt.datetime.now()} - Waiting for connection...' + '\n')
try:
	conn, addr = sock.accept()
except TimeoutError:
	logs.write(f'{dt.datetime.now()} - Сonnection timeout expired.' + '\n')
	logs.close()
	print(f'Сonnection timeout expired.')
	sys.exit()
print(f'Connection is set. Addres is {addr}')
logs.write(f'{dt.datetime.now()} - Connecton is set. Addres is: {addr}' + '\n')
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
		sock.settimeout(30)
		logs.write(f'{dt.datetime.now()} - Connection lost. Waiting for connection...' + '\n')
		try:
			conn, addr = sock.accept()
		except TimeoutError:
			logs.write(f'{dt.datetime.now()} - Сonnection timeout expired.' + '\n')
			logs.close()
			print(f'Сonnection timeout expired.')
			sys.exit()
		print(f'Connecton is set. Addres is: {addr}')
		logs.write(f'{dt.datetime.now()} - Connection is set. Addres is: {addr}' + '\n')

conn.close()
logs.close()
