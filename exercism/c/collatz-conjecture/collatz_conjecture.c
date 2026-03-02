#include "collatz_conjecture.h"

int steps(int start) {
  if (start < 1)
    return ERROR_VALUE;

  int num = start, c = 0;
  while (num != 1) {
    if (num % 2 == 0)
      num /= 2;
    else
      num = num * 3 + 1;
    c++;
  }
  return c;
}

// Another implementation using bitwise operators.
int steps2(int start) {
  if (start < 1)
    return ERROR_VALUE;

  int c = 0;
  while (start != 1) {
    if (!(start & 1))
      start = start >> 1;
    else
      start = start * 3 + 1;
    c++;
  }
  return c;
}
