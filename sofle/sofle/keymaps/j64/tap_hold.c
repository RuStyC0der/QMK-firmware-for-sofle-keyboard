
bool get_hold_on_other_key_press(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case LT(1, KC_SPC):
            // Immediately select the hold action when another key is pressed.
            return true;
        case LT(2, KC_ENT):
            // Immediately select the hold action when another key is pressed.
            return true;            
        default:
            // Do not select the hold action when another key is pressed.
            return false;
    }
}

uint16_t get_quick_tap_term(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case LT(1, KC_SPC):
            return 50;
        case LT(2, KC_ENT):
            return 50; 
        default:
            return QUICK_TAP_TERM;
    }
}

uint16_t get_tapping_term(uint16_t keycode, keyrecord_t *record) {

    switch (keycode) {
        case LT(1, KC_SPC):
            return 250;
        case LT(2, KC_ENT):
            return 250; 
        default:
            return TAPPING_TERM;
    }
}