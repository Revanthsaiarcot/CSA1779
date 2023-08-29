% Define facts for individuals with their names and DOBs
person(john, date(1990, 5, 15)).
person(lisa, date(1985, 9, 23)).
person(michael, date(1995, 2, 10)).
person(sarah, date(2000, 11, 7)).

% Predicate to find the age of a person
age(Person, Age) :-
    person(Person, DOB),
    current_date(CurrentYear, CurrentMonth, CurrentDay),
    DOB = date(Year, Month, Day),
    Age is CurrentYear - Year - (if_before_birthday(Month, Day, CurrentMonth, CurrentDay), 1, 0).

% Predicate to check if the current date is before the person's birthday
if_before_birthday(Month, Day,CurrentMonth, CurrentDay) :-
    (Month < CurrentMonth; (Month == CurrentMonth, Day =< CurrentDay)).

% Current date (for demonstration purposes)
current_date(2023,�8,�12).
