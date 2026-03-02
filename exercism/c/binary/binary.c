#include "binary.h"
#include <stddef.h>

int convert(const char *input) {
  int decimal = 0;

  for (size_t i = 0; input[i] != '\0'; i++) {
    if (input[i] != '0' && input[i] != '1')
      return INVALID;

    decimal = decimal * 2 + (input[i] == '0' ? 0 : 1);
  }

  return decimal;
}
