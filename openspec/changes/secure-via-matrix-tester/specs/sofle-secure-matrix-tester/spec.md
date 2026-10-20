# Spec Delta

## Purpose

Lets the owner use VIA's matrix tester on the `j64` firmware without leaving a permanently open channel that other programs on the host could use to log keystrokes.

## ADDED Requirements

### Requirement: Matrix state is withheld while locked
The `j64` firmware on both `mx` and `choc` SHALL report no key state to VIA's matrix tester while the keyboard is locked, and SHALL start locked at every power-up. The firmware SHALL NOT enable an unrestricted matrix feed.

#### Scenario: Matrix tester is enabled while locked
- **WHEN** VIA's Test matrix option is on and the keyboard is locked
- **THEN** VIA shows no pressed keys regardless of which physical keys are pressed

#### Scenario: Keyboard has just been powered
- **WHEN** the keyboard starts
- **THEN** it is locked

### Requirement: Physical unlock sequence reveals matrix state
The firmware SHALL provide a *Request Unlock* key. After it is activated, the firmware SHALL ignore normal key input until the user presses the top-left outer, top-left inner, top-right inner, and top-right outer physical matrix positions in order within 5 seconds. A correct sequence SHALL unlock the keyboard and VIA's matrix tester SHALL then show pressed keys on both halves.

#### Scenario: Correct sequence
- **WHEN** the user activates Request Unlock and presses the four positions in order within 5 seconds
- **THEN** the keyboard unlocks and VIA's matrix tester shows subsequent key presses

#### Scenario: Wrong key during the sequence
- **WHEN** the user presses any other position while the unlock is pending
- **THEN** the keyboard stays locked and the matrix tester stays empty

#### Scenario: Sequence times out
- **WHEN** 5 seconds pass after Request Unlock without a complete sequence
- **THEN** the keyboard returns to the locked state

#### Scenario: Unlock is independent of the active layer
- **WHEN** the user remaps layers in VIA
- **THEN** the same four physical positions still complete the unlock sequence

### Requirement: Unlocked state expires
The firmware SHALL relock after 60 seconds without a key press, SHALL treat each key press while unlocked as activity that restarts that period, and SHALL provide a *Lock* keycode that relocks immediately.

#### Scenario: Idle after unlock
- **WHEN** the keyboard is unlocked and no key is pressed for 60 seconds
- **THEN** it relocks and the matrix tester shows nothing

#### Scenario: Testing keeps the session open
- **WHEN** the user keeps pressing keys during a matrix test
- **THEN** the keyboard stays unlocked

### Requirement: Request Unlock key is available on the Lower layer
The compiled `j64` keymap SHALL place Request Unlock on the Lower layer at the left `T` position on both revisions, and the unlock keycode SHALL be assignable through VIA for keyboards whose stored keymap predates this change.

#### Scenario: Fresh keymap
- **WHEN** the Lower layer is active on a keyboard whose EEPROM keymap was reset
- **THEN** the key at the left `T` position requests an unlock

#### Scenario: Keyboard already holds an older VIA keymap
- **WHEN** the user assigns Request Unlock to a key through VIA
- **THEN** that key starts the unlock sequence

### Requirement: Default keymap is unaffected
The `default` keymap SHALL NOT include VIA or Secure behavior.

#### Scenario: Default keymap is built
- **WHEN** either revision is built with the `default` keymap
- **THEN** it contains no Secure feature and no unlock key
