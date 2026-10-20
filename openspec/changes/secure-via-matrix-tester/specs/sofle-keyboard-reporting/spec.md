# Spec Delta

## Purpose

Fixes the USB keyboard report mode that every Sofle revision and keymap uses, so rollover behavior is the same on all boards.

## ADDED Requirements

### Requirement: NKRO is disabled on every board
Every buildable Sofle revision and keymap SHALL be built with NKRO disabled, using the standard 6-key rollover HID report, and no board or keymap SHALL override that setting.

#### Scenario: Any revision is built
- **WHEN** `mx` or `choc` is built with the `default` or `j64` keymap
- **THEN** the resolved configuration reports NKRO as disabled

#### Scenario: More than six keys are held
- **WHEN** more than six non-modifier keys are held at once
- **THEN** the host receives at most six of them in the keyboard report

#### Scenario: A revision directory sets its own features
- **WHEN** a revision's metadata declares other features
- **THEN** it does not re-enable NKRO
