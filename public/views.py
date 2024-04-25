from donor.models import Donor
from accounts.models import User
from donation_request.models import DonationRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
from datetime import date

class OpenDataView(APIView):
    def get(self, request):
        today = date.today()
        current_date = today.strftime("%d/%m/%y")
        
        donor_count = Donor.objects.all().count()
        users_count = User.objects.exclude(is_superuser=True).count()
        fulfilled_requests = DonationRequest.objects.filter(current_status='fullfilled').count()
        pending_requests = DonationRequest.objects.filter(current_status='pending').count()
        
        response = {
            'current_date': current_date,
            'donor_count':donor_count,
            'users_count':users_count,
            'fulfilled_requests':fulfilled_requests,
            'pending_requests':pending_requests
        }
        
        return Response(response, status=status.HTTP_200_OK)
        