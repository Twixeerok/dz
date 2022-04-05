from rest_framework import serializers
from api.models import State

class SerializerMain(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ('title','text')

