import sys
import json
import pickle as pkl
sys.path.insert(0, '/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/')
from eval.overnight.data.datamodel import *
from temp.codebank import *
from temp.codebank import *
api = API.from_file('/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/eval/overnight/data/db_socialnetwork.json')

def socialnetwork_train_2653():
    alice = api.find_person_by_id('en.person.alice')
    students_started_on_alices_birthday = []
    for person in api.people:
        if person.education and any((e.start_date == alice.birthdate for e in person.education)):
            students_started_on_alices_birthday.append(person)
    with open('temp/result_pred.json', 'w') as f1:
        json.dump(str(students_started_on_alices_birthday), f1)
    with open('temp/result_pred.pkl', 'wb') as f1:
        pkl.dump(students_started_on_alices_birthday, f1)
socialnetwork_train_2653()