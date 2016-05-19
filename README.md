# measuring the score
To measure the score of any algorithm I have filtered train.csv by year/term
## train and test samples for this script

The output after filtering train.csv with is_booking=1 was divided in **two** parts:

1. The first file is meant to "train" your algorithm or to extract any information (recomended to avoid bias in the score estimation) A file with 2013+2014-I  meant for the training was generated: wget http://test-carrillo.web.cern.ch/test-carrillo/kag/exp/train20132014I.csv.zip

1. The second file is meant to measure the score of your algorithm.  

  * The file with the true hotel_clusters called int_hc_loic.txt was generated from the second half. (in this repo)

  * A file called test_2014II_isbooking.csv.zip, with the same format of test.csv was generated from the second half. wget http://test-carrillo.web.cern.ch/test-carrillo/kag/exp/test_2014II_isbooking.csv.zip
  * The procedure was: addthe id column and remove is_booking,cnt and hotel_cluster columns. 

## running the script 
"python MPA5.py int_hc_loic.txt submission_XXX.csv" will measure the score of any algorithm predicting for mytest.csv youralg(test_2014II_isbooking.csv)=submission_XXX.csv
 
The first argument is this script is the file with the true hotel clusters (id hotel_cluster)

If not extra-arguments are provided (python MPA5.py int_hc.txt) it will estimate the score of 4 benchmark examples:
- submit_top5.txt (Most Frequent clusters)
- submit_random5.txt (random integers organized in the right output format)
- submit_perfect1.txt (perfect hotel_cluster prediction in the first position)
- submit_perfect2.txt (perfect hotel_cluster prediction in the second position)

This is the output of the script python MPA5.py int_hc.txt (ran by this script)
Benchmarks:
- for Top 5: 0.073
- for Random: 0.022
- for Sample: 0.019
- for Perfect1: 1.0
- for Perfect2: 0.5

This is what we see in the Public Score (ran by kaggle score estimation)
- Most Frequent Benchmark	0.059
- Random Guess Benchmark	0.023
- Sample Submission Benchmark 	0.017

Results are compatible, there is an error due to the lower statistics available for this script and also due to the difference spliting by year in the kaggle script, here we are spliting by number of lines.
