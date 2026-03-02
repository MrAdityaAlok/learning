#include "leap.h"
#include <stdbool.h>

bool leap_year(int year) {
  return year % 4 != 0 ? false : (year % 100 != 0 ? true : year % 400 == 0);
}
