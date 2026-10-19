# VIA host definition

The maintained host-side definitions are not compiled into QMK:

- `sofle-mx-via.json` is for `rustyc0der/sofle/mx:j64`. Its companion
  `sofle-mx-keyboard-layout.json` is the Keyboard Layout Editor source used to
  maintain its physical layout.
- `sofle-choc-via.json` is for `rustyc0der/sofle/choc:j64`. It describes the
  Choc 10x7 matrix, left encoder, and right five-way switch and exposes RGB
  Matrix controls only.

To use the definition:

1. Flash the `j64` firmware on both halves and connect the keyboard.
2. Open a VIA client, enable the Design tab in VIA's settings, and open that
   tab.
3. Choose **Load Draft Definition** and select the JSON matching the firmware.
4. Return to Configure. VIA should identify **Sofle RGB Custom** for MX or
   **Sofle Choc** for Choc and expose five dynamic layers, macros, RGB Matrix
   controls, and the matching encoder map.

The definition's `0xFC32:0x0288` USB identity, 10x7 matrix, and five right-side
seventh-column switch positions must remain synchronized with
`keyboards/rustyc0der/sofle/mx/keyboard.json`.

The Choc definition's `0xFC32:0x0287` USB identity, 10x7 matrix, single encoder
push position, and five right-side seventh-column switch positions must remain
synchronized with `keyboards/rustyc0der/sofle/choc/keyboard.json`. It
intentionally has no conventional backlight menu or indicator LED.
