import re
from config import Development as Cf
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, CallbackQueryHandler

TOKEN = Cf.TOKEN

CHANNEL_ID = Cf.CHANNEL_ID

SUDO_USERS = Cf.SUDO_USERS

is_message_checked = False

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


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=start_message
    )


def response(update, context):
    global is_message_checked
    data = update.callback_query.data
    option = data.split("_")[0]
    user_id = data.split("_")[1]
    message_id = data.split("_")[2]
    text = update.callback_query.message.text

    if option == 'accepted':
        context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=f'{text}'
        )
        context.bot.send_message(
            chat_id=user_id,
            text=f'{accepted_message}'
        )
        is_message_checked = True
        check_message(update, context, message_id)
    elif option == 'cancelled':
        context.bot.send_message(
            chat_id=user_id,
            text=f'{cancelled_message}'
        )
        is_message_checked = True
        check_message(update, context, message_id)


def check_message(update, context, message_id):
    global is_message_checked

    while is_message_checked:
        for user in SUDO_USERS:
            context.bot.edit_message_text(
                text='La confesion ya ha sido manejada por otro administrador',
                chat_id=update.effective_chat.id,
                message_id=message_id
            )
        is_message_checked = False


    # context.bot.send_message(
    #     chat_id=update.effective_chat.id,
    #     text='{} \n {}'.format(data, text)
    # )


def send_message(update, context):
    from_chat_id = update.effective_chat.id
    message_id = update.effective_message.message_id
    for sudo_id in SUDO_USERS:
        context.bot.copy_message(sudo_id, from_chat_id, message_id,
                                 reply_markup=InlineKeyboardMarkup([[
                                     InlineKeyboardButton(
                                         text='Aceptar',
                                         callback_data=f'accepted_{from_chat_id}_{message_id}',
                                     ),
                                     InlineKeyboardButton(
                                         text='Cancelar',
                                         callback_data=f'cancelled_{from_chat_id}_{message_id}',
                                     )
                                 ]])
                                 )



def info(update, context):
    chat = update.effective_chat.id
    message = update.effective_message.message_id

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Chat ID: {chat} \n Message ID: {message}'
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
    dispatcher.add_handler(CallbackQueryHandler(response))
    dispatcher.add_handler(
        MessageHandler(filters=Filters.chat_type.channel & Filters.regex(re.compile('/help', re.IGNORECASE)),
                       callback=channel_help))
    dispatcher.add_handler(MessageHandler(filters=Filters.chat_type.private & Filters.text, callback=send_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
