// Copyright 2025 PandaKB
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once

#define SPLIT_HAND_PIN_LOW_IS_LEFT
#define USB_VBUS_PIN GP19
#define SERIAL_PIO_USE_PIO0

/* Both revisions replace the right encoder with a five-way matrix switch. */
#define NUM_ENCODERS_RIGHT 0

/* Reset. */
#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET
#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET_TIMEOUT 1000U

#ifdef OLED_ENABLE
#    define I2C_DRIVER I2CD1
#    define I2C1_SDA_PIN GP2
#    define I2C1_SCL_PIN GP3
#    define OLED_DISPLAY_64X128
#    define OLED_IC OLED_IC_SH1107
#    define OLED_FONT_H "lib/glcdfont.c"
#    define OLED_BRIGHTNESS 180
#    define OLED_TIMEOUT 60000
#endif
