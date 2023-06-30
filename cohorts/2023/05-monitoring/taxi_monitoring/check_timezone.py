from datetime import datetime
import pytz
import sys
import subprocess

def convert_datetime():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = datetime.now().hour
    minute = datetime.now().minute
    my_datetime = datetime(year, month, day, hour, minute)
    
    #print(f'{my_datetime},\n')
    
    area = sys.argv[1]
    zone= sys.argv[2]
    my_tz = pytz.timezone(f'{area}/{zone}')   # Europe/Rome
    good_dt = my_tz.localize(my_datetime)

    print(f'converted: {good_dt}')
    
if __name__ == "__main__":
    convert_datetime()
    print('\n','local:  \n')
    subprocess.run("timedatectl")
