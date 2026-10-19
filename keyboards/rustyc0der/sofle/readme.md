# Sofle RGB Custom

An RP2040 split keyboard based on the [Sofle RGB](https://github.com/josefadamcik/SofleKeyboard),
adapted for two 64x128 SH1107 OLEDs and a five-way switch in place of the
right encoder. The left encoder, 72-key RGB Matrix, VIA-enabled personal
keymap, and conventional default keymap are supported by upstream QMK.

The hardware build and source files are maintained in the
[project repository](https://github.com/RuStyC0der/QMK-firmware-for-keyboards).
The display and five-way switch used by the original build are linked from the
repository's top-level README.

## Supported targets

- `default`: a conventional keymap without VIA or personal behaviors.
- `j64`: the maintained personal keymap with VIA, encoder maps, OLED rendering,
  tap dance, home-row mods, Caps Word, and gaming-layer lighting.

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

From the QMK checkout, confirm the target and compile either keymap:

```sh
qmk list-keyboards | grep '^rustyc0der/sofle$'
qmk compile -kb rustyc0der/sofle -km default
qmk compile -kb rustyc0der/sofle -km j64
```

## Flashing

Each RP2040 half must receive the same selected firmware. From the QMK checkout,
run the flash command, put one half into the bootloader when prompted, and then
repeat for the other half:

```sh
qmk flash -kb rustyc0der/sofle -km j64
```

The board enables RP2040 double-tap reset. If automatic flashing cannot find the
device, double-tap reset to mount the `RPI-RP2` drive and copy the generated
`rustyc0der_sofle_j64.uf2` to it. Disconnect the split cable before flashing a
half, and reconnect it only after both controllers have left bootloader mode.

See the repository's migration record and hardware validation checklist for the
exact toolchain baseline and post-flash checks.
