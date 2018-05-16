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

#
def portScan():
    cnx, cursor = connectToDB()
    query = ("SELECT * FROM fwlogs")
    cursor.execute(query)
    result = cursor.fetchall()
    for line in result:
        print line[0]
    cursor.close()
    cnx.close()

