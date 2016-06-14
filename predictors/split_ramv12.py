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
        assert(len(column)==24)

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
            book_week = (book_month-1)*4+(book_day/7+1)
        else:
            book_year = int(column[0][:4])
            book_month = int(column[0][5:7])
            book_day = int(column[0][8:9])
            book_season = (int(float(book_month)/3.))%4
            book_week = (book_month-1)*4+(book_day/7+1)

        if column[11] != '':
            ci_year = int(column[11][:4])
            ci_month = int(column[11][5:7])
            ci_day = int(column[11][8:9])
            ci_season = (int(float(ci_month)/3.))%4
            ci_week = (ci_month-1)*4+(ci_day/7+1)


        if column[12] != '':
            co_year = int(column[12][:4])
            co_month = int(column[12][5:7])
            co_day = int(column[12][8:9])
            co_season = (int(float(co_month)/3.))%4
            co_week = (co_month-1)*4+(co_day/7+1)


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
            if is_booking:
                fillme((-31-),array_31,hotel_cluster,append_1,True)
                fillme((-32-),array_32,hotel_cluster,append_1,True)
                fillme((-33-),array_33,hotel_cluster,append_1,True)

        #4
        if 4 in sequence:
            if book_year == 2014:
                fillme((-41-),array_41,hotel_cluster,append_1,True)
                fillme((-42-),array_42,hotel_cluster,append_1,True)
                fillme((-43-),array_43,hotel_cluster,append_1,True)

        #5
        if 5 in sequence:
            fillme((-51-),array_51,hotel_cluster,append_1,True)
            fillme((-52-),array_52,hotel_cluster,append_1,True)
            fillme((-53-),array_53,hotel_cluster,append_1,True)
            
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
    a0len=len(sys.argv[0])
    
    outfile_name = str(sys.argv[0][a0len-5])+str(sys.argv[0][a0len-4])+"_"+str(sys.argv[1])+"_"+str(sys.argv[2])+"_"+str(sys.argv[3])+"_sequence_"+str(sequence[0])+str(sequence[1])+str(sequence[2])+str(sequence[3])+str(sequence[4])+str(sequence[5])+str(sequence[6])+str(sequence[7])+str(sequence[8])+"-52-.csv"

    print "file_train_name:",file_train_name
    print "file_test_name:",file_test_name
    print "outfile_name:",outfile_name

    outfile = open(pathout+outfile_name, "w")
    #histofile = open(pathout+"histo_"+outfile_name, "w")
    file_test = open(file_test_name, "r") 
    file_test.readline()
    
    count = [0,0,0,[0,0,0,0],[0,0,0,0],[0,0,0,0],0,0,0,0,0,0,0,[0,0,0,0]]

    outfile.write("id,hotel_cluster\n")
    #histofile.write("id,algo\n")

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
        book_week = (book_month-1)*4+(book_day/7+1)

        if column[12] != "":
            ci_year = int(column[12][:4])
            ci_month = int(column[12][5:7])
            ci_day = int(column[12][8:10])
            ci_season = (int(float(ci_month)/3.))%4
            ci_week = (ci_month-1)*4+(ci_day/7+1)


        if column[13] != "":
            co_year = int(column[13][:4])
            co_month = int(column[13][5:7])
            co_day = int(column[13][8:10])
            co_season = (int(float(co_month)/3.))%4
            co_week = (co_month-1)*4+(co_day/7+1)


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

            #3
            if sequence[round]==3:
                count[3][1] += algos((-31-),array_31,filled,maxs[3][1],history,sequence[round])
                count[3][2] += algos((-32-),array_32,filled,maxs[3][2],history,sequence[round])
                count[3][3] += algos((-33-),array_33,filled,maxs[3][3],history,sequence[round])

            #4
            if sequence[round]==4:
                count[4][1] += algos((-41-),array_41,filled,maxs[4][1],history,sequence[round])
                count[4][2] += algos((-42-),array_42,filled,maxs[4][2],history,sequence[round])
                count[4][3] += algos((-43-),array_43,filled,maxs[4][3],history,sequence[round])

            #5
            if sequence[round]==5:
                count[5][1] += algos((-51-),array_51,filled,maxs[5][1],history,sequence[round])
                count[5][2] += algos((-52-),array_52,filled,maxs[5][2],history,sequence[round])
                count[5][3] += algos((-53-),array_53,filled,maxs[5][3],history,sequence[round])

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
        #histofile.write(str(id)+","+str(history[0])+" "+str(history[1])+" "+str(history[2])+" "+str(history[3])+" "+str(history[4])+"\n")


    outfile.close()
    #histofile.close()
    file_test.close()
    d=float(count[0]*5)
    count[5][0]=count[5][1]+count[5][2]+count[5][3]
    count[4][0]=count[4][1]+count[4][2]+count[4][3]
    count[3][0]=count[3][1]+count[3][2]+count[3][3]
    count[13][0]=count[13][1]+count[13][2]+count[13][3]
    fractions = [float("{0:.3f}".format(100.*float(count[0]*5)/d)),float("{0:.3f}".format(100.*float(count[1])/d)),float("{0:.3f}".format(100.*float(count[2])/d)),[float("{0:.3f}".format(100.*float(x)/d)) for x in count[3]],[float("{0:.3f}".format(100.*float(x)/d)) for x in count[4]],[float("{0:.3f}".format(100.*float(x)/d)) for x in count[5]],float("{0:.3f}".format(100.*float(count[6])/d)),float("{0:.3f}".format(100.*float(count[7])/d)),float("{0:.3f}".format(100.*float(count[8])/d)),float("{0:.3f}".format(100.*float(count[9])/d)),[float("{0:.3f}".format(100.*float(x)/d)) for x in count[13]]]
    print count
    print fractions


#Main Code

print sys.argv



#argv[2]
assert(str(sys.argv[2])=="batch" or str(sys.argv[2])=="pcwits" or  str(sys.argv[2])=="dell" or  str(sys.argv[2])=="lx")
path = '/home/carrillo/kaggle/data/'
pathout = ""
if str(sys.argv[2])=="batch":
    path = '/afs/cern.ch/user/c/carrillo/workspace/input/'
    pathout = "/afs/cern.ch/user/c/carrillo/workspace/expout/"
if str(sys.argv[2])=="lx":
    path = '/afs/cern.ch/user/c/carrillo/workspace/input/'
    pathout = ""   
if str(sys.argv[2])=="pcwits":
    path = '/data08/carrillo/input/'
    pathout = ""
if str(sys.argv[2])=="dell":
    path = '/home/carrillo/kaggle/data/'
    pathout = ""
file_train_name = ""

#argv[3]
measure_score = True
assert(str(sys.argv[3])=="True" or str(sys.argv[3])=="False")
if str(sys.argv[3])=="True":
    measure_score = True
if str(sys.argv[3])=="False":
    measure_score = False
speedy = int(sys.argv[1])

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
sequence = [0,0,0,0,0,0,0,0,0,9]
for i in range(0,len(sys.argv)-4):
    print i
    if sys.argv[i+4]:
        sequence[i]=int(sys.argv[i+4])
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
