from Log_Parser import *
SRC_IP = 0
DST_IP = 1

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
def pingSweep():
    cnx, cursor = connectToDB()
    query = ("SELECT SRC_IP, DST_IP FROM fwlogs WHERE PORT = 0")
    cursor.execute(query)
    result = cursor.fetchall()
    dic = {}
    lst_values = []
    for line in result:
        if line[SRC_IP] in dic.keys():
            lst_values.append(line[DST_IP])
            dic[line[SRC_IP]] = lst_values
            if len(lst_values) == 10:
                print line[SRC_IP], '->', len(lst_values)
        else:
            lst_values = []
            lst_values.append(line[DST_IP])
            dic[line[SRC_IP]] = lst_values