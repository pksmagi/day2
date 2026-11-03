def get_grade(mark):
    """Return the grade for a mark from 0 to 100."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    return "E"


def add_student():
    """Ask for a student's name and mark, validate them, and store the record."""
    print("\n--- Add Student ---")

    while True:
        name = input("Enter student name (or press Enter to cancel): ").strip()
        if not name:
            print("Name cannot be empty. Student entry cancelled.")
            return
        break

    while True:
        raw_mark = input("Enter mark (0-100): ").strip()

        if not raw_mark:
            print("Mark cannot be empty. Please try again.")
            continue

        try:
            mark = float(raw_mark)
        except ValueError:
            print("Invalid mark. Please enter a number, such as 85 or 72.5.")
            continue

        if not 0 <= mark <= 100:
            print("Mark must be between 0 and 100.")
            continue
        break

    students.append({
        "name": name,
        "mark": mark,
        "grade": get_grade(mark),
    })
    print(f"Added {name} successfully. Grade: {get_grade(mark)}")


def show_results():
    """Print the student table and class statistics."""
    print("\n--- Student Results ---")

    if not students:
        print("No student records yet. Use option 1 to add a student.")
        return

    name_width = max(4, min(30, max(len(s["name"]) for s in students)))
    print(f"{'Name':<{name_width}}  {'Mark':>7}  {'Grade':>5}")
    print("-" * (name_width + 18))

    for student in students:
        # Keep the table aligned even when a name is long.
        display_name = student["name"][:name_width]
        print(
            f"{display_name:<{name_width}}  "
            f"{student['mark']:>7.1f}  "
            f"{student['grade']:>5}"
        )

    marks = [student["mark"] for student in students]
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("-" * (name_width + 18))
    print(
        f"Average: {average:.1f}    "
        f"Highest: {highest:g}    "
        f"Lowest: {lowest:g}"
    )
    print(f"Total students: {len(students)}")


def main():
    """Run the add/show/quit menu until the user chooses to quit."""
    print("=" * 34)
    print("       STUDENT GRADE MANAGER")
    print("=" * 34)

    while True:
        print("\nMenu")
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Thank you for using Student Grade Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram closed. Goodbye!")
