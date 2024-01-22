#!/bin/bash

for seed in 12 42 64 
do
	for model in 7 13 34
	do
		./scripts_test/run_codellama-${model}b_baseline.sh ${seed} 
	done
done
