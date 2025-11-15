# Sofle RGB Custom

This repo started as fork when I decided to add a little bit of a personal touch to my pandakb's sofle rgb kit.

![keeb](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/keeb.jpg?raw=true)

![lightning](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/ligtning.jpg?raw=true)

## Keeb got a few upgrades since first build

### Case
It still uses stock tenting case from stock Sofle rgb but i decided to cut top part out of transparent acryl plastic and bottom part out of aluminium for more rich and decent sound. 

It also includes custom-molded silicone sound absorber, I used silicone with hardness by shore at 25 points and I satisfied with that, but i used tin-based catalyst and compound comes out oily and always wet, so I recommend using platinum-based catalyst if you want to do this.

Some other small upgrades include painter tape mod and pe foam mod.

![case bottom](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/case_bottom.jpg?raw=true)
![case top](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/case_top.jpg?raw=true)

### Display
Stock version uses 32x128px display. I decided to change them to 64x128px 1.3 inch display to fit my canvas, [link](https://www.aliexpress.com/item/1005005777499038.html).

here is some picture with old display to compare with:
![old display](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/old_display.jpg?raw=true)

### Joystick
Instead of right knob it used 5-direction switch([link](https://www.aliexpress.com/item/1005004108793838.html)) It was wired as additional column to pin 28
![old display](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/joystic.jpg?raw=true)

### Switches
This keeb uses Keychron smoothie switches at the moment.

### Keycaps
At the moment I use blank cherry white PBT caps from Aliexpress [link](https://www.aliexpress.com/item/1005009662975948.html)

### Hardware
It uses stock rpi2040 board from pandakb kit

### Firmware
Stock firmware was vial as it supports rotary knob and via did no support this feature at the time. Via also provides several advanced features from ui, such as tap dance, and so on. But as it provides this functionality from ui you can not use it from code so you can not use functions like `tap dance` and `tap hold per-key features`. And since now via also supports rotary encoders and do not revent me from using those features I create keymap for via without vial

### Keymap
Keymap uses home-row keys (CSAG) and also uses layer-tap on layer buttons, right layer button is enter if tapped and left one is space as well as caps word feature. 
Also I have separate layer for gaming, when switched to it left halve's indicator turns red. 
On default layer joystic buttons serve to manipulate window position (win+up, win+down and so on)
Keymap screenshoots from via:
![l0](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/l0.png?raw=true)
![l1](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/l1.png?raw=true)
![l2](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/l2.png?raw=true)
![l3](https://github.com/RuStyC0der/QMK-firmware-for-sofle-keyboard/blob/main/assets/pictures/l3.png?raw=true)
