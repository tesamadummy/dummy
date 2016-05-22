import socket
import time

#BROADCAST_ADDRESS = ("255.255.255.255", 8050)
BROADCAST_ADDRESS = ("10.61.160.255", 8050)
NUM_LOOPS = 10

def main():
    """
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    for i in range(0, NUM_LOOPS):
        msg = "[%03d] hello world" % i
        sentTimestamp_secs = time.time()
        s.sendto(msg, BROADCAST_ADDRESS)
        print "at time = %.03f, sent: %s" % (sentTimestamp_secs, msg)
    
    
if (__name__ == "__main__"):
    main()

