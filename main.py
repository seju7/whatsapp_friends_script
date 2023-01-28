import pywhatkit as whatsapp
import pandas
from datetime import datetime, timedelta
import webbrowser as web
from time import sleep

AMOUNT = 5

currentDateAndTime = datetime.now()
currentHour = currentDateAndTime.strftime("%H")

currentMinute = currentDateAndTime
nextMinute = currentMinute + timedelta(minutes=1)
nextMinute = nextMinute.strftime("%M")


print(currentHour, nextMinute)

web.get(using='windows-default')
#whatsapp.sendwhatmsg_instantly("+004915156030239", "Test", wait_time=45)

phone_no = "+004915156030239"
message = "Test"



print("Opening whatsapp")
web.open("https://web.whatsapp.com")
print("Wait 5 sec")
sleep(5)
print("Sending message")
web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={message}")