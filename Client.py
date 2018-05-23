from Log_Parser import *
from Log_Analizer import *


def main():

    readLogFile()
    port_lst = [444, 445]
#    spcificPort(port_lst)
    portScan()
  #  pingSweep()

if __name__ == '__main__':
    main()