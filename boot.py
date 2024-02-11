from mpython import *

def display_message(message):
    oled.fill(0)
    oled.DispChar(str(message), 0, 0, 1, True)
    oled.show()

while True:
    display_message('Flag OS BIOS')
    display_message('A - System')
    display_message('B - User(main.py)')
    oled.hline(50, 62, 30, 1)

    if button_a.is_pressed():
        display_message('Attempting to boot to System...')
        import Flag_OS.system.main
        break
    elif button_b.is_pressed():
        display_message('Attempting to boot to User(main.py)...')
        break
