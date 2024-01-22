import sys
import json
import pickle as pkl
sys.path.insert(0, '/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/output2/from_experiment_2024_01_18_12_13_task_overnight_dataset_socialnetwork_refactor_5_filter_5_redo_done_False_comments_False_helpers_second_True')
from codebank import *
sys.path.insert(0, '/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/')
from eval.overnight.data.datamodel import *
api = API.from_file('/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/eval/overnight/data/db_socialnetwork.json')

def socialnetwork_train_2926():
    alice = api.find_person_by_id('en.person.alice')
    employees_started_after_alice_started = []
    for person in api.people:
        if person.employment and any((employment.start_date > alice_education.start_date for alice_education in alice.education for employment in person.employment)):
            employees_started_after_alice_started.append(person)
    with open('/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/output2/from_experiment_2024_01_18_12_13_task_overnight_dataset_socialnetwork_refactor_5_filter_5_redo_done_False_comments_False_helpers_second_True/result_pred.json', 'w') as f1:
        json.dump(str(employees_started_after_alice_started), f1)
    with open('/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/output2/from_experiment_2024_01_18_12_13_task_overnight_dataset_socialnetwork_refactor_5_filter_5_redo_done_False_comments_False_helpers_second_True/result_pred.pkl', 'wb') as f1:
        pkl.dump(employees_started_after_alice_started, f1)
socialnetwork_train_2926()