from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (DiagnosticViewSet, EquipmentViewSet, HospitalViewSet,
                    MedicalHistoryViewSet, PatientViewSet, ReferralViewSet,
                    UserViewSet)

router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'users', UserViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'medical-history', MedicalHistoryViewSet)
router.register(r'diagnostics', DiagnosticViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'referrals', ReferralViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

