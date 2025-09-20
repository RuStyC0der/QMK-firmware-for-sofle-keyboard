
#define HOLD_ON_OTHER_KEY_PRESS_PER_KEY

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