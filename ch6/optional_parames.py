def get_formatted_date(day=1, month=1, year=2020):
    # Format and return the date as a string in "day/month/year" format
    return f"{day}/{month}/{year}"


def main():
    # Default date: 1/1/2020
    print(get_formatted_date())

    # Custom date: 25/12/2020 (day and month provided)
    print(get_formatted_date(25, 12))

    # Custom date: 25/1/2021 (day and year provided with keyword arguments)
    print(get_formatted_date(day=25, year=2021))

    # Custom date: 1/10/1999 (month and year provided with keyword arguments)
    print(get_formatted_date(month=10, year=1999))

    # Custom date: 30/11/1998 (all parameters provided with keyword arguments in different order)
    print(get_formatted_date(year=1998, month=11, day=30))

    # Custom date: 31/12/2020 (all parameters provided positionally)
    print(get_formatted_date(31, 12, 2020))


if __name__ == "__main__":
    main()
