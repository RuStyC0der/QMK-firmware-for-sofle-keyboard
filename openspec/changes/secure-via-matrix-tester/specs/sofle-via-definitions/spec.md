# Spec Delta

## Purpose

Keeps the maintained VIA host definitions consistent with the physical layout of the boards they describe, so the VIA editor draws each keyboard faithfully.

## ADDED Requirements

### Requirement: Choc VIA layout matches the MX layout
The Choc VIA definition SHALL describe the same physical key layout as the MX VIA definition, covering the same 64 key positions, matrix coordinates, encoder, and right five-way switch, and SHALL differ from it only in keyboard name and USB product ID.

#### Scenario: Definitions are compared
- **WHEN** the layout sections of the MX and Choc VIA definitions are compared
- **THEN** they are identical

#### Scenario: Choc definition is loaded
- **WHEN** the Choc definition is loaded as a draft in VIA
- **THEN** VIA identifies the keyboard as Sofle Choc with product ID `0x0287` and draws the same key arrangement as MX

### Requirement: Definitions follow the QMK layout
Each VIA definition's matrix size, USB identity, and key matrix coordinates SHALL match its revision's QMK layout, and a layout change SHALL be applied to both definitions.

#### Scenario: Matrix coordinates are checked
- **WHEN** a definition's key coordinates are compared with `qmk info` for its revision
- **THEN** every VIA coordinate exists in the QMK layout and no QMK key is missing
