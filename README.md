# My own calendar system

*Work is in the earliest stage of development.*

## Explanation

This library provides tools to work with the person-centric calendar (which I currently call 777-calendar) that I have invented to use for various purposes and for fun.  The tools help to easily convert dates between Gregorian and 777-calendar.

The main ideas of this calendar are:
 * It's epoch is a person's birth date, and year changes happen on birthday.
 * It has 7 months (currently called meriods), every such meriod has 7 weeks, and every week has 7 days.
 * These 49 weeks of the calendar share days of the week with the Gregorian date, while remaining 22 or 23 days of the year are near the birthday.
 * The date is written as `<year>.<meriod>.<week>.<day>` (such as 29.2.5.1) or as `<year>.<meriod>.<day>` (such as 29.8.3, for days near birthday).

Exact calendar rules are described in [sevencal/sevencalendar.py](sevencal/sevencalendar.py).

## TODO list:
### The library
 * Support both python 2 and python 3 and test both with test script
 * have better tests
 * Add link to calendar explanation
 * add alternative __str__ methods
 * add coding guidelines
 * add development notes
 * add functions
    * number of days in 0 and 8 meriods in a given year

### Other stuff
 * make library in JavaScript (well, initially thought of making this is JavaScript, python version is just a coincidence, because I was too lazy for couple of years and forgot)
 * Add links to projects related to the calendar

## Short notes

Sometimes I use a system to write a date with origin as my date of birth.  So I write this software to automatically convert dates to/from my calendar.

## License

The project is licensed with the MIT license, you can find it in the [LICENSE](LICENSE) file.

## Version history

### v0.0.3 -- 2018-07-10
 * Add more tests.
 * Add more examples in explanation.
 * Add offset argument in command-line tool.

### v0.0.2 -- 2018-07-06
 * Add method to parse from datetime and use it in command-line tool.

### v0.0.1 -- 2018-07-01 -- First versioned version.
 * Add command-line options in tool for date to parse and birth date.
