import st7036, backlight#, joystick

lcd = st7036.st7036(register_select_pin=25)
lcd.clear()
