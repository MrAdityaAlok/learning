class Allergies:
    ALLERGENS = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }

    def __init__(self, score: int) -> None:
        if score < 0:
            raise ValueError("Allergy score cannot be negative")

        self.score = score

    def allergic_to(self, item: str) -> bool:
        return (Allergies.ALLERGENS[item] & self.score) > 0

    @property
    def lst(self) -> list[str]:
        return [a for a in Allergies.ALLERGENS if self.allergic_to(a)]
