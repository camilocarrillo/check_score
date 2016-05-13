# check_score

python MPA5.py <input> will measure the score for input files:

If not argument is provided the script will run 4 benchmark examples:
1. submit_top5.txt (top hotel_clusters in the trainig samples)
2. submit_random5.txt (random integers organized in the right output format)
3. submit_perfect1.txt (perfect hotel_cluster prediction in the first position)
4. submit_perfect2.txt (perfect hotel_cluster prediction in the second position)

The analog file to test.csv is measure_score.txt (these 10.000 lines are the ones you should run with your algorithm and produce an output file like: submit_*.txt)

Once you have produce your file you can measure the efficiency by:
python MPA5.py submit_YOURFILE.txt
