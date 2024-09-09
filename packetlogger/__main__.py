from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue


G = 23786635532332886537261431906453031264918297
P = 632158881801130885249042417232212770524741295422564233061391190031954228421232913648184592218883487397503624904102572293826728806813079


def server_process(server_socket, server_queue):
	while True:
		server_data = server_socket.recv(1024)
		if len(server_data) == 0:
			exit()

		print("SEND:", str(server_data)[2:-1])
		server_queue.put(server_data)


def client_process(client_socket, client_queue):
	while True:
		client_data = client_socket.recv(1024)
		if len(client_data) == 0:
			exit()

		print("RECV:", str(client_data)[2:-1])
		client_queue.put(client_data)


def main_process(server_socket, client_socket, server_queue, client_queue):
	try:
		while True:
			while not server_queue.empty():
				server_packet = server_queue.get()
				client_socket.sendall(server_packet)

			while not client_queue.empty():
				client_packet = client_queue.get()
				server_socket.sendall(client_packet)

	except:
		print("Socket error, quitting...")
		exit()


def main(address, port):
	server_queue = Queue()
	client_queue = Queue()

	s = socket(AF_INET, SOCK_STREAM)
	s.bind(('localhost', port))
	s.listen()

	print("Waiting for connection...")
	server_socket, _ = s.accept()

	print("Habbo Client connected to packetlogger")

	client_socket = socket(AF_INET, SOCK_STREAM)
	client_socket.connect((address, port))
	print("Packetlogger connected to Habbo Server")

	client_thrad = Thread(
		target=client_process,
		args=[client_socket, client_queue]
		)

	server_thread = Thread(
		target=server_process, 
		args=[server_socket, server_queue]
		)

	main_thread = Thread(
		target=main_process,
		args=[server_socket, client_socket, server_queue, client_queue]
		)

	server_thread.start()
	client_thrad.start()
	main_thread.start()

	print("MITM attack successful")

	server_thread.join()
	client_thrad.join()
	main_thread.join()


if __name__ == '__main__':
	ADDRESS = '18.199.57.67'
	PORT = 40_001

	try:
		main(ADDRESS, PORT)

	except KeyboardInterrupt:
		print("\nbye")
		exit()
