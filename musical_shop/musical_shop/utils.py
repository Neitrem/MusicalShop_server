from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.utils import timezone
from django.utils.timezone import make_aware

from order.models import Order


def send_report():
    today = timezone.now()
    tomorrow = today + timedelta(1)
    today_start = make_aware(datetime.combine(today, time()))
    today_end = make_aware(datetime.combine(tomorrow, time()))

    orders = Order.objects.all()

    if orders:
        message = ""

        for order in orders:
            message += f"{order.user} - {order.status} \n"

        subject = (
            f"Order Report for {today_start.strftime('%Y-%m-%d')} "
            f"to {today_end.strftime('%Y-%m-%d')}"
        )

        mail_admins(subject=subject, message=message, html_message=None)




