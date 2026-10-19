# Tasks

## 1. Establish the Sofle family and preserve MX

- [x] 1.1 Capture the current `rustyc0der/sofle` resolved `qmk info`, generated hardware defines, lint result, and successful `default` and `j64` builds before moving files; verify the baseline records the current matrix pins, 64x128 OLED, one encoder, five-way positions, 72 RGB LEDs, and `0x0288` PID.
- [x] 1.2 Replace the buildable family-root `keyboard.json` with minimal shared family fragments and add buildable `mx` and `choc` revision directories; verify `qmk list-keyboards` contains both explicit revision paths and not revision-neutral `rustyc0der/sofle`.
- [x] 1.3 Move the existing hardware configuration, `default` keymap, `j64` keymap, display/font support, and VIA host definition into the MX revision without behavior changes; verify both MX keymaps compile, MX lint passes, and resolved MX hardware values match the task 1.1 baseline apart from the target name.
- [x] 1.4 Update the keyboard documentation with the two-revision structure, the breaking MX command migration, and correct MX build/flash commands; verify every documented MX command resolves the new target and no active example builds the revision-neutral path.

## 2. Add the Choc hardware revision

- [x] 2.1 Add the Choc data-driven ordinary matrix, right-only `GP28` seventh column, MX-compatible 64-position layout, split transport, handedness, left encoder, USB `0x0287`, and 58-LED RGB Matrix configuration; verify `qmk info -kb rustyc0der/sofle/choc` reports the Choc row pins, 10x7 matrix, one encoder, five column-6 switch positions, and `[29, 29]` LED split.
- [x] 2.2 Keep the physical 128x64 SH1107 OLED configuration shared with MX (logical 64x128 portrait framebuffer), RP2040 reset configuration without a Choc indicator LED, and an MX-equivalent `default` keymap; verify the default target compiles and its key assignments match MX while omitting `RP2040_BOOTLOADER_DOUBLE_TAP_RESET_LED`, conventional backlight, and RGB underglow.
- [x] 2.3 Update the Choc VIA host definition for the MX-compatible 64-position physical layout, one encoder, five-way switch, 10x7 matrix, and distinct USB identity; verify the JSON parses, matches the Choc QMK layout and PID, and exposes no second encoder or separate backlight control.
- [x] 2.4 Document the Choc hardware traits, build/flash commands, source-reference assumptions, and physical verification checklist; verify the documentation identifies the shared physical OLEDs, left encoder, right five-way switch, matching key assignments/graphics, 58 per-key LEDs, absent backlight circuit, and absent indicator LED.

## 3. Share and adapt the maintained j64 behavior

- [x] 3.1 Share the common `j64` declarations, tap-hold decisions, tap dance, record processing, RGB hook, custom OLED font, dog/status renderer, and girl graphic through explicit family-local modules; verify MX `j64` still compiles to its baseline hash after each moved boundary.
- [x] 3.2 Make the Choc `default` and `j64` key assignments, layers, macros, tap configuration, one-encoder map, five-way behavior, and OLED graphics match MX; verify `rustyc0der/sofle/choc:j64` compiles with VIA and exposes all 64 common physical positions.
- [x] 3.3 Verify matching dynamic behavior by checking both `j64` builds, VIA definitions, dynamic layer/macro counts, one-encoder map counts, five-way positions, shared OLED object/font, and USB identities together; confirm MX remains `0x0288`, Choc remains `0x0287`, and only revision-specific electrical values differ.

## 4. Integration and hardware validation

- [x] 4.1 Run the complete automated build matrix for `default` and `j64` on both revisions, run per-revision QMK lint plus applicable format/license checks, and verify all commands pass and produce four RP2040 UF2 images.
- [x] 4.2 Compare final resolved/generated configuration across revisions; verify common RP2040, split, handedness, serial, I2C, physical OLED, 64-position layout, one-encoder/five-way behavior, key assignments, layers, macros, and graphics agree while matrix row wiring, RGB topology, PID, and indicator capability match only their intended revision.
- [ ] 4.3 Flash both MX halves and complete its documented matrix, split, physical 128x64 SH1107 OLEDs in portrait, left encoder, five-way switch, 72-LED RGB, suspend/wake, double-tap reset, VIA remapping, and persistence checks; record each check as passing or capture any failure before marking complete.
- [ ] 4.4 Flash both Choc halves and complete its documented matrix, split, physical 128x64 SH1107 OLEDs in portrait, dog/girl graphics, left encoder, right five-way switch, 58 per-key RGB, suspend/wake, indicator-free double-tap reset, VIA remapping, and persistence checks; record each check as passing or capture any failure before marking complete.
