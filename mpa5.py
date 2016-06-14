import commands
import random
import math
import sys 
import collections

def loadTrue (filename,ide,month,true):
    del true[:]
    del month[:]
    del ide[:]
    f = open(filename, 'r')
    first = True
    for line in f:
        if first == False:
            ide.append(int(line.split()[0]))
            true.append(int(line.split()[1]))
            #print line
            month.append(int(line.split()[2]))
        else:
            first = False
    return

def loadPrediction (filename,predictions,ide):
    del predictions[:]
    f = open(filename, 'r')
    lines = 1
    for line in f:
        if lines != 1:
            #print lines,line.split(',')[0]
            #if lines < 100:
            #    print "comp:",line.split(',')[0],ide[lines]-2
            #assert( int(line.split(',')[0]) == int(ide[lines]-2) )
            
            hotel_clusters = line.split(',')[1]
            array_hotel_clusters = []
            array_hotel_clusters[:] = [int(i) for i in hotel_clusters.split(' ')]
            predictions.append(array_hotel_clusters)
        lines=lines+1
    return

def compute_score (true,predictions,month):
    assert (len(true)==len(predictions) and len(predictions) == len(month))
    P = [0] * 13
    
    for i in range(0,len(predictions)):
        prediction=predictions[i]
        for j in range(0,len(prediction)):
            if(prediction[j] == true[i]):
                P[0]+=(1/float(j+1.))
                P[month[i]]+=(1/float(j+1.))
                break 
    
    len_predictions=float(len(predictions))
    counter=collections.Counter(month)
    score = [0] * 13
    score[0] = (P[0]/len_predictions)
    for m in range(1,13):
        if counter[m]!=0:
            score[m] = (P[m]/counter[m])
    formattedScore = [ '%.4f' % elem for elem in score ]
    print formattedScore
    print score[0]

    score[0] = 1000*((P[0]/len_predictions)-0.5)
    for m in range(1,13):
        if counter[m]!=0:
            score[m] = 1000*((P[m]/counter[m])-0.5)
    formattedScore = [ '%.3f' % elem for elem in score ]
    print formattedScore
    return score[0]


ide = []
month = []
true_hotel_cluster = []
predictioninput = []

true_filename=sys.argv[1]
print "true file:"+true_filename
loadTrue(true_filename,ide,month,true_hotel_cluster)


if(len(sys.argv)==1):
    print "please provide the first input file with the true hotel clusters format (id hotel_cluster) "

elif(len(sys.argv)==2):
    print "Only true hotel_clusters provided, running trivial examples, if you want to analyze other file(s) provide it as extra argument(s)"
    print "for Benchmarks: measured (expected)"
#benchmark 1
    loadPrediction('submit_top5.txt',predictioninput,ide)
    print "for Top 5:",compute_score(true_hotel_cluster,predictioninput,month)," (0.059)"

#benchmark 2
    loadPrediction('submit_random5.txt',predictioninput,ide)
    print "for Random:",compute_score(true_hotel_cluster,predictioninput,month)," (0.023)"
    
#benchmark 3
    loadPrediction('submit_sample.txt',predictioninput,ide)
    print "for Sample:",compute_score(true_hotel_cluster,predictioninput,month)," (0.017)"

#benchmark 4
    loadPrediction('submit_perfect1.txt',predictioninput,ide)
    print "for Perfect1:",compute_score(true_hotel_cluster,predictioninput,month)," (1.0)"

#benchmark 5
    loadPrediction('submit_perfect2.txt',predictioninput,ide)
    print "for Perfect2:",compute_score(true_hotel_cluster,predictioninput,month)," (0.5)"

elif len(sys.argv)>2:
    print "\nAnalyzing Input Files:",sys.argv[2:]
    for argument in sys.argv[2:]:
        loadPrediction(argument,predictioninput,ide)
        print argument,compute_score(true_hotel_cluster,predictioninput,month)

