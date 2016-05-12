import commands
from numpy import arange,array,ones,linalg
import random
import math
import numpy as np
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
    print len(true)
    return

def loadPrediction (filename,predictions):
    f = open(filename, 'r')
    lines = 1
    for line in f:
        if lines != 1:
            id=line.split(',')[0]
            hotel_clusters = line.split(',')[1]
            array_hotel_clusters = []
            array_hotel_clusters[:] = [int(i) for i in hotel_clusters.split(' ')]
            predictions.append(array_hotel_clusters)
        lines=lines+1
    print len(predictions)
    return

def compute_score (true,predictions):
    sum = 0.
    #print true[0],predictions[0]
    #i=0
    P = 0
    
    for i in range(0,len(predictions)):
        prediction=predictions[i]
        for j in range(0,len(prediction)):
            if(prediction[j] == true[i]):
                #P+=(1/float(j+1.))/float(len(prediction)
                P+=(1/float(j+1.))
        #if (i<10):
            #print int(100*random.random())," ",int(100*random.random())," ",int(100*random.random())," ",int(100*random.random())," ",int(100*random.random())          
            #print "i:",i,"prediction:",prediction,"len(prediction)",len(prediction),"true:",true[i],"P:",P
    
    len_predictions=float(len(predictions))
    score = P/len_predictions
    #error = math.sqrt(score(1.-score)/len_predictions)
    #rint score,"+/-",error
    print score
    return 

true_hotel_cluster = []
predictiontop5 = []
predictionrandom5 = []
predictioninput = []
#loadTrue("int_hc_100.txt",true)
#loadPrediction('submit_top5_100.txt',prediction)
loadTrue("int_hc.txt",true_hotel_cluster)
loadPrediction('submit_top5.txt',predictiontop5)
loadPrediction('submit_random5.txt',predictionrandom5)
print "for Top 5:"
compute_score(true_hotel_cluster,predictiontop5)
print "for Random:"
compute_score(true_hotel_cluster,predictionrandom5)
print "for "+sys.argv[1]
loadPrediction(sys.argv[1],predictioninput)
compute_score(true_hotel_cluster,predictioninput)

