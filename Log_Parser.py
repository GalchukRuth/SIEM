import mysql.connector
from mysql.connector import errorcode

user = 'root'
password = 'P@ssw0rd'
host = '192.168.75.133'
database = 'siem'
LOG_FILE = r'C:\Users\Owner\Downloads\Drive_Cyber_Course\Python\20 - SIEM\Port_Scan.txt'
#LOG_FILE = r'C:\Users\Owner\Downloads\Drive_Cyber_Course\Python\20 - SIEM\Port_Scan.txt'
KEYS = ['DATE', 'SRC_IP', 'DST_IP', 'PORT', 'ACTION', 'PROTOCOL']
PORTS = {'21' : 'FTP', '22' : 'SSH', '23' : 'TELNET', '25' : 'SMTP' , '67' : 'DHCP' , '53'  : 'DNS' , '80' : 'HTTP', '445' : 'SMB' ,'443' : 'HTTPS'}


#get list values from line
def lineToListValues(line):
    lst_values = line.split(' ')
    lst_values[0] = lst_values[0] + ' ' + lst_values[1]
    lst_values.remove(lst_values[1])
    return lst_values

#get a port number and return protocol name
def portToProtocol(port):
    for key in PORTS:
        if port == key:
            return PORTS[key]
        else:
            return 'UNKNOWN'

#get dictionary from log file and insert it into the DB
def readLogFile():
    cnx, cursor = connectToDB()
    deleteFromDB(cnx, cursor)
    with open(LOG_FILE) as file:
        for line in file:
            line = line[:len(line)-1]
            values = lineToListValues(line)
            protocol = portToProtocol(values[3])
            values.append(protocol)
            dic = dict(zip(KEYS, values))
            insertToDB(dic, cnx, cursor)

#insert log file to Database
def insertToDB(log, cnx, cursor):
    add_log = ("""INSERT INTO fwlogs
                (ID, DATE, SRC_IP, DST_IP, PORT, PROTOCOL, ACTION)
                VALUES (NULL, %(DATE)s, %(SRC_IP)s, %(DST_IP)s, %(PORT)s, %(PROTOCOL)s, %(ACTION)s)""")
    cursor.execute(add_log, log)
    cnx.commit()

def deleteFromDB(cnx, cursor):
    add_log = ("""TRUNCATE TABLE fwlogs""")
    cursor.execute(add_log)
    cnx.commit()

def connectToDB():
    try:
        cnx = mysql.connector.connect(user=user, password=password,
                                      host=host, database=database)
        return cnx, cnx.cursor(buffered=True)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None