
def has_start_date(education, year):

    return any((e.start_date != year for e in education))

def is_start_date_larger(start_date, year):

    return start_date > year

def filter_employments_by_start_date(employments, start_date):

    return [employment.employer for employment in employments if employment.start_date == start_date]

def filter_people_by_height(people, height):

    return [person for person in people if person.height == height]

def filter_people_by_birthplace(people, birthplace):

    return [person for person in people if person.birthplace == birthplace]

def get_birthplaces(employees):

    return set([employee.birthplace for employee in employees])

def find_employer_of_tall_person(height):

    tall_people = filter_people_by_height(api.people, height)
    employers = set([e.employer for person in tall_people for e in person.employment])
    return employers

def count_occurrences(lst):

    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts

def filter_employees_by_start_date(employees, start_date):

    return [employee for employee in employees if employee.employment and any((e.start_date < start_date for e in employee.employment))]

def get_employees_ended_not_2004(api):

    return [person for person in api.people if person.employment and any((e.end_date != 2004 for e in person.employment))]

