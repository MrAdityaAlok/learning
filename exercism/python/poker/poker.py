"""
This module implements a function `best_hands` to find the best hand of a poker game.
It is currently limited to games with five cards in a hand only.
"""

from collections import Counter
from dataclasses import dataclass, field
from enum import IntEnum
import functools


class HandType(IntEnum):
    """Types of hand possible in a game of poker"""

    ROYAL_FLUSH = 9
    STRAIGHT_FLUSH = 8
    FOUR_OF_A_KIND = 7
    FULL_HOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


@dataclass
class Card:
    """A class representing a 'card' in a game of poker"""

    face: str
    suit: str
    face_value: int = field(init=False)

    def __post_init__(self) -> None:
        self.face_value = Card.get_face_value(self.face)

    @staticmethod
    def get_face_value(face: str) -> int:
        """Returns the face value of a card. ACE_LOW is represented using 'AL'"""
        match face:
            case "AL":
                return 1
            case "A":
                return 14
            case "K":
                return 13
            case "Q":
                return 12
            case "J":
                return 11
            case numbered_face:
                return int(numbered_face)


class Hand:
    "A class representing a 'hand' in a game of poker"

    ACE_LOW_SEQUENCE_SCORE = 8222  # score before knowing that this 'A' is acutally '1'
    ROYAL_FLUSH_SCORE = 15872
    SEQUENCES_SCORE = {992, 1984, 3968, 7936, 15872, 496, 248, 124, 62, 31}

    def __init__(self, hand: str) -> None:
        self.cards: list[Card] = []
        self.hand_repr = hand

        ace_card = None  # used for ace low check below

        for card in hand.split():
            c = Card(face=card[:-1], suit=card[-1])
            self.cards.append(c)

            if c.face_value == 14:
                ace_card = c

        # check for ace low
        if self.score == Hand.ACE_LOW_SEQUENCE_SCORE:
            del self.score  # make it re-compute next time it is called
            ace_card.face_value = Card.get_face_value("AL")  # pyright: ignore[reportOptionalMemberAccess]

    def __repr__(self) -> str:
        return self.hand_repr

    @functools.cached_property
    def score(self) -> int:
        """It calculates and return a tie-breaker score within same HandType"""
        _score = 0

        for face_value, count in Counter(
            card.face_value for card in self.cards
        ).items():
            face_value_index = face_value - 1
            if count == 3:
                _score |= 1 << (28 + face_value_index)
            elif count in (2, 4):
                _score |= 1 << (14 + face_value_index)
            else:
                _score |= 1 << face_value_index

        return _score

    def _is_same_suit(self) -> bool:
        cards_iter = iter(self.cards)
        first_card_suit = next(cards_iter).suit

        return all(card.suit == first_card_suit for card in cards_iter)

    def _is_in_sequence(self) -> bool:
        return self.score in Hand.SEQUENCES_SCORE

    def _is_royal_flush(self) -> bool:
        return self.score == Hand.ROYAL_FLUSH_SCORE

    @functools.cached_property
    def hand_type(self) -> HandType:
        """Calculates and returns the HandType of this hand"""
        if self._is_same_suit():
            if self._is_royal_flush():
                return HandType.ROYAL_FLUSH
            if self._is_in_sequence():
                return HandType.STRAIGHT_FLUSH
            return HandType.FLUSH

        if self._is_in_sequence():
            return HandType.STRAIGHT

        match sum(
            c * c for c in Counter(card.face_value for card in self.cards).values()
        ):
            case 17:
                return HandType.FOUR_OF_A_KIND
            case 13:
                return HandType.FULL_HOUSE
            case 11:
                return HandType.THREE_OF_A_KIND
            case 9:
                return HandType.TWO_PAIRS
            case 7:
                return HandType.ONE_PAIR
            case _:
                return HandType.HIGH_CARD


def best_hands(hands: list[str]) -> list[str]:
    """Calculates the best hands in a game of poker"""
    top_hand: list = []
    top_hand_type: HandType | None = None

    for hand_str in hands:
        hand = Hand(hand_str)

        if top_hand_type is None or hand.hand_type > top_hand_type:
            top_hand_type = hand.hand_type
            top_hand = [hand]
        elif hand.hand_type == top_hand_type:
            top_hand.append(hand)

    winner = []
    max_score = top_hand[0].score

    for hand in top_hand:
        if not winner or hand.score > max_score:
            max_score = hand.score
            winner = [repr(hand)]
        elif hand.score == max_score:
            winner.append(repr(hand))

    return winner


# [NOTE:] score
# - the score function simply represents the poker cards (1-14) using bit field (max 42 bit)
# - it flips the bit to '1' whichever 'face_value' card is present
# - to give more priority to pairs it writes paired 'face_value' to 14+ (TWO_PAIRS) or 28+ (THREE_OF_A_KIND)
# - thus, hands can then be simply compared using arithmetic.
