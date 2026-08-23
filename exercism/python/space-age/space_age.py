class SpaceAge:
    EARTH_YEAR_IN_SECONDS = 31_557_600

    def __init__(self, seconds):
        self.seconds = seconds

    def _calc_age(self, m: float) -> float:
        return round(self.seconds / (SpaceAge.EARTH_YEAR_IN_SECONDS * m), 2)

    def on_earth(self) -> float:
        return self._calc_age(1.0)

    def on_mercury(self) -> float:
        return self._calc_age(0.2408467)

    def on_venus(self) -> float:
        return self._calc_age(0.61519726)

    def on_mars(self) -> float:
        return self._calc_age(1.8808158)

    def on_jupiter(self) -> float:
        return self._calc_age(11.862615)

    def on_saturn(self) -> float:
        return self._calc_age(29.447498)

    def on_uranus(self) -> float:
        return self._calc_age(84.016846)

    def on_neptune(self) -> float:
        return self._calc_age(164.79132)
