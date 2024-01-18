
def filter_start_date(person):

    return person.employment and any((e.start_date != 2004 for e in person.employment))

def filter_end_date(person):

    return person.employment and any((e.end_date > 2004 for e in person.employment))

def is_end_date_at_most(end_date, year):

    return end_date <= year

def is_end_date_not(end_date, year):

    return end_date != year

def is_start_date_not(start_date, year):

    return start_date != year

def is_start_date_at_least(start_date, year):

    return start_date >= year

def is_end_date(end_date, year):

    return end_date == year

def has_start_date_before(person, year):

    return any((e.start_date <= year for e in person.education))

def has_start_date_after(person, year):

    return any((e.start_date > year for e in person.education))

def has_start_date_after_or(person, year1, year2):

    return any((e.start_date > year1 or e.start_date > year2 for e in person.education))

def has_start_date(person, year1, year2):

    return any((e.start_date == year1 or e.start_date == year2 for e in person.education))

def has_employment_start_date_before(person, birthdate):

    return any((employment.start_date <= birthdate for employment in person.employment))

def has_more_than_two_friends(person):

    return len(person.friends) > 2

def get_gender(person):

    return person.gender

def is_start_date_before(date):

    return date < 2004 or date < 2010

def is_start_date_after(date):

    return date > 2004 or date > 2010

def is_start_date_in(date):

    return date == 2004 or date == 2010

def is_end_date_at_least(date):

    return date >= 2004 or date >= 2010

def filter_friends_by_birthplace(alice, birthplace):

    return [friend for friend in alice.friends if friend.birthplace == birthplace]

def filter_friends_by_height(alice, height):

    return [friend for friend in alice.friends if friend.height == height]

def filter_people_by_birthplace_count(people):

    return [person for person in people if len(set(person.birthplace)) == 2]

def get_birthplace_counts(people):

    birthplace_counts = {}
    for person in people:
        birthplace_counts[person.birthplace] = birthplace_counts.get(person.birthplace, 0) + 1
    return birthplace_counts

def extract_genders(employees):

    return set([employee.gender for employee in employees])

def filter_employees_by_end_date(employees, year):

    return [person for person in employees if person.employment and any((e.end_date < year for e in person.employment))]

def filter_employees_by_start_date(employees, year):

    return [person for person in employees if person.employment and any((e.start_date < year for e in person.employment))]

def extract_end_dates(employment):

    return [e.end_date for e in employment if e.end_date is not None]

def filter_employment_by_end_date(employment, year):

    return [e for e in employment if e.end_date == year]

def extract_end_date(employment):

    return employment[0].end_date if employment else None

def filter_students_by_end_date(students, year):

    return [student for student in students if student.education and any((e.end_date != year for e in student.education))]

def get_smallest_end_date(students):

    return min((e.end_date for student in students for e in student.education if e.end_date is not None))

def filter_employments_by_start_date(employments, year):

    return [employment.employer for employment in employments if employment.start_date == year]

def filter_people_by_birthdate(people, birthdate):

    return [person for person in people if person.birthdate >= birthdate]

def filter_people_by_birthplace(people, birthplace):

    return [person for person in people if person.birthplace == birthplace]

def filter_people_by_height(people, height):

    return [person for person in people if person.height == height]

def extract_birthplaces(employees):

    return set([employee.birthplace for employee in employees])

def filter_friends_by_education(person, field_of_study):

    return [friend for friend in person.friends if any((education.field_of_study != field_of_study for education in friend.education))]

def filter_people_by_job_title(people, job_title):

    return [person for person in people if person.employment and all((e.job_title != job_title for e in person.employment))]

def filter_people_by_relationship_status(people, relationship_status):

    return [person for person in people if person.relationship_status != relationship_status]

def has_education_before_2004(person):

    return person.education and any((e.start_date < 2004 for e in person.education))

def has_employment_after_2004(person):

    return person.employment and any((e.end_date > 2004 for e in person.employment))

def count_occurrences(items):

    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

def get_friends_of_friends(person):

    friends_of_friends = [friend for friend in person.friends for friend in friend.friends]
    return friends_of_friends

def has_friend_with_employment_end_before(person):

    for friend in person.friends:
        if friend.employment and any((e.end_date < 2004 for e in friend.employment)):
            return True
    return False

def has_friend_with_employment_end_at_most(person):

    for friend in person.friends:
        if friend.employment and any((e.end_date <= 2004 for e in friend.employment)):
            return True
    return False

def has_friend_with_employment_start_at_most(person):

    for friend in person.friends:
        if friend.employment and any((e.start_date <= 2004 for e in friend.employment)):
            return True
    return False

def has_friend_with_employment_start_before(person):

    for friend in person.friends:
        if friend.employment and any((e.start_date < 2004 for e in friend.employment)):
            return True
    return False

def is_student_with_education_start_after(person):

    if person.education and any((e.start_date > 2004 for e in person.education)):
        return True
    return False

def has_friend_with_education_end_after(person):

    for friend in person.friends:
        if friend.education and any((e.end_date >= 2004 for e in friend.education)):
            return True
    return False

def has_friend_with_employment_start_after(person):

    for friend in person.friends:
        if friend.employment and any((e.start_date > 2004 for e in friend.employment)):
            return True
    return False

def has_employment_start_after(person):

    return person.employment and any((e.start_date >= 2004 for e in person.employment))

def has_education_not_2004(person):

    return person.education and any((e.start_date != 2004 for e in person.education))

def extract_relationship_status(students):

    return set([student.relationship_status for student in students])

def filter_students_by_date(api, date):

    return [person for person in api.people if person.education and any((e.end_date <= date for e in person.education))]

def extract_birthplace(students):

    return set([student.birthplace for student in students])

