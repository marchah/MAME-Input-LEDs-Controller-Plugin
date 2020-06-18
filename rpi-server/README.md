# Server For MAME Input LEDs Controller Plugin

## Install

In terminal type:

```
sudo apt-get update
sudo apt-get install rpi.gpio

# install PIP
# check python version
python --version

# for python v2.*
sudo apt-get install python-pip
# for python v3.* (not tested with python 3)
sudo apt-get install python3-pip

pip install flask
```

- start server
- setup auto start https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen

## Usage

By defaults when no game is running all the LEDs will be turn on.
If you want the default behaviour do be all the LEDs off set the env variable `LED_DEFAULT_VALUE` to `OFF`

Start server

```
python server.py
```

## API

```
# Set LEDs behaviour for playing game
POST /game/<romname>
# Body
{
  inputs: Array<string>
}
# Return
{
  success: boolean
  message: string # set only if success if false
}

# Reset all LEDs to default behaviour
DELETE /game/<romname>
# Body
{}
# Return
{
  success: boolean
  message: string # set only if success if false
}

# Debug request body
POST /debug
# Body
{
  *
}
# Return
{
  success: boolean
  message: string # set only if success if false
}
```

## TODO

- Ctrl + c not handled
- If game unknown light all leds
- If game pause make start button blink
- If no coins make coins button blink
- Support more input layouts
- Create a http server without using `flask`
- Add env variables to only light up player inputs based on game number of players
- Add support for ServoStik joystick
- Having issue install dependencies for Pi B+, works for Zero W and 3B
