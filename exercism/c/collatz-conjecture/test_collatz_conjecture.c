#include "collatz_conjecture.h"
#include "test-framework/unity.h"

void setUp(void) {}

void tearDown(void) {}

static void test_zero_steps_for_one(void) {
  TEST_ASSERT_EQUAL(0, steps(1));
  TEST_ASSERT_EQUAL(0, steps2(1));
}

static void test_divide_if_even(void) {
  TEST_ASSERT_EQUAL(4, steps(16));
  TEST_ASSERT_EQUAL(4, steps2(16));
}

static void test_even_and_odd_steps(void) {
  TEST_ASSERT_EQUAL(9, steps(12));
  TEST_ASSERT_EQUAL(9, steps2(12));
}

static void test_large_number_of_even_and_odd_steps(void) {
  TEST_ASSERT_EQUAL(152, steps(1000000));
  TEST_ASSERT_EQUAL(152, steps2(1000000));
}

static void test_zero_is_an_error(void) {
  TEST_ASSERT_EQUAL(ERROR_VALUE, steps(0));
  TEST_ASSERT_EQUAL(ERROR_VALUE, steps2(0));
}

static void test_negative_value_is_an_error(void) {
  TEST_ASSERT_EQUAL(ERROR_VALUE, steps(-15));
  TEST_ASSERT_EQUAL(ERROR_VALUE, steps2(-15));
}

int main(void) {
  UNITY_BEGIN();

  RUN_TEST(test_zero_steps_for_one);
  RUN_TEST(test_divide_if_even);
  RUN_TEST(test_even_and_odd_steps);
  RUN_TEST(test_large_number_of_even_and_odd_steps);
  RUN_TEST(test_zero_is_an_error);
  RUN_TEST(test_negative_value_is_an_error);

  return UNITY_END();
}
