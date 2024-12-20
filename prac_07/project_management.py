"""
Project Management Program
Estimated Time: 300 minutes
Actual Time: 400 minutes
"""

from datetime import datetime
from prac_07.project import Project

MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")

def main():
    """Main program for project management."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == 'L':
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Filename to save projects to: ")
            save_projects(projects, filename)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save = input("Would you like to save to projects.txt? ")
    if save.lower().startswith('y'):
        save_projects(projects, "projects.txt")
    print("Thank you for using custom-built project management software.")

def load_projects(filename='projects.txt'):
    """Load projects from file."""
    projects = []
    with open(filename) as file:
        file.readline()
        for line in file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


def save_projects(projects, filename='projects.txt'):
    """Save projects to file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t"
                       f"{project.completion_percentage}\n")
    return projects

def display_projects(projects):
    """Display projects in two groups: incomplete and complete."""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not project.is_complete()]
    for project in sorted(incomplete_projects):
        print(f"  {project}")

    print("Completed projects:")
    completed_projects = [project for project in projects if project.is_complete()]
    for project in sorted(completed_projects):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects that start after specified date."""
    start_date= input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.strptime(start_date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)


def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update a project's completion percentage and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_percentage, new_priority)


if __name__ == '__main__':
    main()
