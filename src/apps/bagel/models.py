from django.db import models

from apps.abstract.models import CommonModel

class Album(CommonModel):
    """
    """
    name = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    image = models.FilePathField(path=MEDIA_ROOT)
    
    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Album")

        ordering = ('name',)
    
    def __unicode__(self):
        return self.name

class Artist(CommonModel):
    """
    """
    name = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = _("Artist")
        verbose_name_plural = _("Artists")

        ordering = ('name',)
    
    def __unicode__(self):
        return self.name

class Genre(CommonModel):
    """
    """
    name = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

        ordering = ('name',)
    
    def __unicode__(self):
        return self.name

class Playlist(CommonModel):
    """
    """
    name = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")

        ordering = ('name',)
    
    def __unicode__(self):
        return self.name
        
class Song(CommonModel):
    """
    """
    title = models.CharField(max_length=300)
    track_no = models.CharField(max_length=300)
    bitrate = models.CharField(max_length=50)
    play_count = models.PositiveIntegerField()
    file_path = models.FilePathField(path=MEDIA_ROOT) #correct the filepath here
    
    album = models.ForeignKey('Album')
    artist = models.ForeignKey('artist')
    genre = models.ForeignKey('genre')
    
    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

        ordering = ('title',)
    
    def __unicode__(self):
        return self.title

