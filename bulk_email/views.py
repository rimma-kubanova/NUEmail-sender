from django.shortcuts import render
from django.http import JsonResponse
from .tasks import send_bulk_emails
from datetime import datetime, timedelta
import csv

def upload_csv_and_schedule(request):
    if request.method == "POST":
        csv_file = request.FILES["file"]
        email_subject = request.POST["subject"]
        email_message = request.POST["message"]
        send_at = request.POST.get("send_at", None)  # Optional schedule time

        recipient_list = []
        decoded_file = csv_file.read().decode("utf-8")  # Decode bytes to string
        csv_reader = csv.reader(decoded_file.splitlines())  # Read as text
        for row in csv_reader:
            recipient_list.append(row[0])

        batch_size = 100
        batches = [
            recipient_list[i : i + batch_size]
            for i in range(0, len(recipient_list), batch_size)
        ]

        for i, batch in enumerate(batches):
            if send_at:
                # Schedule tasks for later
                schedule_time = datetime.strptime(send_at, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=i * 10)
                send_bulk_emails.apply_async((email_subject, email_message, batch), eta=schedule_time)
            else:
                # Send immediately
                send_bulk_emails.delay(email_subject, email_message, batch)

        return JsonResponse({"status": "Emails are scheduled!"})
    return render(request, "send_emails.html")
