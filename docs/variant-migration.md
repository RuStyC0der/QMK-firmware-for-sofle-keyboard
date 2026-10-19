# Sofle hardware-variant migration record

This record captures the buildable `rustyc0der/sofle` target immediately before
it is split into explicit MX and Choc revisions. It complements the earlier
modernization evidence in [baseline-configuration.md](baseline-configuration.md)
and is the comparison source for `rustyc0der/sofle/mx`.

## Pre-revision MX baseline

- Repository commit: `ded1783` plus only the untracked
  `add-sofle-choc-variant` OpenSpec planning directory.
- Upstream QMK commit: `180f394b489c238cb231c2bf8b080262155e03c0`.
- `qmk lint -kb rustyc0der/sofle`: passed.
- `qmk compile -kb rustyc0der/sofle -km default`: passed; UF2 SHA-256
  `5f443a80295fad24ee10ede53bf26fbfa8a8dc6d8467d0aa13fa72deda9a8079`.
- `qmk compile -kb rustyc0der/sofle -km j64`: passed; UF2 SHA-256
  `ef2411fa4c055da4b703a03421ad176338035a9387b762aec4aebc5802a1ba40`.

The resolved `j64` configuration reports RP2040/rp2040, USB `FC32:0288`, a
10x7 matrix, one encoder, 72 RGB Matrix LEDs split 36/36, and the five
right-hand switch positions at matrix column 6. Generated hardware defines
contain:

| Surface | Pre-revision value |
| --- | --- |
| Left rows | `GP13, GP6, GP7, GP12, GP9` |
| Left columns | `GP27, GP26, GP22, GP20, GP23, GP21, NO_PIN` |
| Right rows | `GP13, GP12, GP7, GP8, GP9` |
| Right columns | `GP27, GP26, GP22, GP20, GP23, GP21, GP28` |
| Encoder | `GP29` / `GP28`, resolution 4 |
| Split serial / handedness | `GP1` / `GP4` |
| WS2812 / RGB Matrix | `GP0`, 72 LEDs, split 36/36 |
| OLED | Physical SH1107 128x64, logical 64x128 portrait framebuffer, I2C1 on `GP2` / `GP3` |
| Bootloader indicator | `GP17` |

The complete expected feature and physical-layout values remain documented in
[post-consolidation-configuration.md](post-consolidation-configuration.md) and
[j64-behavior-equivalence.md](j64-behavior-equivalence.md).

## MX revision migration result

After moving the buildable definition to `rustyc0der/sofle/mx`, both `default`
and `j64` compiled successfully and `qmk lint -kb rustyc0der/sofle/mx` passed.
The resolved MX `j64` information retains the baseline processor, USB identity,
matrix pins and dimensions, split settings, encoder, 72-entry RGB Matrix,
five-way-switch positions, and maintained keymap feature set. OLED geometry,
I2C pins, and the custom font are family-owned; only the `GP17` indicator
remains MX-owned.

At the revision-move checkpoint, both MX artifacts were byte-for-byte identical
to the pre-revision baseline: the `default` SHA-256 was
`5f443a80295fad24ee10ede53bf26fbfa8a8dc6d8467d0aa13fa72deda9a8079` and
the `j64` SHA-256 was
`ef2411fa4c055da4b703a03421ad176338035a9387b762aec4aebc5802a1ba40`.
The later shared OLED/font/RGB extraction and the explicit
`NUM_ENCODERS_RIGHT 0` correction rebuild the final artifacts. The correction
prevents QMK's split-encoder fallback from scanning the left encoder pins on
the right half, where `GP28` belongs to the five-way matrix. Final artifacts
are recorded below and validated by the paired configuration and behavior
checks.

## Final revision comparison

Both revisions resolve to RP2040/rp2040, `COL2ROW`, vendor ID `0xFC32`, split
hand pin `GP4`, vendor serial transport on `GP1`, WS2812 data on `GP0`, USB
VBUS detection on `GP19`, I2C1 on `GP2`/`GP3`, and physical 128x64 SH1107
OLEDs using logical 64x128 portrait framebuffers. Both enable the shared
one-second RP2040 double-tap reset and synchronize layer, modifier, OLED, WPM,
and indicator state across the split.

| Surface | MX | Choc |
| --- | --- | --- |
| USB PID | `0x0288` | `0x0287` |
| Matrix | 10x7; revision-specific left/right rows and right `GP28` column | 10x7; rows `GP5`-`GP9`, six ordinary columns, right `GP28` column |
| Physical layout | 64 positions, including five column-6 switch positions | Same 64 positions and five column-6 switch positions |
| Controls | Left encoder, `GP29`/`GP28`; right five-way switch | Left encoder, `GP28`/`GP29`; right five-way switch |
| OLED | Physical 128x64 SH1107; logical 64x128 portrait; dog/status and girl graphics | Same hardware, font, and graphics |
| RGB Matrix | 72 LEDs, split 36/36 | 58 LEDs, split 29/29 |
| Reset indicator | `GP17` | None |
| Separate backlight / underglow | None | None |

The final automated gate passed for both `default` and `j64` on both revisions,
per-revision QMK lint, QMK C and keyboard-JSON formatting, license checks, and
VIA JSON parsing. Final artifact SHA-256 values are:

| Target | SHA-256 |
| --- | --- |
| `rustyc0der/sofle/mx:default` | `5f6e7c34414b36a0e1eb24759a0bcf4febe72e5e85eca35f629ab94d39ec4eeb` |
| `rustyc0der/sofle/mx:j64` | `6a9cdace58e9d6646a59e0a9b1bae16aab9ee798add94ee64f867c33cdebcd61` |
| `rustyc0der/sofle/choc:default` | `916f2ad3231a0eb7dd9b4552c9abf5097b63ef516bd90a33d3550bbe7d06fb09` |
| `rustyc0der/sofle/choc:j64` | `187914abe59827fcd10febca7f7505af3d0750a11dbef63cee6e23f00dfd5b57` |

All four files identify as Raspberry Pi RP2040 UF2 images.
