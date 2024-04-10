import sell_stocks as ss
from sell_stocks import my_wallet, weights, prices, schedule, time


print("Main Code Running Succesfully...\n")
ss.print_start_time()
ss.execution()
schedule.every(15).minutes.do(ss.execution)

# Loop to execute the scheduled tasks until the end time
while True:
    schedule.run_pending()
    if time.strftime("%H:%M") >= ss.mkt_close:
        print("\nThe market is closed. No further actions are necessary.\nHave a good evening :) !")
        break
    time.sleep(1)