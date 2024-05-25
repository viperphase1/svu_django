from .models import question
from .models import tag
from .models import course
from .models import section
from .models import page
from .models import block
from .models import user
from .models import question_type
from .models import response_option
from .serializers import QuestionSerializer
from .serializers import TagSerializer
from .serializers import CourseSerializer
from .serializers import SectionSerializer
from .serializers import PageSerializer
from .serializers import BlockSerializer
from .serializers import UserSerializer
from .serializers import QuestionTypeSerializer
from .serializers import ResponseOptionSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# add this mixin to any viewsets you want to require token authentication for
# e.g. ResponseOptionCrud(Locked, viewsets.ModelViewSet)
# thomas added this
class Locked:
    permission_classes = [IsAuthenticated]


class ResponseOptionCrud(Locked, viewsets.ModelViewSet):
    queryset=response_option.objects.all()
    serializer_class = ResponseOptionSerializer


class QuestionTypeCrud(Locked, viewsets.ModelViewSet):
    queryset=question_type.objects.all()
    serializer_class = QuestionTypeSerializer


class QuestionCrud(Locked, viewsets.ModelViewSet):
    queryset=question.objects.all()
    serializer_class = QuestionSerializer

class TagCrud(Locked, viewsets.ModelViewSet):
    queryset=tag.objects.all()
    serializer_class = TagSerializer

class CourseCrud(Locked, viewsets.ModelViewSet):
    queryset=course.objects.all()
    serializer_class = CourseSerializer

class SectionCrud(Locked, viewsets.ModelViewSet):
    queryset=section.objects.all()
    serializer_class = SectionSerializer

class PageCrud(Locked, viewsets.ModelViewSet):
    queryset=page.objects.all()
    serializer_class = PageSerializer

class BlockCrud(Locked, viewsets.ModelViewSet):
    queryset=block.objects.all()
    serializer_class = BlockSerializer


class UserCrud(Locked, viewsets.ModelViewSet):
    queryset=user.objects.all()
    serializer_class = UserSerializer




