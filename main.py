class Date:

    """
    The Date class is designed for creating, storing, and validating a date object,
    as well as for further operations with this date: comparing two dates for
    equality and chronological order, checking for a leap year, verifying the number
    of days in a month, and determining the ordinal day of the year.

    Within the Date class, the parameters are internal variables that store the values
    of a specific date. These are defined in the __init__ constructor.
    """

    def __init__(self, day: int, month: int, year: int):
        """
        The __init__ method initializes a date object, checking the validity
        of the input values for the day, month, and year.

        :param day: an integer representing the day of the month (from 1 to 31).
        :param month: an integer representing the month (from 1 to 12).
        :param year: an integer representing the year (strictly greater than 0).

        The __init__ method checks if all parameters are integers; otherwise,
        a 'TypeError' is raised. It also verifies that the year is not negative,
        checks the month for the correct range, and ensures that the day
        is valid for the corresponding month and year (for this, it calls
        the days_in_month method, which determines the number of days
        in the month); otherwise, a 'ValueError' is raised.
        """
        if not isinstance(day, int):
            raise TypeError("Day cannot be a non-integer number!")
        if not isinstance(month, int):
            raise TypeError("Month cannot be a non-integer number!")
        if not isinstance(year, int):
            raise TypeError("Year cannot be a non-integer number!")
        if year < 1:
            raise ValueError("There is no such thing as a negative year...")
        if not 1 <= month <= 12:
            raise ValueError("Only 12 months.")
        if not 1 <= day <= self.days_in_month(month, year):
            raise ValueError(f"Day {day} is not valid for month {month} and year {year}.")
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        """
        The __str__ method is used to create a text representation
        of the date object in the format 'DD/MM/YYYY' with a two-digit day
        and mont.

        This method does not have any additional parameters besides
        the standard 'self'.

        :return: a string containing the date in the format 'DD/MM/YYYY'.
        """
        return f"{self._day:02d}/{self._month:02d}/{self._year}"

    def __eq__(self, other):
        """
        The __eq__ method allows for comparing two Date class objects for equality.

        :param other: the parameter representing another object that
        the current object will be compared with.
        :return: 'True' (if both objects have the same values for the day,
        month, and year) or 'False' (if the two objects have different values
        for at least one of the parameters).
        """
        if not isinstance(other, Date):
            return False
        return (self._day, self._month, self._year) == (other._day, other._month, other._year)

    def __lt__(self, other):
        """
        The __lt__ method enables the comparison of two Date class objects
        (which represent dates) using the less than operator (<).

        :param other: the parameter representing another object that
        the current object will be compared with.
        :return: 'True' if the date of 'self' is earlier than the date of 'other',
        or 'False' if the date of 'self' is not earlier than 'other' (or if 'other' is not a Date class object).
        """
        if not isinstance(other, Date):
            return False
        return (self._year, self._month, self._day) < (other._year, other._month, other._day)

    def __gt__(self, other):
        """
        The __gt__ method compares two Date class objects using the
        'greater than' (>) operator.

        :param other: the parameter representing another object that
        the current object will be compared with.
        :return: 'True' if the current object's date (self) is later than
        the 'other' object's date or 'False' if the current object's
        date is not later than the 'other' object's date (or if 'other'
        is not an instance of the Date class).
        """
        if not isinstance(other, Date):
            return False
        return (self._year, self._month, self._day) > (other._year, other._month, other._day)

    def __le__(self, other):
        """
        The __le__ method compares two Date class objects using the
        'less than or equal to' (<=) operator.

        :param other: the parameter representing another object that
        the current object will be compared with.
        :return: 'True' if the current object's date (self) is less than or equal
        to the 'other' object's date or 'False' if the current object's date
        is greater than the 'other' object's date (or if 'other' is not an instance of the Date class).
        """
        if not isinstance(other, Date):
            return False
        return ((self._year, self._month, self._day) < (other._year, other._month, other._day)
                or (self._year, self._month, self._day) == (other._year, other._month, other._day))

    def leap_year(self, year: int) -> bool:
        """
        The leap_year method checks if a year is a leap year.

        :return: 'True' if the year is a leap year, and 'False' otherwise.
        """
        if year % 4 != 0:
            return False
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True

    def days_in_month(self, month: int, year: int) -> int:
        """
        The leap_year method returns the number of days in the specified
        month for the given year.

        :param month: an integer representing the month (from 1 to 12).
        :param year: an integer representing the year.
        :return: returns the number of days in the month.
        """
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9,11):
            return 30
        elif month == 2:
            return 29 if self.leap_year(year) else 28
        else:
            raise ValueError("Invalid month")

    def day_of_year(self) -> int:
        """
        The leap_year method returns the day number of the year for the current date.

        :return: an integer representing the day number in the year.
        """
        days_in_months = [31, 29 if self.leap_year(self._year) else 28, 31, 30, 31, 30,
                          31, 31, 30, 31, 30, 31]
        return sum(days_in_months[:self._month - 1]) + self._day

if __name__ == "__main__":
    try:
        data1 = Date(28, 9, 2007)
        print("data1:", data1)
    except ValueError as e:
        print("Error creating data1:", e)

    try:
        data2 = Date(3, 11, 1986)
        print("data2:", data2)
    except ValueError as e:
        print("Error creating data2:", e)

    try:
        data3 = Date(22, 11, 2002)
        print("data3:", data3)
    except ValueError as e:
        print("Error creating data3:", e)

    try:
        data4 = Date(31, 2, 2020)
        print("data4:", data4)
    except ValueError as e:
        print("Error creating data4:", e)

print("data1 == data2:", data1 == data2)
print("data1 < data2:", data1 < data2)
print("data1 > data2:", data1 > data2)
print("data1 <= data2:", data1 <= data2)
print("data1 leap year:", data1.leap_year(data1._year))
print("data2 leap year:", data2.leap_year(data2._year))
print("Days in month for data1:", data1.days_in_month(data1._month, data1._year))
print("Day of year for data1:", data1.day_of_year())
