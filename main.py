from re import S
import socket;
import sys;
import pyfiglet;
import threading
import math

def PortScan(target, close,start,incr,end):
    try:
        for port in range(start,end,incr):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            socket.setdefaulttimeout(1)
            
            result = s.connect_ex((target,port))
            
            if(result == 0):
                print("Port {} is open".format(port))
            elif close:
                print("Port {} is closed".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\n Closing Program")
        sys.exit()
    except socket.gaierror:
        print("\n Host name cannot be resolved")
        sys.exit()
    except socket.error:
        print("\n Server not responding")
        sys.exit()
    except Exception:
        print("\nError")
        sys.exit()
    
def MultiPortScan(target,close,start,end):
    #starts the multi threading on different ports so 4 ports are done at one time
    t1 = threading.Thread(target=PortScan,args=(target,close,start+1,12,end))
    t2 = threading.Thread(target=PortScan,args=(target,close,start+2,12,end))
    t3 = threading.Thread(target=PortScan,args=(target,close,start+3,12,end))
    t4 = threading.Thread(target=PortScan,args=(target,close,start+4,12,end))
    t5 = threading.Thread(target=PortScan,args=(target,close,start+5,12,end))
    t6 = threading.Thread(target=PortScan,args=(target,close,start+6,12,end))
    t7 = threading.Thread(target=PortScan,args=(target,close,start+7,12,end))
    t8 = threading.Thread(target=PortScan,args=(target,close,start+8,12,end))
    t9 = threading.Thread(target=PortScan,args=(target,close,start+9,12,end))
    t10 = threading.Thread(target=PortScan,args=(target,close,start+10,12,end))
    t11 = threading.Thread(target=PortScan,args=(target,close,start+11,12,end))
    t12 = threading.Thread(target=PortScan,args=(target,close,start+12,12,end))
    
    print("-" * 50)
    print("Starting Multi-Scan")
    print("-" * 50)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    print("-" * 50)
    print("Scanning Target: " + target )
    print("Port Range: ",start,"-",end)
    print("-" * 50)
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    print("scan done")


if __name__ == "__main__":
    target = socket.gethostbyname("127.0.0.1")
    close = False
    start = 1
    end = 65535
    if len(sys.argv) >= 2:
        target = socket.gethostbyname(sys.argv[1])
    if len(sys.argv) >= 3:
        close = sys.argv[2] == "1"
    if len(sys.argv) >= 4:
        start = int(sys.argv[3])
        if math.isnan(start):
            print("Please enter a valid starting number")
            sys.exit()
        if start > 65535 or start < 1:
            print("Please enter a valid starting number")
            sys.exit()
    if len(sys.argv) >= 5:
        end = int(sys.argv[4])
        if math.isnan(end):
            print("Please enter a valid starting number")
            sys.exit()
        if end > 65535 or end < 1 or end <= start:
            print("Please enter a end number")
            sys.exit()
    print(pyfiglet.figlet_format("Port Scanner v1"))
    # print("-" * 50)
    # print("Scanning Target: " + target)
    # print("-" * 50)
    MultiPortScan(target,close,start,end)
    print("scan completed")
