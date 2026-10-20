# Spec Delta

## Purpose

Defines how the Choc revision compensates for the five-way switch contacts that were soldered to the wrong matrix rows, so that each physical direction produces its own logical action.

## ADDED Requirements

### Requirement: Choc five-way directions follow the soldered wiring
The Choc revision SHALL map the right five-way switch so that a physical direction triggers the logical position of the same name: physical right at the `joy-r` position, down at `joy-d`, left at `joy-l`, up at `joy-u`, and center at `joy-m`. Because the contacts are wired to the swapped rows, `joy-r` SHALL use matrix cell `[6,6]`, `joy-d` `[5,6]`, `joy-l` `[9,6]`, `joy-u` `[7,6]`, and `joy-m` `[8,6]`. This mapping SHALL be expressed only in the Choc `LAYOUT`, and the shared keymaps and the MX revision SHALL be unchanged.

#### Scenario: Direction is pressed
- **WHEN** the user presses up, down, left, or right on the Choc five-way switch
- **THEN** the firmware performs the action assigned to that same direction on the active layer

#### Scenario: Center is pressed
- **WHEN** the user presses center on the Choc five-way switch
- **THEN** the firmware performs the action assigned to the center position

#### Scenario: MX is built
- **WHEN** the MX revision is built
- **THEN** its five-way matrix cells are `[5,6]` right, `[6,6]` down, `[7,6]` left, `[8,6]` center, and `[9,6]` up

### Requirement: Choc VIA definition reflects the five-way wiring
The Choc VIA definition SHALL draw the cell reported by each physical direction at that direction's position, and its five-way cells SHALL be the only cells that differ from the MX VIA layout. The wiring deviation SHALL be documented where the VIA definition and keyboard are described, together with the need to reset EEPROM or reassign the four direction cells after reflashing.

#### Scenario: Matrix tester is used
- **WHEN** the user unlocks the matrix tester and presses each physical direction on the Choc five-way switch
- **THEN** VIA highlights the key drawn at that direction

#### Scenario: Definitions are compared
- **WHEN** the layout sections of the MX and Choc VIA definitions are compared
- **THEN** they differ only in the legends of the four direction cells

#### Scenario: Definition follows the QMK layout
- **WHEN** the Choc VIA coordinates are compared with `qmk info` for the Choc revision
- **THEN** every coordinate exists in the QMK layout and none is missing
