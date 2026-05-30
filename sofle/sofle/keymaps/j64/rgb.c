#define J64_GAME_LAYER 3

static void j64_apply_layer_rgb(layer_state_t state) {
    if (get_highest_layer(state) == J64_GAME_LAYER) {
        for (uint8_t i = 0; i < RGB_MATRIX_LED_COUNT; i++) {
            if (g_led_config.flags[i] != LED_FLAG_NONE) {
                rgb_matrix_set_color(i, 255, 0, 0);
            }
        }
    }
}

layer_state_t layer_state_set_user(layer_state_t state) {
    j64_apply_layer_rgb(state);
    return state;
}

bool rgb_matrix_indicators_user(void) {
    j64_apply_layer_rgb(layer_state);
    return false;
}
