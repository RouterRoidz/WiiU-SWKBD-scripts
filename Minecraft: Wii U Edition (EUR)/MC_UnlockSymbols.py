# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x30000000, 0x109CCAC4)
tcp.pokemem(0x10000000, 0x50000000)
tcp.pokemem(0x31000000, 0x00003BB4)
tcp.pokemem(0x30100000, 0x00000000)
tcp.pokemem(0x10000000, 0x50000000)
tcp.pokemem(0x00123D48, 0x00000000)
tcp.pokemem(0x00123D5C, 0x00000100)
tcp.pokemem(0x00123E88, 0x00000000)
tcp.pokemem(0x00123E9C, 0x00000100)
tcp.pokemem(0xD0000000, 0xDEADCAFE)
tcp.s.close()
print("Minecraft symbols unlocked!")
