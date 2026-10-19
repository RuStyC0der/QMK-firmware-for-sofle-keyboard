# Design

## Context

See `proposal.md` for motivation and the capability specs for required behavior. The current `keyboards/rustyc0der/sofle/keyboard.json` is both buildable and specific to the customized MX board: it declares a seven-column right matrix for the five-way switch, 64x128 SH1107 OLED support, one encoder, and 72 RGB Matrix LEDs. Its `j64` layout also embeds the five switch positions directly.

PandaKB's published `sofle/sofle_choc` sources describe a related RP2040 board with a 10x6 ordinary-key matrix, two encoders, and 58 per-key RGB LEDs. The local Choc build replaces the published right encoder with the same right five-way switch used by MX, wired as a right-only seventh matrix column on `GP28`. It also uses the same physical 128x64 SH1107 modules as MX; both are mounted in portrait and use QMK's logical 64x128 framebuffer. The published sources contain legacy/Vial-era configuration that must be treated as a hardware reference rather than copied. This Choc build has no physical conventional backlight and the user's controller has no `GP17` indicator LED.

QMK's current keyboard guidelines use a non-buildable parent with shared `info.json` fragments and a `keyboard.json` in each buildable revision. More-specific JSON and configuration files override parent values, making that hierarchy suitable only when the parent contains genuinely common settings.

## Goals / Non-Goals

**Goals:**

- Make the selected hardware revision explicit in every build command.
- Share only verified common RP2040, split, transport, and toolchain configuration.
- Share the identical OLED hardware and graphics, physical layout positions, input behavior, key assignments, layers, macros, and VIA behavior.
- Keep only actual hardware differences revision-specific: matrix row wiring, RGB topology, USB identity, switch type, and indicator capability.
- Preserve the current MX firmware by comparing resolved configuration and compiled behavior before and after the move.

**Non-Goals:**

- Supporting the Vial firmware fork or importing PandaKB's legacy Vial keymap unchanged.
- Making Choc versus MX switch mechanics visible to firmware when they do not affect an electrical input.
- Adding inputs or artwork not physically present on either revision.
- Changing the PCB wiring, adding an indicator or backlight circuit, or claiming physical validation from compilation alone.

## Decisions

### Use a non-buildable Sofle family with two buildable revisions

Convert `keyboards/rustyc0der/sofle` into the family root, with shared metadata/configuration fragments but no root `keyboard.json`. Add buildable `mx/keyboard.json` and `choc/keyboard.json` leaves, producing `rustyc0der/sofle/mx` and `rustyc0der/sofle/choc`.

Only processor, bootloader, diode direction, split enablement, handedness, serial transport, USB VBUS detection, I2C controller selection, and other values verified as common belong at the family level. Matrix pins and layouts remain in each revision because the current MX firmware has five-way-switch matrix additions and per-half row overrides that do not match the published Choc matrix.

Alternatives considered:

- Keep `rustyc0der/sofle` buildable and add only a `choc` child. Rejected because the child would inherit a hardware-complete parent and require fragile negation of the MX layout, indicator, RGB, and OLED settings.
- Add an unrelated `rustyc0der/sofle_choc` keyboard. It would compile, but would duplicate the shared RP2040/split foundation and obscure that these are maintained revisions of one family.
- Add a Choc keymap. Rejected because keymaps do not accurately model matrix geometry, USB identity, display hardware, encoder count, or LED topology.

### Migrate the current target to the MX revision before adding Choc behavior

Capture the current `default` and `j64` build results plus resolved `qmk info` values before moving files. Establish `rustyc0der/sofle/mx` first and require equivalent processor, matrix, split pins, display geometry, encoder, RGB layout/count, USB identifiers, and feature flags before proceeding.

The build identifier change is intentional and documented. No compatibility target remains at `rustyc0der/sofle`, because silently defaulting to one physical revision defeats explicit hardware selection.

Alternative considered: migrate both revisions simultaneously. Rejected because it would make an MX regression harder to distinguish from new Choc configuration work.

### Port Choc hardware facts into revision-owned data-driven configuration

Use PandaKB's published Choc sources as the baseline for its matrix, OLED, encoder, RGB, split, and USB values, then express every supported field in `keyboard.json`. Retain C or make configuration only where the audited QMK schema has no equivalent.

The Choc revision uses its published six ordinary-key columns, five rows, left encoder, and 58-LED split RGB Matrix. The local right five-way switch uses `GP28` as a seventh column, replacing the published right encoder and matching MX matrix positions `[5,6]` through `[9,6]`. Choc retains PandaKB's `0x0287` product ID while MX retains `0x0288`. Conventional backlight and RGB underglow remain disabled. RP2040 double-tap reset remains enabled, but Choc does not define `RP2040_BOOTLOADER_DOUBLE_TAP_RESET_LED`.

