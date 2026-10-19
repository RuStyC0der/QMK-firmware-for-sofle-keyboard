# Sofle hardware family

RP2040 split-keyboard firmware for two related PandaKB Sofle builds. The `mx`
revision has two 128x64 SH1107 OLEDs, a left encoder, a right five-way switch,
and 72 RGB Matrix LEDs. The `choc` revision has the same two 128x64 SH1107
OLEDs, left encoder, right five-way switch, and 58 per-key RGB LEDs, with no
separate backlight or bootloader indicator LED. Both revisions mount the
displays in portrait, so QMK uses a logical 64x128 framebuffer and both render
the same dog/status and girl graphics.

| Revision | Displays | Controls | RGB hardware | Reset indicator |
| --- | --- | --- | --- | --- |
| `mx` | 2 x 128x64 SH1107, portrait | One encoder and a five-way switch | 72 per-key RGB Matrix LEDs; no separate backlight | GP17 |
| `choc` | 2 x 128x64 SH1107, portrait | One encoder and a five-way switch | 58 per-key RGB Matrix LEDs; no separate backlight | None |

The hardware build and source files are maintained in the
[project repository](https://github.com/RuStyC0der/QMK-firmware-for-keyboards).
The custom MX display and five-way switch are linked from the repository's
top-level README. PandaKB's published Sofle Choc firmware is the electrical
reference for the Choc revision's rows, ordinary columns, left encoder, RGB,
and split wiring. This repository adds the locally fitted 128x64 SH1107
displays and replaces the published right encoder with the same right five-way
switch as MX on a right-only `GP28` matrix column.

## Supported revisions and keymaps

- `rustyc0der/sofle/mx`: customized MX hardware. This replaces the former
  `rustyc0der/sofle` build identifier.
- `rustyc0der/sofle/choc`: low-profile Choc hardware.

- `default`: a conventional keymap without VIA or personal behaviors, with the
  same assignments on both revisions.
- `j64`: the maintained personal keymap with VIA, the shared encoder map and
  five-way behavior, identical dog/girl OLED rendering,
  tap dance, home-row mods, Caps Word, and gaming-layer lighting.

The family root is intentionally not buildable; always select a revision.

The verified upstream baseline is QMK `0.34.7`, commit
`180f394b489c238cb231c2bf8b080262155e03c0`, including that checkout's pinned
submodules.

## Development installation

Link the vendor directory into a separate QMK checkout. Use absolute paths and
run these commands from this repository:

```sh
repo_root=/absolute/path/to/QMK-firmware-for-keyboards
qmk_root=/absolute/path/to/qmk_firmware
ln -s "$repo_root/keyboards/rustyc0der" "$qmk_root/keyboards/rustyc0der"
```

`ln -s` fails if the destination already exists, so this does not replace
`qmk_firmware/keyboards/sofle` or any other upstream keyboard. Remove only the
`keyboards/rustyc0der` link when the development integration is no longer
needed.

From the QMK checkout, confirm both targets and compile the matching revision:

```sh
qmk list-keyboards | grep '^rustyc0der/sofle/'
qmk compile -kb rustyc0der/sofle/mx -km default
qmk compile -kb rustyc0der/sofle/mx -km j64
qmk compile -kb rustyc0der/sofle/choc -km default
qmk compile -kb rustyc0der/sofle/choc -km j64
```

## Flashing

Each RP2040 half must receive the same selected firmware. From the QMK checkout,
run the flash command, put one half into the bootloader when prompted, and then
repeat for the other half:

```sh
qmk flash -kb rustyc0der/sofle/mx -km j64
# or
qmk flash -kb rustyc0der/sofle/choc -km j64
```

The board enables RP2040 double-tap reset. If automatic flashing cannot find the
device, double-tap reset to mount the `RPI-RP2` drive and copy the generated
revision-specific UF2 to it. Disconnect the split cable before flashing a half,
and reconnect it only after both controllers have left bootloader mode.

See the repository's migration record and hardware validation checklist for the
exact toolchain baseline and post-flash checks.
