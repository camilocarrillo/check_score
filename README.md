# check_score
python MPA5.py <input> will measure the score of 3 submit files:

1. submit_top5.txt (top hotel_clusters in the trainig samples)
2. submit_random5.txt (random integers organized in the right output format)
3. Whatever file you put as first argument <input> (python MPA5.py <input>)

The analog file to test.csv is measure_score.txt (these 10.000 lines are the ones you should run with your algorithm and produce an output file like: submit_top5.txt)

Once you have produce your file you can measure the efficiency by:
python MPA5.py submit_YOURFILE.txt
