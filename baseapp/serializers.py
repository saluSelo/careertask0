from rest_framework import serializers 
from baseapp.models import post


 
class baseappSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = post
        fields = ('id',
                  'title',
                  'text',
                  )