import socket


HOST = ''
PORT = 9000

sock = socket.socket(
	socket.AF_INET, 
	socket.SOCK_STREAM
	)

sock.bind(HOST, PORT)
sock.listen(1)

connection, address = sock.accept()
print('Connected by ', address)	