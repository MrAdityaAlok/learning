#include "complex_numbers.h"
#include <math.h>

static complex_t c_reciprocal(complex_t a) {
  double sq = a.real * a.real + a.imag * a.imag;
  return (complex_t){a.real / sq, -a.imag / sq};
}

complex_t c_add(complex_t a, complex_t b) {
  return (complex_t){a.real + b.real, a.imag + b.imag};
}

complex_t c_sub(complex_t a, complex_t b) {
  return (complex_t){a.real - b.real, a.imag - b.imag};
}

complex_t c_mul(complex_t a, complex_t b) {
  return (complex_t){a.real * b.real - a.imag * b.imag,
                     a.real * b.imag + a.imag * b.real};
}

complex_t c_div(complex_t a, complex_t b) { return c_mul(a, c_reciprocal(b)); }

double c_abs(complex_t x) { return sqrt(x.real * x.real + x.imag * x.imag); }

complex_t c_conjugate(complex_t x) { return (complex_t){x.real, -x.imag}; }

double c_real(complex_t x) { return x.real; }

double c_imag(complex_t x) { return x.imag; }

complex_t c_exp(complex_t x) {
  double e = exp(x.real);
  return (complex_t){e * cos(x.imag), e * sin(x.imag)};
}
