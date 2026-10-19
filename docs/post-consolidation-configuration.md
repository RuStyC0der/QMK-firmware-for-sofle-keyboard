# Post-consolidation configuration comparison

This comparison was captured immediately after data-driven configuration was
consolidated, before keymap source refactoring. The build used upstream QMK
commit `180f394b489c238cb231c2bf8b080262155e03c0`.

`qmk compile -kb rustyc0der/sofle -km j64` completed successfully and produced
`rustyc0der_sofle_j64.uf2` with SHA-256
`d2d7a885593e7946cd0b454ff3dfdcd32405af3c9420f502a8b56d42f6be0a7f`.

## Hardware comparison

| Surface | Baseline | Consolidated | Result |
| --- | --- | --- | --- |
| Processor / bootloader | `RP2040` / `rp2040` | same | Match |
| USB identity | `FC32:0288`, version `1.0.0` | same | Match |
| Matrix dimensions | 10x7 | same | Match |
| Left rows | `GP13, GP6, GP7, GP12, GP9` | same | Match |
| Left columns | `GP27, GP26, GP22, GP20, GP23, GP21, null` | same | Match |
| Right rows | `GP13, GP12, GP7, GP8, GP9` | same | Match |
| Right columns | `GP27, GP26, GP22, GP20, GP23, GP21, GP28` | same | Match |
| Split serial | vendor, `GP1`, PIO0 | same | Match |
| Handedness | `GP4`, low is left | same | Match |
| Encoder | `GP29`/`GP28`, resolution 4 | same | Match |
| WS2812 | vendor, `GP0` | same | Match |
| RGB Matrix | WS2812, 72 LEDs, 36/36, brightness 128 | same | Match |
| OLED / I2C | SH1107 64x128, `I2CD1`, `GP2`/`GP3` | same | Match |

The complete 72-entry RGB coordinate/flag array is unchanged.

## Behavior comparison

The consolidated `j64` target still resolves Bootmagic Lite, mouse keys, extra
keys, NKRO, console, Caps Word, split support, encoder and encoder map, OLED,
WPM, RGB Matrix, VIA, tap dance, five dynamic layers, 16 macros, tapping term
200 ms, and tap-code delay 10 ms.

Expected representation-only differences are:

- default debounce, disabled features, disabled matrix-state synchronization,
  and default RGB on/saturation/value properties are no longer redundantly
  declared;
- the unused RGB Light configuration was removed because RGB Matrix owns the
  72 LEDs;
- I2C0 is no longer enabled because the OLEDs use only I2C1;
- `USB_VBUS_PIN` now uses the current `GP19` spelling instead of numeric `19`.

No hardware-critical difference is unexplained. The remaining obsolete Vial
option warning belongs to the planned `vialj64` removal task and does not affect
this successful upstream-QMK build.

## Final comparison

The comparison was repeated after keymap modernization and Vial removal. Final
`qmk info` contains the same processor, bootloader, USB identity, matrix pins,
split transport and synchronization, handedness, encoder, WS2812, RGB Matrix,
OLED/I2C, tapping, and maintained `j64` feature values listed above. It reports
72 RGB Matrix entries, and the final coordinate/flag array has the same
normalized SHA-256 as the baseline:
`dffb7e4849e87d9f056b15672ade9cb285dbdbe541fa60183b2ee73fbc30ab13`.

The final VIA definition matches VID/PID `FC32:0288`, matrix dimensions 10x7,
and all 64 `LAYOUT` matrix positions, including the five right-hand
seventh-column switch positions and the encoder's compound `4,5…e0` entry.
`j64` retains five dynamic layers and 16 dynamic macros. Final `qmk info`
produced no merge, duplicate, deprecated, or invalid-option warnings.
