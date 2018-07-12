import Log_Parser
import Log_Analizer
import Sniffer
import argparse
import time

LOG_PIS = r'C:\Users\Owner\PycharmProjects\SIEM\Ping_Sweep.txt'
LOG_POS = r'C:\Users\Owner\PycharmProjects\SIEM\Port_Scan.txt'
LOG_SPO = r'C:\Users\Owner\PycharmProjects\SIEM\Suspicious_Port.txt'
LOG_SNIFF = r'C:\Users\Owner\PycharmProjects\SIEM\Sniff_Log.txt'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('op', type=str, choices=['parse', 'analise', 'sniff'], help='Enter a option')
    parser.add_argument('--file', type=str, choices=[LOG_SPO, LOG_POS, LOG_PIS, LOG_SNIFF], help='Enter a file for options "sniff" and "parse"')
    parser.add_argument('--func', type=str, choices=['spo', 'pos', 'pis', 'pist', 'all'], help='Enter a function for option "analise" to '
                'detect attack: spo - Specific Port; pos - Port Scan; pis - Ping Swip; pist - Ping Swip with time; all - all sort of atttacks')
    parser.add_argument('--port', type=int, help='Enter a port for detect Specific Port attack')
    parser.add_argument('--time', type=int, help='Enter a time in seconds for time differences to Ping Sweep attack conditions')


    args = parser.parse_args()

    if args.op == 'parse':
        Log_Parser.readLogFile(args.file)
    elif args.op == 'sniff':
        with open(args.file, 'a') as f:
            Sniffer.sniffPackets(f)
    elif args.op == 'analise':
        if args.func == 'spo':
            Log_Analizer.specificPort(args.port)
        elif args.func == 'pos':
            Log_Analizer.portScan()
        elif args.func == 'pis':
            Log_Analizer.pingSweep()
        elif args.func == 'pist':
            Log_Analizer.pingSweepWithTime(args.time)
        elif args.func == 'all':
            while True:
                Log_Analizer.specificPort(args.port)
                Log_Analizer.portScan()
                Log_Analizer.pingSweep()
                Log_Analizer.pingSweepWithTime(args.time)
                time.sleep(5)
                continue

if __name__ == '__main__':
    main()