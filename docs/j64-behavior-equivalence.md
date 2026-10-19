# j64 behavior-equivalence check

The modularized `j64` keymap was compared with source commit
`7a3d4aead48098b272ed894bf2f3bcc2c5cc87ff` and the preserved user edits, then
compiled successfully on the documented upstream QMK baseline.

- The full keymap and encoder-map initializer is byte-identical:
  SHA-256 `0f3428bf9d502d139bf2a64c43461606e282658a5b836773bd756aceffbf0198`.
- The OLED implementation and all bitmap arrays are byte-identical after
  ignoring the newly added shared-header include and an insignificant trailing
  blank line: SHA-256
  `1b8a8fa05f3621975900976a8e31f643f62bbd50063632c9f28407d6313bc78a`.
- The per-key tap-hold implementation is byte-identical after ignoring its new
  shared-header include: SHA-256
  `3059c5e4a807c85da9f59a25c2c0a711ef7f5d61d3be9a517d1573733e093c1c`.
- Four keymap layers and all four encoder-map layers remain defined.
- The base and game layers retain all five right-switch shortcuts, the base
  encoder remains volume down/up, and the raise encoder remains brightness
  down/up.
- Home-row mod-taps, Space/Enter layer-taps, 200 ms default tapping term,
  250 ms layer-tap term, 170 ms Shift mod-tap term, and 50 ms quick-tap terms
  remain unchanged.
- Tap dance, Caps Word, WPM, VIA, encoder maps, and the red `_GAME` RGB Matrix
  indicator are enabled in `j64`.
- `M0` retains the user-owned `SS_DELAY(50)` between GUI-down and Space.

The only structural changes are declarations moved to `j64.h`, modules compiled
through `SRC`, and use of the named `_GAME` layer constant instead of literal
layer number 3.
