#include "Keyboard.h"

int layers[1][24] = {0};
int time[3] = {0}; // last time then modifier key was pressed

void initializeLayers(bool IS_MASTER) {
    if (IS_MASTER) {
        layers[0][0] = ' ';
        layers[0][1] = KEY_TAB;
        layers[0][2] = KEY_LEFT_SHIFT;
        layers[0][3] = KEY_KP_ENTER; // or '\n'?
        layers[0][4] = KEY_CAPS_LOCK; // encoder`s button
        layers[0][5] = KEY_LEFT_GUI; // = fn + LEFT_ARROW
        layers[0][6] = 'b';
        layers[0][7] = 'v';
        layers[0][8] = 'c';
        layers[0][9] = 'x';
        layers[0][10] = 'z';
        layers[0][11] = KEY_LEFT_ALT;
        layers[0][12] = 'g';
        layers[0][13] = 'f';
        layers[0][14] = 'd';
        layers[0][15] = 's';
        layers[0][16] = 'a';
        layers[0][17] = KEY_LEFT_CTRL; // cant reach this key, copied to key_5
        layers[0][18] = 't';
        layers[0][19] = 'r';
        layers[0][20] = 'e';
        layers[0][21] = 'w';
        layers[0][22] = 'q';
        layers[0][23] = '`';
    }
}
