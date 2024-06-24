from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from socket import socket, AF_INET, SOCK_STREAM
from json import loads, dumps, JSONDecodeError
from threading import Thread
from queue import Queue
from RC4 import RC4


class webserver(BaseHTTPRequestHandler):
	def log_message(self, format, *args):
		pass

	def do_POST(self):
		length = self.headers.get('content-length')
		request_data = self.rfile.read(int(length))

		try:
			json_request = loads(request_data)
			print("webserver request: ", json_request)
			self.send_response(200)

		except JSONDecodeError as e:
			print("webserver error:", e)
			self.send_response(500)


def server_process(server_socket, server_queue, cypher):
	decrypt = False

	while True:
		server_data = server_socket.recv(1024)
		if len(server_data) == 0:
			exit()

		if decrypt:
			decrypted_packet = cypher.crypt(server_data)
			print("SEND:", str(decrypted_packet)[2:-1])
		else:
			print("SEND:", str(server_data)[2:-1])

		if server_data == b'@@BCJ':
			decrypt = True

		server_queue.put(server_data)


def client_process(client_socket, client_queue):
	while True:
		client_data = client_socket.recv(1024)
		if len(client_data) == 0:
			exit()

		print("RECV:", str(client_data)[2:-1])
		client_queue.put(client_data)


def main_process(server_socket, client_socket, server_queue, client_queue):
	while True:
		while not server_queue.empty():
			server_packet = server_queue.get()
			client_socket.sendall(server_packet)

		while not client_queue.empty():
			client_packet = client_queue.get()
			server_socket.sendall(client_packet)


def main(address, port):
	server_queue = Queue()
	client_queue = Queue()

	decryptoor = RC4(0, "776169776f72696e616f776169776f72696e616f")

	s = socket(AF_INET, SOCK_STREAM)
	s.bind(('localhost', port))
	s.listen()

	print("Waiting for connection...")
	server_socket, _ = s.accept()

	print("Habbo Client connected to packetlogger")

	client_socket = socket(AF_INET, SOCK_STREAM)
	client_socket.connect((address, port))
	print("Packetlogger connected to Habbo server")

	client_thrad = Thread(
		target=client_process,
		args=[client_socket, client_queue]
		)

	server_thread = Thread(
		target=server_process, 
		args=[server_socket, server_queue, decryptoor]
		)

	main_thread = Thread(
		target=main_process,
		args=[server_socket, client_socket, server_queue, client_queue]
		)

	server_thread.start()
	client_thrad.start()
	main_thread.start()

	print("MITM attack successful")

	webserver_thread = ThreadingHTTPServer(("localhost", 8080), webserver)
	webserver_thread.serve_forever()

	server_thread.join()
	client_thrad.join()
	main_thread.join()


if __name__ == '__main__':
	ADDRESS = '18.199.57.67'
	PORT = 40001

	try:
		main(ADDRESS, PORT)
	except KeyboardInterrupt:
		print("\nbye")
