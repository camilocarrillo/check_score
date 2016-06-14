#!/bin/bash
export file='/afs/cern.ch/user/c/carrillo/EXP/software_versions/split_ramv11.py'
#3
export v31='srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent,ci_week,co_week'
export v32='srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent,ci_week'
export v33='srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent'
#4
export v41=$v31
export v42=$v32
export v43=$v33
#5
export v51='srch_destination_id,hotel_country,hotel_market'
export v52='hotel_market,srch_rm_cnt,book_day'
export v53='hotel_market,srch_rm_cnt'

cat $file | sed -e "s|-31-|$v31|g" | sed -e "s|-41-|$v41|g" | sed -e "s|-41-|$v41|g" | sed -e "s|-51-|$v51|g" | sed -e "s|-32-|$v32|g" | sed -e "s|-42-|$v42|g" | sed -e "s|-52-|$v52|g" | sed -e "s|-33-|$v33|g" | sed -e "s|-43-|$v43|g" | sed -e "s|-53-|$v53|g" > run_book_dayci_month_split_ramv10.py

echo "#"$v31 >> run_book_dayci_month_split_ramv10.py
echo "#"$v32 >> run_book_dayci_month_split_ramv10.py
echo "#"$v33 >> run_book_dayci_month_split_ramv10.py

echo "#"$v41 >> run_book_dayci_month_split_ramv10.py
echo "#"$v42 >> run_book_dayci_month_split_ramv10.py
echo "#"$v43 >> run_book_dayci_month_split_ramv10.py

echo "#"$v51 >> run_book_dayci_month_split_ramv10.py
echo "#"$v52 >> run_book_dayci_month_split_ramv10.py
echo "#"$v53 >> run_book_dayci_month_split_ramv10.py

free
python run_book_dayci_month_split_ramv10.py 1 lx True 1 2 13 3 4 5 6 7 8
free

#ratios:[100.0, 4.28, 0.252, [0.581, 0.139, 0.008, 0.434], [4.472, 2.653, 0.112, 1.706], [89.971, 86.443, 0.3, 3.227], 0.042, 0.039, 0.001, 0.0, [0.361, 0.361, 0.0, 0.0]]
