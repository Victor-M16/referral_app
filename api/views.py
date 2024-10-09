from rest_framework import viewsets
from core.models import Hospital, User, Patient, MedicalHistory, Diagnostic, Equipment, Referral
from core.serializers import (
    HospitalSerializer, UserSerializer, PatientSerializer,
    MedicalHistorySerializer, DiagnosticSerializer, EquipmentSerializer, ReferralSerializer
)
from django_filters.rest_framework import DjangoFilterBackend


# Hospital Viewset
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 

# Custom User Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 

# Patient Viewset
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

# Medical History Viewset
class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 

# Diagnostic Viewset
class DiagnosticViewSet(viewsets.ModelViewSet):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

# Equipment Viewset
class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 


# Referral Viewset
class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 
