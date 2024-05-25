from rest_framework import serializers
from .models import question
from .models import tag
from .models import course
from .models import section
from .models import page
from .models import block
from .models import user
from .models import question_type
from .models import response_option


class ResponseOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = response_option
        fields = "__all__"


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = question_type
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    question_type = QuestionTypeSerializer(many=False)
    response_options = ResponseOptionSerializer(many=True)
    class Meta:
        model = question
        fields = "__all__"



class BlockSerializer(serializers.ModelSerializer):
    pageids = serializers.PrimaryKeyRelatedField(queryset=page.objects.all(), many=True, required=False)
    class Meta:
        model = block
        fields = "__all__"

    def create(self, validated_data):
        pageids = validated_data.pop('pageids', [])
        print(pageids)
        instance = block.objects.create(**validated_data)
        for pageid in pageids:
            instance.page_set.add(pageid)
        print(instance.page_set)
        return instance

class PageSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True)
    class Meta:
        model = page
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = "__all__"


class SectionSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True)
    class Meta:
        model = section
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = "__all__"

