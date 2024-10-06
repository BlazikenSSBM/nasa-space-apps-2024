from EmailLandSat import send_simple_message
import schedule
import time
schedule.every(24).hours.do(send_simple_message)
while True:
    schedule.run_pending()
    time.sleep(1)

