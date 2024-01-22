import sys
import json
import pickle as pkl
sys.path.insert(0, '/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/')
from eval.overnight.data.datamodel import *
from ..codebank import *
api = API.from_file('/nas-ssd2/esteng/program_refactoring/third_party/code-semparse/code_semparse/eval/overnight/data/db_socialnetwork.json')

def socialnetwork_train_2430():
    people_born_in_ny = [person for person in api.people if person.birthplace == 'en.city.new_york']
    genders = set([person.gender for person in people_born_in_ny])
    with open('./result_pred.json', 'w') as f1:
        json.dump(str(genders), f1)
    with open('./result_pred.pkl', 'wb') as f1:
        pkl.dump(genders, f1)
socialnetwork_train_2430()