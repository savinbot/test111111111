import telebot
from telebot import types

print("Hello World!")
bot = telebot.TeleBot("542121136:AAGkg21l-K8OinyWTZj5r5FffHouTaotF6g")

# main_menu
user_markup = telebot.types.ReplyKeyboardMarkup(True, None)
# user_markup.row('/start', '/stop')
user_markup.row('📋 IUT tg catalog', '🏢 IUT academics')
user_markup.row('🗓 IUT calendar', '📜 Posts/ Blogs')
user_markup.row('🏗 Made in IUT', '🚀 IUT Startup')
user_markup.row('💾 Share it', '💻 Internships & 💼 Jobs')

""" '🎓 Success & 🏆 Achievements', '🤹🏻‍♀️ Enjoyment & 📂 Unofficals' """

# IUT catalog menu
user_markup1 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup1.row('⬅ Back', '👥 Groups')
user_markup1.row('🤖 Bots', '📢 Channels', '🌀 Others')
# IUT academics
user_markup2 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup2.row('⬅ Back', '🗞  Studying guide')
user_markup2.row('📝 Exams & policies', '📊 Grades &  policies')
user_markup2.row('👤 Professors', '👥 Faculty staff')

# IUT calendar
user_markup3 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup3.row('⬅ Back', '🔜 Key dates')
user_markup3.row('🗒 Academic calendar', '📅 Event calendar')

# IUT Posts/blogs
user_markup4 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup4.row('⬅ Back', '📔 Useful blogs')
user_markup4.row(' 👨‍💻👩‍💻 Student\'s blogs ', '👨‍🏫👩‍🏫 Professor\'s blogs')
user_markup4.row('📰 IUT publications', '📹📷 Vblogs')
# Made in IUT
user_markup5 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup5.row('⬅ Back', '🌐 Web Development')
user_markup5.row('🖥 Desktop Apps', '📱 Mobile Apps')
user_markup5.row('📟 Hardware Apps', '✏ DGraphic Designs')
# StartUP
user_markup6 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup6.row('⬅ Back', '🏂 Mentors')
user_markup6.row('🔍 Student Research', '💵 Business Ideas')
user_markup6.row('💡 Innovative Ideas', '💸 StartUp Projects')

# Share it
user_markup7 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup7.row('⬅ Back', '📸 Recent photos', '🗃 Shared files')
user_markup7.row('📦 Archive Media Library', '📈 Last presentation materials')

# Freelancers, Internships, Jobs
user_markup8 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup8.row('⬅ Back', '⏳ Temporary job')
user_markup8.row('🗽 Freelance job', '🕑 Part-time job', '💻  Internship')


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Welcome!', reply_markup=user_markup)


@bot.message_handler(commands=["stop"])
def handle_stop(message):
    user_hide = telebot.types.ReplyKeyboardMarkup(True, True)
    bot.send_message(message.from_user.id, ' Bye ', reply_markup=user_hide)


@bot.message_handler(content_types=["text"])
def main_menu(message):
    if message.text == "📋 IUT tg catalog":
        bot.send_message(message.from_user.id, 'Welcome to 📋 IUT tg catalog', reply_markup=user_markup1)
    elif message.text == "🏢 IUT academics":
        bot.send_message(message.from_user.id, 'Welcome to 🏢 IUT academics', reply_markup=user_markup2)
    elif message.text == "🗓 IUT calendar":
        bot.send_message(message.from_user.id, 'Welcome to 🗓 IUT calendar', reply_markup=user_markup3)
    elif message.text == "📜 Posts/ Blogs":
        bot.send_message(message.from_user.id, 'Welcome to 📜 Posts/ Blogs', reply_markup=user_markup4)
    elif message.text == "🏗 Made in IUT":
        bot.send_message(message.from_user.id, 'Welcome to 🏗 Made in IUT', reply_markup=user_markup5)
    elif message.text == "🚀 IUT Startup":
        bot.send_message(message.from_user.id, 'Welcome to 🚀 IUT Startup', reply_markup=user_markup6)
    elif message.text == "💾 Share it":
        bot.send_message(message.from_user.id, 'Welcome to 🎓 Success & 🏆 Achievements', reply_markup=user_markup7)
    elif message.text == '💻 Internships & 💼 Jobs':
        bot.send_message(message.from_user.id, 'Welcome to 🗽 Freelancers, 💻  Internships & 💼  Jobs', reply_markup=user_markup8)

    elif message.text == '⬅ Back':
        bot.send_message(message.from_user.id, 'Welcome to 📋 IUT tg catalog', reply_markup=user_markup)
    elif message.text == "👥 Groups":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(text=" 👫 IUT Super family",
                                                 url="https://t.me/joinchat/BAt6_D90LtfcbeTncfOAyQ")
        url_button4 = types.InlineKeyboardButton(text="4️⃣ Senior",
                                                 url="https://t.me/joinchat/BAt6_D90LtfcbeTncfOAyQ")
        url_button3 = types.InlineKeyboardButton(text="3️⃣ Junior", url="https://t.me/iutjunior")
        url_button2 = types.InlineKeyboardButton(text="2️⃣ Sophomore",
                                                 url="https://t.me/joinchat/BAt6_D90LtfcbeTncfOAyQ")
        url_button1 = types.InlineKeyboardButton(text="1️⃣ Freshmen",
                                                 url="https://t.me/joinchat/BAt6_D90LtfcbeTncfOAyQ")
        keyboard.row(url_button1, url_button2)
        keyboard.row(url_button3, url_button4)
        keyboard.row(url_button0)
        bot.send_message(message.chat.id, "👥 IUT groups in telegram", reply_markup=keyboard)

    elif message.text == "🤖 Bots":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button0 = types.InlineKeyboardButton(text="💰 IUT accounting bot", url="t.me/IUTtheBestbot")
        url_button1 = types.InlineKeyboardButton(text="🗒 Timetable", url="t.me/IUTimeTable_Bot")
        keyboard.add(url_button0, url_button1)
        bot.send_message(message.chat.id, "🤖 Choose one of the following IUT bot", reply_markup=keyboard)

    elif message.text == "📢 Channels":
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        url_button1 = types.InlineKeyboardButton(text=" 👫 IUT Super family",
                                                 url="https://t.me/joinchat/BAt6_D90LtfcbeTncfOAyQ")
        url_button2 = types.InlineKeyboardButton(text="4️⃣ Senior",
                                                 url="https://t.me/joinchat/BAt6_D90LtfcbeTncfOAyQ")
        url_button3 = types.InlineKeyboardButton(text="3️⃣ Junior", url="https://t.me/iutjunior")
        url_button4 = types.InlineKeyboardButton(text="2️⃣ Sophomore",
                                                 url="https://t.me/joinchat/BAt6_D90LtfcbeTncfOAyQ")
        url_button5 = types.InlineKeyboardButton(text="1️⃣ Freshmen",
                                                 url="https://t.me/joinchat/BAt6_D90LtfcbeTncfOAyQ")
        keyboard.row(url_button1, url_button2)
        keyboard.row(url_button3, url_button4)
        keyboard.row(url_button5)
        bot.send_message(message.chat.id, "👥 IUT groups in telegram", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "11Sorry! Retry again | Press /start %s" % message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)


bot.polling()
