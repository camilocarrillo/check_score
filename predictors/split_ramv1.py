import datetime
import sys
import math
from heapq import nlargest
from operator import itemgetter

def algos(s,array_s,filled,maxim,history,algoid):
    contador = 0
    allfull=True
    for entry in s:
        allfull=allfull and (entry != '')
    if allfull==True:
        if s in array_s:
            d = array_s[s]
            topitems = nlargest(maxim, sorted(d.items()), key=itemgetter(1))
            for i in range(len(topitems)):
                if topitems[i][0] in filled:
                    continue
                if len(filled) == 5:
                    return int(contador)
                filled.append(topitems[i][0])
                history.append(algoid)
                contador += 1
    return int(contador)


def fillme (s,array_s,hotel_cluster,append,checkfull):
    allfull=True
    if checkfull:
        for entry in s:
            allfull=allfull and (entry != '')
    if allfull==True:
        if  s in array_s:                               
            if hotel_cluster in array_s[s]:
                array_s[s][hotel_cluster] += append
            else:
                array_s[s][hotel_cluster] = append
        else:
            array_s[s] = dict()
            array_s[s][hotel_cluster] = append

def prepare_arrays_match():
    file_train.readline()
    
    total = 0

    
    # Calc count
    print "starting loop to fill"
    while 1:
        line = file_train.readline().strip()
        total += 1

        #if total > 1000:
        #    break
        
        if total % 100000 == 0:
            print"loading..."+str(total)

        #if line == '' or total>1000:
        if line == '':
            break
      
        column = line.split(",")

        site_name = int(column[1])
        posa_continent = int(column[2])
        user_location_country = int(column[3])
        user_location_region = int(column[4])
        user_location_city = int(column[5])
        orig_destination_distance = column[6]
        user_id = int(column[7])
        is_mobile = int(column[8])
        is_package = int(column[9])
        channel = int(column[10])

        srch_adults_cnt = int(column[13])
        srch_children_cnt = int(column[14])
        srch_rm_cnt = int(column[15])
        srch_destination_id = int(column[16])
        srch_destination_type_id = int(column[17])

        is_booking = int(column[18])
        hotel_continent = int(column[20])
        hotel_country = column[21]
        hotel_market = column[22]

        hotel_cluster = int(column[23])

        #bo 0
        #ci 11
        #co 12
        if column[11] != '':
            book_year = int(column[11][:4])
            book_month = int(column[11][5:7])
            book_day = int(column[11][8:9])
            book_season = (int(float(book_month)/3.))%4
        else:
            book_year = int(column[0][:4])
            book_month = int(column[0][5:7])
            book_day = int(column[0][8:9])
            book_season = (int(float(book_month)/3.))%4

        if column[11] != '':
            ci_year = int(column[11][:4])
            ci_month = int(column[11][5:7])
            ci_day = int(column[11][8:9])
            ci_season = (int(float(ci_month)/3.))%4


        if column[12] != '':
            co_year = int(column[12][:4])
            co_month = int(column[12][5:7])
            co_day = int(column[12][8:9])
            co_season = (int(float(co_month)/3.))%4


        if book_month<1 or book_month>12 or book_year<2012 or book_year>2015:
            #print(book_month)
            #print(book_year)
            #print(line)
            continue

        append_0 = (book_year - 2012)*12 + book_month
        if not (append_0>12 and append_0<=48):
            print(book_year)
            print(book_month)
            print(line)
            print(append_0)
            continue
        
        parabola = C3*append_0 * append_0 *append_0+C2*append_0 * append_0 + C1*append_0 + C0
        append_1 = parabola * (6.0 + 19.0*float(is_booking))
        append_2 = 2.0 * math.floor(((book_month+1)%12) / 4) + 8.0*float(is_booking)

        #1 leak untouchable
        if 1 in sequence:
            fillme((user_location_city, orig_destination_distance),array_1,hotel_cluster,append_0,True)
            
        if is_booking==1:
        #2 when the distance is missing, match by the most popular in the city of the user going to the hotel country in the same market
            if 2 in sequence and user_location_city != '' and orig_destination_distance == '' and user_id !='' and srch_destination_id != '' and hotel_country != '':
                fillme((user_id, user_location_city, srch_destination_id, hotel_country, hotel_market),array_2,hotel_cluster,append_0,False)

        #13 considering the case when the user was not in the same city!
            if 13 in sequence and orig_destination_distance != '':
                #13A 
                fillme((user_id, user_location_city, srch_destination_id, hotel_country, hotel_market),array_13A,hotel_cluster,append_0,True)
                #13B 
                if user_location_city != '' and user_id !='' and srch_destination_id != '' :
                    fillme((user_id,srch_destination_id, hotel_country, hotel_market),array_13B,hotel_cluster,append_0,False)
    
        #3 
        if 3 in sequence:
            fillme((srch_destination_id,hotel_country,hotel_market,is_package,user_id,ci_year,book_year),array_31,hotel_cluster,append_1,True)
            fillme((srch_destination_id,hotel_country,hotel_market,is_package,user_id,ci_year),array_32,hotel_cluster,append_1,True)
            fillme((srch_destination_id,hotel_country,hotel_market,is_package,user_id),array_33,hotel_cluster,append_1,True)
        #5
        if 5 in sequence:
            fillme((srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent,hotel_continent,srch_destination_type_id),array_51,hotel_cluster,append_1,True)
            fillme((srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent,hotel_continent),array_52,hotel_cluster,append_1,True)
            fillme((srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent),array_53,hotel_cluster,append_1,True)
        #4            
        if 4 in sequence:
            fillme((srch_destination_id,hotel_country,hotel_market,is_package,user_id),array_41,hotel_cluster,append_1,True)
            fillme((srch_destination_id,hotel_country,hotel_market,is_package),array_42,hotel_cluster,append_1,True)           
            #81%
            fillme((srch_destination_id,hotel_country,hotel_market),array_43,hotel_cluster,append_1,True)
            
        #6 most popular in the hotel market
        if 6 in sequence:
            fillme((hotel_market),array_6,hotel_cluster,append_2,True)

        #7 most popular in the hotel country
        if 7 in sequence:
            fillme((hotel_country),array_7,hotel_cluster,append_2,True)

        #8 popular hotel_cluster in the world
        if 8 in sequence:
            if hotel_cluster in array_8:
                array_8[hotel_cluster] += append_0
            else:
                array_8[hotel_cluster] = append_0

    file_train.close()

