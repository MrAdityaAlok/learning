#include "luhn.h"

#include <stddef.h>
#include <string.h>

bool luhn(const char *num) {
  size_t len = strlen(num);

  if (len <= 1)
    return false;

  const char *c = num;

  for (; *c; c++);

  size_t sum = 0, p = 0;

  for (--c; c >= num; c--) {
    unsigned char n = *c - '0';
    if (n > 9) { // not a number.
      if (*c == ' ')
        continue;
      return false;
    }
    if ((++p & 1) == 0) { // same as ++p % 2 == 0.
      n = n > 4 ? n * 2 - 9 : n * 2;
    }
    sum += n;
  }

  // p > 1: did we find more than one digit?
  return p > 1 && sum % 10 == 0;
}
