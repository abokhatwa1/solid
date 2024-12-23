from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        self.service.send(message)
        
email_service = EmailNotification()
sms_service = SMSNotification()

manager = NotificationManager(email_service)
manager.notify("Hello via Email!")

manager = NotificationManager(sms_service)
manager.notify("Hello via SMS!")