#include "allergies.h"

/* How does a bitmask and filter work?
 *
 * Insteading of thinking in mathematical terms (see your previous
 * implementation), think in computational terms. Assume the score to be a field
 * of bits [0,0,0,0,0,0,0,0]. Now each allergen is represented by a 1 if affects
 * the person. Thus we can check whether that particular bit for the allergen is
 * set or not.
 *
 * How?
 *
 * 1 << allergen does bitwise left shift and then & compare it with score.
 * Now if the bit for that particular allergen was set then only that bit will
 * be 1 in the result.
 * Thus result will be > 0.
 * Hence, checked successfully!
 *
 * Why 1U?
 * Since shifting to signed bit of literal 1 (signed int) is not defined, make
 * it unsigned. Although it is of no use here currently.
 */

bool is_allergic_to(allergen_t allergen, uint32_t score) {
  return ((1U << allergen) & score) > 0;
}

allergen_list_t get_allergens(uint32_t score) {
  allergen_list_t list = {.count = 0, .allergens = {false}};

  for (allergen_t i = ALLERGEN_EGGS; i < ALLERGEN_COUNT; i++) {
    if (is_allergic_to(i, score)) {
      list.count += 1;
      list.allergens[i] = true;
    }
  }

  return list;
}

/* Previous implementation:
 *
 * #include "allergies.h"
 *
 * #define ALLERGEN_SCORE_BOUNDARY 256
 * #define ALLERGEN_MAX_VALUE 128
 *
 * bool is_allergic_to(allergen_t allergen, uint16_t score) {
 *  return get_allergens(score).allergens[allergen];
 * }
 *
 * allergen_list_t get_allergens(uint16_t score) {
 *  score %= ALLERGEN_SCORE_BOUNDARY;
 *
 *  allergen_list_t list = {.count = 0, .allergens = {false}};
 *
 *  if (score > 0) {
 *    for (uint8_t v = ALLERGEN_MAX_VALUE, i = 7; score != 0; v /= 2, i--) {
 *      if (score >= v) {
 *        list.count += 1;
 *        list.allergens[i] = true;
 *        score %= v;
 *      }
 *    }
 *  }
 *
 *  return list;
 * }
 *
 */
