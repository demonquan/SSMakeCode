def on_received_string(receivedString):
    global 开关打开
    if receivedString == "A":
        开关打开 = False
        basic.pause(200)
    else:
        开关打开 = True
        basic.pause(200)
radio.on_received_string(on_received_string)

开关打开 = False
开关打开 = False
radio.set_group(12)

def on_forever():
    global 开关打开
    if ModuleWorld_Digital.button(ModuleWorld_Digital.mwDigitalNum.P0P1,
        ModuleWorld_Digital.enButton.PRESS):
        开关打开 = not (开关打开)
        basic.pause(200)
basic.forever(on_forever)

def on_forever2():
    if 开关打开:
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.WHITE)
        basic.show_icon(IconNames.YES)
    else:
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.OFF)
        basic.show_icon(IconNames.NO)
basic.forever(on_forever2)

def on_forever3():
    global 开关打开
    if input.button_is_pressed(Button.A):
        开关打开 = True
        basic.pause(200)
basic.forever(on_forever3)

def on_forever4():
    global 开关打开
    if input.button_is_pressed(Button.B):
        开关打开 = False
        basic.pause(200)
basic.forever(on_forever4)

def on_forever5():
    global 开关打开
    if input.logo_is_pressed():
        开关打开 = not (开关打开)
        basic.pause(200)
basic.forever(on_forever5)
