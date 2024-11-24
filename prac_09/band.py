"""
CP1404/CP5632 Practical
Band class
"""

class Band:
    """Band class representing a music band with a list of musicians."""

    def __init__(self, band_name):
        """Initialize the band with a name and an empty list of musicians."""
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band and its musicians."""
        return f"{self.band_name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Play the band's music, showing which instrument each musician is playing."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)

