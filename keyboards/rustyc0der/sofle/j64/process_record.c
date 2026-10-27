// Copyright 2025 RustyC0der
// SPDX-License-Identifier: GPL-2.0-or-later

#include "j64.h"

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
#ifdef SECURE_ENABLE
    // Keep an unlocked VIA matrix tester session alive while keys are being used.
    if (record->event.pressed) {
        secure_activity_event();
    }
#endif
    switch (keycode) {
        case KC_LCTL:
        case KC_RCTL:
            if (record->event.pressed) {
                isSneaking = true;
            } else {
                isSneaking = false;
            }
            break;
        case KC_SPC:
            if (record->event.pressed) {
                isJumping  = true;
                showedJump = false;
            } else {
                isJumping = false;
            }
            break;
        case M0:
            if (record->event.pressed) {
                SEND_STRING(SS_DOWN(X_LGUI) SS_DELAY(50) SS_TAP(X_SPACE) SS_DELAY(30) SS_UP(X_LGUI));
            } else {
                // when keycode QMKBEST is released
            }
            break;
    }
    return true; // Let QMK send the enter press/release events
}
