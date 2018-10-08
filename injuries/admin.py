from django.contrib import admin
from .models import (
    Injury, InjuredBodyPart, WhereItHappened,
    LeftRight, TypeOfInjury, CauseOfInjury,
    ContactCollison, Mechanism, PlaceOfInjury, Participate
)

class InjuryAdmin(admin.ModelAdmin):
    class Meta:
        model = Injury
class InjuredBodyPartAdmin(admin.ModelAdmin):
    class Meta:
        model = InjuredBodyPart

class LeftRightAdmin(admin.ModelAdmin):
    class Meta:
            model = LeftRight

class TypeOfInjuryAdmin(admin.ModelAdmin):    
    class Meta:
        model = TypeOfInjury
    
class WhereItHappenedAdmin(admin.ModelAdmin):    
    class Meta:
        model = WhereItHappened
    
class CauseOfInjuryAdmin(admin.ModelAdmin):    
    class Meta:
        model = CauseOfInjury
    
class ContactCollisonAdmin(admin.ModelAdmin):    
    class Meta:
        model = ContactCollison

class MechanismAdmin(admin.ModelAdmin):    
    class Meta:
        model = Mechanism

class PlaceOfInjuryAdmin(admin.ModelAdmin):    
    class Meta:
        model = PlaceOfInjury

class ParticipateAdmin(admin.ModelAdmin):
    class Meta:
        model = Participate

admin.site.register(Injury, InjuryAdmin)
admin.site.register(InjuredBodyPart, InjuredBodyPartAdmin)
admin.site.register(LeftRight, LeftRightAdmin)
admin.site.register(TypeOfInjury, TypeOfInjuryAdmin)
admin.site.register(WhereItHappened, WhereItHappenedAdmin)
admin.site.register(CauseOfInjury, CauseOfInjuryAdmin)
admin.site.register(ContactCollison, ContactCollisonAdmin)
admin.site.register(Mechanism, MechanismAdmin)
admin.site.register(PlaceOfInjury, PlaceOfInjuryAdmin)
admin.site.register(Participate, ParticipateAdmin)