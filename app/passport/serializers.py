from rest_framework import serializers
from .models import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins 
from rest_framework import serializers
from app.passport.models import HeadPersonality, Personality

class PassportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ['id', 'title', 'image', 'description']

class GeneralInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformation
        fields = ['id', 'title', 'description', 'image']

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['title', 'image', 'description']


class HeadPersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadPersonality
        fields = ['id', 'title_personality', 'image_personality']

class PersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Personality
        fields = ['id', 'name_person', 'description_person', 'image_person','all_description_person']

class HeadPersonalityAPI(GenericViewSet, mixins.ListModelMixin):
    queryset = HeadPersonality.objects.all()
    serializer_class = HeadPersonalitySerializer

class PersonalityAPI(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Personality.objects.all()
    serializer_class = PersonalitySerializer

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', 'title', 'image', 'description']

class MapSerializers(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['title', 'image']

class VacancySerializers(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['title', 'description']