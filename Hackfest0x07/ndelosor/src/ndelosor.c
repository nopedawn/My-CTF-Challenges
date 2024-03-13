#include <stdio.h>
#include <string.h>

void hexStringToByteArray(const char *hexString, unsigned char *byteArray) {
    for (size_t i = 0, j = 0; i < strlen(hexString); i += 2, ++j) {
        sscanf(hexString + i, "%2hhx", &byteArray[j]);
    }
}

void xorEncrypt(unsigned char *message, size_t message_length, const char *key) {
    size_t key_length = strlen(key);
    for (size_t i = 0, j = 0; i < message_length; ++i, ++j) {
        j = (j == key_length) ? 0 : j;
        message[i] ^= key[j];
    }
}

int main() {
    unsigned char encrypted_message[] = {
        0x11, 0x0e, 0x16, 0x4b, 0x0b, 0x0c, 0x14, 0x1c, 0x44, 0x58, 0x52, 0x52, 0x5b, 0x03, 0x18, 0x1b, 
        0x16, 0x10, 0x2d, 0x0b, 0x5a, 0x09, 0x48, 0x28, 0x18, 0x55, 0x1a, 0x54, 0x47, 0x06, 0x02, 0x11, 
        0x1f, 0x2a, 0x08, 0x43, 0x1a, 0x58, 0x1b, 0x5e, 0x52, 0x36, 0x1e, 0x5b, 0x1f, 0x55, 0x2b, 0x06, 
        0x1d, 0x47, 0x52, 0x36, 0x07, 0x11, 0x04, 0x5b, 0x50, 0x7f, 0x55, 0x38, 0x11
    };

    char key[] = "You might be wondering what the question is.. this is the only way to get the answer, so what is your answer?";

    size_t message_length = sizeof(encrypted_message) / sizeof(encrypted_message[0]);

    xorEncrypt(encrypted_message, message_length, key);

    char user_input[100];
    printf("%s \nInput: ", key);
    fgets(user_input, sizeof(user_input), stdin);
    user_input[strcspn(user_input, "\n")] = '\0';

    if (strncmp(user_input, (char *)encrypted_message, message_length) == 0) {
        printf("Nice!\n");
        printf("%s\n", user_input);
    } else {
        printf("Sorry mate! I appreciate that\n");
    }

    return 0;
}
