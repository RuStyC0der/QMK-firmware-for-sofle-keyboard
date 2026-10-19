# Spec Delta

## Purpose

Defines the hardware integration and maintained firmware behavior for the PandaKB RP2040 Sofle Choc with portrait 128x64 OLEDs, a left encoder, a right five-way switch, and per-key RGB lighting.

## ADDED Requirements

### Requirement: Choc split matrix is scanned correctly
The Choc revision SHALL scan five rows per half using row pins `GP5`, `GP6`, `GP7`, `GP8`, and `GP9`, six ordinary-key columns on `GP27`, `GP26`, `GP22`, `GP20`, `GP23`, and `GP21`, and `COL2ROW` diodes. The left seventh column SHALL be unpopulated, while the right half SHALL use `GP28` as a seventh column for its five-way switch.

#### Scenario: Any Choc key is pressed
- **WHEN** a physical key on either Choc half is pressed
- **THEN** the firmware reports the key assigned to its corresponding matrix position

### Requirement: Choc split transport and handedness are supported
The Choc revision SHALL use the RP2040 vendor serial transport on `GP1` and the active-low handedness input on `GP4` so either connected half identifies its side and exchanges required state.

#### Scenario: Both Choc halves are connected
- **WHEN** either half is attached to the host with the split cable connected
- **THEN** key, layer, modifier, display, lighting, and WPM state required by the selected keymap is available across both halves

### Requirement: Choc OLED hardware is supported
The Choc revision SHALL drive the same physical 128x64 SH1107 OLED displays as MX over I2C1 using `GP2` for SDA and `GP3` for SCL on both halves. Because the modules are mounted in portrait, QMK SHALL use a logical 64x128 framebuffer.

#### Scenario: Choc firmware starts with displays connected
- **WHEN** either half initializes normally
- **THEN** its OLED uses the 128x64 physical panel with the 64x128 portrait framebuffer and renders the content assigned to that half

#### Scenario: OLED timeout expires
- **WHEN** keyboard inactivity exceeds the configured timeout
- **THEN** both displays enter the QMK OLED timeout state without disrupting keyboard input

### Requirement: Choc encoder and five-way switch are available
The Choc revision SHALL expose the left encoder on `GP28` and `GP29`. It SHALL expose the right five-way switch at right-half matrix positions `[5,6]` through `[9,6]`, using the same logical positions and key assignments as MX.

#### Scenario: Left encoder is rotated
- **WHEN** the user rotates the left encoder
- **THEN** the firmware sends the same action assigned to the MX encoder for that direction and active layer

#### Scenario: VIA changes an encoder mapping
- **WHEN** a supported encoder action is remapped through VIA
- **THEN** the left encoder uses the persisted dynamic mapping after restart

#### Scenario: Five-way direction is pressed
- **WHEN** the user presses any direction or center on the Choc right five-way switch
- **THEN** the firmware reports the same matrix position and logical action as MX

### Requirement: Choc per-key RGB is supported without separate backlight
The Choc revision SHALL control 58 WS2812 per-key RGB LEDs as two groups of 29 through `GP0`, and SHALL NOT enable a separate QMK backlight or RGB-underglow feature.

#### Scenario: RGB Matrix is enabled
- **WHEN** the Choc firmware initializes normally
- **THEN** all 58 per-key LEDs are addressable by the configured RGB Matrix effects

#### Scenario: Lighting is suspended
- **WHEN** the host suspends the keyboard
- **THEN** per-key RGB enters the configured sleep state without relying on a separate backlight circuit

### Requirement: Choc firmware does not require an indicator LED
The Choc revision SHALL support RP2040 double-tap reset without assigning or driving a bootloader indicator LED pin.

#### Scenario: Double-tap reset enters the bootloader
- **WHEN** the Choc controller receives the configured double-tap reset sequence
- **THEN** it enters the RP2040 bootloader without attempting to signal through `GP17` or another indicator LED

### Requirement: Maintained Choc key behavior is available
The Choc `default` and `j64` targets SHALL use the same compiled key assignments as their MX counterparts. Choc `j64` SHALL retain the same base, raise, lower, and game layers, home-row mod-taps, layer-tap Space and Enter keys, tap dance, Caps Word, macros, encoder map, five-way behavior, VIA dynamic keymap configuration, OLED dog animation, and OLED girl graphic.

#### Scenario: Shared typing behavior is used
- **WHEN** the user activates a maintained key behavior on a physical position common to both revisions
- **THEN** the Choc target produces the same logical action as the MX target

#### Scenario: Shared five-way positions are exposed
- **WHEN** the Choc keymap is inspected or opened in VIA
- **THEN** it exposes the same 64 physical positions and five-way matrix assignments as MX, under the Choc USB identity

#### Scenario: OLED graphics are rendered
- **WHEN** Choc `j64` runs with both halves connected
- **THEN** the primary half renders the same dog and status artwork as MX and the secondary half renders the same girl graphic as MX
