

logdir=$1

python run_experiment.py --dataset_name overnight --overnight_domain socialnetwork --split_name iid_with_dev --n_training_demonstrations 10 --n_test_samples 20 --prompt_lang python --icl_selection_method bm25_utt  --prompt_method full_dd --eval_set_name valid 
