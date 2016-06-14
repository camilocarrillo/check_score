echo "#3"
cat $1 | grep -w -A 5 "#3" | awk -F '\\(' '{print $3}' | awk -F '\\)' '{print $1}' 
echo "#4"
cat $1 | grep -w -A 5 "#4" | awk -F '\\(' '{print $3}' | awk -F '\\)' '{print $1}' 
echo "#5"
cat $1 | grep -w -A 5 "#5" | awk -F '\\(' '{print $3}' | awk -F '\\)' '{print $1}' 