def gen_submission():
    outfile_name = "sequence_"+str(sequence[0])+str(sequence[1])+str(sequence[2])+str(sequence[3])+str(sequence[4])+str(sequence[5])+str(sequence[6])+str(sequence[7])
    #outfile_name += "_maxs_"+str(maxs[1])+str(maxs[2])+"_"+str(maxs[13][1])+str(maxs[13][2])+str(maxs[13][3])+"_"+str(maxs[3][1])+str(maxs[3][2])+str(maxs[3][3])+"_"+str(maxs[4][1])+str(maxs[4][2])+str(maxs[4][3])+"_"+str(maxs[5][1])+str(maxs[5][2])+str(maxs[5][3])+"_"+str(maxs[6])+str(maxs[7])+str(maxs[8])
    #outfile_name += "_C3_"+str(C3)+"_C2_"+str(C2)+"_C1_"+str(C1)+"_C0_"+str(C0)
    outfile_name += "_5322_.csv"

    print "file_train_name:",file_train_name
    print "file_test_name:",file_test_name
    print "outfile_name:",outfile_name

    outfile = open(pathout+outfile_name, "w")
    histofile = open(pathout+"histo_"+outfile_name, "w")
    file_test = open(file_test_name, "r") 
    file_test.readline()
    
    count = [0,0,0,[0,0,0,0],[0,0,0,0],[0,0,0,0],0,0,0,0,0,0,0,[0,0,0,0]]

    outfile.write("id,hotel_cluster\n")
    histofile.write("id,algo\n")

    print "starting loop to write"
    while 1:
        line = file_test.readline().strip()

        if count[0] % 100000 == 0:
            print 'writings...'+str(count[0])

        if line == '':
            break

        column = line.split(",")
        id = column[0]
        
        #bo 1
        #ci 12 
        #co 13

        book_year = int(column[1][:4])
        book_month = int(column[1][5:7])
        book_day = int(column[1][8:10])
        book_season = (int(float(book_month)/3.))%4

        if column[12] != "":
            ci_year = int(column[12][:4])
            ci_month = int(column[12][5:7])
            ci_day = int(column[12][8:10])
            ci_season = (int(float(ci_month)/3.))%4


        if column[13] != "":
            co_year = int(column[13][:4])
            co_month = int(column[13][5:7])
            co_day = int(column[13][8:10])
            co_season = (int(float(co_month)/3.))%4


        site_name = int(column[2])
        posa_continent = int(column[3])
        user_location_country = int(column[4])
        user_location_region = int(column[5])
        user_location_city = int(column[6])
        orig_destination_distance = column[7]
        user_id = int(column[8])
        is_mobile = int(column[9])
        is_package = int(column[10])
        channel = int(column[11])
        
        srch_adults_cnt = int(column[14])
        srch_children_cnt = int(column[15])
        srch_rm_cnt = int(column[16])
        srch_destination_id = int(column[17])
        srch_destination_type_id = int(column[18])

        hotel_continent = int(column[19])
        hotel_country = column[20]
        hotel_market = column[21]

        filled = []
        history = []
        
        for round in range(0,10):
            if len(filled) == 5:
                break
            #print round
            if sequence[round]==1:
                #1 this is the leak
                count[1] += algos((user_location_city, orig_destination_distance),array_1,filled,maxs[1],history,sequence[round])
                
            if sequence[round]==2:
                #2 distance missing check queries from the same uid at the same country,market,,ulc,destid,hco,hma
                if orig_destination_distance == '':
                    count[2] += algos((user_id, user_location_city, srch_destination_id, hotel_country, hotel_market),array_2,filled,maxs[2],history,sequence[round])
                 

            if sequence[round]==13:
                #13 considering the case when the user was not in the same city
                s00 = (user_id, user_location_city, srch_destination_id, hotel_country, hotel_market)
                s01 = (user_id,srch_destination_id, hotel_country, hotel_market)
                if s01 in array_13B and s00 not in array_13A:
                    count[13][1] += algos(s01,array_13B,filled,maxs[13][1],history,sequence[round])

   
            if sequence[round]==3:
                #3                   (srch_destination_id,hotel_country,hotel_market,is_package,user_id,ci_year,book_year 
                count[3][1] += algos((srch_destination_id,hotel_country,hotel_market,is_package,user_id,ci_year,book_year),array_31,filled,maxs[3][1],history,sequence[round])
                count[3][2] += algos((srch_destination_id,hotel_country,hotel_market,is_package,user_id,ci_year),array_32,filled,maxs[3][2],history,sequence[round])
                count[3][3] += algos((srch_destination_id,hotel_country,hotel_market,is_package,user_id),array_33,filled,maxs[3][3],history,sequence[round])

            #5##CHECK WITH ARRAY_51 IN ALL I JUST GOT 53 IN JULY!
            if sequence[round]==5:
                count[5][1] += algos((srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent,hotel_continent,srch_destination_type_id),array_51,filled,maxs[5][1],history,sequence[round])
                count[5][2] += algos((srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent,hotel_continent),array_52,filled,maxs[5][2],history,sequence[round])
                count[5][3] += algos((srch_destination_id,hotel_country,hotel_market,is_package,user_id,posa_continent),array_53,filled,maxs[5][3],history,sequence[round])

            #4 THIS IS THE ALGO TO IMPROVE!
            if sequence[round]==4:
                if hotel_continent:        
                    count[4][1] += algos((srch_destination_id,hotel_country,hotel_market,is_package,user_id),array_41,filled,maxs[4][1],history,sequence[round])
                    count[4][2] += algos((srch_destination_id,hotel_country,hotel_market,is_package),array_42,filled,maxs[4][2],history,sequence[round])
                count[4][3] += algos((srch_destination_id,hotel_country,hotel_market),array_43,filled,maxs[4][3],history,sequence[round])
                   
            #6
            if sequence[round]==6:
                count[6] += algos((hotel_market),array_6,filled,maxs[6],history,sequence[round])

           #7
            if sequence[round]==7:
                count[7] += algos((hotel_country),array_7,filled,maxs[7],history,sequence[round])

            #8
            if sequence[round]==8:
                for i in range(len(top_world_clusters)):
                    if top_world_clusters[i][0] in filled:
                        continue
                    if len(filled) == maxs[8]:
                        break
                    filled.append(top_world_clusters[i][0])
                    history.append(sequence[round])
                    count[8] += 1

            #9 -1 missing entries
            if sequence[round]==9:
                for i in range(1,6):
                    if len(filled) == 5:
                        break
                    filled.append(-1*i)
                    history.append(sequence[round])
                    count[9] += 1

        count[0] += 1
        assert(len(filled)==5)
        assert(count[0]*5==count[1]+count[2]+count[13][1]+count[13][2]+count[13][3]+count[3][1]+count[3][2]+count[3][3]+count[4][1]+count[4][2]+count[4][3]+count[5][1]+count[5][2]+count[5][3]+count[6]+count[7]+count[8]+count[9])
        outfile.write(str(id)+","+str(filled[0])+" "+str(filled[1])+" "+str(filled[2])+" "+str(filled[3])+" "+str(filled[4])+"\n")
        histofile.write(str(id)+","+str(history[0])+" "+str(history[1])+" "+str(history[2])+" "+str(history[3])+" "+str(history[4])+"\n")


    outfile.close()
    histofile.close()
    file_test.close()
    d=float(count[0]*5)
    count[5][0]=count[5][1]+count[5][2]+count[5][3]
    count[4][0]=count[4][1]+count[4][2]+count[4][3]
    count[3][0]=count[3][1]+count[3][2]+count[3][3]
    count[13][0]=count[13][1]+count[13][2]+count[13][3]
    fractions = [float("{0:.3f}".format(100.*float(count[0]*5)/d)),float("{0:.3f}".format(100.*float(count[1])/d)),float("{0:.3f}".format(100.*float(count[2])/d)),[float("{0:.3f}".format(100.*float(x)/d)) for x in count[3]],[float("{0:.3f}".format(100.*float(x)/d)) for x in count[4]],[float("{0:.3f}".format(100.*float(x)/d)) for x in count[5]],float("{0:.3f}".format(100.*float(count[6])/d)),float("{0:.3f}".format(100.*float(count[7])/d)),float("{0:.3f}".format(100.*float(count[8])/d)),float("{0:.3f}".format(100.*float(count[9])/d)),[float("{0:.3f}".format(100.*float(x)/d)) for x in count[13]]]
    print count
    print fractions


