/* Copyright 2020 Josef Adamcik
 * Modification for VIA support and RGB underglow by Jens Bonk-Wiltfang
 * Modification for Vial support by Drew Petersen
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

// clang-format off

#include QMK_KEYBOARD_H
#include "oled.c"
#include "process_record.c"
#include "tap_hold.c"

// Default keymap. This can be changed in Vial. Use oled.c to change beavior that Vial cannot change.

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
/*
 * QWERTY
 */

[0] = LAYOUT(
  QK_GESC,    KC_1,         KC_2,         KC_3,         KC_4,           KC_5,             RGUI(KC_RIGHT),  KC_6,         KC_7,           KC_8,         KC_9,         KC_0,              KC_GRV,
  QK_GESC,    KC_Q,         KC_W,         KC_E,         KC_R,           KC_T,             RGUI(KC_DOWN),   KC_Y,         KC_U,           KC_I,         KC_O,         KC_P,              KC_BSPC,
  KC_TAB,     LGUI_T(KC_A), LALT_T(KC_S), LSFT_T(KC_D), LCTL_T(KC_F),   KC_G,             RGUI(KC_LEFT),   KC_H,         RCTL_T(KC_J),   RSFT_T(KC_K), LALT_T(KC_L), RGUI_T(KC_SCLN),   KC_QUOT,
  KC_LSFT,    KC_Z,         KC_X,         KC_C,         KC_V,           KC_B,   KC_MUTE,  RGUI(KC_PGUP),   KC_N,         KC_M,           KC_COMM,      KC_DOT,       KC_SLSH,           KC_RSFT,
              KC_LGUI,      KC_LALT,      KC_LCTL,      LT(1, KC_SPC),  KC_SPC,           RGUI(KC_UP),     KC_ENT,       LT(2, KC_ENT),  KC_RALT,      M0,           KC_RCTL
),
/*
 * RAISE
 */
[1] = LAYOUT(
  KC_F1,     KC_F2,          KC_F3,      KC_F4,          KC_F5,             KC_F6,                          XXXXXXX,    KC_F7,       KC_F8,       KC_F9,      KC_F10,          KC_F11,     KC_F12,
  KC_GRV,    KC_1,           KC_2,       KC_3,           KC_4,              KC_5,                           XXXXXXX,    KC_6,        KC_7,        KC_8,       KC_9,            KC_0,       KC_BSPC,
  KC_MINUS,  LSFT(KC_1),     LSFT(KC_2), LSFT(KC_3),     LSFT(KC_4),        LSFT(KC_5),                     XXXXXXX,    LSFT(KC_6),  LSFT(KC_7),  LSFT(KC_8), LSFT(KC_9),      LSFT(KC_0), LSFT(KC_BSLS),
  _______,   LSFT(KC_MINUS), KC_EQUAL,   LSFT(KC_EQUAL), LSFT(KC_LBRC),     LSFT(KC_RBRC), _______,         XXXXXXX,    KC_LBRC,     KC_RBRC,     KC_SCLN,    LSFT(KC_SCLN),   KC_BSLS,    _______,
             _______,        _______,    _______,        _______,           _______,                        XXXXXXX,    _______,     _______,     _______,    _______,          _______
),
/*
 * LOWER
 */
[2] = LAYOUT(
  _______, _______, _______, _______, _______,  _______,                  KC_MNXT,  _______, _______, _______, _______,  _______, KC_WSCH,
  _______, KC_INS,  KC_PSCR, KC_APP,  XXXXXXX,  XXXXXXX,                  KC_VOLD,  KC_PGUP, KC_HOME, KC_UP,   KC_END,   _______, _______,
  _______, KC_LGUI, KC_LALT, KC_LSFT, KC_LCTL,  KC_CAPS,                  KC_MPRV,  KC_PGDN, KC_LEFT, KC_DOWN, KC_RGHT,  KC_DEL,  _______,
  _______, KC_UNDO, KC_CUT,  KC_COPY, KC_PASTE, XXXXXXX,   _______,       KC_MPLY,  XXXXXXX, _______, XXXXXXX, _______,  XXXXXXX, _______,
                    _______, _______, _______,  _______,   _______,       KC_VOLU,  _______, _______, _______, _______,  TG(3)
),
/*
 * GAME
 */

[3] = LAYOUT(
  KC_KP_4,  QK_GESC,  KC_1,     KC_2,     KC_3,    KC_4,                  XXXXXXX,   KC_5,    _______,  _______,  _______,  _______,  _______,
  KC_KP_3,  QK_GESC,  KC_Q,     KC_W,     KC_E,    KC_R,                  XXXXXXX,   KC_T,    _______,  _______,  _______,  _______,  _______,
  KC_KP_2,  KC_TAB,   KC_A,     KC_S,     KC_D,    KC_F,                  XXXXXXX,   KC_G,    _______,  _______,  _______,  _______,  _______,
  KC_KP_1,  KC_LSFT,  KC_Z,     KC_X,     KC_C,    KC_V,    _______,      XXXXXXX,   KC_B,    _______,  _______,  _______,  _______,  _______,
            XXXXXXX,  KC_LALT,  KC_LCTL,  KC_KP_0, KC_SPC,                XXXXXXX,   KC_ENT,  _______,  _______,  _______,  TG(3)
)
};

const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][2] = {
    [0] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU)},
    [1] = { ENCODER_CCW_CW(KC_BRID, KC_BRIU)},
    [2] = { ENCODER_CCW_CW(KC_TRNS, KC_TRNS)},
    [3] = { ENCODER_CCW_CW(KC_TRNS, KC_TRNS)},
};
