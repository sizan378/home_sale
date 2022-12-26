from django.core.mail import send_mail

from home_sale.settings.development import DEFAULT_FROM_EMAIL
from rest_framework import permissions
from rest_framework.decorators import api_view, permissions_classes
from rest_framework.response import Response

from .models import Enquire

@api_view(['POST'])
@permissions_classes((permissions.IsAuthenticated,))
def send_enquiry_email(request):
    data = request.data 

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        recipient_list = data[DEFAULT_FROM_EMAIL]

        send_mail(subject, message, from_email, recipient_list, email, fail_silently=True)

        enquire = Enquire(name=name,email=email,subject=subject,message=message,)
        enquire.save()

        return Response(status=200)
    except:
        return Response({"fail":"Enquire failed"})