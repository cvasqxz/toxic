import subprocess
import struct
import re
import os

RC4_TABLE_SIZE = 256
RC4_INVALID_VALUE = 65535  # Representación de u16 máximo
hotelSettings = type("hotelSettings", (object,), {"tableAlignment": 8, "invalidMask": 0xFFFFFFFB_FFFFFF00})() # Se asume estos valores.


from subprocess import check_output
def get_pid(name):
	try:
		pid = subprocess.check_output(["pidof", name])
		return int(pid)
	except subprocess.CalledProcessError:
		return None


def checkMapOffset(startingIndex, buffer, bufferAddr, bufferLen):
	tableAlignment = 8
	validEntries = 0
	valueToIndex = [RC4_INVALID_VALUE] * RC4_TABLE_SIZE
	indexToValue = [RC4_INVALID_VALUE] * RC4_TABLE_SIZE
	i = startingIndex
	while i < bufferLen:
		value = buffer[i]
		tableIndex = (i // tableAlignment) % RC4_TABLE_SIZE
		oldValue = indexToValue[tableIndex]
		if oldValue != RC4_INVALID_VALUE:
			valueToIndex[oldValue] = RC4_INVALID_VALUE
			indexToValue[tableIndex] = RC4_INVALID_VALUE
			validEntries -= 1
		isValueUnique = valueToIndex[value] == RC4_INVALID_VALUE
		if isValueUnique:
			validEntries += 1
		else:
			indexToValue[valueToIndex[value]] = RC4_INVALID_VALUE
		valueToIndex[value] = tableIndex
		indexToValue[tableIndex] = value
		if validEntries == RC4_TABLE_SIZE:
			tablePos = i - ((RC4_TABLE_SIZE - 1) * tableAlignment)
			tableAddr = bufferAddr + tablePos
			tableSize = RC4_TABLE_SIZE * tableAlignment
			check_valid(tableAddr, buffer[tablePos : tablePos + tableSize])
		i += tableAlignment

def check_valid(address, buffer):
    table_alignment = 8
    invalid_mask = 0xFFFFFFFB_FFFFFF00
    table = [0] * 256
    i = 0
    while i < len(buffer):
        value = struct.unpack("<Q", buffer[i:i + table_alignment].ljust(8, b'\x00'))[0]
        is_valid = (value & invalid_mask) == 0
        if not is_valid:
            return
        table[i // table_alignment] = value & 0xFF
        i += table_alignment
    print(f"Found potential RC4 table at: 0x{address:08x}")
    hex_string = "".join(f"{value:02x}" for value in table)
    print(hex_string)

pid = get_pid("Habbo.exe")

if pid != None:
	maps_file = open(f"/proc/{pid}/maps", 'r')
	mem_file = open(f"/proc/{pid}/mem", 'rb', 0)

	for line in maps_file.readlines():  # for each mapped region
		m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
		if m.group(3) == 'r':  # if this is a readable region
			start = int(m.group(1), 16)
			end = int(m.group(2), 16)
			mem_file.seek(start)  # seek to region start
			chunk = mem_file.read(end - start)  # read region contents
			checkMapOffset(8, chunk, start, end-start)
	maps_file.close()
	mem_file.close()

