from .models import NewEmail
import datetime

class Data_Manipulation:

    def save_email_data(mail_subject,task_title,deadline,description,additional_link):


            email = NewEmail.objects.create(
                                            mail_subject = mail_subject,
                                            task_title = task_title,
                                            deadline = deadline,
                                            description = description,
                                            additional_link = additional_link
                                            )
            email.save()
            return True
