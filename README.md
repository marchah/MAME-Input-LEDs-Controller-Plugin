# Plugin MAME Input LEDs Controller Plugin

# WIRING

![WIRING](img/MILCP_wiring.png)

## Install

- Move folder `milcp` from `mame/plugins` inside your mame `plugins` folder
- Set your server IP in `milcp/constants.py`

Open PowerShell (shift + right click)

```
python # will open windows store, click Get

# when install is done do:
pip install requests
```

# Server

- [Setup Raspberry Pi](/rpi-server)

# Demo

[Youtube link](https://www.youtube.com/watch?v=P2EGnTRAedU)

## Issues

- When using MAME UI game window get minimize, working fine in command line and CoinOPS NEXT

## TODO

- Use mosfets instead of relays
- Improve ugly wiring diagram
- MAME seems to know how many buttons the game use, investigate that
- Find a way set the game input configuration from the lua plugin
- Find a way to go the http request directly from the lua plugin
- Use .bat script instead of python in MAME plugin
- Parse http query and display to user if error
- If game pause make start button blink
- If no coins make coins button blink
- Support more input layouts
- Add support for ServoStik joystick
- Server: ctrl + c not handled
- Server: if game unknown light all leds
- Server: create a http server without using `flask`
- Server: add env variables to only light up player inputs based on game number of players
- Server: having issue install dependencies for Pi B+, works for Zero W and 3B
