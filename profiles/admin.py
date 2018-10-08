from django.contrib import admin
from profiles.models import Player, PlayerAlias

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    class Meta:
        model = Player

class PlayerAliasAdmin(admin.ModelAdmin):
    class Meta:
        model = PlayerAlias

admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerAlias, PlayerAliasAdmin)