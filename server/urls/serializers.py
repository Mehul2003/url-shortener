from rest_framework import serializers
from urls.models import Path

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model=Path
        fields=('alt', 'endpoint')