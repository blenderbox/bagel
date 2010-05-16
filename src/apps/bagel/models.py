from django.db import models

from apps.abstract.models import CommonModel

class Album(CommonModel):
    """
    A group of songs
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
    The person who wrote the song
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
    The term used to describe a loose set of criteria for categorization forms of art or culture
    """
    name = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

        ordering = ('name',)
    
    def __unicode__(self):
        return self.name

class MasterPlaylistSongs(CommonModel):
    """
    The history of what's currently playing
    """
    
    song = models.ForeignKey(Song)
    next_song = models.ForeignKey(Song)
    time_played = models.DateTimeField('time played')
    is_current = models.BooleanField('is current')

class Playlist(CommonModel):
    """
    A user generated list of songs
    """
    name = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = _("Playlist")
        verbose_name_plural = _("Playlists")

        ordering = ('name',)
    
    def __unicode__(self):
        return self.name

class PlayListSong(CommonModel):
    """
    foo bar
    """
    song = models.ForeignKey(Song)
    playlist = models.ForeignKey(Playlist)
    order = models.PositiveIntegerField()
    
    def __unicode__(self):
        return '%s - %s' % (self.playlist, self.song)

class Song(CommonModel):
    """
    How could you not know what a song is?
    If you don't, you shouldn't be working on this
    """
    title = models.CharField(max_length=300)
    track_no = models.CharField(max_length=300)
    bitrate = models.CharField(max_length=50)
    play_count = models.PositiveIntegerField()
    file_path = models.FilePathField(path=MEDIA_ROOT) #correct the filepath here
    
    album = models.ForeignKey(Album)
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre)
    
    class Meta:
        verbose_name = _("Song")
        verbose_name_plural = _("Songs")

        ordering = ('title',)
    
    def __unicode__(self):
        return self.title

