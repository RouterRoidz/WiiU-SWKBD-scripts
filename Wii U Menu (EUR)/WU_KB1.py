# -*- coding: cp1252 -*- # Wii U SWKBD Keyboard Hack Template - by RandomUser_101
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.13.156") # Your Wii U's IP address goes here
tcp.pokemem(0x3A8FC3F8, 0xe000e001) # lowercase Starts here - q/w
tcp.pokemem(0x3A8FC3FC, 0xe002e003) # e/r
tcp.pokemem(0x3A8FC400, 0xe004e005) # t/y
tcp.pokemem(0x3A8FC404, 0xe006e007) # u/i
tcp.pokemem(0x3A8FC408, 0xe008e009) # o/p
tcp.pokemem(0x3A8FC40C, 0xe00ae00b) # @/a
tcp.pokemem(0x3A8FC410, 0xe00ce00d) # s/d
tcp.pokemem(0x3A8FC414, 0xe00ee00f) # f/g
tcp.pokemem(0x3A8FC418, 0xe010e011) # h/j
tcp.pokemem(0x3A8FC41C, 0xe012e013) # k/l
tcp.pokemem(0x3A8FC420, 0xe014e015) # '/-
tcp.pokemem(0x3A8FC424, 0xe015e016) # z/x
tcp.pokemem(0x3A8FC428, 0xe017e018) # c/v
tcp.pokemem(0x3A8FC42C, 0xe019e01a) # b/n
tcp.pokemem(0x3A8FC430, 0xe01be01c) # m/,
tcp.pokemem(0x3A8FC434, 0xe01de01e) # ./? - lowercase ends here.
tcp.pokemem(0x3A8FC438, 0xe01fe020) # UPPERCASE starts here - Q/W
tcp.pokemem(0x3A8FC43C, 0xe021e022) # E/R
tcp.pokemem(0x3A8FC440, 0xe023e024) # T/Y
tcp.pokemem(0x3A8FC444, 0xe025e026) # U/I
tcp.pokemem(0x3A8FC448, 0xe027e028) # O/P
tcp.pokemem(0x3A8FC44C, 0xe029e02a) # @/A
tcp.pokemem(0x3A8FC450, 0xe02be02c) # S/D
tcp.pokemem(0x3A8FC454, 0xe02de02e) # F/G
tcp.pokemem(0x3A8FC458, 0xe02fe030) # H/J
tcp.pokemem(0x3A8FC45C, 0xe031e032) # K/L
tcp.pokemem(0x3A8FC460, 0xe033e034) # '/-
tcp.pokemem(0x3A8FC464, 0xe035e036) # Z/X
tcp.pokemem(0x3A8FC468, 0xe037e038) # C/V
tcp.pokemem(0x3A8FC46C, 0xe039e03a) # B/N
tcp.pokemem(0x3A8FC470, 0xe03be03c) # M/,
tcp.pokemem(0x3A8FC474, 0xe03de03e) # ./? - UPPERCASE ends here - Code ends here
tcp.s.close()
print("Hacked Keyboard 1 applied for Wii U Menu!") # Message to print when the code is sent successfully.
