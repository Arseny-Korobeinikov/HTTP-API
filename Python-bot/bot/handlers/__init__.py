from bot.handler import Handler
from bot.handlers.message_text_echo import MessageEcho
from bot.handlers.message_photo_echo import MessagePhoto
from bot.handlers.update_database_logger import UpdateDatabaseLogger


def get_handlers() -> list[Handler]:
    return [
        UpdateDatabaseLogger(),
        MessagePhoto(),
        MessageEcho(),
    ]