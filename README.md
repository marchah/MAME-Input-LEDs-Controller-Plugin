# Plugin MAME Input LEDs Controller Plugin

# WIRING

![WIRING](img/raspberry_pi_1b_failure.png)

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

![Youtube link](https://www.youtube.com/watch?v=P2EGnTRAedU)

## Issues

- When using MAME UI game window get minimize, working fine in command line and CoinOPS NEXT

## TODO

- Use mosfets instead of relays
- Improve ugly wiring diagram
- Display message in MAME when rom doesn't have input config
- MAME seems to know how many buttons the game use, investigate that
- Find a way set the game input configuration from the lua plugin
- Find a way to go the http request directly from the lua plugin
- Parse http query and display to user if error
