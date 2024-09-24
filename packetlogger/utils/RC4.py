from binascii import unhexlify

# https://github.com/UnfamiliarLegacy/G-Earth/
# ShockwavePacketHandler.java

class RC4:
	def __init__(self, key, artificial_key):
		self.TABLE_SIZE = 256
		self.table = [0]*self.TABLE_SIZE
		self.x = 0
		self.y = 0

		artificial_key = unhexlify(artificial_key)
		self.build_table(key, artificial_key)


	def crypt(self, data):
		data = unhexlify(data)
		result = b''

		for i in range(len(data)):
			self.x = (self.x + 1) % self.TABLE_SIZE
			self.y = (self.y + self.table[self.x] & 0xff) % self.TABLE_SIZE
			self.swap(self.table, self.x, self.y)

			xorIndex =  self.table[self.x] & 0xff
			xorIndex += self.table[self.y] & 0xff
			xorIndex %= self.TABLE_SIZE

			newByte = (0x7f & (data[i] ^ self.table[xorIndex & 0xff]))
			result += newByte.to_bytes(1, 'big')

		return result


	def build_table(self, key, artificial_key):
		modKey = [0]*20

		j = 0
		for i in range(20):
			if j >= len(artificial_key):
				j = 0
			modKey[i] = key & modKey[j]
			j += 1

		for i in range(self.TABLE_SIZE):
			if i < 128:
				self.table[i] = i
			else:
				self.table[i] = i - self.TABLE_SIZE
		
		j = 0
		for q in range(self.TABLE_SIZE):
			j += self.table[q] & 0xff
			j += modKey[q % len(modKey)]
			j %= self.TABLE_SIZE
			self.swap(self.table, q, j)


	def swap(self, table, i, j):
		temp = self.table[i]
		self.table[i] = self.table[j]
		self.table[j] = temp

