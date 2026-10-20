# Tasks

## 1. Disable NKRO everywhere

- [x] 1.1 Set `"nkro": false` in the family `info.json` and remove the `"nkro": true` override from `mx/keyboard.json`; verify `qmk info -kb rustyc0der/sofle/mx -km j64` and the `choc` equivalent report NKRO disabled.
- [x] 1.2 Update the docs that list NKRO as enabled (`docs/baseline-configuration.md`, `docs/post-consolidation-configuration.md`) and note the 6KRO behavior in the keyboard readme; verify no active doc still claims NKRO is enabled.
- [x] 1.3 Build all four targets and verify each generated `info_rules.mk` contains `NKRO_ENABLE ?= no`.

## 2. Secure matrix tester

- [x] 2.1 Add `SECURE_ENABLE = yes` to both `j64` keymap `rules.mk` files and the unlock sequence to both `config.h` files; verify `qmk info` for each revision reports Secure enabled with the sequence `[[0,0],[0,5],[5,5],[5,0]]`.
- [x] 2.2 Place `SE_REQ` on the Lower layer at the left `T` position in both `j64` keymaps and add the activity refresh to `j64/process_record.c`; verify both `j64` targets compile without warnings and the `default` keymaps contain no Secure feature.
- [x] 2.3 Document the unlock procedure, the EEPROM-reset or `0x7C63` step, and the lock timing in the keyboard readme and `via/README.md`; verify the documented key positions match the `LAYOUT` and the matrix coordinates in `config.h`.

## 3. Choc VIA layout

- [x] 3.1 Replace `via/sofle-choc-via.json` with the MX layout, changing only name (`Sofle Choc`) and product ID (`0x0287`); verify the JSON parses and its `layouts` section equals the MX definition's.
- [x] 3.2 Update `via/README.md` to say the layouts are shared and must be edited together; verify the README matches the files.
- [x] 3.3 Check each VIA definition's coordinates against `qmk info -f json` for its revision; verify every VIA key exists in the QMK layout and none is missing.

## 4. Integration and hardware validation

- [x] 4.1 Build `default` and `j64` for `mx` and `choc` in the Docker toolchain and run `qmk lint` for both; verify all four builds link and lint passes.
- [ ] 4.2 Flash both halves of each board, reset EEPROM, and verify with the matrix tester that it stays empty while locked, shows both halves after the unlock sequence, relocks after 60 s idle and on `SE_LOCK`, and stays empty after a wrong key; record each result.
- [ ] 4.3 Load the Choc draft definition in VIA and verify it draws the same key arrangement as the MX definition, with all keys, the encoder, and the five-way switch selectable; record the result.
- [ ] 4.4 Confirm in a keyboard tester that at most six non-modifier keys are reported on each board; record the result.
