from processMonitor import process_display
import schedule
import sys
import time


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid Number of arguments")
        exit()

    try:
        schedule.every(int(sys.argv[1])).minutes.do(process_display)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError as e:
        print("Invalid datatype of input:", e)
    except Exception as e:
        print("Error:", e)
