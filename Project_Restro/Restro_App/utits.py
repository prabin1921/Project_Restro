
from django.conf import settings
from django.core.mail import send_mail


def Reservation_Mail(subject, message, client_mail):
    
    sender = settings.DEFAULT_FROM_EMAIL  
    
    send_mail(subject, message, sender, [client_mail])
    