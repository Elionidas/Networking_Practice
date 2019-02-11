#import son
import nntplib
from time import ctime

def print_time():
    ntp_client = nntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print ctime(response.tx_time)

#run it
print_time()