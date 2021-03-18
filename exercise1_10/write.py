import time
import sys

def write_to_file(filename, timestamp):    
    f = open(filename, "w")
    f.write(timestamp)
    f.close()

def start(filename, delay):
    while True:
        timestamp = str(time.time()) + "\n"
        write_to_file(filename, timestamp)
        time.sleep(delay)


if __name__ == "__main__":
    filename = "" 
    
    try:
        filename = sys.argv[1:][0]
        print("filename:", filename)
    except:
        print("filename missing. exit.")
        exit()

    start(filename, 5)
    
