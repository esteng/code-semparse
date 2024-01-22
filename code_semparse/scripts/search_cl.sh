#!/bin/bash

#for split in  0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
split=0.2
demos=8
max_helpers=10
logdir="../../../new_logs/experiment_2024-01-19_21_58_task_overnight_dataset_socialnetwork_refactor_10_filter_10_redo_done_False_comments_False_helpers_second_True"

for filter_threshold in -0.2 -0.1 0.0 0.1 0.2
do
	python run_experiment.py \
		--dataset_name overnight \
		--overnight_domain socialnetwork \
		--split_name iid_with_dev \
		--n_training_demonstrations 10 \
		--n_test_samples 24 \
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
		--filter_threshold ${filter_threshold} \
		--prompt_idx 1 

	for min_usage in 2 3 4
	do 
		python run_experiment.py \
			--dataset_name overnight \
			--overnight_domain socialnetwork \
			--split_name iid_with_dev \
			--n_training_demonstrations 10 \
			--n_test_samples 24 \
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
			--filter_threshold ${filter_threshold}\
			--cut_low_usage \
			--filter_min_usage ${min_usage} \
			--prompt_idx 1 
	done
done
