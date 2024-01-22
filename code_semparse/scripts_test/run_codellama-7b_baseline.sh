


python run_experiment.py --dataset_name overnight --overnight_domain socialnetwork --split_name iid_with_dev --n_training_demonstrations 10 --prompt_lang python --icl_selection_method bm25_utt  --prompt_method full_dd --eval_set_name test --special_path ../datasets/overnight/train_200_generated.jsonl --model "codellama/CodeLlama-7b-Python-hf" --batch_size 8 --seed ${1} 
