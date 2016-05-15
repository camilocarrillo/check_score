# measuring the score
To measure the score of any algorithm I have filtered train.csv just taking into account the is_booking=1 lines, there are ~3M lines (~10% of the original train.csv). 
## train and test samples for this script

The output after filtering train.csv with is_booking=1 was divided in **two** parts each with 1.5M lines.

1. The first half, 1.5M lines are meant to "train" your algorithm or to extract any information (recomended to avoid bias in the score estimation) A file with the first 1.5M lines meant for the training was generated ~150M: wget http://test-carrillo.web.cern.ch/test-carrillo/kag/exp/train_is_booking_A.csv

1. The second 1.5M lines are meant to measure the score of your algorithm.  

  * The file with the true hotel_clusters called int_hc.txt was generated from the second half. (in this repo)

  * A file called mytest.csv, with the same format of test.csv was generated from the second half. The procedure was:
   * the id column
   * remove is_booking,cnt and hotel_cluster columns. 
  ~150M. wget http://test-carrillo.web.cern.ch/test-carrillo/kag/exp/mytest.csv

## running the script 
"python MPA5.py int_hc.txt submission_XXX.csv" will measure the score of any algorithm predicting for mytest.csv youralg(mytest.csv)=submission_XXX.csv
 
The first argument is this script is the file with the true hotel clusters (id hotel_cluster)

If not extra-arguments are provided (python MPA5.py int_hc.txt) it will estimate the score of 4 benchmark examples:
- submit_top5.txt (Most Frequent in the first 1.5M lines with is_booking=1: i.e 91 48 42 59 28)
- submit_random5.txt (random integers organized in the right output format)
- submit_perfect1.txt (perfect hotel_cluster prediction in the first position)
- submit_perfect2.txt (perfect hotel_cluster prediction in the second position)

This is the output of the script python MPA5.py int_hc.txt

Benchmarks:
- for Top 5: 0.0725446999999
- for Random: 0.0224846777778
- for Perfect1: 1.0
- for Perfect2: 0.5

This is what we see in the Public Score
- Most Frequent Benchmark	0.05949
- Random Guess Benchmark	0.02260
