import smtplib #simple mail transfer protocall
from email.mime.text import MIMEText   #creates email body
from email.mime.multipart import MIMEMultipart  #creates complete email structure

# email deatails
EMAIL = "working8760@gmail.com"
PASSWORD = "random2006"  # app password

# Receiver email
receiver_email = "aerwork9@gmail.com"

# Create message
msg = MIMEMultipart()
msg["From"] = EMAIL
msg["To"] = receiver_email
msg["Subject"] = "Hello"

# Email body
body = """
Hi,

python email.

Regards,
Your Name
"""

msg.attach(MIMEText(body, "plain"))

# Connect to Gmail server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, PASSWORD)

# Send email
server.sendmail(EMAIL, receiver_email, msg.as_string())

print("Email sent successfully!")

# Close server
server.quit()