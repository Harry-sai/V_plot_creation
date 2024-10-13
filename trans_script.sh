#!/bin/bash
zless mapped.bed.gz | awk 'BEGIN{OFS="\t"} {transform_range=(1000/($4-$3))*((($9+$10)/2)-$3)-500;print transform_range,$12}' > Range.tsv 

sort Range.tsv | uniq -c > Range_sort.tsv  
 
cat Range_sort.tsv |tr -s ' ' '\t'  > RS_rms.tsv 

sed 's/\t//' RS_rms.tsv > final_file.tsv 

(echo -e "Freq\tx_axis\ty_axis" && zless final_file.tsv) > final_plot_file.tsv && column -t final_plot_file.tsv |python3 program.py

