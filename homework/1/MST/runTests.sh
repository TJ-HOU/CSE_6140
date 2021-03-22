#!/bin/bash


graphFiles=`ls ./data/ | grep .gr`

for graph in $graphFiles
do
	filename=`echo $graph | cut -d'.' -f1`
	echo $graph $filename
	python ./src/run_experiments.py ./data/$graph ./data/$filename.extra ./results/$filename.out


done
