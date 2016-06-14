#!/bin/bash
export file='/afs/cern.ch/user/c/carrillo/EXP/software_versions/split_ramv9.py'
#3
export v31='srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent,hotel_continent,hotel_country'
export v32='srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent,hotel_continent'
export v33='srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent'
#4
export v41='srch_destination_id,hotel_country,hotel_market,is_package,user_id,ci_year,book_year'
export v42='srch_destination_id,hotel_country,hotel_market,is_package,user_id,ci_year'
export v43='srch_destination_id,hotel_country,hotel_market,is_package,user_id'
#5
export v51='srch_destination_id,hotel_country,hotel_market,is_package,user_id'
export v52='srch_destination_id,hotel_country,hotel_market,is_package'
export v53='srch_destination_id,hotel_country,hotel_market'

#[194550, 41633, 2454, [0, 0, 0, 0], [49154, 49154, 0, 0], [840878, 3, 824991, 15884], 34723, 383, 10, 0, 0, 0, 0, [3515, 3515, 0, 0]]


cat $file | sed -e "s|-31-|$v31|g" | sed -e "s|-41-|$v41|g" | sed -e "s|-41-|$v41|g" | sed -e "s|-51-|$v51|g" | sed -e "s|-32-|$v32|g" | sed -e "s|-42-|$v42|g" | sed -e "s|-52-|$v52|g" | sed -e "s|-33-|$v33|g" | sed -e "s|-43-|$v43|g" | sed -e "s|-53-|$v53|g" > run_split_ramv9.py

echo "#"$v31 >> run_-new1--new2-_split_ramv9.py
echo "#"$v32 >> run_-new1--new2-_split_ramv9.py
echo "#"$v33 >> run_-new1--new2-_split_ramv9.py

echo "#"$v41 >> run_-new1--new2-_split_ramv9.py
echo "#"$v42 >> run_-new1--new2-_split_ramv9.py
echo "#"$v43 >> run_-new1--new2-_split_ramv9.py

echo "#"$v51 >> run_-new1--new2-_split_ramv9.py
echo "#"$v52 >> run_-new1--new2-_split_ramv9.py
echo "#"$v53 >> run_-new1--new2-_split_ramv9.py

free
python run_split_ramv9.py 1 pcwits True 1 2 13 3 4 5 6 7 8  
free