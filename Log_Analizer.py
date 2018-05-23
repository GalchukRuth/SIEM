from Log_Parser import *
SRC_IP = 0
DST_IP = 1

#get all source IP addresses that connecting on port 444 or 445
def specificPort(port_lst):
    cnx, cursor = connectToDB()
    query = ("SELECT DISTINCT SRC_IP, PORT FROM fwlogs WHERE PORT={} OR PORT={}".format(port_lst[0],port_lst[1]))
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    if len(result) != 0:
        for line in result:
            print 'source IP :', line[0], '-> port :', line[1]
        return True
    else:
        return False

#port scan defined by any IP address that trying to connect another computer in more than 10 different ports
def portScan():
    cnx, cursor = connectToDB()
    query = ("SELECT DISTINCT SRC_IP, DST_IP, PORT FROM fwlogs")
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    dic = {}
    for line in result:
        if line[:2] in dic.keys():
            dic[line[:2]] += 1
        else:
            dic[line[:2]] = 1
    for key, value in dic.iteritems():
        if value >= 10:
            print 'source IP :', key[0], '->', value, 'ports'

#ping sweep defined by same IP address that trying to get more than 10 different IP addresses with ping (Here it will be port 0)
def pingSweep():
    cnx, cursor = connectToDB()
    query = ("SELECT DISTINCT SRC_IP, DST_IP FROM fwlogs WHERE PORT = 0")
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    dic = {}
    for line in result:
        if line[SRC_IP] in dic.keys():
            dic[line[SRC_IP]] += 1
        else:
            dic[line[SRC_IP]] = 1
    for key, value in dic.iteritems():
        if value >= 10:
            print 'source IP :', key, '->', value, 'times'