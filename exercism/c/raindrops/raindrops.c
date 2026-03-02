#include "raindrops.h"
#include <stdio.h>
#include <string.h>

void convert(char result[], int drops) {
  // clang-format off
  if (drops % 3 == 0) strcat(result, "Pling");
  if (drops % 5 == 0) strcat(result, "Plang");
  if (drops % 7 == 0) strcat(result, "Plong");
  if (!*result) sprintf(result, "%d", drops);
  // clang-format on
}
