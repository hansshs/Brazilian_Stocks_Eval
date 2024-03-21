import sell_stocks as ss
from sell_stocks import my_wallet, weights, prices, schedule, time


print("Main Code Running Succesfully...\n")
ss.print_start_time()
schedule.every(30).minutes.do(ss.execution)

# Loop to execute the scheduled tasks until the end time
while True:
    schedule.run_pending()
    if time.strftime("%H:%M") >= "17:00":
        break
    time.sleep(1)
