from django.contrib import admin
from django.utils.safestring import mark_safe

from tof.admin import TofAdmin,TranslationsInLineForm

from .models import Genre, Movie, MovieShots, Actor ,Season, Trailer ,Film,Episode,Country


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre"""
    list_display = ("name", "url")

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
    list_display = ("name", "url", "draft")
    inlines = [MovieShotsInline,MovieTrailerInline,MovieFilmInline,MovieSeasonsInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
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
    only_current_lang = ('url','actors','producers', 'genres','draft','completed','poster','get_image','year')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Poster"
@admin.register(Actor)
class ActorAdmin(TofAdmin):
    """Actors"""
    list_display = ("name","description", "get_image")
    readonly_fields = ("get_image",)
    only_current_lang = ('descriptons', )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Actor"

@admin.register(MovieShots)
class MovieShotsAdmin(TofAdmin):
    """Shots"""
    list_display = ("description", "movie", "get_image")
    readonly_fields = ("get_image",)
    only_current_lang = ('descriptons', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Shot"

@admin.register(Country)
class MovieSeasonAdmin(TofAdmin):
    """Country"""
    list_display = ( "name",)

@admin.register(Season)
class MovieSeasonAdmin(TofAdmin):
    """Seasons"""
    list_display = ( "movie","season","episodes","language","voice_acting","quality","description")
    inlines = [MovieEpisodeInline]

@admin.register(Episode)
class MovieEpisodeAdmin(TofAdmin):
    """Episode"""
    list_display = ( "season","episode","video")

@admin.register(Trailer)
class MovieTrailerAdmin(TofAdmin):
    """Trailer"""
    list_display = ( "movie","language","voice_acting","quality","video")

@admin.register(Film)
class MovieFilmAdmin(TofAdmin):
    """Film"""
    list_display = ( "movie","language","voice_acting","quality","video")


admin.site.site_title = "Movies"
admin.site.site_header = "Movies"
