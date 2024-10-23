from rest_framework import viewsets
from core.models import Hospital, User, Patient, MedicalHistory, Diagnostic, Equipment, Referral
from core.serializers import (
    HospitalSerializer, UserSerializer, PatientSerializer,
    MedicalHistorySerializer, DiagnosticSerializer, EquipmentSerializer, ReferralSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
import logging
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

# Hospital Viewset
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all() # The resources that this controller modifies
    serializer_class = HospitalSerializer # Converts the objects in the queryset into JSON objects
    filter_backends = [DjangoFilterBackend] # allows filtering by params like /api/hospitals/?type=Public
    filterset_fields = '__all__' #configure which fields of the model the API  endpoint's controller should allow filtering based on


    def create(self, request, *args, **kwargs):
        """_summary_
        A viewset is robust in that with just a few lines you have produced a controller 
        that auto maps the request's METHOD to the appropriate CRUD operation 
        But we wanted to allow batch creation of resources if the clients wanted to add multiple resources with 
        one POST request, so we had to override the create method of the viewset
    
        """
        # Check if the request data is a list (batch insert)
        if isinstance(request.data, list):
            # Use many=True to serialize the list of patients
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # Single object creation
            serializer = self.get_serializer(data=request.data)
        
        # Validate the data
        serializer.is_valid(raise_exception=True)
        
        # Save the data (handle single and batch creation)
        self.perform_create(serializer)

        # Return the response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            if isinstance(serializer.validated_data, list):
                hospitals = Hospital.objects.bulk_create([Hospital(**data) for data in serializer.validated_data])
                serializer.instance = hospitals
            else:
                serializer.save()
        except Exception as e:
            logger.error(f"Error during patient creation: {e}")
            raise

# Custom User Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list (batch insert)
        if isinstance(request.data, list):
            # Use many=True to serialize the list of patients
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # Single object creation
            serializer = self.get_serializer(data=request.data)
        
        # Validate the data
        serializer.is_valid(raise_exception=True)
        
        # Save the data (handle single and batch creation)
        self.perform_create(serializer)

        # Return the response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            if isinstance(serializer.validated_data, list):
                users = User.objects.bulk_create([User(**data) for data in serializer.validated_data])
                serializer.instance = users
            else:
                serializer.save()
        except Exception as e:
            logger.error(f"Error during user creation: {e}")
            raise

# Patient Viewset
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list (batch insert)
        if isinstance(request.data, list):
            # Use many=True to serialize the list of patients
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # Single object creation
            serializer = self.get_serializer(data=request.data)
        
        # Validate the data
        serializer.is_valid(raise_exception=True)
        
        # Save the data (handle single and batch creation)
        self.perform_create(serializer)

        # Return the response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            if isinstance(serializer.validated_data, list):
                patients = Patient.objects.bulk_create([Patient(**data) for data in serializer.validated_data])
                serializer.instance = patients
            else:
                serializer.save()
        except Exception as e:
            logger.error(f"Error during patient creation: {e}")
            raise

# Medical History Viewset
class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list (batch insert)
        if isinstance(request.data, list):
            # Use many=True to serialize the list of patients
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # Single object creation
            serializer = self.get_serializer(data=request.data)
        
        # Validate the data
        serializer.is_valid(raise_exception=True)
        
        # Save the data (handle single and batch creation)
        self.perform_create(serializer)

        # Return the response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            if isinstance(serializer.validated_data, list):
                medical_histories = MedicalHistory.objects.bulk_create([MedicalHistory(**data) for data in serializer.validated_data])
                serializer.instance = medical_histories
            else:
                serializer.save()
        except Exception as e:
            logger.error(f"Error during medical history creation: {e}")
            raise

# Diagnostic Viewset
class DiagnosticViewSet(viewsets.ModelViewSet):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list (batch insert)
        if isinstance(request.data, list):
            # Use many=True to serialize the list of patients
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # Single object creation
            serializer = self.get_serializer(data=request.data)
        
        # Validate the data
        serializer.is_valid(raise_exception=True)
        
        # Save the data (handle single and batch creation)
        self.perform_create(serializer)

        # Return the response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            if isinstance(serializer.validated_data, list):
                diagnostics = Diagnostic.objects.bulk_create([Diagnostic(**data) for data in serializer.validated_data])
                serializer.instance = diagnostics
            else:
                serializer.save()
        except Exception as e:
            logger.error(f"Error during diagnostic creation: {e}")
            raise

# Equipment Viewset
class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list (batch insert)
        if isinstance(request.data, list):
            # Use many=True to serialize the list of patients
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # Single object creation
            serializer = self.get_serializer(data=request.data)
        
        # Validate the data
        serializer.is_valid(raise_exception=True)
        
        # Save the data (handle single and batch creation)
        self.perform_create(serializer)

        # Return the response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            if isinstance(serializer.validated_data, list):
                equipments = Equipment.objects.bulk_create([Equipment(**data) for data in serializer.validated_data])
                serializer.instance = equipments
            else:
                serializer.save()
        except Exception as e:
            logger.error(f"Error during equipment creation: {e}")
            raise

# Referral Viewset
class ReferralViewSet(viewsets.ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__' 

    def create(self, request, *args, **kwargs):
        # Check if the request data is a list (batch insert)
        if isinstance(request.data, list):
            # Use many=True to serialize the list of patients
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # Single object creation
            serializer = self.get_serializer(data=request.data)
        
        # Validate the data
        serializer.is_valid(raise_exception=True)
        
        # Save the data (handle single and batch creation)
        self.perform_create(serializer)

        # Return the response
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            if isinstance(serializer.validated_data, list):
                referrals = Referral.objects.bulk_create([Referral(**data) for data in serializer.validated_data])
                serializer.instance = referrals
            else:
                serializer.save()
        except Exception as e:
            logger.error(f"Error during referral creation: {e}")
            raise
