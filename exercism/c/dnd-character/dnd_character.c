#include "dnd_character.h"
#include <math.h>
#include <stdlib.h>
#include <time.h>

int ability(void) {
  srand(time(NULL));
  int sum = rand() % 7, s = sum, r;
  for (int i = 0; i < 3; i++) {
    r = rand() % 7;
    sum += r;
    if (r < s)
      s = r;
  }
  return sum - s;
}

int modifier(int score) { return floor((score - 10) / 2.0); }

dnd_character_t make_dnd_character(void) {
  dnd_character_t character;

  character.charisma = ability();
  character.constitution = ability();
  character.dexterity = ability();
  character.hitpoints = 10 + modifier(character.constitution);
  character.intelligence = ability();
  character.strength = ability();
  character.wisdom = ability();

  return character;
}
