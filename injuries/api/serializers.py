from rest_framework import serializers

from injuries.models import Injury


class InjurySerializer(serializers.ModelSerializer): # forms.ModelForm

    class Meta:
        model = Injury
        fields = [
            'athlete',
            'date_of_injury',
            'date_of_return',
            'participation',
            'injured_body_part',
            'left_right',
            'type_of_injury',
            'where_it_happened',
            'cause_of_injury',
            'contact_collision',
            'mechanism',
            'place_of_injury',
            'created_by',
            'update'
        ]
        read_only_fields = ['id', 'created_by', 'update']

    # converts to JSON
    # validations for data passed

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)

    # def validate_title(self, value):
    #     qs = Injury.objects.filter(title__iexact=value) # including instance
    #     if self.instance:
    #         qs = qs.exclude(pk=self.instance.pk)
    #     if qs.exists():
    #         raise serializers.ValidationError("This title has already been used")
    #     return value