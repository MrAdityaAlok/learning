#include "perfect_numbers.h"

kind classify_number(int n) {
  // clang-format off
  if (n < 1) return ERROR;
  // clang-format on

  int sum = 0, pair;

  for (int i = 1; i * i < n; i++) {
    if (n % i == 0) {
      pair = n / i;
      sum = sum + i + (pair != n ? pair : 0);
    }
  }

  return n < sum   ? ABUNDANT_NUMBER
         : n > sum ? DEFICIENT_NUMBER
                   : PERFECT_NUMBER;
}
