"""
Project Class
Estimated Time: 300 minutes
Actual Time: 400 minutes
"""

from datetime import datetime

class Project:
    """Represent a project with name, start date, priority, cost estimate and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string representation of Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than, used for sorting projects by priority."""
        return self.priority < other.priority

    def __eq__(self, other):
        """Check if two projects have the same priority."""
        return self.priority == other.priority

    def is_complete(self):
        """Determine if project is complete."""
        return self.completion_percentage == 100

    def update(self, completion_percentage="", priority=""):
        """Update completion percentage and/or priority if new values are provided."""
        if completion_percentage:
            self.completion_percentage = int(completion_percentage)
        if priority:
            self.priority = int(priority)