#include "robot_simulator.h"

robot_status_t robot_create(robot_direction_t direction, int x, int y) {
  return (robot_status_t){.direction = direction,
                          .position = (robot_position_t){x, y}};
}

void robot_move(robot_status_t *robot, const char *commands) {
  for (; *commands; commands++) {
    switch (*commands) {
    case 'R':
      robot->direction = (robot->direction + 1) % DIRECTION_MAX;
      break;
    case 'L':
      robot->direction = (robot->direction - 1) % DIRECTION_MAX;
      break;
    case 'A':
      if (robot->direction == DIRECTION_NORTH)
        robot->position.y += 1;
      else if (robot->direction == DIRECTION_SOUTH)
        robot->position.y -= 1;
      else if (robot->direction == DIRECTION_EAST)
        robot->position.x += 1;
      else
        robot->position.x -= 1;
      break;
    }
  }
}
