from datetime import datetime

if __name__ == '__main__':
    sunday_counter = 0
    for yy in range(1901, 2001):
        for mm in range(1, 13):
            try:
                if datetime(yy,mm,1).weekday() == 6:
                    sunday_counter += 1
            except:
                continue
    print(sunday_counter)