# Spec Delta

## Purpose

Defines a reproducible, collision-free integration with upstream QMK and the quality checks required for the custom keyboard to remain maintainable as QMK evolves.

## ADDED Requirements

### Requirement: Keyboard uses a collision-free QMK namespace
The keyboard SHALL be installed and identified as `rustyc0der/sofle` so its configuration does not inherit settings from the unrelated upstream `sofle` keyboard family.

#### Scenario: QMK resolves the keyboard
- **WHEN** QMK resolves the `rustyc0der/sofle` build target
- **THEN** the resolved processor, split serial pin, WS2812 pin, matrix pins, and metadata come from this keyboard rather than `keyboards/sofle/info.json`

### Requirement: Maintained targets compile on upstream QMK
The `j64` and default keymaps SHALL compile successfully against the documented upstream QMK baseline using QMK's pinned submodules and supported toolchain.

#### Scenario: j64 firmware build
- **WHEN** `qmk compile -kb rustyc0der/sofle -km j64` runs in the supported QMK checkout
- **THEN** the command exits successfully and produces an RP2040 UF2 firmware image

#### Scenario: Default firmware build
- **WHEN** `qmk compile -kb rustyc0der/sofle -km default` runs in the supported QMK checkout
- **THEN** the command exits successfully and produces an RP2040 UF2 firmware image

### Requirement: Keyboard passes current QMK validation
The packaged keyboard SHALL pass `qmk lint -kb rustyc0der/sofle` without keyboard or keymap errors.

#### Scenario: Full keyboard lint
- **WHEN** QMK lint checks the keyboard and every retained keymap
- **THEN** it reports a passing result with no missing metadata, invalid feature scope, duplicate defaults, formatting-policy violations, or missing license headers

### Requirement: Hardware configuration has an authoritative source
Each QMK-supported hardware or feature setting SHALL be declared in data-driven keyboard configuration when a supported schema field exists, and SHALL not be redundantly overridden in `config.h` or `rules.mk`.

#### Scenario: Resolved configuration is generated
- **WHEN** QMK generates the merged keyboard configuration
- **THEN** it reports the intended RP2040 hardware and enabled features without duplicate-setting warnings

#### Scenario: Non-data-driven option is required
- **WHEN** a required hardware option has no QMK data-driven equivalent
- **THEN** it remains in the appropriate C or make configuration file with no duplicate data-driven declaration

### Requirement: Repository documents the supported integration
The repository SHALL document the keyboard hardware, collision-free QMK installation path, supported build targets, build prerequisites, and flashing workflow.

#### Scenario: New contributor prepares a build
- **WHEN** a contributor follows the repository documentation with a current QMK checkout
- **THEN** they can install or link the keyboard at the correct path and invoke the maintained build without replacing the upstream Sofle directory

### Requirement: A default keymap is available
The keyboard SHALL include a minimal, usable QMK `default` keymap that exercises the hardware layout without enabling VIA or carrying the personal `j64` behaviors.

#### Scenario: Default keymap is inspected
- **WHEN** a contributor inspects or compiles the default keymap
- **THEN** it provides ordinary key assignments for the complete layout and keeps personal dynamic-keymap, macro, OLED-pet, and gaming-layer behavior in `j64`

### Requirement: Unsupported Vial target is absent
The upstream-QMK package SHALL NOT advertise or retain `vialj64` as a build target because Vial-fork integration is outside the supported firmware scope.

#### Scenario: Available keymaps are listed
- **WHEN** QMK lists keymaps for `rustyc0der/sofle`
- **THEN** no `vialj64` target or Vial-only definition artifacts are present

### Requirement: Source files follow QMK maintenance conventions
Retained source and configuration files SHALL use QMK-compatible formatting, SPDX-compatible licensing headers, valid include syntax, and explicit module boundaries without empty included translation units.

#### Scenario: Automated style and license checks run
- **WHEN** retained files are checked by QMK formatting, lint, and license tooling
- **THEN** no actionable convention violations are reported
