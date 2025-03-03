import io
import binascii
import struct


# https://github.com/UnfamiliarLegacy/G-Earth/blob/moon/G-Earth/src/main/java/gearth/protocol/crypto/RC4Base64.java
class RC4Base64:
	BASE64_ENCODING_MAP = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
	BASE64_DECODING_MAP = [
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
		52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1,
		-1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
		15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1,
		-1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
		41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
	]


	def __init__(self, state, q, j):
		if len(state) != 256:
			raise ValueError(f"State must be 256 bytes long, was {len(state)}")
		self.state = bytearray(state)
		self.q = q
		self.j = j

	def cipher(self, data, offset=0, length=None):
		if length is None:
			length = len(data)
		result = io.BytesIO()
		for i in range(0, length, 3):
			first_byte = data[offset + i] ^ self.move_up()
			second_byte = data[offset + i + 1] ^ self.move_up() if length > i + 1 else 0
			result.write(self.BASE64_ENCODING_MAP[(first_byte & 0xFC) >> 2:((first_byte & 0xFC) >> 2)+1])
			result.write(self.BASE64_ENCODING_MAP[(((first_byte & 0x03) << 4) | ((second_byte & 0xF0) >> 4)):(((first_byte & 0x03) << 4) | ((second_byte & 0xF0) >> 4))+1])
			if length > i + 1:
				third_byte = data[offset + i + 2] ^ self.move_up() if length > i + 2 else 0
				result.write(self.BASE64_ENCODING_MAP[(((second_byte & 0x0F) << 2) | ((third_byte & 0xC0) >> 6)):(((second_byte & 0x0F) << 2) | ((third_byte & 0xC0) >> 6))+1])
				if length > i + 2:
					result.write(self.BASE64_ENCODING_MAP[third_byte & 0x3F:(third_byte & 0x3F)+1])
		return result.getvalue()

	def decipher(self, data, offset=0, length=None):
		if length == None:
			length = len(data)

		buffer = memoryview(data)[offset:offset + length]
		result_buffer = io.BytesIO()

		index = 0
		while index < len(buffer):
			first_byte = self.BASE64_DECODING_MAP[buffer[index]]
			index += 1
			second_byte = self.BASE64_DECODING_MAP[buffer[index]]
			index += 1

			byte1a = first_byte << 2
			byte1b = (second_byte & 0x30) >> 4

			result = (byte1a | byte1b) ^ self.move_up()
			result_buffer.write(bytes([result & 0xFF]))  # Apply the mask

			if index < len(buffer):
				third_byte = self.BASE64_DECODING_MAP[buffer[index]]
				index += 1

				byte2a = (second_byte & 0x0F) << 4
				byte2b = (third_byte & 0x3C) >> 2

				result = (byte2a | byte2b) ^ self.move_up()
				result_buffer.write(bytes([result & 0xFF]))  # Apply the mask

				if index < len(buffer):
					fourth_byte = self.BASE64_DECODING_MAP[buffer[index]]
					index += 1

					byte3a = (third_byte & 0x03) << 6
					byte3b = fourth_byte & 0x3F

					result = (byte3a | byte3b) ^ self.move_up()
					result_buffer.write(bytes([result & 0xFF]))  # Apply the mask

		return result_buffer.getvalue()

	def get_state(self):
		return bytes(self.state)

	def get_q(self):
		return self.q

	def get_j(self):
		return self.j

	def deep_copy(self):
		return RC4Base64(self.state[:], self.q, self.j)

	def move_up(self):
		self.q = (self.q + 1) & 0xff
		self.j = (self.state[self.q] + self.j) & 0xff
		tmp = self.state[self.q]
		self.state[self.q] = self.state[self.j]
		self.state[self.j] = tmp
		if (self.q & 0x3F) == 0x3F:
			x2 = (297 * (self.q + 67)) & 0xff
			y2 = (self.j + self.state[x2]) & 0xff
			tmp = self.state[x2]
			self.state[x2] = self.state[y2]
			self.state[y2] = tmp
		xor_index = (self.state[self.q] + self.state[self.j]) & 0xff
		return self.state[xor_index]

	def move_down(self):
		if (self.q & 0x3F) == 0x3F:
			return False  # Unsupported
		tmp = self.state[self.q]
		self.state[self.q] = self.state[self.j]
		self.state[self.j] = tmp
		self.j = (self.j - self.state[self.q]) & 0xff
		self.q = (self.q - 1) & 0xff
		return True

	def undo_rc4(self, length):
		for _i in range(length):
			if not self.move_down():
				return False
		return True


