#include "binary_search.h"

const int *binary_search(int value, const int *arr, const size_t length) {

  if (!arr || length == 0 || value < arr[0] || value > arr[length - 1])
    return NULL;

  if (length == 1)
    return arr;

  size_t start = 0, end = length, middle;

  while (start < end) {
    middle = (start + end) / 2; // half: [start, end)
    if (arr[middle] == value)
      return (const int *)(arr + middle);
    else if (arr[middle] > value)
      end = middle;
    else
      start = middle + 1;
  }

  return NULL;
}
