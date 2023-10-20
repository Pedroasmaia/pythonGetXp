def validate_pin(pin):
    x = pin.isnumeric()
    if len(pin) == 4 and x == True or len(pin) == 6 and x == True:
        return True
    else:
        return False