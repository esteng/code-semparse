import json 
import numpy as np
np.random.seed(12)

with open("../datasets/overnight/train_200_generated.jsonl") as f1:
    sub_train_data = [json.loads(x) for x in f1.readlines()]

with open("../datasets/overnight/socialnetwork.all.jsonl") as f1:
    all_data = [json.loads(x) for x in f1.readlines()]


train_ids = [x['qid'] for x in sub_train_data]
all_ids = [x['qid'] for x in all_data if "train" in x['qid']] 
elig_dev_ids = list(set(all_ids) - set(train_ids))
np.random.shuffle(elig_dev_ids)
dev_ids = elig_dev_ids[:100]

with open("../datasets/overnight/splits/iid/socialnetwork.json") as f1:
    split_data = json.load(f1)

# replace dev and train 
split_data['train'] = train_ids
split_data['valid'] = dev_ids

with open("../datasets/overnight/splits/iid_with_dev/socialnetwork.json", "w") as f1:
    json.dump(split_data, f1, indent=4)