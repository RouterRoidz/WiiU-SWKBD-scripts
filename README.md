# WiiU-SWKBD-scripts
This method is considered obsolete in favor of Ro's Wii U custom keybord which works everywhere and is permanent. Updated Video link is [here](https://www.youtube.com/watch?v=DtZPjN-st8o), however it imposes a brick risk if installed the wrong way.
Scripts will continue to be created here for those who prefer this method, which is safer for the non tech-savvy.
===========================
# Description
My pyGecko scripts made for interfacing with the Wii U's Software Keyboard (SWKBD).

These scripts are made for editing keys on the Wii U software keyboard, otherwise known as SWKBD.
If you want to use some of these files (the ones made for the Applets and the Mii Maker), you'll need to use the older version of TCPGecko (the one on Loadiine.ovh) which involves downgrading browser files to run 5.5.1 exploits.

Don't expect a ton of things here. I'll make them when I want to make them.

You will need Python 2 or higher to use these scripts, however Python 3 or above is recommended. A copy of pyGecko is included in each folder. 

Run with `python (script).py` (or just double click the script if you're on Windows). 

Make sure to change the IP address at the top of the script to that of your console's IP address.

Using the latest version of TCPGecko will NOT work for system appliets (Friends List, Miiverse, etc...)

Mii Maker also will not work with the latest TCPGecko due to the nature of homebrew on Wii U.



Keep in mind most of these scripts will be intented for EUR/PAL versions of games/applets. I don't have access to a USA/NTSC-U or JPN/NTSC-J console. However, if you somehow port these scripts to different regions, and you would like them uploaded, hit me up (Randm#5310 on Discord or create an Issue here) and I'll add them here!





# FAQ:

Q: When I run the script, it doesn't connect to my console, and the script closes!

A: Make sure the IP address at the top of the script is set to that of your console's IP. You can get your IP address through programs like FTPiiU. Also make sure you have the `common.py`, `common.pyc`, `tcpgecko.py` and `tcpgecko.pyc` files in the same folder as the script(s).

=

Q: A folder named `__pycache__` was created! Should I be worried?

A: No, that's a folder Python creates. Don't worry about it.

=

Q: I get an error that says `No module named 'tcpgecko'`!

A: Make sure the `common.py`, `common.pyc`, `tcpgecko.py` and `tcpgecko.pyc` files are in the same folder as the script(s).

=

Q: The script connects and sends, but the keyboard doesn't change!

A: If you sent the script when the keyboard was open, press the Caps Lock key on the keyboard (the a↷A key) or re-open the keyboard. If it still doesn't change, there is a bug with the script. 

Please contact me on Discord `Randm#5310` or create an Issue here if that's the case.

=

Q: I've edited the script to have different keys, and the console now freezes when I send it!

A: Revert the changes you made. If this happens with unmodified scripts, contact me ASAP.

=

=

# What keys do what

KB1 thru KB3 = Hacked symbols and special unicode characters. 0009 is included in KB3 here (the key with the red rectangle on it) ![0009](https://user-images.githubusercontent.com/54253840/152971588-25d92cfc-56fe-4942-98c2-2c874b365f1c.png)

KB4 = Wide QWERTY keyboard and special unicode characters

KB5 and KB6 = Japanese Hiragana and Katakana.

Have fun! Feel free to suggest what characters should be added!

# DISCLAIMER
Even though these are considered safe, I am NOT responsible if you mess up your console using these scripts. These scripts are tested before they get uploaded here.
If you mess up your console or data using these scripts, that's your fault, not mine.

# CREDITS
- **NWPlayer123** for making the pyGecko library
- **Chadderz and Marionumber1** for making the TCPGecko codehandler
- **Tyre3** for helping me find USA addresses for many of the USA versions here

###### psst! hey! these scripts are customizable to your liking! feel free to change stuff around! try not to burn the place down though.
