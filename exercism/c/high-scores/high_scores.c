#include "high_scores.h"
#include <string.h>

// Descending order insertion sort. Best for n ~20.
static void sort(int32_t *arr, size_t arr_len) {
  int32_t temp;
  for (size_t i = 1; i < arr_len; i++) {
    for (size_t j = i; j > 0; j--) {
      if (arr[j - 1] >= arr[j])
        break;
      temp = arr[j - 1];
      arr[j - 1] = arr[j];
      arr[j] = temp;
    }
  }
}

int32_t latest(const int32_t *scores, size_t scores_len) {
  return scores[scores_len - 1];
}

int32_t personal_best(const int32_t *scores, size_t scores_len) {
  int32_t sorted_scores[scores_len];

  memcpy(sorted_scores, scores, scores_len * sizeof(int32_t));
  sort(sorted_scores, scores_len);

  return sorted_scores[0];
}

size_t personal_top_three(const int32_t *scores, size_t scores_len,
                          int32_t *output) {
  int32_t sorted_scores[scores_len];

  memcpy(sorted_scores, scores, scores_len * sizeof(int32_t));
  sort(sorted_scores, scores_len);

  size_t i = 0;

  for (; i < (3 < scores_len ? 3 : scores_len); i++) {
    output[i] = sorted_scores[i];
  }

  return i;
}
