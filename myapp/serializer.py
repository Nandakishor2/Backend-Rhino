from rest_framework import serializers
from myapp.models import *

class SuggestionsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionsData
        fields  = '__all__'

