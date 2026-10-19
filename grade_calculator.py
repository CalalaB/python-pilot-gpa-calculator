def get_score(subject_number):
    """Ask for one score and keep asking until it is a number from 0 to 100."""
    while True:
        try:
            score = int(input(f"Enter score for subject {subject_number} (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100. Try again.")
        except ValueError:
            print("Please enter a whole number.")


def get_grade(average):
    if average >= 85:
        return "HD"
    elif average >= 75:
        return "D"
    elif average >= 65:
        return "C"
    elif average >= 50:
        return "P"
    else:
        return "F"


def main():
    scores = [get_score(i) for i in range(1, 5)]
    average = sum(scores) / len(scores)
    grade = get_grade(average)

    print(f"\nAverage score: {average:.2f}")
    print(f"Final grade: {grade}")


if __name__ == "__main__":
    main()
