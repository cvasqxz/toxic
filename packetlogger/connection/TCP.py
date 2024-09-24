from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue


class Socket:
	def __init__(self, type, address, port):
		self.type = type
		self.queue = Queue()
		self.hostport = (address, port)

		self.conn = None
		self.thread = None
		self.prefix = None
		self.connected = False

	def setup(self):
		if self.type == "server":
			self.prefix = "SEND"
			self.conn = socket(AF_INET, SOCK_STREAM)
			self.conn.connect(self.hostport)
			print("Toxic connected to Habbo server")

		if self.type == "client":
			self.prefix = "RECV"
			s = socket(AF_INET, SOCK_STREAM)
			s.bind(self.hostport)
			s.listen()
			print("Waiting for connection...")
			self.conn, _ = s.accept()
			print("Habbo client connected to Toxic")

		self.connected = True

	def process(self):
		while self.connected:
			packet = self.conn.recv(32768)
			if len(packet) > 0:
				print(f"{self.prefix}:", str(packet)[2:-1])
				self.queue.put(packet)
			else:
				self.stop()

	def start(self):
		self.thread = Thread(target=self.process, args=[])
		self.thread.daemon = True
		self.thread.start()

	def stop(self):
		self.connected = False
		self.conn.close()
		
	def join(self):
		self.thread.join()
		self.stop()
