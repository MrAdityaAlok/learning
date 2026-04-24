#include "triangle.h"

static bool is_triangle(triangle_t *t) {
  return t->a > 0 && t->b > 0 && t->c > 0 && t->a + t->b >= t->c &&
         t->b + t->c >= t->a && t->a + t->c >= t->b;
}

bool is_equilateral(triangle_t triangle) {
  if (!is_triangle(&triangle))
    return false;
  return triangle.a == triangle.b && triangle.a == triangle.c;
}

bool is_isosceles(triangle_t triangle) {
  if (!is_triangle(&triangle))
    return false;
  // exercise say triangles' with atleast two sides but in reality only two
  // sides must be equal:
  return triangle.a == triangle.b || triangle.b == triangle.c ||
         triangle.c == triangle.a;
}

bool is_scalene(triangle_t triangle) {
  if (!is_triangle(&triangle))
    return false;
  return !is_isosceles(triangle);
}
