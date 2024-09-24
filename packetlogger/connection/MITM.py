from threading import Thread


class MITM:
	def __init__(self, client, server):
		self.client = client
		self.server = server

		self.thread = None
		self.processing = False

	def process(self):
		while self.processing:
			try:
				while not self.server.queue.empty():
					packet = self.server.queue.get()
					self.client.conn.sendall(packet)

				while not self.client.queue.empty():
					packet = self.client.queue.get()
					self.server.conn.sendall(packet)

			except Exception as e:
				print("MITM process error:", e)
				self.stop()

	def start(self):
		self.thread = Thread(target=self.process, args=[])
		self.thread.daemon = True
		self.processing = True
		self.thread.start()

	def stop(self):
		self.processing = False
		self.client.stop()
		self.server.stop()

	def join(self):
		self.thread.join()
		self.stop()
