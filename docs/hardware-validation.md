# Manual hardware validation

Use the final verified revision-specific `j64` UF2 on both halves. Record the
date, QMK commit, firmware checksum, host OS, and result of every item before
accepting the migration. These checks require physical keyboards and therefore
remain incomplete after compile-only validation.

## Common connection and behavior

- [ ] Flash the same matching UF2 onto both RP2040 halves, with the split cable
  disconnected during flashing.
- [ ] Connect the split cable, attach USB to the left half, and confirm that both
  halves type and neither controller enters the bootloader.
- [ ] Repeat with USB on the right half to confirm handedness and primary-side
  selection.
- [ ] Test Space and Enter as taps and held layer keys, home-row mods, tap dance,
  Caps Word, the delayed `M0` shortcut, and entering/exiting the gaming layer.
- [ ] Leave the board idle for more than 60 seconds, verify both OLEDs time out,
  and wake them with a keypress.
- [ ] Suspend and wake the host. Confirm input, both displays, and RGB Matrix
  resume without changing the active layer.
- [ ] Double-tap reset on each half and confirm entry into the RP2040 bootloader.
- [ ] Load the matching VIA JSON, confirm all five dynamic layers and the
  expected encoder map, remap a harmless key and encoder direction, power-cycle,
  and verify persistence before restoring the compiled defaults.

## MX revision (`rustyc0der/sofle/mx:j64`)

- [ ] Flash both halves with the MX UF2 and confirm USB PID `0x0288`.
- [ ] Test all ordinary keys and the five right-side seventh-column matrix
  positions without phantom presses.
- [ ] Test the right five-way switch: up, down, left, right, and center.
- [ ] Rotate and press the left encoder; confirm base-layer volume and
  raise-layer brightness directions.
- [ ] Confirm both physical 128x64 SH1107 OLEDs initialize in portrait with the
  logical 64x128 framebuffer and render the full primary/secondary j64 content
  and pet animation.
- [ ] Exercise all 72 per-key RGB Matrix LEDs (36 per half), then verify the
  gaming-layer red indication and its restoration after suspend/wake.
- [ ] Confirm the GP17 reset indicator operates during double-tap reset.

## Choc revision (`rustyc0der/sofle/choc:j64`)

- [ ] Flash both halves with the Choc UF2 and confirm USB PID `0x0287`.
- [ ] Test every ordinary key and all five positions on the right-only seventh
  column; confirm the 10x7 VIA matrix produces no phantom presses.
- [ ] Test the right five-way switch: up, down, left, right, and center, and
  confirm its assignments match MX on every maintained layer.
- [ ] Rotate and press the left encoder, checking both directions on every
  maintained layer against the shared MX encoder map.
- [ ] Confirm both physical 128x64 SH1107 OLEDs initialize in portrait with the
  logical 64x128 framebuffer, with the same dog/status artwork on the primary
  half and girl graphic on the secondary half as MX.
- [ ] Exercise all 58 fitted per-key RGB Matrix LEDs (29 per half), then verify
  the gaming-layer red indication and its restoration after suspend/wake.
- [ ] Confirm there is no conventional backlight/underglow control in VIA and no
  separate backlight circuit illuminates; the 58 per-key LEDs are RGB Matrix.
- [ ] During double-tap reset, confirm bootloader entry succeeds without relying
  on or attempting to drive an indicator LED, because none is physically fitted.
