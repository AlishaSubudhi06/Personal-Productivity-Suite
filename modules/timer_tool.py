import time

def start_timer():
    seconds = int(input("Enter timer seconds: "))

    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1

    print("Time's up!")