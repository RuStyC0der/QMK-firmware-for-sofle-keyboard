# Proposal

## Why

The maintained `j64` firmware builds on current QMK only when installed outside the upstream `sofle/` namespace, while the repository still contains stale configuration, lint failures, and an obsolete Vial keymap. Modernizing now establishes a reproducible upstream-QMK baseline without changing the custom 64x128 OLED, five-way switch, split, RGB, encoder, or keymap behavior.

## What Changes

- Repackage the keyboard under the collision-free `rustyc0der/sofle` QMK namespace and document the supported build workflow.
- Consolidate supported hardware and feature configuration into current data-driven QMK configuration, retaining C and make configuration only where QMK has no data-driven equivalent.
- Preserve the `j64` VIA keymap, custom tap-hold behavior, tap dance, OLED rendering, layer RGB indication, left encoder, and right five-way switch mappings.
- Add the files and metadata expected by current QMK tooling, including a keyboard README, a default keymap, licensing headers, and consistently formatted sources.
- Make current upstream QMK compilation and `qmk lint` passing verification requirements.
- **BREAKING**: Remove the obsolete `vialj64` keymap and Vial-only artifacts; support for the separate Vial firmware fork is not retained.

## Capabilities

### New Capabilities

- `custom-sofle-firmware`: Defines the custom Sofle hardware and maintained keymap behavior, including the split RP2040 hardware, 64x128 OLEDs, RGB matrix, left encoder, right five-way switch, VIA, and custom key behaviors.
- `upstream-qmk-compatibility`: Defines how the keyboard is packaged, built, linted, and documented against current upstream QMK without inheriting an unrelated upstream keyboard configuration.

### Modified Capabilities

None.

## Impact

- Affects the keyboard directory layout and build identifier, hardware configuration, `j64` keymap sources, and project documentation.
- Changes the supported build target from an ambiguous `sofle/sofle` placement to `rustyc0der/sofle:j64` and a corresponding default-keymap target.
- Removes the unmaintained `vialj64` directory and its Vial-specific JSON/configuration files.
- Requires a current upstream QMK checkout and its pinned submodules for verification; no QMK core changes are required.