Alternative considered: derive Choc by overriding the MX JSON wholesale. Rejected because object/array merge behavior could retain an MX-only matrix position, RGB entry, or feature; both revision files should be independently inspectable hardware truth.

### Keep layouts and peripheral presentation revision-specific

Each revision retains an independently inspectable hardware definition and VIA identity, but both expose the same 64 layout positions: ordinary keys, the left encoder button, and five right-hand switch positions. Their `default` and `j64` assignments, single-encoder map, layers, macros, and five-way behavior match.

The common OLED hardware configuration describes the physical 128x64 SH1107 module as a logical 64x128 portrait framebuffer. A shared renderer and font provide the same animated dog/status screen on the primary half and girl graphic on the secondary half. The common `j64` behavior retains layer, tap-hold, macro, Caps Word, tap-dance, dynamic-keymap, encoder, and five-way semantics.

Separate VIA JSON definitions describe each product ID, physical layout, matrix, and encoder count. The existing MX definition is updated for the new target name; a Choc definition is added rather than making one conditional definition represent both devices.

### Share behavior through explicit modules, not copied keymaps

Move shared `j64` declarations, tap-hold decisions, tap dance, custom key processing, layer identifiers, OLED implementation, font, and lighting hook into explicit family-local modules. Each revision retains a keymap entry point using its own data-driven `LAYOUT`, but the compiled assignments and peripheral map match.

Compile the shared sources normally through QMK's source list and a shared header. Do not include C files directly or make the conventional `default` keymaps compile personal behavior modules.

Alternative considered: duplicate all of `j64` under both revisions. Rejected because fixes to tap-hold and macro behavior would drift. A single conditional `keymap.c` was also rejected because its preprocessor branches would hide two materially different physical layouts in one file.

### Verify generated configuration before hardware testing

Use `qmk info`, generated configuration, four supported builds, and per-revision lint as the automated acceptance surface. Compare MX against its captured baseline and Choc against the hardware contract in `sofle-choc-firmware/spec.md`. Physical validation then flashes both halves of each board and exercises every matrix position, split transport, displays, encoders or five-way switch, RGB LEDs, suspend/wake, reset, and VIA persistence.

## Risks / Trade-offs

- [Moving the root target breaks existing scripts and saved commands] -> Mark the change as breaking and document exact replacements using `/mx` or `/choc`.
- [Parent configuration leaks an MX-only setting into Choc] -> Keep the parent minimal and diff each revision's resolved `qmk info` and generated defines, including an explicit absence check for the Choc indicator LED.
- [The published PandaKB firmware is stale or differs from the physical Choc board] -> Treat it as a reference, compare its pins and counts with the user's board before flashing, and require a two-half hardware checklist after compile validation.
- [The matching `j64` copies drift] -> Verify the two keymap/config files remain identical and share OLED, font, lighting, tap-hold, tap-dance, and macro modules directly.
- [Different USB identities or VIA definitions lose existing EEPROM mappings] -> Keep the current MX VID/PID unchanged, use the Choc's distinct PID, document that dynamic mappings are device-specific, and test reset plus persistence separately.
- [A clean compile misses electrical or orientation errors] -> Treat compilation as configuration validation only and retain explicit physical tests for every revision-specific device.

## Migration Plan

1. Record the current MX dirty-state check, `qmk info`, lint result, and successful `default`/`j64` builds.
2. Create the family-level shared fragments and move the existing hardware definition into the `mx` revision without changing its resolved values.
3. Move the MX keymaps and VIA definition to the explicit target, compile and lint it, and compare it with the baseline.
4. Add the data-driven Choc hardware definition from the verified PandaKB electrical values plus the local `GP28` five-way column, use the OLED hardware shared with MX, and explicitly omit the indicator LED and separate backlight features.
5. Add matching Choc `default` and `j64` assignments, the shared dog/girl renderer, the single-encoder/five-way map, and the separate Choc VIA identity; extract their common behavior and graphics into shared modules.
6. Run resolved-configuration comparisons, all four builds, full family lint, formatting, licensing, and VIA-definition validation.
7. Flash and test both halves of the MX and Choc boards using the documented hardware checklists.

Rollback is a Git revert of the family migration, which restores `rustyc0der/sofle` as the sole buildable target. Previously flashed MX firmware remains usable; Choc firmware can be replaced by flashing both halves with the last known-good image.
