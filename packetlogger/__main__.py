from connection.TCP import Socket
from connection.MITM import MITM

def main():
	client = Socket("client", "localhost", 40_001)
	client.setup()
	client.start()
	
	server = Socket("server", "18.199.57.67", 40_001)
	server.setup()
	server.start()
	
	mitm = MITM(client, server)
	mitm.start()

	try:
		mitm.join()
		server.join()
		client.join()

	except KeyboardInterrupt:
		print("\nBYE")


if __name__ == "__main__":
	main()