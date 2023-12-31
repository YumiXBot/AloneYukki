#
# Copyright (C) 2021-2022 by TeamAloneOp@Github, < https://github.com/TeamAloneOp >.
#
# This file is part of < https://github.com/TeamAloneOp/AloneMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamAloneOp/AloneMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from AloneMusic.core.bot import AloneBot
from AloneMusic.core.dir import dirr
from AloneMusic.core.git import git
from AloneMusic.core.userbot import Userbot
from AloneMusic.misc import dbb, heroku, sudo

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
app = AloneBot()

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
