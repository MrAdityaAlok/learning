#include "high_scores.h"
#include <stdint.h>
#include <string.h>

static void merge(int32_t *arr, size_t left, size_t mid, size_t right) {
  int n1 = mid - left + 1;
  int n2 = right - mid;

  int L[n1], R[n2];

  for (int i = 0; i < n1; i++)
    L[i] = arr[left + i];
  for (int j = 0; j < n2; j++)
    R[j] = arr[mid + 1 + j];

  int i = 0, j = 0, k = left;

  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }
}

static void merge_sort(int32_t *arr, size_t left, size_t right) {
  if (left < right) {
    int mid = left + (right - left) / 2;

    merge_sort(arr, left, mid);
    merge_sort(arr, mid + 1, right);

    merge(arr, left, mid, right);
  }
}

int32_t latest(const int32_t *scores, size_t scores_len) {
  return scores[scores_len - 1];
}

int32_t personal_best(const int32_t *scores, size_t scores_len) {
  int32_t sorted_scores[scores_len];
  memcpy(sorted_scores, scores, scores_len * sizeof(scores[0]));
  merge_sort(sorted_scores, 0, scores_len - 1);
  return sorted_scores[scores_len - 1];
}

/// Write the highest scores to `output` (in non-ascending order).
/// Return the number of scores written.
size_t personal_top_three(const int32_t *scores, size_t scores_len,
                          int32_t *output) {
  int32_t sorted_scores[scores_len];
  memcpy(sorted_scores, scores, scores_len * sizeof(scores[0]));
  merge_sort(sorted_scores, 0, scores_len - 1);
}
