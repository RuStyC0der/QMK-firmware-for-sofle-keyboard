# Tasks

## 1. Layout remap

- [x] 1.1 In `choc/keyboard.json`, set the matrix cells of `joy-r`, `joy-d`, `joy-l`, `joy-u` to `[6,6]`, `[5,6]`, `[9,6]`, `[7,6]` and leave `joy-m` at `[8,6]`; verify `qmk info -kb rustyc0der/sofle/choc -l` lists the five cells and `mx` is unchanged.
- [x] 1.2 Build `choc:j64` and `choc:default` and verify the compiled keymap places the `RGUI(KC_*)` direction keys at the swapped cells and no keymap source was edited.

## 2. VIA definition

- [x] 2.1 In `via/sofle-choc-via.json`, swap the legends `"7,6"`↔`"9,6"` and `"5,6"`↔`"6,6"`; verify the JSON parses and a diff against `sofle-mx-via.json` shows only name, product ID, and those four legends.
- [x] 2.2 Check the Choc VIA coordinates against `qmk info -f json`; verify every coordinate exists in the layout and none is missing.

## 3. Documentation

- [x] 3.1 Update `via/README.md` and the keyboard `readme.md` with the wiring deviation, the revert procedure, and the EEPROM reset or manual reassignment step; verify the documented cells match `keyboard.json`.

## 4. Hardware validation

- [ ] 4.1 Reflash both Choc halves and reset EEPROM; verify up, down, left, right, and center each perform their own base-layer action; record the result.
- [ ] 4.2 Unlock the matrix tester and verify each physical direction highlights the matching drawn key; record the result.
