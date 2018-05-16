import mysql.connector
from mysql.connector import errorcode

user = 'root'
password = 'P@ssw0rd'
host = '192.168.75.133'
database = 'siem'
LOG_FILE = r'C:\Users\Owner\Downloads\Drive_Cyber_Course\Python\20 - SIEM\Port_Scan.txt'
KEYS = ['DATE', 'SRC_IP', 'DST_IP', 'PORT', 'ACTION', 'PROTOCOL']
PORTS = {'21' : 'FTP', '22' : 'SSH', '23' : 'TELNET', '25' : 'SMTP' , '67' : 'DHCP' , '53'  : 'DNS' , '80' : 'HTTP', '445' : 'SMB' ,'443' : 'HTTPS'}

def main():
    cnx, cursor = ConnectToDB()
    query = ("SELECT * FROM fwlogs")
    cursor.execute(query)
    result = cursor.fetchall()
    for line in result:
        print line[2]
    cursor.close()
    cnx.close()
 #   readLogFile()
#    commitLogFileToDB()

def lineToValue(line):
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

def readLogFile():
    with open(LOG_FILE) as file:
        for line in file:
            line = line[:len(line)-1]
            values = lineToValue(line)
            protocol = portToProtocol(values[3])
            values.append(protocol)
            dic = dict(zip(KEYS, values))
            cnx, cursor = ConnectToDB()
            InsertToDB(dic, cnx, cursor)
            print dic
 #   return content

def InsertToDB(log, cnx, cursor):
    add_log = ("""INSERT INTO fwlogs
                (ID, DATE, SRC_IP, DST_IP, PORT, PROTOCOL, ACTION)
                VALUES (NULL, %(DATE)s, %(SRC_IP)s, %(DST_IP)s, %(PORT)s, %(PROTOCOL)s, %(ACTION)s)""")
    cursor.execute(add_log, log)
    cnx.commit()

def ConnectToDB():
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

def AnalyzeSusPort():
    cnx, cursor = ConnectToDB()
    query = ("SELECT SRC_IP FROM fwlogs WHERE PORT IN ({})".format(','))
    cursor.execute(query)
    query_result = []
    for line in cursor:
        query_result.append(line[0])
    cursor.close()
    cnx.close()
    return set(query_result)

if __name__ == '__main__':
    main()

