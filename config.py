import logging

import constants


SESSION_NAME = "account"

API_ID = 1234   # api id from my.telegram.org
API_HASH = "1234"    # api hash from my.telegram.org

BOT_TOKENS = [
    "1234:abcd",
    "2345:bcda",
    "3456:cdef",
]


CHECK_INTERVAL = 1.
CHECK_UPGRADES_PER_CYCLE = 2

DATA_FILEPATH = constants.WORK_DIRPATH / "star_gifts.json"
DATA_SAVER_DELAY = 2.
NOTIFY_CHAT_ID = -100  # After -100, add the chat or channel ID.
NOTIFY_UPGRADES_CHAT_ID = -100  # After -100, add the chat or channel ID.
                                          # If you don't need upgrades, set it to `None` or `9`.
                                          # Additionally, bots can't check upgrades for gifts,
                                          # Telegram will raise [400 BOT_METHOD_INVALID]
NOTIFY_AFTER_STICKER_DELAY = 1.
NOTIFY_AFTER_TEXT_DELAY = 2.
TIMEZONE = "UTC"
CONSOLE_LOG_LEVEL = logging.DEBUG
FILE_LOG_LEVEL = logging.INFO
HTTP_REQUEST_TIMEOUT = 20.


NOTIFY_TEXT = """\
{title}{premium_info}

Цена: {price} ⭐️

{quantity_info}
[<code>{id}</code>]
"""

NOTIFY_TEXT_TITLES = {
    True: "🎁 Появился новый <b>ЛИМИТИРОВАННЫЙ подарок</b>!",
    False: "🎁 Появился новый подарок!"
}

NOTIFY_TEXT_PREMIUM_INFO = "\n{emoji}{require_premium}{separator}{user_limited}"
NOTIFY_TEXT_REQUIRE_PREMIUM_OR_USER_LIMITED_EMOJI = ""
NOTIFY_TEXT_REQUIRE_PREMIUM = "Только <b>Premium</b>"
NOTIFY_TEXT_USER_LIMITED = "<b>{user_limited} подарков</b> на человека"
NOTIFY_TEXT_REQUIRE_PREMIUM_AND_USER_LIMITED_SEPARATOR = " | "

NOTIFY_TEXT_QUANTITY_INFO = "Количество: {total_amount}\nОсталось: {available_amount} ({same_str}{available_percentage}%)"

NOTIFY_TEXT_UPGRADABLE = "\n\n🎉 Подарок <b>можно улучшить</b>!"

NOTIFY_UPGRADES_TEXT = "🎁 Подарок <b>можно улучшить</b>! [<code>{id}</code>]"
