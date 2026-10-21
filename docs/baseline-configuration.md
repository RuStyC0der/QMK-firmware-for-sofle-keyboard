# Pre-migration configuration snapshot

This snapshot was captured from `qmk info -kb rustyc0der/sofle -km j64 -f json`
against QMK commit `180f394b489c238cb231c2bf8b080262155e03c0`, plus values that are
only present in the legacy C configuration. It is the comparison source for the
modernized `rustyc0der/sofle` target.

## Controller and identity

| Setting | Baseline value |
| --- | --- |
| Processor | `RP2040` |
| Bootloader | `rp2040` |
| USB VID | `0xFC32` |
| USB PID | `0x0288` |
| Device version | `1.0.0` |
| Diode direction | `COL2ROW` |
| Matrix dimensions | 10 rows x 7 columns |

## Matrix, split, and controls

| Setting | Baseline value |
| --- | --- |
| Left row pins | `GP13, GP6, GP7, GP12, GP9` |
| Left column pins | `GP27, GP26, GP22, GP20, GP23, GP21, null` |
| Right row pins | `GP13, GP12, GP7, GP8, GP9` |
| Right column pins | `GP27, GP26, GP22, GP20, GP23, GP21, GP28` |
| Split transport | serial, vendor driver |
| Serial pin | `GP1` (legacy `SERIAL_USART_TX_PIN`) |
| RP2040 serial PIO | PIO0 (`SERIAL_PIO_USE_PIO0`) |
| Handedness pin | `GP4`, low is left |
| Split synchronization | layer state, LED indicators, modifiers, WPM, OLED; matrix state disabled |
| Encoder | one rotary encoder, `GP29`/`GP28`, resolution 4 |

The five right-hand switch positions occupy matrix positions `[5,6]`, `[6,6]`,
`[7,6]`, `[8,6]`, and `[9,6]`. The left seventh column is deliberately `null`.

## Lighting

| Setting | Baseline value |
| --- | --- |
| WS2812 driver/pin | vendor / `GP0` |
| RGB Matrix driver | `ws2812` |
| RGB Matrix LED count | 72, split 36/36 |
| RGB Matrix max brightness | 128 |
| RGB Matrix sleep | enabled |
| Default effect | solid color, hue 158, saturation 255, value 255 |
| Enabled effects | solid color, solid reactive cross |

The disabled `rgblight` block repeated the count and split values but did not
drive the hardware; it is not an independent migration requirement.

## OLED and I2C

| Setting | Baseline value |
| --- | --- |
| OLED controller | SH1107 |
| OLED geometry | Physical 128x64; logical 64x128 portrait framebuffer |
| I2C driver | `I2CD1` |
| I2C SDA/SCL | `GP2` / `GP3` |
| Brightness | 180 |
| Timeout | 60000 ms |
| Font | `lib/glcdfont.c` |

The board-level legacy config declared `OLED_DISPLAY_128X32`, but the `j64`
keymap explicitly undefined it and selected the physical 128x64 SH1107 panel's
logical 64x128 portrait framebuffer.
The modernized board records only the actual hardware.

## Resolved j64 build features

Enabled in the successful baseline build:

- Bootmagic Lite, mouse keys, extra keys, console, Caps Word (NKRO was enabled
  in this baseline build and has since been disabled for all boards)
- split keyboard, encoder, encoder map
- OLED and WPM
- RGB Matrix
- VIA with 5 dynamic keymap layers and 16 macros
- tap dance
- link-time optimization
- per-key tapping term, hold-on-other-key-press, and quick-tap decisions

Explicitly disabled or inactive in the resolved build: audio, backlight,
command, RGB Light, Combo, Key Override, and Swap Hands. Legacy Vial options
were ignored/invalid on upstream QMK and are not part of the maintained
baseline.

Other behavior-critical values are tapping term 200 ms and tap-code delay
10 ms. The personal `M0` macro includes a 50 ms delay before GUI+Space.
