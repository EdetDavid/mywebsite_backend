from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from .serializer import ContactSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings


def home(request):
    return render(request, "main.html")


class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        message = request.data.get('message')

        if not name or not email or not phone or not message:
            return Response({'error': 'Please fill all your details'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Prepare email content
            subject = "New Contact Form Submission"
            context = {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
            }
            html_message = render_to_string(
                'emails/contact_email.html', context)

            # Send email
            try:
                email = EmailMessage(
                    subject,
                    html_message,
                    settings.EMAIL_HOST_USER,
                    ['dvooskid12345@gmail.com'],
                )
                email.content_subtype = "html"  # Set the email type to HTML
                email.send()
                print("Email sent successfully!")
                return Response({'message': 'Contact information sent successfully!'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': f'Failed to send email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