# https://github.com/UnfamiliarLegacy/G-Earth/blob/moon/G-Earth/src/test/java/TestRc4Shockwave.java
def testRc4Base64():
	c = RC4Base64(
		binascii.unhexlify("D6EAA2D902B1797E759D5F8C26175B93BEC1235764E6F26972A6D85343B259CA715CB9418A19CC984EDB617F3E9E0947EB5A7D46ECAEC26E1C5D62E33D226D39337B0BD4783F49AC6A1FB8AB0A14CD7CC6F3D701895EE4E8D3F9FF8BF628E70058A183BD1B32813B31060F1DDC9B35E58D7740A320EE731584D5B30536A01116DF4854FA37742E2C50B6AF4B9A4D0D4F6BBF9CC3666CCE45D2A525FB4A8E182F3C2776A7F499C438210EA87AB5043463136512958F4CFC68C9B7C7C042BA109786A43A08DA2B1E55B4D0DDE9871A6FCF30F0E185FE5192800CDE29BCADEF2D03C5CBE2E0A9EDD12A5652FDF896F1F79491F5679F24600790BBC84482B070AA88"),
		152,
		211)

	print(binascii.hexlify(c.get_state()))

	out = c.decipher(binascii.unhexlify("3270635A4F67"))
	assert(binascii.hexlify(out) == b"01020304")

	c2 = RC4Base64(
		binascii.unhexlify("D6EAA2D902B1797E759D5F8C26175B93BEC1235764E6F26972A6D85343B259CA715CB9418A19CC984EDB617F3E9E0947EB5A7D46ECAEC26E1C5D62E33D226D39337B0BD4783F49AC6A1FB8AB0A14CD7CC6F3D701895EE4E8D3F9FF8BF628E70058A183BD1B32813B31060F1DDC9B35E58D7740A320EE731584D5B30536A01116DF4854FA37742E2C50B6AF4B9A4D0D4F6BBF9CC3666CCE45D2A525FB4A8E182F3C2776A7F499C438210EA87AB5043463136512958F4CFC68C9B7C7C042BA109786A43A08DA2B1E55B4D0DDE9871A6FCF30F0E185FE5192800CDE29BCADEF2D03C5CBE2E0A9EDD12A5652FDF896F1F79491F5679F24600790BBC84482B070AA88"),
		152,
		211)

	out2 = c2.decipher(binascii.unhexlify("3270635A4F714A4D742F43545551"))
	assert(binascii.hexlify(out2) == b"0102030405060708090a")

	c3 = RC4Base64(
		binascii.unhexlify("F2FD7883352075B654143213705596EBE2D166331F49A8A9B750D7DDE580F77BFC3982AA7D28F5E92E1785005947194136275BE0254F91F8606EC09A05FA5161C87FFF5286CD9BFBC4A15DB06C694EEEB388E399AE72F01C5608ADA44C93373F9D6D34121558BA84C60D7E897A8DF4D8D96A3A8C31A6EA90CF7C4A57B8D6ED792AAF7607DC03733C5F6230CEDF6511F9F11B2C106394FEB2BCDB640CCB2DCADE9E2FCCDA040AE1C240BD2B6838290EE7B1AC81928A2224425CC1B5A3EF71B477AB9F1E9723A0F6443B3D5A4B95C3438F450BD3A57467D2069821BF09C5161AE8F36B9C8BD5A2A701876F5EC7BBE68E48B93E0FE4D4ECC9465302D01D264D18BE"),
		156,
		238)

	c3.undo_rc4(4)
	out3 = c3.decipher(binascii.unhexlify("4A422B2B4441"))
	assert(binascii.hexlify(out3) == b"01020304")


def testMoveUpDown():
	rc = RC4Base64(
		binascii.unhexlify("cfa4debb4f28d4279d0f668aabba13810b8f7f4c7917eb1618296937c852d05a5d5f41ffc65c4d63bdacf22ebea27e913f56016fd6dae11ab749e068d59a99656ca8c91bf5779b4b03eda560fdc2742a2421517afa6242470e87f8c45edfbc59e650826e4a4810b9ca7df31e1db16175723354c564a67820e3b4dd5b3dd7b39f73a30d96053c71c795ae5707b611a04ead268eb5220cf9e7b2ee23f6bf9e76a7e5a1e9587c408583af3a8b7be8d13000fc86452f929738350206b0c398fb8dfe09f7c1e41ff18470d86d672d1c8ccc806bd332f025ef90a9ea08d26a89dbb8cbec4615f4e29c5544aa53c0d9883b433493ce0adc12cd2c1914942b36043e3139"),
		0,
		0)

	table_a = rc.get_state()
	table_a_X = rc.get_q()
	table_a_Y = rc.get_j()

	rc.move_up()
	rc.move_down()

	table_b = rc.get_state()
	table_b_X = rc.get_q()
	table_b_Y = rc.get_j()

	assert(table_a == table_b)
	assert(table_a_X == table_b_X)
	assert(table_a_Y == table_b_Y)


if __name__ == '__main__':
	testRc4Base64()
	testMoveUpDown()