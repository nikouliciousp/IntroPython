def get_user_seconds():
    """
    Prompt the user to enter a number of seconds and print it in terms of hours, minutes, and seconds.

    :return: The number of seconds entered by the user as an integer.
    """
    seconds = int(input("Enter the number of seconds: "))
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    print(f"{seconds} seconds is equal to {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")
    return seconds


get_user_seconds()
