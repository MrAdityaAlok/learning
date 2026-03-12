#include "high_scores.h"

int32_t latest(const int32_t *const scores, const size_t scores_len) {
  return scores[scores_len - 1];
}

int32_t personal_best(const int32_t *const scores, const size_t scores_len) {
  int32_t highest = INT32_MIN;
  for (size_t i = 0; i < scores_len; i++) {
    if (scores[i] > highest)
      highest = scores[i];
  }
  return highest;
}

size_t personal_top_three(const int32_t *const scores, const size_t scores_len,
                          int32_t *const output) {
  // clang-format off
  if (scores_len == 0 || !scores_len) return 0;

  int32_t a, b, c; a = b = c = INT32_MIN;
  // clang-format on

  for (size_t i = 0; i < scores_len; i++) {
    if (scores[i] > a) {
      c = b;
      b = a;
      a = scores[i];
    } else if (scores[i] > b) {
      c = b;
      b = scores[i];
    } else if (scores[i] > c) {
      c = scores[i];
    }
  }

  size_t count = scores_len > 3 ? 3 : scores_len;

  output[0] = a;

  // clang-format off
  if (count > 1) output[1] = b;
  if (count > 2) output[2] = c;
  // clang-format on

  return count;
}
