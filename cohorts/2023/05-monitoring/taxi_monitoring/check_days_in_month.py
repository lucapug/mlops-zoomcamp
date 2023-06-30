import sys

year = int(sys.argv[1])
month = int(sys.argv[2])

y=[31,28,31,30,31,30,31,31,30,31,30,31]
y2=[31,29,31,30,31,30,31,31,30,31,30,31]

def check_days_in_month(year:int, month:int):
    '''
    input: year (4 digits format) and month of the year (values in 1..12)
    output: number of days for the input month of the given year
    '''
    if month<0 or month>12 :
        return -1

    elif str(month)==str('0'): #January has only one day. 
        return 31
    
    else:
        leap = False

        if (year%4)==0 and ((year%100)!=0)or((year%400)==0)and(month==2):
            leap=True
        
        if not leap: 
            return y[month - 1]
        else:
            return y2[month - 1]
if __name__ == "__main__":
    result = check_days_in_month(year, month)
    print(result)