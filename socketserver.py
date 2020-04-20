import socket
def bind():
	server_socket=socket.socket()
	server_socket.bind((socket.gethostname(),1234))
	print('listening ...')
	server_socket.listen(1)
	c,addr = server_socket.accept()
	return c

def server_messages(c):
	while True:
		data=str(c.recv(1024).decode())
		data=data.lower()
		if data == "bye from client-harini":
			print(data)
			c.send(str.encode("Bye from Server"))
			break
		elif data == "hello from client-harini":
			print(data)
			c.send(str.encode("Hello from Server"))
		else:
			print(data)
			c.send(str.encode(data))
def main():
	c=bind()
	server_messages(c)
	c.close()

if __name__== "__main__":
	main()