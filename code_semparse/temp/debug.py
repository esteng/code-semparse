import sys
import json
import pickle as pkl
sys.path.insert(0, '/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/')
from eval.overnight.data.datamodel import *
from temp.codebank import *
from temp.codebank import *
api = API.from_file('/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/eval/overnight/data/db_socialnetwork.json')

#def socialnetwork_train_2653():
#    alice = api.find_person_by_id('en.person.alice')
#    students_started_on_alices_birthday = []
#    for person in api.people:
#        if person.education and any((education.start_date == alice.birthdate for education in person.education)):
#            students_started_on_alices_birthday.append(person)
#    with open('temp/result_pred.json', 'w') as f1:
#        json.dump(str(students_started_on_alices_birthday), f1)
#    with open('temp/result_pred.pkl', 'wb') as f1:
#        pkl.dump(students_started_on_alices_birthday, f1)
#socialnetwork_train_2653()

def filter_people_by_birthplace(people, birthplace):

    return [person for person in people if person.birthplace == birthplace]
import pdb 
def answer():
    logged_in_people = [person for person in api.people if person.logged_in]
    pdb.set_trace()
    people_born_in_new_york = filter_people_by_birthplace(logged_in_people, 'en.city.new_york')
    return people_born_in_new_york

print(answer())
