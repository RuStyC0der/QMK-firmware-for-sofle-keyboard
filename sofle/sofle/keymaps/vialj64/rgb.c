layer_state_t layer_state_set_user(layer_state_t state) {
    switch (get_highest_layer(state)) {
    case 3:
        rgb_matrix_set_color(0, 32, 0, 0);
        break;
    default: //  for any other layers, or the default layer
        rgb_matrix_set_color(0, 0,0,0);
        break;
    }
  return state;
}
