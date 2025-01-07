def main():
    grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

    # Print the original grades
    print(f"original grades: {grades}")

    # Upgrade grades by adding 10 to grades <= 90, else keep them unchanged
    upgraded_grades = [grade + 10 if grade <= 90 else grade for grade in grades]

    # Print the type of the upgraded grades list
    print(f"type of upgraded grades: {type(upgraded_grades)}")

    # Print the upgraded grades
    print(f"upgraded grades: {upgraded_grades}")


# Entry point of the program
if __name__ == "__main__":
    main()
