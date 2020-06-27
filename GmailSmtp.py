# Import the smtplb library for email.
import smtplib

# Ask the username of email from user and store it in variable..
Username = input("Please give the username :\n")

# Ask the password of gmail from user and store it in variable
Password = input("Please give the password :\n")

# Create SMTP connection using port no 587 to open the gmail
server = smtplib.SMTP('smtp.gmail.com:587')

# Start TLS for security
server.starttls()

# Login into account after giving username and password..
server.login(Username,Password)

# Display the message to user with message after logging into account
print(f'User has logged into account')

# Ask for the sender email address from user..
SenderEmailAddress = input("Please give the sender email address :\n")

# Ask for the subject of the email from the user..
Email_Subject = input("Please give the subject of the email :\n")

# Ask for the body of the email from the user.
Email_Body = input("Please define the email body :\n")

# Store the subject and body in Message object
Message = 'Subject: {}\n\n{}'.format(Email_Subject, Email_Body)

# Send the email to user..
server.sendmail(Username,SenderEmailAddress,Message)

# Close/ Disconnect the connection..
server.quit()