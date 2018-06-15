import Log_Parser
import Log_Analizer
#LOG_FILE = r'C:\Users\Owner\PycharmProjects\SIEM\Ping_Sweep.txt'
LOG_FILE = r'C:\Users\Owner\PycharmProjects\SIEM\Port_Scan.txt'
#LOG_FILE = r'C:\Users\Owner\PycharmProjects\SIEM\Suspicious_Port.txt'

def main():

    Log_Parser.readLogFile(LOG_FILE)
    port_lst = [444, 445]
    print Log_Analizer.specificPort(port_lst)
#    Log_Analizer.portScan()
#    Log_Analizer.pingSweep()
    Log_Analizer.pingSweepWithTime(10)

if __name__ == '__main__':
    main()