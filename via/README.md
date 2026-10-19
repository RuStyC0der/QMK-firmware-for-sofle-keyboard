# VIA host definition

`sofle-via.json` is the maintained host-side definition for the
`rustyc0der/sofle:j64` firmware. It is not compiled into QMK. The companion
`sofle-keyboard-layout.json` is the Keyboard Layout Editor source used to
maintain its physical layout.

To use the definition:

1. Flash the `j64` firmware on both halves and connect the keyboard.
2. Open a VIA client, enable the Design tab in VIA's settings, and open that
   tab.
3. Choose **Load Draft Definition** and select `sofle-via.json`.
4. Return to Configure. VIA should identify **Sofle RGB Custom** and expose five
   dynamic layers, macros, RGB Matrix controls, and the encoder map.

The definition's `0xFC32:0x0288` USB identity, 10x7 matrix, and five right-side
seventh-column switch positions must remain synchronized with
`keyboards/rustyc0der/sofle/keyboard.json`.
