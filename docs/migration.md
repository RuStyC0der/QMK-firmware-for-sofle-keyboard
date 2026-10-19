# Upstream QMK migration record

This document records the reproducible baseline and verification evidence for the
`modernize-qmk-keyboard` change. Hardware checks that require the physical
keyboard are deliberately tracked separately in [hardware-validation.md](hardware-validation.md).

## Verified pre-migration baseline

- Source repository commit: `7a3d4aead48098b272ed894bf2f3bcc2c5cc87ff`
- Upstream QMK commit: `180f394b489c238cb231c2bf8b080262155e03c0`
- Upstream QMK version: `0.34.7`
- Build command, run from the QMK checkout:
  `qmk compile -kb rustyc0der/sofle -km j64`
- Result: successful RP2040 UF2 build (`rustyc0der_sofle_j64.uf2`)
- Baseline UF2 SHA-256:
  `816462a761deaafcc780bba5d5e1ac971bf03bfba5d5cb13b6271e60eaae8`

The temporary baseline integration linked QMK's
`keyboards/rustyc0der` path to the repository's legacy `sofle` directory. It
was used because the legacy `sofle/sofle` identifier inherited incompatible
`D2` and `D3` settings from upstream Sofle.

The resolved baseline used an RP2040 with the `rp2040` bootloader; USB VID/PID
`FC32:0288`; a 10x7 split matrix; left columns
`GP27, GP26, GP22, GP20, GP23, GP21, null`; right columns
`GP27, GP26, GP22, GP20, GP23, GP21, GP28`; left rows
`GP13, GP6, GP7, GP12, GP9`; right rows
`GP13, GP12, GP7, GP8, GP9`; serial transport on `GP1`; handedness on
`GP4`; encoder pins `GP29`/`GP28`; WS2812 data on `GP0`; and 72 RGB Matrix
LEDs split 36/36. The OLED configuration used `I2CD1` on `GP2`/`GP3`, SH1107,
64x128 geometry, brightness 180, and a 60-second timeout. The complete
machine-comparable record is in [baseline-configuration.md](baseline-configuration.md).

## User-owned working-tree changes preserved as migration inputs

Before migration, the following tracked edits were present and are intentional:

- `keyboard.json`: left row pins changed from `GP5, GP6, GP7, GP8, GP9` to
  `GP13, GP6, GP7, GP12, GP9`; right row pins changed from
  `GP5, GP6, GP7, GP8, GP9` to `GP13, GP12, GP7, GP8, GP9`.
- `keymaps/j64/process_record.c`: the `M0` shortcut gained a 50 ms delay
  between pressing GUI and tapping Space (`SS_DELAY(50)`).
- `keymaps/j64/suspend.c`: the previous wake callback was removed, leaving the
  file empty. The migration removes that empty module and retains layer-color
  restoration in the RGB Matrix indicator callback.

At capture time, `.agents/` and `openspec/` were also untracked planning/tooling
content. They are unrelated to keyboard behavior.

## Final verification

The intermediate configuration-equivalence result is recorded in
[post-consolidation-configuration.md](post-consolidation-configuration.md).

Final verification used QMK `0.34.7` at commit
`180f394b489c238cb231c2bf8b080262155e03c0` and its pinned submodules. The
following commands passed from the QMK checkout:

```sh
qmk clean
qmk compile -kb rustyc0der/sofle -km default
qmk compile -kb rustyc0der/sofle -km j64
qmk lint -kb rustyc0der/sofle
qmk license-check keyboards/rustyc0der/sofle
qmk format-c -n keyboards/rustyc0der/sofle/config.h # plus every retained C/header source
qmk format-json -p keyboards/rustyc0der/sofle/keyboard.json # output compared byte-for-byte
qmk format-text keyboards/rustyc0der/sofle/keymaps/j64/rules.mk keyboards/rustyc0der/sofle/readme.md
```

`qmk format-text` has no dry-run option, so it was run twice and the input
SHA-256 values were unchanged on the second pass. The host did not provide the
optional `dos2unix` executable, so a temporary scoped compatibility executable
supplied its required `--add-eol` interface; it was removed immediately after
the idempotence check. VIA/KLE JSON lives outside QMK's schemas and was checked
with `jq empty` rather than passed to `qmk format-json`, which misclassifies VIA
draft definitions as QMK keymaps.

Final clean-build artifacts:

| Target | Size | SHA-256 |
| --- | ---: | --- |
| `rustyc0der/sofle:default` | 94,720 bytes | `5f443a80295fad24ee10ede53bf26fbfa8a8dc6d8467d0aa13fa72deda9a8079` |
| `rustyc0der/sofle:j64` | 113,664 bytes | `ef2411fa4c055da4b703a03421ad176338035a9387b762aec4aebc5802a1ba40` |

Both clean builds completed without compiler or generated-configuration
warnings. QMK lint passed, every retained C/header file was recognized by the
license checker, and the C/JSON formatter dry checks produced no diff.

## Final diff audit

The final repository audit confirmed:

- USB VID/PID/version remain `FC32:0288` / `1.0.0`.
- The user's left rows (`GP13, GP6, GP7, GP12, GP9`) and right rows
  (`GP13, GP12, GP7, GP8, GP9`) remain present, along with every recorded
  column, transport, handedness, encoder, OLED/I2C, and WS2812 pin.
- The normalized physical `LAYOUT` is byte-equivalent to the baseline
  (`6ee218de7d71eae42fe494987cb2563ef82324bcfe4c4bc8fd8ff487acaf139c`).
- The normalized 72-entry RGB coordinate/flag array is byte-equivalent
  (`dffb7e4849e87d9f056b15672ade9cb285dbdbe541fa60183b2ee73fbc30ab13`).
- The OLED hexadecimal graphics stream is byte-equivalent
  (`dee9f20f91b577376c11f7606a2bfaa031d01b867472d3f4777371888e7a60c6`),
  and the custom font stream is byte-equivalent
  (`fcad6ea7aaa7bfc6a4dd605f179e9e1c6a62354c4abc4e56dafc8149e9cb6e56`).
- The full `j64` keymap/encoder initializer remains byte-equivalent
  (`0f3428bf9d502d139bf2a64c43461606e282658a5b836773bd756aceffbf0198`).
- The user's `SS_DELAY(50)` remains in `M0`; the intentionally emptied suspend
  module is removed rather than reintroduced.
- `git diff --check` passes. Every source, configuration, documentation, and
  removal difference maps to the approved namespace migration, data-driven
  consolidation, keymap modularization, default/VIA support, Vial removal,
  conventions, or verification work.

The pre-existing untracked `.agents/` tooling directory was not modified as
keyboard implementation content. OpenSpec artifacts remain in `openspec/` as
the planning and task record for this change.
