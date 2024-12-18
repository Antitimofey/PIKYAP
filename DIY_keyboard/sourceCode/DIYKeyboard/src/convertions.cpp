#include "convertions.hpp"

/**
 * @exception returning -1 means error
 */
int convertMasterInput(int pin) {
    switch (pin)
    {
    case 15:
        return 0;
        break;

    case 14:
        return 1;
        break;

    case 6:
        return 2;
        break;

    case 5:
        return 3;
        break;

    case 16:
        return 4;
        break;

    case 10:
        return 5;
        break;

    default:
        return -1;
        break;
    }
    return -1;
}

int convertNumberToInputPin(int number) {
    switch (number)
    {
    case 0:
        return 15;
        break;

    case 1:
        return 14;
        break;

    case 2:
        return 6;
        break;

    case 3:
        return 5;
        break;

    case 4:
        return 16;
        break;

    case 5:
        return 10;
        break;

    default:
        return -1;
        break;
    }
    return -1; 
}


int convertButton(int output, int input) {
    //output = convertMasterOutput(output);
    output -= 18;

    return output*6 + input;
}