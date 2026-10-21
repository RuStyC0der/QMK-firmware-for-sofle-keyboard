# Proposal

## Why

VIA's matrix tester shows no keystrokes on the `j64` firmware. Current upstream QMK deliberately returns an empty matrix to VIA unless the firmware opts in, because an unrestricted matrix feed lets any local program with raw-HID access log keystrokes. The Choc VIA definition also draws a hand-built key grid that does not match the MX board even though both boards share one physical layout, and NKRO is enabled although the boards should report with standard rollover.

## What Changes

- Build the `j64` keymap on both `mx` and `choc` with QMK Secure so VIA's matrix tester works only after a deliberate physical unlock, instead of enabling the always-open insecure matrix feed.
- Define a four-key unlock sequence on the physical matrix, put a *Request Unlock* key on the Lower layer, and refresh the idle timeout on key presses so a test session is not cut off mid-use.
- Disable NKRO for every board by setting it at the family level and removing the MX override.
- Replace the Choc VIA key layout with the MX definition's layout, keeping only the Choc name and USB product ID.
- Document the unlock procedure and the VIA definition relationship.
- **BREAKING**: Keyboards report with 6KRO instead of NKRO, so more than six simultaneously held non-modifier keys are no longer all reported.

## Capabilities

### New Capabilities

- `sofle-secure-matrix-tester`: Defines when VIA's matrix tester may read key state, and how the user unlocks, relocks, and times out that access.
- `sofle-keyboard-reporting`: Defines the USB keyboard report mode shared by every Sofle revision and keymap.
- `sofle-via-definitions`: Defines how the maintained VIA host definitions relate to the QMK physical layouts.

### Modified Capabilities

None. There are no main specs yet; the in-flight `add-sofle-choc-variant` change is not modified.

## Impact

- Affects `keyboards/rustyc0der/sofle/info.json`, `mx/keyboard.json`, the `j64` keymap `rules.mk`, `config.h`, and `keymap.c` for both revisions, and `j64/process_record.c`.
- Replaces `via/sofle-choc-via.json` and updates `via/README.md` and the keyboard `readme.md`.
- Requires reflashing both halves. Because VIA keeps the active keymap in EEPROM, the new Request Unlock key reaches an already-flashed keyboard only after an EEPROM reset or a manual VIA assignment.
- Adds no dependencies and does not change the `default` keymap, which has no VIA.
