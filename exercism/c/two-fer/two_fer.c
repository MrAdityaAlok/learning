#include "two_fer.h"
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 100

void two_fer(char *buffer, const char *name) {
  if (snprintf(buffer, BUFFER_SIZE, "One for %s, one for me.",
               name ? name : "you") < 0) {
    exit(EXIT_FAILURE); // Encoding error.
  }
}
