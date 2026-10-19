# Spec Delta

## Purpose

Defines the hardware integration and maintained firmware behavior for the RP2040-based custom Sofle with 64x128 OLEDs and a right-hand five-way switch.

## ADDED Requirements

### Requirement: Custom split matrix is preserved
The firmware SHALL scan the five-row split matrix using the configured RP2040 row and column pins, including a seventh right-hand column for all five positions of the five-way switch and no seventh left-hand column.

#### Scenario: Five-way switch input
- **WHEN** any direction or center position of the right-hand five-way switch is pressed
- **THEN** the firmware reports the key assigned to the corresponding right-hand matrix position

#### Scenario: Ordinary key scanning
- **WHEN** a key on either half is pressed
- **THEN** the firmware reports the key at the matching matrix position without a phantom seventh-column input on the left half

### Requirement: Split transport and handedness remain functional
The firmware SHALL use the existing serial connection and handedness pin so either RP2040 half identifies its side and exchanges the state required by the configured keymap, OLED, and lighting behaviors.

#### Scenario: Both halves are connected
- **WHEN** the two halves are connected and either half is attached to the host
- **THEN** key events from both halves and synchronized display state are available to the primary half

### Requirement: Custom OLED hardware is supported
The firmware SHALL drive the SH1107 64x128 OLED hardware over the configured I2C bus on both halves and retain the existing `j64` rendering behavior.

#### Scenario: Keyboard starts normally
- **WHEN** either half initializes with its OLED connected
- **THEN** the display uses the 64x128 SH1107 geometry and renders the content assigned to that half

#### Scenario: OLED timeout
- **WHEN** keyboard inactivity exceeds the configured OLED timeout
- **THEN** the display enters the QMK OLED timeout state without disrupting keyboard input

### Requirement: RGB matrix hardware and layer indication are preserved
The firmware SHALL control 72 WS2812 LEDs as two groups of 36, retain the configured default lighting behavior, and indicate the gaming layer using the existing red layer indication.

#### Scenario: Normal layer lighting
- **WHEN** the gaming layer is inactive
- **THEN** the RGB matrix uses the configured normal color and enabled effects

#### Scenario: Gaming layer lighting
- **WHEN** the gaming layer becomes active
- **THEN** the layer indication changes the intended keyboard lighting to red

### Requirement: Encoder and five-way mappings remain available
The firmware SHALL preserve the left rotary encoder mappings and the right five-way switch mappings across the maintained keymap layers.

#### Scenario: Base-layer encoder rotation
- **WHEN** the left encoder is rotated on the base layer
- **THEN** the firmware sends volume down or volume up according to direction

#### Scenario: Base-layer directional switch
- **WHEN** a five-way direction is pressed on the base layer
- **THEN** the firmware sends the corresponding window-management shortcut

### Requirement: Maintained j64 key behavior is preserved
The maintained keymap SHALL provide its base, raise, lower, and game layers, home-row mod-taps, layer-tap Space and Enter keys, tap dance, Caps Word, macro, and per-key tap-hold decisions.

#### Scenario: Layer-tap key is tapped
- **WHEN** the user taps either maintained layer-tap key within its configured tapping behavior
- **THEN** the key sends Space or Enter as assigned

#### Scenario: Layer-tap key is held
- **WHEN** the user holds either maintained layer-tap key or presses another key during its hold decision
- **THEN** the corresponding raise or lower layer becomes active according to the configured per-key tap-hold policy

#### Scenario: Gaming layer is selected
- **WHEN** the user toggles the gaming layer
- **THEN** the home-row keys use their non-mod-tap gaming assignments and the gaming layer can be toggled off again

### Requirement: VIA remapping remains supported
The maintained firmware SHALL expose the dynamic keymap and encoder-map functionality required by VIA while preserving a usable compiled default keymap.

#### Scenario: Firmware is opened in VIA
- **WHEN** a host VIA client connects to the keyboard
- **THEN** the client can read and update the supported dynamic keymap layers and macros

#### Scenario: Dynamic configuration is absent
- **WHEN** the keyboard starts with reset or uninitialized dynamic keymap storage
- **THEN** the compiled maintained keymap provides the default assignments
