#!/bin/bash

i=0

until [ $i -ge 5 ]
do
  ((i++))
  filename=result-${i}-time.txt
  /usr/bin/time -f "%E" java -jar collatex-tools-1.7.1.jar data/results/result.json --format csv --output json-result-{$i}.csv 2> $filename
  cat $filename >> total-time.txt
  rm $filename
done

