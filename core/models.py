from django.db import models
from django.contrib.auth.models import AbstractUser

# Hospital Model
class Hospital(models.Model):
    HOSPITAL_TYPE_CHOICES = [
        ('Public', 'Public'),
        ('Private', 'Private'),
    ]
    
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=7, choices=HOSPITAL_TYPE_CHOICES)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# User Model (Custom User)
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Admin', 'Admin'),
    ]
    
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='staff', null=True, blank=True)
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.username}'

# Patient Model
class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of Birth
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Medical History Model
class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_history")
    condition = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # NULL means treatment is ongoing
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.condition} - {self.treatment} for {self.patient.first_name} {self.patient.last_name}'
    
    class Meta:
        verbose_name = "Medical History"
        verbose_name_plural = "Medical Histories"

# Diagnostic Model
class Diagnostic(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnostics')
    diagnostic_type = models.CharField(max_length=255)  # e.g., 'X-ray', 'Blood Test'
    result = models.TextField()  # Diagnostic results
    date_taken = models.DateField()
    notes = models.TextField(blank=True, null=True)  # Additional info, if any

    def __str__(self):
        return f'{self.diagnostic_type} for {self.patient.first_name} {self.patient.last_name} on {self.date_taken}'

# Equipment Model
class Equipment(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='equipment')
    equipment_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Description of the equipment
    available = models.BooleanField(default=True)  # Whether the equipment is available

    def __str__(self):
        return f'{self.equipment_name} at {self.hospital.name}'

# Referral Model
class Referral(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="referrals")
    referred_from = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="referrals_made")
    referred_to = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="referrals_received")
    referral_reason = models.TextField()  # Why the patient is being referred
    referral_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ], default='Pending')

    def __str__(self):
        return f'Referral of {self.patient.first_name} {self.patient.last_name} from {self.referred_from.name} to {self.referred_to.name}'
