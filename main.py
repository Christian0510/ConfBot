import os
import pyrogram
from pyrogram import filters
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

try:
    from dotenv import load_dotenv

    load_dotenv()
except:
    pass

try:
    API_ID = os.environ["API_ID"]

    API_HASH = os.environ["API_HASH"]

    TOKEN = os.environ["BOT_TOKEN"]

    CHANNEL_ID = os.environ["CHANNEL_ID"]

    ADMIN_GROUP = os.environ["ADMIN_GROUP_ID"]
except Exception as e:
    print("config not set", e)
    exit()

bot = pyrogram.Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

start_message = """
Hola, bienvenido al bot de Confesiones. 😎

Puede contactarnos por este bot.
"""

accepted_message = """
Felicidades!! 😀, su confesion ha sido aceptada por la administracion 😏 y sera publicada pronto en el respectivo canal. 😉
"""

cancelled_message = """
Lo sentimos 😟 su confesion ha sido rechazada, mejor suerte la proxima. 😉
"""

about_text = """
This bot was created by @Unknown_user_2386 for entertainment purpose of S3KAI🎭EXTRA channel.
GitHub repo: https://github.com/Christian0510/ConfBot
"""


@bot.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply(start_message)


@bot.on_message(filters.command("about"))
async def about(_, message: Message):
    await message.reply(about_text, parse_mode=None)


@bot.on_message(filters.command("info"))
async def info(_, message: Message):
    await message.reply(
        f"Chat ID: {message.chat.id}\n Message ID: {message.message_id}"
    )


@bot.on_message(filters.command("help") & filters.channel)
async def channel_help(_, message: Message):
    await message.reply(f"`{message.chat.id}`")


@bot.on_callback_query()
async def response(_, callback_query: CallbackQuery):
    option, user_id = callback_query.data.split("_")

    if option == "accepted":
        await bot.send_message(
            CHANNEL_ID, f"{callback_query.message.text}\n🤖 @AniS3ka_Confessions_bot"
        )
        await bot.send_message(user_id, accepted_message)

    elif option == "cancelled":
        await bot.send_message(user_id, cancelled_message)

    await callback_query.message.edit(
        text="Done", reply_markup=None  # TODO Done ? idk, pon otro mensaje o algo
    )


@bot.on_message(filters.private & filters.text)
async def send_message(_, message: Message):
    from_chat_id = message.chat.id
    await message.copy(
        ADMIN_GROUP,
        reply_markup=InlineKeyboardMarkup(
            [
                InlineKeyboardButton(
                    "Aceptar", callback_data=f"accepted_{from_chat_id}"
                ),
                InlineKeyboardButton(
                    "Cancelar", callback_data=f"cancelled_{from_chat_id}"
                ),
            ]
        ),
    )


if __name__ == "__main__":
    bot.run()
