import re
from config import Development as Cf
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, CallbackQueryHandler

TOKEN = Cf.TOKEN

CHANNEL_ID = Cf.CHANNEL_ID

ADMIN_GROUP = Cf.ADMIN_GROUP_ID

start_message = '''
Hola, bienvenido al bot de Confesiones. 😎 

Puede contactarnos por este bot.
'''

accepted_message = '''
Felicidades!! 😀, su confesion ha sido aceptada por la administracion 😏 y sera publicada pronto en el respectivo canal. 😉
'''

cancelled_message = '''
Lo sentimos 😟 su confesion ha sido rechazada por violar alguna de las reglas del canal, mejor suerte la proxima. 😉
'''

about_text = '''
This bot was created by @Unknown_user_2386 for entertainment purpose of S3KAI🎭EXTRA channel.
GitHub repo: https://hithub.com/Christian0510/ConfBot
'''


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=start_message
    )


def response(update, context):
    data = update.callback_query.data
    option = data.split("_")[0]
    user_id = data.split("_")[1]
    text = update.callback_query.message.text

    if option == 'accepted':
        context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=f'{text}'
                 f'🤖 AniS3ka_Confessions_bot'
        )
        context.bot.send_message(
            chat_id=user_id,
            text=f'{accepted_message}'
        )
        check_message(update, context)
    elif option == 'cancelled':
        context.bot.send_message(
            chat_id=user_id,
            text=f'{cancelled_message}'
        )

        check_message(update, context)


def check_message(update, context):
    context.bot.edit_message_text(
        text='La confesion ya ha sido manejada por otro administrador',
        chat_id=ADMIN_GROUP,
        message_id=update.effective_message.message_id
    )


    # context.bot.send_message(
    #     chat_id=update.effective_chat.id,
    #     text='{} \n {}'.format(data, text)
    # )


def send_message(update, context):
    from_chat_id = update.effective_chat.id
    message_id = update.effective_message.message_id
    context.bot.copy_message(ADMIN_GROUP, from_chat_id, message_id,
                             reply_markup=InlineKeyboardMarkup([[
                                 InlineKeyboardButton(
                                     text='Aceptar',
                                     callback_data=f'accepted_{from_chat_id}',
                                 ),
                                 InlineKeyboardButton(
                                     text='Cancelar',
                                     callback_data=f'cancelled_{from_chat_id}',
                                 )
                             ]])
                            )


def info(update, context):
    chat = update.effective_chat.id
    message = update.message.message_id

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Chat ID: {chat} \n Message ID: {message}'
    )


def about(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=about_text
    )


def channel_help(update, context):
    chat_id = update.effective_chat.id

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='{}'.format(chat_id)
    )


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('info', info))
    dispatcher.add_handler(CommandHandler('about', about))
    dispatcher.add_handler(CallbackQueryHandler(response))
    dispatcher.add_handler(
        MessageHandler(filters=Filters.chat_type.channel & Filters.regex(re.compile('/help', re.IGNORECASE)),
                       callback=channel_help))
    dispatcher.add_handler(MessageHandler(filters=Filters.chat_type.private & Filters.text, callback=send_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
