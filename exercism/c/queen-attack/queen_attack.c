#include "queen_attack.h"

static int absolute(int v) { return v * ((v > 0) - (v < 0)); }
static int on_board(position_t p) { return p.row < 8 && p.column < 8; }

attack_status_t can_attack(position_t queen_1, position_t queen_2) {
  if (!on_board(queen_1) || !on_board(queen_2))
    return INVALID_POSITION;

  int horizontal_offset = absolute(queen_1.column - queen_2.column);
  int vertical_offset = absolute(queen_1.row - queen_2.row);

  if (horizontal_offset + vertical_offset == 0)
    return INVALID_POSITION;

  if (horizontal_offset == 0 || vertical_offset == 0 ||
      horizontal_offset == vertical_offset)
    return CAN_ATTACK;

  return CAN_NOT_ATTACK;
}

/* Explanation of `absolute` function:

TIf v is positive, the expression (v>0) is true and will have the value 1 while
(v<0) is false (with a value 0 for false). Hence, when v is positive ((v>0) -
(v<0)) = (1-0) = 1. And the whole expression is: v * (1) == v.

If v is negative, the expression (v>0) is false and will have the value 0 while
(v<0) is true (value 1). Thus, for negative v, ((v>0) - (v<0)) = (0-1) = -1. And
the whole expression is: v * (-1) == -v.

When v == 0, both (v<0) and (v>0) will evaluate to 0, leaving: v * 0 == 0.
*/
