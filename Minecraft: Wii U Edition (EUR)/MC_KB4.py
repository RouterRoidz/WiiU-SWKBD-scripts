# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x15A650F8, 0xff51ff57)
tcp.pokemem(0x15A650FC, 0xff45ff52)
tcp.pokemem(0x15A65100, 0xff54ff59)
tcp.pokemem(0x15A65104, 0xff55ff49)
tcp.pokemem(0x15A65108, 0xff4fff50)
tcp.pokemem(0x15A6510C, 0x0000ff41)
tcp.pokemem(0x15A65110, 0xff53ff44)
tcp.pokemem(0x15A65114, 0xff46ff47)
tcp.pokemem(0x15A65118, 0xff48ff4a)
tcp.pokemem(0x15A6511C, 0xff4bff4c)
tcp.pokemem(0x15A65120, 0x00000000)
tcp.pokemem(0x15A65124, 0xff5aff58)
tcp.pokemem(0x15A65128, 0xff43ff56)
tcp.pokemem(0x15A6512C, 0xff42ff4e)
tcp.pokemem(0x15A65130, 0xff4d0000)
tcp.pokemem(0x15A65134, 0xff01ff1f)
tcp.pokemem(0x15A65138, 0x27762777)
tcp.pokemem(0x15A6513C, 0x27782779)
tcp.pokemem(0x15A65140, 0x277a277b)
tcp.pokemem(0x15A65144, 0x277c277d)
tcp.pokemem(0x15A65148, 0x277e277f)
tcp.pokemem(0x15A6514C, 0xffe520af)
tcp.pokemem(0x15A65150, 0x210a25a1)
tcp.pokemem(0x15A65154, 0x25a225b2)
tcp.pokemem(0x15A65158, 0x25b325b7)
tcp.pokemem(0x15A6515C, 0x25bc25bd)
tcp.pokemem(0x15A65160, 0x25c125c6)
tcp.pokemem(0x15A65164, 0x25c725c9)
tcp.pokemem(0x15A65168, 0x25cb25ce)
tcp.pokemem(0x15A6516C, 0x26012600)
tcp.pokemem(0x15A65170, 0x26022603)
tcp.pokemem(0x15A65174, 0x260e261c)
tcp.s.close()
print("Hacked Keyboard 4 applied for Minecraft!")
