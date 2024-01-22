#!/bin/bash

for split in  0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
do 
	./scripts/run_codellama-13b_main_agent.sh ../../../new_logs/experiment_2024-01-19_21_58_task_overnight_dataset_socialnetwork_refactor_10_filter_10_redo_done_False_comments_False_helpers_second_True ${split} 
done
