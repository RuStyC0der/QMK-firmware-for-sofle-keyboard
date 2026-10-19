# Tasks

## 1. Preserve the Verified Baseline

- [x] 1.1 Record the existing dirty-file diff, current source commit, upstream QMK commit, successful `j64` build command, UF2 checksum, and hardware-critical `qmk info` values in a migration note; verify the note includes the user's row-pin edits, `M0` delay, and empty `j64/suspend.c` change.
- [x] 1.2 Add a pre-migration configuration snapshot suitable for comparison during implementation; verify it captures processor/bootloader, USB IDs, matrix and split pins, encoder pins, WS2812 pin, RGB counts, OLED/I2C settings, and enabled `j64` features.

## 2. Establish Collision-Free Keyboard Packaging

- [x] 2.1 Move the keyboard sources into `keyboards/rustyc0der/sofle` while preserving Git history and all baseline changes; verify QMK lists `rustyc0der/sofle` when the repository's `keyboards/rustyc0der` directory is linked into the QMK checkout.
- [x] 2.2 Add the keyboard-level `readme.md` with hardware support, availability/reference links, `rustyc0der/sofle` build commands, safe symlink installation, flashing instructions, and the upstream QMK baseline; verify every documented shell command resolves the new path without replacing `qmk_firmware/keyboards/sofle`.
- [x] 2.3 Remove documentation and integration references to `sofle/sofle`; verify a repository search finds no supported build instruction using the collision-prone identifier.

## 3. Consolidate Hardware Configuration

- [x] 3.1 Expand `keyboard.json` to own all supported data-driven processor, bootloader, feature, matrix, split, serial, handedness, encoder, RGB Matrix, and WS2812 settings; verify `qmk info -kb rustyc0der/sofle -f json` resolves the baseline hardware values without inheriting `D2` or `D3`.
- [x] 3.2 Remove duplicate/default/disabled data-driven values and obsolete board-level feature flags from `rules.mk` and `config.h`; verify QMK emits no duplicate-setting warnings and `qmk lint -kb rustyc0der/sofle` reports none of the prior duplicate-default or invalid keyboard-level Combo errors.
- [x] 3.3 Keep only non-data-driven RP2040, handedness-polarity, USB VBUS, I2C, and 64x128 SH1107 options in C configuration, reduce `mcuconf.h` to required I2C peripherals, and correct the `halconf.h` include form; verify generated configuration contains `GP1` serial, `GP0` WS2812, `GP4` handedness, `I2CD1` on `GP2`/`GP3`, and the 64x128 SH1107 defines.
- [x] 3.4 Compile `rustyc0der/sofle:j64` immediately after configuration consolidation; verify it produces a UF2 and compare the post-migration configuration snapshot against task 1.2 with no unexplained hardware-critical differences.

## 4. Modernize and Preserve Keymaps

- [x] 4.1 Add a pristine `default` keymap with ordinary assignments for every layout position and no VIA or personal behavior; verify `qmk compile -kb rustyc0der/sofle -km default` succeeds and its rules do not enable VIA, WPM pet rendering, tap dance, or gaming-layer logic.
- [x] 4.2 Introduce a shared `j64` header and compile retained modules through keymap `SRC` entries instead of including C files from `keymap.c`; verify each module compiles as a separate translation unit and `keymap.c` contains no direct `.c` includes.
- [x] 4.3 Preserve the `j64` layer layout, five-way switch shortcuts, encoder mappings, home-row mods, layer-tap timing, tap dance, Caps Word, RGB gaming indication, OLED bitmap/rendering data, and delayed `M0` macro; verify the compiled keymap data and relevant constants match the baseline and all four encoder-map layers remain defined.
- [x] 4.4 Remove the empty `j64/suspend.c` module and confirm the RGB Matrix indicator hook restores the correct layer color after initialization and wake; verify the build has no suspend source reference and the manual validation checklist includes suspend/wake on the gaming layer.
- [x] 4.5 Relocate the maintained VIA host definition outside the compiled keymap directory, correct the displayed `RGB` name, and document how to load it; verify its VID, PID, matrix dimensions, and layout match `keyboard.json` and VIA can still be enabled only by `j64`.
- [x] 4.6 Remove `vialj64`, Vial-only JSON, and ignored Vial/QMK Settings flags; verify `qmk list-keymaps -kb rustyc0der/sofle` reports only retained upstream-QMK targets and a repository search finds no `VIAL_ENABLE`, `VIAL_INSECURE`, `VIALRGB_ENABLE`, or `QMK_SETTINGS` assignment.

## 5. Apply QMK Source and Documentation Conventions

- [x] 5.1 Add accurate SPDX-compatible copyright/license headers to every retained C and header file flagged by QMK lint; verify `qmk license-check` or the applicable QMK lint checks report no missing headers for `rustyc0der/sofle`.
- [x] 5.2 Format retained JSON, C, header, and make files with QMK tooling while preserving intentionally protected keymap layout and bitmap blocks; verify dry-run format commands produce no diff.
- [x] 5.3 Update the repository README for the new source layout, maintained `default`/`j64` targets, VIA-versus-Vial support boundary, and 64x128/five-way hardware differences; verify its links and build commands point to files and targets that exist.
- [x] 5.4 Add a manual hardware validation checklist covering both matrix halves, all five switch positions, left encoder, both OLEDs, all 72 RGB LEDs, layer indication, VIA persistence, OLED timeout, and suspend/wake; verify every hardware scenario in `custom-sofle-firmware` maps to a checklist item.

## 6. Integration Verification

- [x] 6.1 From a clean upstream QMK build state, compile both `rustyc0der/sofle:default` and `rustyc0der/sofle:j64`; verify both commands exit successfully and produce RP2040 UF2 images without compiler or generated-configuration warnings.
- [x] 6.2 Run `qmk lint -kb rustyc0der/sofle`, QMK formatting dry runs, and the applicable license check; verify every command passes and record the commands and QMK commit in the migration note.
- [x] 6.3 Compare final `qmk info` output with the baseline snapshot and inspect the retained VIA definition; verify all hardware-critical values and maintained dynamic-keymap settings match the specifications.
- [x] 6.4 Review the final Git diff for accidental changes to matrix wiring, USB IDs, RGB coordinates, OLED graphics, or user-owned baseline edits; verify every remaining difference maps to this change's proposal, design, or tasks.

## Workflow follow-up

- Flash both halves with the verified `j64` UF2 and execute the documented manual hardware validation checklist on the physical keyboard.
- Archive the OpenSpec change after implementation review and physical validation are accepted.
