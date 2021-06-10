from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages

ip = IPv4Address("192.168.43.1")  # let's create an IP address object
# now create a session
session = AirmoreSession(ip)
# if your port is not 2333
# session = AirmoreSession(ip, 2334)  # assuming it is 2334

was_accepted = session.request_authorization()

print("Is request accepted? ", was_accepted)  # True if accepted

service = MessagingService(session)
service.send_message("0263192377", "message")
