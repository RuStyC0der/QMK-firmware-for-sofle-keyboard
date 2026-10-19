# Design

## Context

See `proposal.md` for motivation and the two capability specs for required behavior. The audit verified upstream QMK `0.34.7` at commit `180f394b489c238cb231c2bf8b080262155e03c0`: `j64` builds as `rustyc0der/sofle`, but `sofle/sofle` inherits incompatible `D2`/`D3` settings from upstream Sofle. Current sources also mix data-driven and legacy configuration, include C fragments directly, lack a pristine default keymap, and retain a Vial target that fails on upstream QMK.

The working tree already contains user changes to the matrix row pins, the `M0` delay, and removal of the `j64` suspend hook. Those changes are inputs to the migration and must not be overwritten.

## Goals / Non-Goals

**Goals:**

- Make the repository mirror a collision-free QMK keyboard path that can be linked into a clean QMK checkout.
- Preserve hardware and `j64` behavior while making generated configuration the authoritative verification surface.
- Separate reusable keymap modules with explicit declarations and normal QMK compilation.
- Leave QMK lint and both supported builds clean on the audited upstream baseline.

**Non-Goals:**

- Supporting the Vial firmware fork or retaining the `vialj64` target.
- Modifying QMK core, the upstream `keyboards/sofle` family, PCB wiring, key positions, artwork, or OLED graphics.
- Migrating VIA to its future external module before upstream QMK removes the current compatibility implementation.
- Claiming physical-hardware validation from compile-only checks; final flashing and input/display testing remain a hardware verification step.

## Decisions

### Mirror the QMK vendor namespace in the repository

Move the keyboard to `keyboards/rustyc0der/sofle`. A development checkout links `qmk_firmware/keyboards/rustyc0der` to this repository's `keyboards/rustyc0der`, producing the build identifier `rustyc0der/sofle` without replacing or nesting beneath upstream Sofle.

Alternatives considered:

- `sofle/sofle`: rejected because parent `info.json` values override the RP2040 serial and WS2812 pins in the audited build.
- Replacing `qmk_firmware/keyboards/sofle`: rejected because it deletes or masks an upstream keyboard family and makes updates unsafe.
- External Userspace only: rejected because QMK External Userspace supports external keymaps but does not provide this custom keyboard definition.

### Make `keyboard.json` authoritative for supported data-driven fields

Use `keyboard.json` for processor, bootloader, feature enablement, matrix pins, encoder, RGB matrix, WS2812, split enablement, right-side matrix pins, serial driver/pin, handedness pin, and transport synchronization. Express pins consistently as `GP<n>` strings while retaining `null` for the unused left seventh column.

Remove default-valued properties and the disabled `rgblight` configuration. Keep only options without current schema mappings in C configuration: handedness pin polarity, USB VBUS detection, RP2040 double-tap reset details, I2C driver/pins, the 64x128 SH1107 geometry, and any required RP2040 PIO selection. Retain only I2C1 in `mcuconf.h` because the OLED bus uses `I2CD1`.

Feature scope follows ownership: hardware-dependent features remain at keyboard level; VIA, WPM, tap dance, Caps Word, dynamic keymap sizing, encoder maps, and tap-hold policy remain in `j64`.

Alternative considered: leave working values in `rules.mk` and `config.h`. Rejected because it preserves stale defines and prevents JSON from being the single inspectable source of hardware truth.

### Keep a pristine default keymap and a personal j64 keymap

Add `keymaps/default` as a small conventional keymap covering every physical position with ordinary QWERTY/navigation/media assignments. It will not enable VIA or include the OLED pet, macros, gaming behavior, or personal tap-hold rules. `j64` remains the supported personal/VIA firmware and retains its current behavior.

Alternative considered: alias or copy `j64` as `default`. Rejected because current QMK guidance expects a pristine default keymap and excludes VIA from it; copying would also create two independently maintained copies of personal behavior.

### Compile j64 modules normally with a shared header

Replace direct `#include "*.c"` composition with QMK `SRC +=` entries for the retained modules and introduce a keymap-local header for shared enums, state declarations, and function prototypes. Keep the large OLED bitmap data intact. Remove the empty `suspend.c`; RGB layer state is refreshed through the retained RGB Matrix indicator hook.

Alternative considered: keep direct C-file inclusion. It currently builds, but hides dependencies in include order, prevents independent translation-unit checks, and works against explicit module ownership.

### Retain upstream VIA compatibility and isolate tooling artifacts

Continue using `VIA_ENABLE = yes` for the audited upstream baseline while QMK's transition compatibility remains available. Keep the current VIA definition as a documented host-tool artifact outside the compiled keymap directory, correct its displayed keyboard name, and remove obsolete Vial definitions and flags.

Alternative considered: adopt the announced external VIA module immediately. Rejected because the current upstream checkout still provides the compatibility implementation and the module transition is not required to satisfy the build contract.

### Treat QMK output as a migration equivalence check

Before moving files, capture resolved `qmk info` values and the successful `j64` build. After migration, compare the resolved processor, pins, matrix dimensions, feature flags, RGB counts/layout, split synchronization, USB identifiers, and dynamic keymap settings. Compile `default` and `j64`, run lint, and use QMK's formatting/license checks. Physical verification then flashes both halves and exercises every hardware-specific input/output.

## Risks / Trade-offs

- [Configuration consolidation silently changes a generated define] -> Compare pre/post resolved QMK info and generated configuration for every hardware-critical value before accepting the build.
- [Moving the directory breaks existing local build commands] -> Document the new identifier and symlink layout prominently; retain no ambiguous compatibility alias that would reintroduce upstream inheritance.
- [Separate C compilation exposes hidden include-order dependencies] -> Introduce a shared header and migrate one module at a time, compiling after each dependency boundary is made explicit.
- [A clean build misses electrical or display regressions] -> Add a manual two-half hardware checklist covering matrix keys, all five switch positions, encoder, both OLEDs, RGB, suspend/wake, and VIA persistence.
- [Deleting `vialj64` affects an undocumented user] -> Mark the removal as breaking and preserve its history in Git; restoring it requires a separately scoped Vial-fork compatibility change.
- [Future VIA removal in QMK breaks `VIA_ENABLE`] -> Document the audited QMK baseline and track the external-module migration separately when upstream compatibility is actually removed.

## Migration Plan

1. Record the current dirty-file diff and verified `j64` baseline so user changes and expected hardware values are preserved.
2. Move the keyboard into `keyboards/rustyc0der/sofle` and update documentation/build identifiers before changing configuration semantics.
3. Consolidate data-driven configuration, then compare resolved QMK information and compile before deleting redundant legacy settings.
4. Add the pristine default keymap and refactor `j64` into explicit modules without changing its layout or bitmap data.
5. Relocate the VIA host definition, remove `vialj64`, add licensing/formatting fixes, and update documentation.
6. Run clean builds, lint, formatting/license checks, and resolved-configuration comparisons on the upstream baseline.
7. Flash both halves and complete the manual hardware checklist when the keyboard is available.

Rollback is a Git revert of the migration commits. The QMK checkout integration can be rolled back independently by removing the `keyboards/rustyc0der` development link; the upstream checkout itself remains unmodified apart from generated build outputs and initialized submodules.
