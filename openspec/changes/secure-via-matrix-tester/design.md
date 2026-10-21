# Design

## Context

QMK `0.34.7` (commit `180f394b`) answers VIA's matrix-state request with zeros unless `VIA_INSECURE` is defined, or `SECURE_ENABLE` is on and the keyboard is unlocked. In Secure, an unlock request clears held keys and layers, ignores all key input, and checks each press against a configured matrix sequence until it completes, fails, or times out. QMK never calls `secure_activity_event()` itself, so the 60 s idle timeout otherwise counts from unlock regardless of typing. See proposal.md for motivation.

MX and Choc share the same 10x7 matrix and key coordinates, so a single physical layout serves both VIA definitions. NKRO was set in the family `info.json` and again in `mx/keyboard.json`; Choc inherits the family value.

## Goals / Non-Goals

**Goals:**
- A matrix tester that works on demand and is closed otherwise.
- Identical behavior on `mx` and `choc`.
- One NKRO setting that no revision can silently override.

**Non-Goals:**
- Real encryption or protection against someone with physical access; Secure only gates software access.
- Securing other VIA or HID functions.
- Changing the `default` keymap, which has no VIA.
- Supporting the Vial fork.

## Decisions

- **Secure instead of `VIA_INSECURE`.** `VIA_INSECURE` is two lines but leaves the keystroke feed open permanently. Secure costs one key and a short sequence per session. Accepted because the keyboard is used daily and the tester only occasionally.
- **Enable it in the `j64` keymaps, not the family.** Secure is only meaningful with VIA, which only `j64` enables. The `default` keymap stays minimal. Keymap `rules.mk` and `config.h` are already duplicated between revisions, so the settings are duplicated the same way.
- **Unlock sequence `{0,0}, {0,5}, {5,5}, {5,0}`.** The four top-row outer and inner positions across both halves. Matrix coordinates are physical, so layer remaps cannot break it. Crossing both halves also proves the split link carries key state. The default 5 s unlock timeout is kept; a wrong key relocks.
- **`SE_REQ` on the Lower layer at the left `T` position (matrix `[1,5]`).** That slot was unassigned (`XXXXXXX`), is reachable one-handed with the existing Lower layer-tap, and is out of the way of typing. Request Unlock fires on release, which also avoids the layer-tap interfering because Secure clears layers when the request starts.
- **Refresh the idle timer from `process_record_user`.** Without it a long test session relocks 60 s after unlock even while keys are pressed. The call sits behind `#ifdef SECURE_ENABLE` in the shared `j64/process_record.c`, so it costs nothing in builds without Secure. Alternative: raise `SECURE_IDLE_TIMEOUT`, which relocks later but still not while in use, and leaves the keyboard open longer when idle.
- **NKRO off at the family level, override removed.** Setting `"nkro": false` in the family `info.json` and deleting the MX `true` leaves one source of truth. Merely flipping the MX value would also work but keep two places to drift apart.
- **Choc VIA layout copied from MX.** The previous hand-built Choc grid was not derived from the QMK layout. Reusing the MX layout guarantees identical key positions and coordinates. Only name and product ID differ, which the VIA README now states.

## Risks / Trade-offs

- [VIA stores the keymap in EEPROM, so `SE_REQ` does not appear on an already-flashed keyboard] → Document the EEPROM reset and the manual `0x7C63` assignment in VIA.
- [Unlock timeout of 5 s may be tight for the four-key sequence] → Practice once; raise `SECURE_UNLOCK_TIMEOUT` if it proves awkward.
- [Activity refresh lets normal typing hold the keyboard open indefinitely] → Acceptable: unlock needs a physical sequence, and `SE_LOCK` relocks on demand.
- [6KRO drops keys beyond six when gaming] → Intentional per the proposal; modifiers are not counted against the limit.
- [Two Choc/MX VIA files could drift] → The README states that layout changes go in both; task 3.2 compares them.
- [Secure puts input on hold while pending] → A wrong key or the timeout releases it, and held keys and layers are cleared on entry to avoid stuck keys.

## Migration Plan

1. Build and flash both halves with the new `j64` firmware.
2. Reset EEPROM (or assign `0x7C63` in VIA) so the Request Unlock key is present.
3. Reload the Choc VIA draft definition if it was loaded before.

Rollback: revert the `SECURE_ENABLE` and `SECURE_UNLOCK_SEQUENCE` lines, the `SE_REQ` key, and the activity call, then reflash.

## Open Questions

- Whether to keep `SE_REQ` where it is after a few weeks of use; moving it later only edits the keymap.
