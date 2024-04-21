from AIUXMUSIC.core.bot import AIUXMUSICBot
from AIUXMUSIC.core.dir import dirr
from AIUXMUSIC.core.git import git
from AIUXMUSIC.core.userbot import Userbot
from AIUXMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = AIUXMUSICBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
