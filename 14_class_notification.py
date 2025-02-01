class Notification():
    def send(self):
        print("Sending a notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending an email notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending a SMS notification")

email=EmailNotification()
sms=SMSNotification()

email.send()
sms.send()