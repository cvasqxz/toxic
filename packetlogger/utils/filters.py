import string, re


PRINTABLE = string.ascii_letters + \
			string.punctuation + \
			string.digits + \
			'áéíóúñÁÉÍÓÚÑ' + chr(32)


def bin2str(binary_packet):
	string_packet = binary_packet
	non_ascii = [c for c in binary_packet if chr(c) not in PRINTABLE]

	for non_ascii_char in set(non_ascii):
		bin_char = non_ascii_char.to_bytes(1, byteorder="big")
		str_char = f"[{non_ascii_char}]".encode()
		string_packet = string_packet.replace(bin_char, str_char) 

	return string_packet.decode("latin-1")


def str2bin(string_packet):
	binary_packet = string_packet.encode("latin-1")
	regex_find = re.findall(r"\[(\d+)\]", string_packet)
	
	for replaced_char in set(regex_find):
		bin_char = int(replaced_char).to_bytes(1, byteorder="big")
		str_char = f"[{replaced_char}]".encode()
		binary_packet = binary_packet.replace(str_char, bin_char)

	return binary_packet

