"""Functions to automate Conda airlines ticketing system."""

from typing import Dict, Generator, List


SEAT_LETTERS = ["A", "B", "C", "D"]


def generate_seat_letters(number: int) -> Generator[str]:
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    for i in range(number):
        yield SEAT_LETTERS[i % 4]


def generate_seats(number: int) -> Generator[str]:
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    for i in range(number):
        row = i // 4 + (1 if i < 48 else 2)
        yield f"{(row)}{SEAT_LETTERS[i % 4]}"


def assign_seats(passengers: List[str]) -> Dict[str, str]:
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers: List[str], flight_id: str) -> Generator[str]:
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        tid = f"{seat}{flight_id}"
        yield tid + "0" * (12 - len(tid))
