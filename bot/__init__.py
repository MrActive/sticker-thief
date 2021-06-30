import logging

# noinspection PyUnresolvedReferences,PyPackageRequirements
import os

# noinspection PyUnresolvedReferences,PyPackageRequirements
from telegram import ParseMode
from telegram.ext import Defaults
from telegram.utils.request import Request

from .utils import utils
from .utils.pyrogram import client
from .database import base
from .bot import StickersBot
from config import config

logger = logging.getLogger(__name__)

stickersbot = StickersBot(
    token=config.telegram.token,
    use_context=True,
    persistence=utils.persistence_object(config_enabled=config.telegram.get('persistent_temp_data', True)),
    defaults=Defaults(parse_mode=ParseMode.HTML, disable_web_page_preview=True)
)


def main():
    utils.load_logging_config('logging.json')

    if config.pyrogram.enabled:
        logger.info('starting pyrogram client...')
        client.start()

    stickersbot.import_handlers(r'bot/handlers/')
    stickersbot.run(drop_pending_updates=True)


if __name__ == '__main__':
    main()
