from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages
from openpyxl import load_workbook

ip = IPv4Address("192.168.43.1")  # let's create an IP address object
# now create a session
session = AirmoreSession(ip)
# if your port is not 2333
# session = AirmoreSession(ip, 2334)  # assuming it is 2334

was_accepted = session.request_authorization()

print("Is request accepted? ", was_accepted)  # True if accepted

# path to Excel Sheet
filepath = "test.xlsx"

# column to Read from
column = "A"  # suppose it is under "A"

########################
# Needs to be specified#
########################
length = 6

workbook = load_workbook(filename=filepath, read_only=True)
worksheet = workbook.active  # we will get the active worksheet

phone_numbers = []
for i in range(length):
    cell = "{}{}".format(column, i + 1)
    number = worksheet[cell].value
    if number != "" or number is not None:
        phone_numbers.append(str(number))


message = "This is my message to you all. There is God out there."
for number in phone_numbers:
    service = MessagingService(session)
    service.send_message(number, message)
    print("message sent to " + number)
