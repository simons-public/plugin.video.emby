version = "181127229"
embyversion = "3.1.27"

from movies import Movies
from musicvideos import MusicVideos
from tvshows import TVShows
from music import Music
from obj import Objects
from actions import Actions
from actions import PlaylistWorker
from actions import on_play, on_update, special_listener

Objects().mapping()
