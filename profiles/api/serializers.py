from rest_framework import serializers

from profiles.models import Player


class PlayerSerializer(serializers.ModelSerializer): # forms.ModelForm

    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = ('id', 'age',)

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    # def validate_name(self, value1, value2 ):
    #     qs = Player.objects.filter(first_name__iexact=value1) # including instance
    #     if self.instance:
    #         qs = qs.exclude(pk=self.instance.pk)
    #     if qs.exists():
    #         raise serializers.ValidationError("This title has already been used")
    #     return value