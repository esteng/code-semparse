import sys
sys.path.insert(0, '/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/')
import json
import pickle as pkl
from temp.codebank import *
from eval.overnight.data.datamodel import *
from temp.codebank import *
api = API.from_file('/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/eval/overnight/data/db_socialnetwork.json')

def socialnetwork_train_1972():
    alice = [person for person in api.people if person.name == 'alice'][0]
    employer = [employment.employer for employment in alice.employment if employment.end_date == 2004][0]
    with open('temp/result_pred.json', 'w') as f1:
        json.dump(str(employer), f1)
    with open('temp/result_pred.pkl', 'wb') as f1:
        pkl.dump(employer, f1)
socialnetwork_train_1972()