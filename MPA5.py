import commands
import random
import math
import sys 

def loadTrue (filename,true):
    del true[:]
    f = open(filename, 'r')
    first = True
    for line in f:
        if first == False:
            true.append(int(line.split()[1]))
        else:
            first = False
    #print len(true)
    return

def loadPrediction (filename,predictions):
    del predictions[:]
    f = open(filename, 'r')
    lines = 1
    for line in f:
        #print line
        if lines != 1:
            hotel_clusters = line.split(',')[1]
            array_hotel_clusters = []
            array_hotel_clusters[:] = [int(i) for i in hotel_clusters.split(' ')]
            predictions.append(array_hotel_clusters)
        lines=lines+1
    #print len(predictions)
    return

def compute_score (true,predictions):
    assert (len(true)==len(predictions))
    #print true[0],predictions[0]
    #i=0
    P = 0
    
    for i in range(0,len(predictions)):

        #if i % 100000 == 0:
        #    print('Computing score {} lines...'.format(i))

        prediction=predictions[i]
        for j in range(0,len(prediction)):
            if(prediction[j] == true[i]):
                P+=(1/float(j+1.))
                break 
        #if (i==0):
        #    print "\n"
        #if (i<100):
        #    print "i:",i,"true:",true[i],"prediction:",prediction,"P:",P
    
    len_predictions=float(len(predictions))
    score = P/len_predictions
    #print P,"/",len_predictions
    #error = math.sqrt(score(1.-score)/len_predictions)
    #print score,"+/-",error
    #print score
    return score
    #return 1000*(score-0.5)

true_hotel_cluster = []
predictioninput = []

true_filename=sys.argv[1]
print "true file:"+true_filename
loadTrue(true_filename,true_hotel_cluster)


if(len(sys.argv)==1):
    print "please provide the first input file with the true hotel clusters format (id hotel_cluster) "

elif(len(sys.argv)==2):
    print "Only true hotel_clusters provided, running trivial examples, if you want to analyze other file(s) provide it as extra argument(s)"
    print "for Benchmarks: measured (expected)"
#benchmark 1
    loadPrediction('submit_top5.txt',predictioninput)
    print "for Top 5:",compute_score(true_hotel_cluster,predictioninput)," (0.059)"

#benchmark 2
    loadPrediction('submit_random5.txt',predictioninput)
    print "for Random:",compute_score(true_hotel_cluster,predictioninput)," (0.023)"
    
#benchmark 3
    loadPrediction('submit_sample.txt',predictioninput)
    print "for Sample:",compute_score(true_hotel_cluster,predictioninput)," (0.017)"

#benchmark 4
    loadPrediction('submit_perfect1.txt',predictioninput)
    print "for Perfect1:",compute_score(true_hotel_cluster,predictioninput)," (1.0)"

#benchmark 5
    loadPrediction('submit_perfect2.txt',predictioninput)
    print "for Perfect2:",compute_score(true_hotel_cluster,predictioninput)," (0.5)"

elif len(sys.argv)>2:
    print "\nInput Files:"
    for argument in sys.argv[2:]:
        loadPrediction(argument,predictioninput)
        print argument,compute_score(true_hotel_cluster,predictioninput)

