# Manual hardware validation

Use the final verified `j64` UF2 on both halves. Record the date, QMK commit,
firmware checksum, host OS, and the result of each item before accepting the
migration. These checks require the physical keyboard and are intentionally not
marked complete by the compile-only migration.

## Firmware and connection

- [ ] Flash the same verified `rustyc0der/sofle:j64` UF2 onto both RP2040 halves.
- [ ] With the interconnect attached and USB connected to the left half, confirm
  that both halves type and neither controller enters the bootloader.
- [ ] Repeat with USB connected to the right half to confirm handedness and
  primary-side selection.

## Inputs

- [ ] Test every ordinary matrix key on the left half.
- [ ] Test every ordinary matrix key on the right half and confirm the unused
  left seventh column produces no phantom presses.
- [ ] Test the right five-way switch separately: up, down, left, right, and
  center. On the base layer, confirm the assigned window-management shortcuts.
- [ ] Rotate the left encoder both directions on every maintained layer; confirm
  base-layer volume and raise-layer brightness behavior.
- [ ] Test Space and Enter as both taps and held layer keys, including chords
  that exercise per-key hold-on-other-key-press behavior.
- [ ] Test home-row mods, tap dance, Caps Word, the delayed `M0` shortcut, and
  entering/exiting the gaming layer.

## Displays and lighting

- [ ] Confirm both 64x128 SH1107 OLEDs initialize in the correct orientation
  and render the expected primary/secondary content.
- [ ] Confirm the OLED pet reacts to typing and modifier state.
- [ ] Leave the keyboard inactive for more than 60 seconds and confirm both
  OLEDs enter their timeout state, then wake them with a keypress.
- [ ] Exercise all 72 RGB LEDs and inspect both 36-LED halves for the expected
  coordinates, effects, and brightness.
- [ ] Enter the gaming layer and confirm its intended LEDs turn red; leave the
  layer and confirm normal RGB Matrix behavior resumes.
- [ ] While the gaming layer is active, suspend and wake the host. Confirm the
  keyboard resumes input, both displays resume, and the RGB Matrix indicator
  hook restores the red gaming-layer color without changing layers.

## VIA persistence

- [ ] Load the maintained VIA definition, connect to the `j64` firmware, and
  confirm all five dynamic layers and the encoder map are visible.
- [ ] Remap a harmless key and encoder direction, save or allow VIA to persist
  it, power-cycle the keyboard, and confirm both mappings remain.
- [ ] Restore the intended compiled mapping or clear dynamic keymap storage and
  confirm the compiled defaults are usable.
