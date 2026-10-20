# Design

## Context

The Choc right five-way switch is scanned as a seventh right-half column on `GP28`, one direction per matrix row: `[5,6]` right, `[6,6]` down, `[7,6]` left, `[8,6]` center, `[9,6]` up. Observed behavior after assembly, with VIA's matrix tester:

| physical press | reported cell | firmware name today |
|---|---|---|
| up | `[7,6]` | left |
| left | `[9,6]` | up |
| down | `[5,6]` | right |
| right | `[6,6]` | down |
| center | `[8,6]` | center |

The mapping is two swaps (up/left and down/right), so the correction is its own inverse. Rows `GP5`-`GP9` also scan the ordinary right-half keys, so the direction contacts cannot be re-pinned. See proposal.md for motivation.

## Goals / Non-Goals

**Goals:**
- Each physical direction triggers the action assigned to that direction.
- No change to the keymaps, shared `j64` sources, or MX.
- VIA shows each physical press at the matching drawn position.

**Non-Goals:**
- Fixing the solder joints or adding a matrix remap in C.
- Changing the five-way assignments themselves.

## Decisions

- **Swap `matrix` coordinates in the Choc `LAYOUT`.** The generated `LAYOUT` macro maps argument position to matrix cell, and both keymaps pass the five-way keys positionally. Changing which cell `joy-u` etc. point at therefore routes the existing assignments with no keymap edit, and keeps the wiring quirk in the file that already describes Choc hardware. Alternatives:
  - Remap cells in C at scan time. Rejected: adds Choc-only code for a data problem, and no clean hook exists after the matrix scan runs.
  - Swap keycodes in the Choc `keymap.c`. Rejected: breaks the shared-assignments rule, and VIA would still draw the wrong cell for each press.
- **Mirror the swap in the Choc VIA definition.** VIA addresses keys by matrix cell, so with the layout swapped the drawn legends at `[7,6]`/`[9,6]` and `[5,6]`/`[6,6]` must trade places for the tester and editor to match the hardware. Only these four legend strings change; positions, sizes, and the name/product ID handling are untouched.
- **The Choc layout now differs from MX by the four direction cells.** MX keeps the original assignment. The deviation is recorded in the readmes so reverting is four numbers in `keyboard.json` plus the four legends in the VIA file.

## Risks / Trade-offs

- [EEPROM keeps the old per-cell keymap, so nothing changes after flashing] -> Document the EEPROM reset and the manual VIA reassignment of the four cells.
- [Reading "up-left" as reported→physical versus physical→reported] -> The mapping is an involution, so both readings give the same fix; verify on hardware anyway.
- [Choc and MX VIA layouts now differ] -> The README names the exception so a future layout sync does not undo it.
- [Resoldering later leaves the swap in place and inverts the switch] -> The readmes say to revert the swap together with the hardware fix.
