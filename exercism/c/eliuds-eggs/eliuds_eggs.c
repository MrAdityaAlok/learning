#include "eliuds_eggs.h"

unsigned int egg_count(unsigned int displayed_value) {
  int eggs = 0;
  while (displayed_value) {
    eggs += displayed_value % 2;
    displayed_value = displayed_value / 2;
  }
  return eggs;
}
