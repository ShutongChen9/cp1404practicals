"""
Word Occurrences
Estimate: 20 minutes
Actual:   28 minutes
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"
