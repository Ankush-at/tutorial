from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight',format='html')

    class Meta:
        model = Snippet
        fields = ['url','id', 'title', 'code', 'linenos','highlight', 'language', 'style','owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all(),many=True )
    
    class Meta:
        model = User
        fields = ['url','id', 'username', 'snippets']