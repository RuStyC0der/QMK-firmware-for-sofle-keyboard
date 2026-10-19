# Sofle MX and Choc firmware

Upstream-QMK firmware for two related PandaKB Sofle hardware revisions:

- `rustyc0der/sofle/mx` is the customized MX build with 128x64 SH1107
  displays, a left encoder, a right five-way switch, and 72 RGB Matrix LEDs.
- `rustyc0der/sofle/choc` is the low-profile Choc build with the same 128x64
  SH1107 displays, left encoder, right five-way switch, and 58 per-key RGB
  LEDs. It has no separate backlight circuit and no bootloader indicator LED.

Both revisions use RP2040 controllers and the same vendor namespace, but a
build must always name the physical revision.

| Revision | Switches | OLEDs (physical; QMK framebuffer) | Controls | Per-key RGB | Separate backlight | Reset indicator LED | USB PID |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| `mx` | MX | 2 x 128x64 SH1107; 64x128 portrait | Left encoder; right five-way switch | 72 LEDs | No | GP17 | `0x0288` |
| `choc` | Choc | 2 x 128x64 SH1107; 64x128 portrait | Left encoder; right five-way switch | 58 LEDs | No | None | `0x0287` |

Here, “per-key RGB” means the WS2812 RGB Matrix LEDs fitted beneath the keys;
neither PCB has a separate conventional backlight or RGB-underglow circuit.

![Completed keyboard](assets/pictures/keeb.jpg)

## Firmware layout and support

The QMK package is organized as the non-buildable family
[`keyboards/rustyc0der/sofle`](keyboards/rustyc0der/sofle), with buildable `mx`
and `choc` children. Do not install it as `sofle/sofle`: that path collides with
and inherits settings from QMK's unrelated upstream Sofle family.

Two keymaps are maintained:

- `default` is a conventional QWERTY keymap with ordinary five-way-switch and
  encoder assignments. It does not enable VIA or personal behavior.
- `j64` is the personal VIA keymap with four compiled layers, five dynamic
  layers, home-row mods, Space/Enter layer-taps, tap dance, Caps Word, OLED pet
  rendering, encoder maps, and red gaming-layer indication.

The former `vialj64` target and Vial-only files have been removed. This project
supports current upstream QMK and VIA; supporting the separate Vial firmware
fork would require a separately maintained change.

The audited baseline is QMK `0.34.7` at commit
`180f394b489c238cb231c2bf8b080262155e03c0`, with that checkout's pinned
submodules. Build from the QMK checkout after creating the safe vendor-directory
symlink documented in the [keyboard README](keyboards/rustyc0der/sofle/readme.md):

```sh
qmk compile -kb rustyc0der/sofle/mx -km default
qmk compile -kb rustyc0der/sofle/mx -km j64
qmk compile -kb rustyc0der/sofle/choc -km default
qmk compile -kb rustyc0der/sofle/choc -km j64
```

The former `rustyc0der/sofle` build identifier is intentionally removed. Use
the `/mx` suffix for the previously supported customized keyboard.

Flash the selected UF2 to both halves. The keyboard README contains the full
installation and flashing procedure.

## VIA

Build and flash the matching `j64` target, then load its revision-specific VIA
draft definition. The MX definition is
[`via/sofle-mx-via.json`](via/sofle-mx-via.json), and the Choc definition is
[`via/sofle-choc-via.json`](via/sofle-choc-via.json). See the [VIA definition
guide](via/README.md) for exact steps. VIA is not enabled by `default`.

## Choc hardware reference

The Choc matrix, encoder, RGB Matrix, and split wiring are based on PandaKB's
[published Choc Sofle QMK firmware](https://github.com/PandaKBLab/QMK-firmware-for-keyboards).
This build preserves the published row, ordinary-column, left-encoder, RGB,
and split wiring. It describes the locally fitted 128x64 SH1107 OLEDs shared
with MX and replaces the published right encoder with the same five-way switch
as MX on a right-only `GP28` seventh column. The displays are mounted in
portrait, so QMK uses a logical 64x128 framebuffer. Choc intentionally defines
no separate backlight or reset indicator LED.

## Shared customized hardware notes

### Case and dampening

The build retains the stock tenting case with a transparent acrylic top and an
aluminium bottom. It also uses a custom-molded silicone sound absorber, painter's
tape, and PE foam. A platinum-cure silicone is preferable to the oily tin-cure
compound used in the first version.

![Case bottom](assets/pictures/case_bottom.jpg)
![Case top](assets/pictures/case_top.jpg)

### Displays

The two displays are 1.3-inch 128x64 SH1107 modules mounted in portrait; QMK
therefore uses a logical 64x128 framebuffer. The original build used
[these displays](https://www.aliexpress.com/item/1005005777499038.html).

![Original 32x128 display comparison](assets/pictures/old_display.jpg)

### Five-way switch

The right encoder position on each revision uses a
[five-direction switch](https://www.aliexpress.com/item/1005004108793838.html).
Its five contacts occupy matrix positions `[5,6]` through `[9,6]`.

![Five-way switch](assets/pictures/joystic.jpg)

### Switches and keycaps

The photographed build uses Keychron Smoothie switches and blank white Cherry
profile PBT keycaps.

## j64 keymap

Both revisions use the same compiled key assignments, layers, macros, encoder
map, and five-way behavior. The base layer uses CSAG-style home-row mods, Space
and Enter layer-taps, Caps Word, and five-way shortcuts for window positioning.
The gaming layer replaces home-row mod-taps with ordinary keys and turns the
intended RGB indicators red. Both also render the same dog/status artwork on
the primary OLED and girl graphic on the secondary OLED.

![j64 base layer](assets/pictures/l0.png)
![j64 raise layer](assets/pictures/l1.png)
![j64 lower layer](assets/pictures/l2.png)
![j64 gaming layer](assets/pictures/l3.png)

Migration evidence is in [`docs/`](docs), and the physical post-flash procedure
is in the [manual hardware checklist](docs/hardware-validation.md).
