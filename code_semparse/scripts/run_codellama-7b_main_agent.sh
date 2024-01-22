

logdir=$1

#python run_experiment.py --dataset_name overnight --overnight_domain socialnetwork --split_name iid_with_dev --n_training_demonstrations 10 --n_test_samples 100 --prompt_lang python --icl_selection_method bm25_utt  --prompt_method full_dd --eval_set_name valid --logdir ${logdir} --do_filter --special_path ../datasets/overnight/train_200_generated.jsonl --model "codellama/CodeLlama-7b-Python-hf"

split=0.2
#demos=10
#max_helpers=5
demos=8
max_helpers=10

python run_experiment.py \
	--dataset_name overnight \
	--overnight_domain socialnetwork \
	--split_name iid_with_dev \
	--n_training_demonstrations 10 \
	--n_test_samples 100 \
	--prompt_lang python \
	--icl_selection_method bm25_utt  \
	--prompt_method full_dd \
	--eval_set_name valid \
	--logdir ${logdir} \
	--do_filter \
	--special_path ../datasets/overnight/train_200_generated.jsonl \
	--model "codellama/CodeLlama-7b-Python-hf"\
	--n_training_demonstrations ${demos}	\
	--max_helpers ${max_helpers} \
	--budget_split ${split} \
	--seed 42 \
	--prompt_idx 1 \
	--batch_size 8
