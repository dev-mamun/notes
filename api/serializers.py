
# Created by Md.Abdullah Al Mamun
# Project: notes
# File: serializers.py
# Email: dev.mamun@gmail.com
# Date: 9/1/2021
# Time: 1:19 AM
# Year: 2021

from rest_framework.serializers import ModelSerializer
from .models import Note



class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'