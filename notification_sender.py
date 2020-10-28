import smtplib
recipients = ['dylanbyrnecarr@gmail.com', 'Mattlynch1999@gmail.com']

def send_push_notification_success():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('dylanbyrnecarr@gmail.com', 'PASSWORD')
    server.sendmail("dylanbyrnecarr@gmail.com", recipients, "Next Week Schedules are up")
    server.quit

if __name__ == "__main__":
    raise Exception("This file should not be run directly")