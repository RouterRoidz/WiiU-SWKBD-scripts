# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x15A650F8, 0x30423044)
tcp.pokemem(0x15A650FC, 0x30463048)
tcp.pokemem(0x15A65100, 0x304A304B)
tcp.pokemem(0x15A65104, 0x304C304D)
tcp.pokemem(0x15A65108, 0x304e304f)
tcp.pokemem(0x15A6510C, 0x30513053)
tcp.pokemem(0x15A65110, 0x30553057)
tcp.pokemem(0x15A65114, 0x3059305B)
tcp.pokemem(0x15A65118, 0x305D305F)
tcp.pokemem(0x15A6511C, 0x30613063)
tcp.pokemem(0x15A65120, 0x30663068)
tcp.pokemem(0x15A65124, 0x306a306b)
tcp.pokemem(0x15A65128, 0x306c306d)
tcp.pokemem(0x15A6512C, 0x306e306f)
tcp.pokemem(0x15A65130, 0x30723075)
tcp.pokemem(0x15A65134, 0x3078307B)
tcp.pokemem(0x15A65138, 0x307F3080)
tcp.pokemem(0x15A6513C, 0x30813082)
tcp.pokemem(0x15A65140, 0x30833085)
tcp.pokemem(0x15A65144, 0x30873089)
tcp.pokemem(0x15A65148, 0x308a308b)
tcp.pokemem(0x15A6514C, 0x308c308e)
tcp.pokemem(0x15A65150, 0x30903091)
tcp.pokemem(0x15A65154, 0x30923093)
tcp.pokemem(0x15A65158, 0x30943099)
tcp.pokemem(0x15A6515C, 0x309a309b)
tcp.pokemem(0x15A65160, 0x309c309d)
tcp.pokemem(0x15A65164, 0x309e0000)
tcp.pokemem(0x15A65168, 0x00000000)
tcp.pokemem(0x15A6516C, 0x00000000)
tcp.pokemem(0x15A65170, 0x00000000)
tcp.pokemem(0x15A65174, 0x00000000)
tcp.s.close()
print("Hacked Keyboard 5 applied for Minecraft!")
