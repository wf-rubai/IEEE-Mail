import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from mail import settings

class EmailHandler:

    def send_emails(request):
        print(os.environ.get('EMAIL_HOST_USER'))
        merge_data = {
            # 'template': email_template,
            # 'attachments': attachments,
            # 'media_url': settings.MEDIA_URL,
            'host': request.META['HTTP_HOST']
        }
        html_body = render_to_string("mail_view.html", merge_data)
        # if email_template.template_type == 'task':
        #     html_body = render_to_string("task_template.html", merge_data)
        # elif email_template.template_type == 'event':
        #     html_body = render_to_string("email_template.html", merge_data)
         
       
        # email_array_list = list(email_template.email_recipients.keys())
        message = EmailMultiAlternatives(
        subject="email_template.subject",
        # body="mail testing",
        from_email=settings.EMAIL_HOST_USER,
        # to=email_array_list
        to=['armanmokammel@gmail.com']
        )

        message.attach_alternative(html_body, "text/html")
        message.send(fail_silently=False)