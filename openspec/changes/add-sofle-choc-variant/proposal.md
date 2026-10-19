# Proposal

## Why

The repository currently models the customized MX Sofle as the only buildable hardware target, even though a second PandaKB Sofle Choc shares the same RP2040 split foundation but has a different physical layout and peripheral set. Representing those hardware differences as a keymap would mix PCB capabilities with user key assignments and make it too easy to build firmware for the wrong keyboard.

## What Changes

- Reorganize `rustyc0der/sofle` as a QMK keyboard family with distinct buildable `mx` and `choc` hardware revisions and common configuration at the family level.
- Preserve the existing physical 128x64 SH1107 OLEDs (logical 64x128 portrait framebuffers), left encoder, right five-way switch, 72-LED RGB Matrix, VIA, and `j64` behavior in the `mx` revision.
- Add a `choc` revision for the PandaKB low-profile board with its six ordinary key columns plus the local right-only five-way-switch column, the same physical 128x64 SH1107 OLEDs, a left encoder, 58 per-key RGB LEDs, no separate backlight, and no bootloader indicator LED.
- Provide `default` and `j64` builds with the same physical key assignments, layers, macros, encoder map, five-way behavior, and OLED dog/girl graphics on both revisions while retaining their different matrix rows, RGB topology, USB identity, and indicator capability.
- Document how to select, build, flash, and physically verify each revision against current upstream QMK.
- **BREAKING**: Replace the current `rustyc0der/sofle` build target with explicit `rustyc0der/sofle/mx` and `rustyc0der/sofle/choc` targets so a build always names its hardware revision.

## Capabilities

### New Capabilities

- `sofle-variant-packaging`: Defines the build targets, shared configuration boundaries, supported keymaps, documentation, and upstream-QMK validation for the Sofle hardware family.
- `sofle-choc-firmware`: Defines the Choc revision's matrix, shared displays, left encoder, right five-way switch, per-key RGB hardware, absence of separate backlight and indicator LED, and matching MX key behavior.

### Modified Capabilities

None.

## Impact

- Affects the hierarchy and configuration beneath `keyboards/rustyc0der/sofle`, including keyboard metadata, hardware configuration, layouts, keymaps, and documentation.
- Changes local build and flash commands for the existing customized MX board and introduces corresponding Choc commands.
- Requires migration of variant-neutral settings to family-level fragments and variant-specific settings to buildable revision directories.
- Uses PandaKB's published Sofle Choc firmware as a hardware reference but ports the target to this repository's data-driven, upstream-QMK conventions; it does not restore Vial-fork support.
