import csv 
import sys
import pdb 
import re 
import json 

def clean_prog(program):
    prog = re.sub("```python", "", program)
    prog = re.sub("```", "", prog)
    return prog 

in_file = sys.argv[1]
out_file = sys.argv[2]
to_write = []

with open("../datasets/overnight/socialnetwork.all.jsonl", "r") as f:
    lut_table = {json.loads(line)["qid"]: json.loads(line) for line in f}

with open(in_file) as f1:
    reader = csv.DictReader(f1)
    for row in reader: 
        if row['denotation_accuracy'] != '1':
            continue 
        query = row['query']
        program = clean_prog(row['prediction'])
        gold_answer = row['gold_denotation']
        dcs = lut_table[row['qid']]['dcs']

        output = {"qid": row['qid'], "query": query, "python": program, "python_multiline": program, "dcs": dcs, "dcs_simplified": None, "original": None, "gold_answer": gold_answer}
        to_write.append(output)

with open(out_file, 'w') as f2:
    for line in to_write:
        f2.write(json.dumps(line) + '\n')
