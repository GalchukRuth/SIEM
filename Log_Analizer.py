from Log_Parser import *

#get all source IP addresses that connecting on port 444 or 445
def spcificPort(port_lst):
    cnx, cursor = connectToDB()
    query = ("SELECT DISTINCT SRC_IP FROM fwlogs WHERE PORT={} OR PORT={}".format(port_lst[0],port_lst[1]))
    cursor.execute(query)
    result = cursor.fetchall()
    for line in result:
        print line[0]
    cursor.close()
    cnx.close()

def portScan():
    cnx, cursor = connectToDB()
    query = ("SELECT DISTINCT SRC_IP, DST_IP, PORT FROM fwlogs")
    cursor.execute(query)
    result = cursor.fetchall()
    dic = {}
    for line in result:
        if line[:2] in dic.keys():
            dic[line[:2]] += 1
        else:
            dic.update({line[:2] : 1})
    for k, v in dic.iteritems():
        if v >= 10:
            print k[0], '->', v
    cursor.close()
    cnx.close()
#
def portScan2():
    cnx, cursor = connectToDB()
    query = ("SELECT DISTINCT SRC_IP, DST_IP, PORT FROM fwlogs")
    cursor.execute(query)
    result = cursor.fetchall()
    count = 0
    for i in range(len(result)-1):
        print i, result[i]
        if (result[i][0] == result[i+1][0]) & (result[i][1] == result[i+1][1]):
#            count += 1
 #           if count == 10:
  #              print '\t', result[i][0], result[i][1], ' -> ', count
   #             count = 0
            print '\ty'
        elif (result[i][0] != result[i+1][0]) | (result[i][1] != result[i+1][1]):
            print '\tn'
    cursor.close()
    cnx.close()