measure_score = False
speedy = int(sys.argv[1])

print "measure_score ",measure_score
print "speedy ",speedy
#path = '/afs/cern.ch/user/c/carrillo/eoscarrillo/input/'
#path = '/data08/carrillo/input/'
#path = '/home/carrillo/kaggle/data/'
path = "/afs/cern.ch/user/c/carrillo/workspace/input/"

pathout = "/afs/cern.ch/user/c/carrillo/workspace/expout/"
#pathout = ""

file_train_name = ""

if measure_score:
    if speedy==1:
        file_train_name = path+'train2014_05-06.csv' 
        file_test_name = path+'test_201407_isbooking.csv'
    if speedy==0:
        file_train_name = path+'train20132014I.csv'
        file_test_name = path+'test_from_train2014-II_isbooking_known_uid.csv'
else:
    file_train_name = path+'train.csv'
    file_test_name = path+'test.csv'

print "file_test_name:",file_test_name
print "file_train_name:",file_train_name

maxs = [0,5,5,[0,5,5,5],[0,5,5,5],[0,5,5,5],5,5,5,0,0,0,0,[0,5,5,5]]
#sequence = [1,2,13,3,5,4,6,7,8]
#sequence = [1,2,13,3,4,6,7,8]
#sequence = [1,2,13,3,4,0,0,0,0,9]
#sequence = [6,7,8,0,0,0,0,0,0,9]
sequence = [0,0,0,0,0,0,0,0,0,9]
for i in range(0,len(sys.argv)-2):
    print i
    if sys.argv[i+2]:
        sequence[i]=int(sys.argv[i+2])
print sequence
print maxs
C3=1.0
C2=0.0
C1=0.0
C0=0.0

array_1 = dict()
array_2 = dict()
array_31 = dict()
array_32 = dict()
array_33 = dict()
array_13A = dict()
array_13B = dict()
array_13C = dict()
array_41 = dict()
array_42 = dict()
array_43 = dict()
array_51 = dict()
array_52 = dict()
array_53 = dict()
array_6 = dict()
array_7 = dict()
array_8 = dict()

file_train = open(file_train_name, "r") 
print sequence     
prepare_arrays_match()
top_world_clusters = nlargest(5, sorted(array_8.items()), key=itemgetter(1))
print sequence
gen_submission()

del array_1
del array_2
del array_31
del array_32
del array_33
del array_13A
del array_13B
del array_13C
del array_41
del array_42
del array_43
del array_51
del array_52
del array_53
del array_6
del array_7
del array_8

