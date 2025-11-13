void suspend_wakeup_init_user(void) {
    if (layer_state_is(3)) {
        rgb_matrix_set_color(0, 32, 0, 0);
    }
}