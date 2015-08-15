import struct

def pack(fmt, *args):
	return struct.pack('<' + fmt, *args)

def unpack(fmt, *args):
	return struct.unpack('<' + fmt, *args)

def multichr(values):
	return ''.join(map(chr, values))

def multiord(values):
	return map(ord, values)
