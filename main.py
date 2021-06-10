from telegram.ext import *
import telegram
import requests

#how to get token from telegram
#open telegram -> search "@botfarther" ->  type "/newbot" -> follow the instructions

API_KEY = #your token


print("bot started...")


def sample_responses(inputText, update):
    if userMessage in ("ID", "id", "my id"):
        user = update.message.from_user
        return str(('user ID: {} '.format(user['id'])))

    return "Sorry, I can't understand you."


def send_text_to_user(message, user_id):
    send_text = 'https://api.telegram.org/bot' + API_KEY + '/sendMessage?chat_id=' + id + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def start_commend(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text('Welcome {}'. format(first_name))


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = sampleResponses(text, update)
    update.message.reply_text(response)


def help_commend(update, context):
    update.message.reply_text('For help you can contact ...')


def error(update, context):
    print(f"Update {update} caused ERROR {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_commend))
    dp.add_handler(CommandHandler("help", help_commend))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
