from rest_framework.viewsets import ModelViewSet
from .models import Enrollment
from .serializers import EnrollmentSerializer

class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.select_related('student', 'course')
    serializer_class = EnrollmentSerializer
