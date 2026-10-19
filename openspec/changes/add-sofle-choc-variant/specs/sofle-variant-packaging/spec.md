# Spec Delta

## Purpose

Defines how the related MX and Choc Sofle hardware revisions are selected, built, documented, and validated without treating physical hardware as a keymap choice.

## ADDED Requirements

### Requirement: Hardware revisions have explicit build targets
The firmware SHALL expose `rustyc0der/sofle/mx` and `rustyc0der/sofle/choc` as distinct buildable keyboards, and SHALL NOT expose the revision-neutral `rustyc0der/sofle` path as a buildable target.

#### Scenario: MX target is selected
- **WHEN** QMK resolves `rustyc0der/sofle/mx`
- **THEN** it selects the large-display, five-way-switch MX hardware configuration

#### Scenario: Choc target is selected
- **WHEN** QMK resolves `rustyc0der/sofle/choc`
- **THEN** it selects the low-profile Choc hardware configuration with a left encoder and right five-way switch

### Requirement: Both revisions provide supported keymaps
Each buildable revision SHALL provide a conventional `default` target and a maintained `j64` target appropriate to that revision's physical layout and peripherals.

#### Scenario: Supported build matrix is compiled
- **WHEN** the `default` and `j64` keymaps are compiled for both revisions
- **THEN** all four builds complete successfully and produce RP2040 UF2 firmware images

### Requirement: Shared behavior does not erase hardware differences
The revisions SHALL share compatible configuration, OLED hardware and graphics, physical layout positions, encoder/five-way behavior, layers, macros, and key assignments while retaining revision-specific matrix row wiring, RGB topology, USB identity, and indicator capability.

#### Scenario: Resolved revision information is inspected
- **WHEN** QMK reports the resolved configuration for each revision
- **THEN** common split settings agree and each hardware-specific value matches only the selected revision

#### Scenario: Maintained keymap behavior is compared
- **WHEN** the `j64` keymaps are exercised on their matching revisions
- **THEN** shared typing, layer, tap-hold, macro, Caps Word, and VIA behavior remains equivalent for common physical keys

### Requirement: Existing MX behavior is preserved
The MX revision SHALL retain the current physical 128x64 SH1107 OLEDs using logical 64x128 portrait framebuffers, 72-LED RGB Matrix, left encoder, right five-way switch, split behavior, and maintained keymap semantics.

#### Scenario: MX migration is verified
- **WHEN** the new MX target is compared with the pre-migration `rustyc0der/sofle:j64` build
- **THEN** its resolved hardware configuration and observable keyboard behavior are unchanged apart from the build identifier

### Requirement: Variant family passes upstream QMK validation
Both revisions and all retained keymaps SHALL compile and pass QMK lint against the documented upstream QMK baseline without inheriting unrelated upstream Sofle settings.

#### Scenario: Full family validation runs
- **WHEN** compilation and lint checks run for the Sofle family
- **THEN** both revisions pass with no keyboard or keymap errors and resolve configuration only from the `rustyc0der/sofle` family

### Requirement: Revision selection is documented
The repository SHALL document the hardware traits, build identifiers, build commands, flashing process, and physical verification checklist for both revisions.

#### Scenario: Contributor identifies a target
- **WHEN** a contributor compares their keyboard with the documented variants
- **THEN** they can select and build the matching revision without using a keymap to choose hardware
