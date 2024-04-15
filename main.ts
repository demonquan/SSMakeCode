radio.onReceivedString(function (receivedString) {
    if (receivedString == "A") {
        开关打开 = true
        basic.pause(200)
    } else {
        开关打开 = false
        basic.pause(200)
    }
})
let 开关打开 = false
开关打开 = false
radio.setGroup(12)
basic.forever(function () {
    if (ModuleWorld_Digital.Button(ModuleWorld_Digital.mwDigitalNum.P0P1, ModuleWorld_Digital.enButton.Press)) {
        开关打开 = !(开关打开)
        basic.pause(200)
    }
})
basic.forever(function () {
    if (开关打开) {
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.White)
        basic.showIcon(IconNames.Yes)
    } else {
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.OFF)
        basic.showIcon(IconNames.No)
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        开关打开 = true
        basic.pause(200)
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.B)) {
        开关打开 = false
        basic.pause(200)
    }
})
basic.forever(function () {
    if (input.logoIsPressed()) {
        开关打开 = !(开关打开)
        basic.pause(200)
    }
})
