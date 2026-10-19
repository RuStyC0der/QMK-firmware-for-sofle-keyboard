// Copyright 2026 RustyC0der
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once

#include QMK_KEYBOARD_H

enum layer_names {
    _BASE,
    _RAISE,
    _LOWER,
    _GAME,
};

enum custom_keycodes {
    M0 = SAFE_RANGE,
};

enum tap_dance_keycodes {
    BSK_PRI_SEARCH,
};

extern tap_dance_action_t tap_dance_actions[BSK_PRI_SEARCH + 1];

extern bool isSneaking;
extern bool isJumping;
extern bool showedJump;
