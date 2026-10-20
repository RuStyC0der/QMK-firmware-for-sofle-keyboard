# Proposal

## Why

On the built Choc board the right five-way switch was soldered with its direction contacts on the wrong rows. Physical up reports as left, left as up, down as right, and right as down; center is correct. Every five-way action therefore fires from the wrong direction, and VIA's matrix tester lights the wrong cell. The direction contacts share rows with ordinary keys, so the fault cannot be corrected by changing matrix pins.

## What Changes

- Swap the matrix coordinates of the four direction entries in the Choc `LAYOUT` so each physical direction lands on its own logical `joy-*` position: `joy-r` `[6,6]`, `joy-d` `[5,6]`, `joy-l` `[9,6]`, `joy-u` `[7,6]`, `joy-m` unchanged at `[8,6]`.
- Apply the same swap to the Choc VIA definition so the matrix tester and key editor draw each physical direction where it is.
- Document the wiring deviation in the VIA README and keyboard readme so it is removed if the switch is resoldered.
- No keymap, `j64` source, or MX change. The shared keymaps pass the five-way keys positionally, so the `LAYOUT` remap carries them.

## Capabilities

### New Capabilities

- `sofle-choc-five-way-wiring`: Defines how the Choc revision maps its miswired five-way switch contacts to logical directions, and how the Choc VIA definition reflects that.

### Modified Capabilities

None. There are no main specs yet. This change narrows two in-flight requirements, listed under Impact.

## Impact

- Affects `keyboards/rustyc0der/sofle/choc/keyboard.json`, `via/sofle-choc-via.json`, `via/README.md`, and the keyboard `readme.md`.
- Narrows `add-sofle-choc-variant` ("Choc encoder and five-way switch are available": five-way uses the same matrix assignments as MX) and `secure-via-matrix-tester` ("Choc VIA layout matches the MX layout": differs only in name and product ID). The Choc layout now differs from MX by exactly the four direction cells. Reconcile those requirements when archiving.
- Requires reflashing both halves. VIA keeps the active keymap in EEPROM per matrix cell, so an already-flashed keyboard keeps the old assignments until an EEPROM reset or manual reassignment of the four direction cells.
