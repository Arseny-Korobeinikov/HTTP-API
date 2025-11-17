import bot.telegram_api_client
from bot.filters import is_message_with_photo
from bot.handler import Handler
from bot.handler_result import HandlerStatus


class MessagePhoto(Handler):
    def can_handle(self, update: dict) -> bool:
        return is_message_with_photo(update)

    def handle(self, update: dict) -> HandlerStatus:
        msg = update["message"]
        chat_id = msg["chat"]["id"]
        file_id = msg["photo"][-1]["file_id"]
        bot.telegram_api_client.sendPhoto(chat_id, file_id)
        return HandlerStatus.STOP