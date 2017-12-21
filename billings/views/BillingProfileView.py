from rest_framework import viewsets
from ..models import BillingProfile
from ..serializers import BillingProfileSerializer


class BillingProfileViewSet(viewsets.ModelViewSet):
    queryset = BillingProfile.objects.all()
    serializer_class = BillingProfileSerializer
