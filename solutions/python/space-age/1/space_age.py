class SpaceAge:
    def __init__(self, seconds):
        # Store the age in seconds and define the Earth year constant
        self.seconds = seconds
        self.earth_year_seconds = 31557600
        self.orbital_coefficients = {"Mercury": 0.2408467, "Venus": 0.61519726, "Earth": 1.0, "Mars": 1.8808158, "Jupiter": 11.862615, "Saturn": 29.447498, "Uranus": 84.016846, "Neptune": 164.79132}

    def on_mercury(self):
        # Calculation for Mercury: orbital period 0.2408467
        return round(self.seconds / (self.earth_year_seconds * self.orbital_coefficients["Mercury"]), 2)

    def on_venus(self):
        # Calculation for Venus: orbital period 0.61519726
        return round(self.seconds / (self.earth_year_seconds * self.orbital_coefficients["Venus"]), 2)

    def on_earth(self):
        # Calculation for Earth: orbital period 1.0
        return round(self.seconds / self.earth_year_seconds, 2)

    def on_mars(self):
        # Calculation for Mars: orbital period 1.8808158
        return round(self.seconds / (self.earth_year_seconds * self.orbital_coefficients["Mars"]), 2)

    def on_jupiter(self):
        # Calculation for Jupiter: orbital period 11.862615
        return round(self.seconds / (self.earth_year_seconds * self.orbital_coefficients["Jupiter"]), 2)

    def on_saturn(self):
        # Calculation for Saturn: orbital period 29.447498
        return round(self.seconds / (self.earth_year_seconds * self.orbital_coefficients["Saturn"]), 2)

    def on_uranus(self):
        # Calculation for Uranus: orbital period 84.016846
        return round(self.seconds / (self.earth_year_seconds * self.orbital_coefficients["Uranus"]), 2)

    def on_neptune(self):
        # Calculation for Neptune: orbital period 164.79132
        return round(self.seconds / (self.earth_year_seconds * self.orbital_coefficients["Neptune"]), 2)