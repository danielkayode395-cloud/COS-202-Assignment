print("=" * 55)
print("      PERSONAL POCKET CGPA CALCULATOR")
print("=" * 55)

while True:

    courses = int(input("\nEnter Number of Courses: "))

    units = 0
    points = 0

    for num in range(1, courses + 1):

        print(f"\nCourse {num}")

        credit = int(input("Course Unit: "))
        score = int(input("Course Score: "))

        match score:

            case s if 70 <= s <= 100:
                letter = "A"
                grade = 5

            case s if 60 <= s <= 69:
                letter = "B"
                grade = 4

            case s if 50 <= s <= 59:
                letter = "C"
                grade = 3

            case s if 45 <= s <= 49:
                letter = "D"
                grade = 2

            case s if 40 <= s <= 44:
                letter = "E"
                grade = 1

            case s if 0 <= s <= 39:
                letter = "F"
                grade = 0

            case _:
                print("Invalid Score.")
                continue

        earned = credit * grade

        units += credit
        points += earned

        print("Grade:", letter)
        print("Grade Point:", grade)
        print("Earned Point:", earned)

    cgpa = points / units

    print("\n========== CGPA REPORT ==========")
    print("Total Units:", units)
    print("Total Points:", points)
    print("CGPA:", round(cgpa, 2))
    print("=================================")

    choice = input("\nPress Y to calculate again or N to exit: ").upper()

    match choice:
        case "Y":
            continue
        case "N":
            print("\nThank you for using the CGPA Calculator.")
            break
        case _:
            print("\nInvalid choice.")
            break