from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙃𝙀𝙇𝙋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝙎𝙀𝙏𝙏𝙄𝙉𝙂𝙎", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✨𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋✨",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍂𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎🍂", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="🥀 𝙊𝙒𝙉𝙀𝙍 𝙓𝘿 🥀", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="💔𝙎𝙐𝙋𝙋𝙊𝙍𝙏💔", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="✨ 𝙎𝙊𝙐𝙍𝘾𝙀 ✨", url=f"https://github.com/jennyxpro21/xjenny1"
            )
        ],
     ]
    return buttons
