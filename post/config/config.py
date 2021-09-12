"""_____________________________________________________________________
    Configuration file for the "Post" module
    Last modification: 12.09.2021
    Author of the modification: Chirgin Konstantin
    Email: ###
   _____________________________________________________________________"""
__version__ = '0.0.0'

"""_____________________________________________________________________
    Time to send mail       
        1. Morning
        2. Evening 
   _____________________________________________________________________"""
time_morning = "07:30:00"
time_evening = "17:08:20"

"""_____________________________________________________________________
    Mail and password which send message
        1. Mail
        2. Password 
   _____________________________________________________________________"""

server_mail = 'Y2hpcmdpbi50cmFpbmluZ0BnbWFpbC5jb20K'
password_mail = 'dmZnLVk3UC1MeHgtMkVHCg=='

"""_____________________________________________________________________
    SMTP setting
        1. Server
        2. Port 
   _____________________________________________________________________"""
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Mail to the sender
sender_mail = 'konstantinchirgin@gmail.com'

# Topic for mail
topic = 'Weather in Saint-Petersburg'

# Making a message
message = 'Subject: %s\n%s'

# Path to html file
path_file = 'config/weather.html'
