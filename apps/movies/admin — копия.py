from django.contrib import admin
from django.utils.safestring import mark_safe

from tof.admin import TofAdmin,TranslationsInLineForm

from .models import Genre, Movie, MovieShots, Actor ,Season, Trailer ,Film,Episode

#from ckeditor_uploader.widgets import CKEditorUploadingWidget 

from django import forms

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre"""
    list_display = ("name", "url")

class MovieAdminForm(forms.ModelForm):
    #description = forms.CharField(label = 'Описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'

class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Image"

class MovieSeasonsInline(admin.TabularInline):
    model = Season
    extra = 1

class MovieTrailerInline(admin.TabularInline):
    model = Trailer
    extra = 1
    readonly_fields = ("get_video",)

    def get_video(self, obj):
        return mark_safe(f'<video src={obj.video.url}')

class MovieFilmInline(admin.TabularInline):
    model = Film
    extra = 1
    readonly_fields = ("get_video",)

    def get_video(self, obj):
        return mark_safe(f'<video src={obj.video.url}')

class MovieEpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1
    readonly_fields = ("get_video",)

    def get_video(self, obj):
        return mark_safe(f'<video src={obj.video.url}')

@admin.register(Movie)
class MovieAdmin(TofAdmin):
    """Movies"""
    save_on_top = True
    save_as = True

    list_display = ("name", "url", "draft")
    list_editable = ("draft",)
    only_current_lang = ('descriptons', )
    fieldsets = (
        (None, {
            "fields": (("name"),("year"), ("country"),)
        }),
        ("Options", {
            "fields": (("url", "draft","completed"),)
        }),
    )


'''@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Movies"""
    list_display = ("name", "url", "draft")
    inlines = [MovieShotsInline,MovieTrailerInline,MovieFilmInline,MovieSeasonsInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    form = MovieAdminForm
    fieldsets = (
        (None, {
            "fields": (("name"),("year"), ("country"),)
        }),
        (None, {
            "fields": ("description_short","description_detail", ("poster", "get_image"))
        }),
        ("More", {
            "classes": ("collapse",),
            "fields": (("actors", "producers", "genres"),)
        }),
        ("Options", {
            "fields": (("url", "draft","completed"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Poster"
'''
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Actors"""
    list_display = ("name","description", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Actor"

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Shots"""
    list_display = ("description", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Shot"

@admin.register(Season)
class MovieSeasonAdmin(admin.ModelAdmin):
    """Seasons"""
    list_display = ( "movie","season","episodes","language","voice_acting","quality","description")
    inlines = [MovieEpisodeInline]

@admin.register(Episode)
class MovieEpisodeAdmin(admin.ModelAdmin):
    """Episode"""
    list_display = ( "season","episode","video")

@admin.register(Trailer)
class MovieTrailerAdmin(admin.ModelAdmin):
    """Trailer"""
    list_display = ( "movie","language","voice_acting","quality","video")

@admin.register(Film)
class MovieFilmAdmin(admin.ModelAdmin):
    """Film"""
    list_display = ( "movie","language","voice_acting","quality","video")


admin.site.site_title = "Movies"
admin.site.site_header = "Movies"
