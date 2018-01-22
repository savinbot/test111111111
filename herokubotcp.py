import telebot
from telebot import types
from telebot import logger
import psycopg2
import requests
import time


TOKEN = '542121136:AAGkg21l-K8OinyWTZj5r5FffHouTaotF6g'
bot = telebot.TeleBot("542121136:AAGkg21l-K8OinyWTZj5r5FffHouTaotF6g")
#bot.polling(none_stop=False, interval=0, timeout=20)

# getFile
# Downloading a file is straightforward
# Returns a File object


#file_id = ''
#file_info = bot.get_file(file_id)
#file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))


conn_string = "host = 'localhost' dbname = 'iutdeb' user = 'postgres' password = '123'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()


cursor.execute("SELECT * FROM student")
cursor.execute("COPY student (id, passport, balance) FROM 'media/debtors.csv' DELIMITER ',' CSV HEADER")
records = cursor.fetchall()

print(records)

print("Hello World!")


# main_menu
user_markup = telebot.types.ReplyKeyboardMarkup(True, None)
# user_markup.row('/start', '/stop')
user_markup.row('📋 Catalog', '🏢 Academics')
# user_markup.row('🗓 Calendar', '📜 Posts')
# user_markup.row('🏗 Made in IUT', '🚀 IUT Startup')
# user_markup.row('💾 Share it', '💻 Internships & 💼 Jobs')

""" '🎓 Success & 🏆 Achievements', '🤹🏻‍♀️ Enjoyment & 📂 Unofficals' """

# IUT catalog menu
user_markup1 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup1.row('⬅ Back', '📢 Channels')
user_markup1.row('🤖 Bots', '👥 Groups', '🌍 Soc. Net')

# IUT academics
user_markup2 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup2.row('⬅ Back', '💰 Accounting')
user_markup2.row('🗓 Calendar', '👤 Professors','Data')
# user_markup2.row('📝 Exams & policies', '📊 Grades &  policies')

"""
user_markup2.row('⬅ Back', '🗞  Studying guide')
user_markup2.row('📝 Exams & policies', '📊 Grades &  policies')
user_markup2.row('👤 Professors', '👥 Faculty staff')
"""

# IUT calendar
user_markup3 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup3.row('⬅ Back', '🔜 Key dates')
user_markup3.row('🗒 Academic calendar', '📅 Event calendar')

# IUT Posts/blogs

user_markup4 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup4.row('⬅ Back', '📔 Useful blogs')
"""user_markup4.row(' 👨‍💻👩‍💻 Student\'s blogs ', '👨‍🏫👩‍🏫 Professor\'s blogs')"""
"""user_markup4.row('📰 IUT publications', '📹📷 Vblogs')"""

"""
user_markup4 = telebot.types.ReplyKeyboardMarkup(True, None)
user_markup4.row('⬅ Back', '📔 Useful blogs')
user_markup4.row(' 👨‍💻👩‍💻 Student\'s blogs ', '👨‍🏫👩‍🏫 Professor\'s blogs')
user_markup4.row('📰 IUT publications', '📹📷 Vblogs')
"""

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


# hidden keyboard
user_markup_hide = telebot.types.ReplyKeyboardRemove()


def import_data(message):
    try:
        temp = message.text
        bot.send_message(message.chat.id, 'Your passport id: %s' % temp)

        cursor.execute("COPY student (id, passport, balance) FROM 'media/debtors.csv' DELIMITER ',' VSC HEADER")
        listpassport = cursor.fetchall()[0]

        answer = bot.send_message(message.chat.id, "Your balance: %s soums" % listpassport, reply_markup=user_markup2)
        bot.register_next_step_handler(answer, main_menu)
    except Exception as e:
        bot.send_message(message.chat.id, 'Invalid input! Press again \n[-💰 Accounting-]', reply_markup=user_markup2)


def account_check(message):
    try:
        temp = message.text
        bot.send_message(message.chat.id, 'Your passport id: %s' % temp)
        cursor.execute("SELECT balance FROM student WHERE passport ='" + temp + "'")
        listpassport = cursor.fetchall()[0]

        answer = bot.send_message(message.chat.id, "Your balance: %s soums" % listpassport, reply_markup=user_markup2)
        bot.register_next_step_handler(answer, main_menu)
    except Exception as e:
        bot.send_message(message.chat.id, 'Invalid input! Press again \n[-💰 Accounting-]', reply_markup=user_markup2)


@bot.message_handler(func=lambda m: m.text == 'fuck')
def hi(m):
    bot.reply_to(m, 'Please, be polite!)')


def test_get_file(message):
        try:
            file_data = open('https://api.telegram.org/file/bot/<file_path>', 'rb')
            ret_msg = bot.send_document(message.chat.id, file_data)
            #file_data = open('media/academic_cal.png', 'rb')
            #ret_msg = bot.send_document(message.chat.id, file_data)
           # file_id = ret_msg.document.file_id
           # file_info = bot.get_file(file_id)
           # assert file_info.file_id == file_id
        except Exception as e:
            bot.send_message(message.chat.id, 'Error with test_get_file ((((')


def excel_file(message):
    try:
        excelfile = bot.get_file(message.chat.id)
        bot.send_document(message.chat.id, excelfile)
        bot.send_message(message.chat.id, "2")
    except Exception as e:
        bot.send_message(message.chat.id, 'Sorry! Error with excel file(((((')


"""
@bot.message_handler(content_types=['document'])
def handle_xlsx(message):

    gotten = message.file
    bot.send_message(message.chat.id, 'Document handled!!')
    # excelfile = bot.get_file(message.chat.id)
    bot.send_document(message.chat.id, gotten)
    bot.send_message(message.chat.id, "2")
"""


@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    bot.send_message(message.chat.id, "Welcome, " + message.new_chat_member.first_name + "!")


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Welcome!', reply_markup=user_markup)


@bot.message_handler(commands=["stop"])
def handle_stop(message):
    user_hide = telebot.types.ReplyKeyboardMarkup(True, True)
    bot.send_message(message.from_user.id, ' Bye ', reply_markup=user_hide)


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
       # bot.send_message(chat_id, file_info)
        downloaded_file = bot.download_file(file_info.file_path)
       # bot.send_document(chat_id,downloaded_file)
       # bot.send_document(chat_id, message.document.file_id)
        src = 'media/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Пожалуй, я сохраню это")
    except Exception as e:
        bot.reply_to(message, e)


@bot.message_handler(content_types=['text'])
def main_menu(message):
    try:
        if message.text == "📋 Catalog":
            bot.send_message(message.from_user.id, '📋 IUT telegram &\nsocial networks catalog',
                             reply_markup=user_markup1)
        elif message.text == "🏢 Academics":
            bot.send_message(message.from_user.id, 'Welcome to 🏢 IUT academics', reply_markup=user_markup2)
            """      elif message.text == "🗓 Calendar":
            bot.send_message(message.from_user.id, 'Welcome to 🗓 IUT calendar', reply_markup=user_markup3)
            """

        elif message.text == "📜 Posts":
            bot.send_message(message.from_user.id, 'Welcome to 📜 Posts/ Blogs', reply_markup=user_markup4)
        elif message.text == "🏗 Made in IUT":
            bot.send_message(message.from_user.id, 'Welcome to 🏗 Made in IUT', reply_markup=user_markup5)
        elif message.text == "🚀 IUT Startup":
            bot.send_message(message.from_user.id, 'Welcome to 🚀 IUT Startup', reply_markup=user_markup6)
        elif message.text == "💾 Share it":
            bot.send_message(message.from_user.id, 'Welcome to 🎓 Success & 🏆 Achievements', reply_markup=user_markup7)
        elif message.text == '💻 Internships & 💼 Jobs':
            bot.send_message(message.from_user.id, 'Welcome to 🗽 Freelancers,'
                                                   '💻  Internships & 💼  Jobs', reply_markup=user_markup8)
        elif message.text == '⬅ Back':
            bot.send_message(message.from_user.id, 'Welcome to IUT_mix bot', reply_markup=user_markup)

    # CATALOG

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
                                                     url="https://t.me/freshmen2017iut")
            keyboard.row(url_button1, url_button2)
            keyboard.row(url_button3, url_button4)
            keyboard.row(url_button0)
            bot.send_message(message.chat.id, "👥 IUT telegram groups ", reply_markup=keyboard)

        elif message.text == "🤖 Bots":
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            url_button0 = types.InlineKeyboardButton(text="💰 IUT accounting bot", url="t.me/IUTtheBestbot")
            url_button1 = types.InlineKeyboardButton(text="🗒 Timetable", url="t.me/IUTimeTable_Bot")
            keyboard.add(url_button0, url_button1)
            bot.send_message(message.chat.id, "🤖 IUT telegram bots", reply_markup=keyboard)

        elif message.text == "📢 Channels":
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            url_button1 = types.InlineKeyboardButton(text="📣 Public channel",
                                                     url="https://t.me/inha_uz")
            url_button2 = types.InlineKeyboardButton(text="🇺🇿 IUT Youth Union",
                                                     url="https://t.me/iutyu")
            url_button3 = types.InlineKeyboardButton(text="👥 IUT students", url="https://t.me/studentsinha")
            url_button4 = types.InlineKeyboardButton(text="🚀 IUT share",
                                                     url="https://t.me/iutshare")
            url_button5 = types.InlineKeyboardButton(text="✔ Google I/O extended IUT",
                                                     url="https://t.me/iutextended")
            url_button6 = types.InlineKeyboardButton(text="✔ @IUT",
                                                     url="https://t.me/atiut")
            url_button7 = types.InlineKeyboardButton(text="✔ MUIC Uzbekistan",
                                                     url="https://t.me/muicuzbekistan")
            url_button8 = types.InlineKeyboardButton(text="✔ MITUZ",
                                                     url="https://t.me/wwwmituz")
            url_button9 = types.InlineKeyboardButton(text="✔ ChallengesUz",
                                                     url="https://t.me/challengesuz")
            url_button10 = types.InlineKeyboardButton(text="✔ IUTshnick",
                                                      url="https://t.me/iutshnick")
            url_button11 = types.InlineKeyboardButton(text="✔ Internships",
                                                      url="https://t.me/ustozshogirt")
            keyboard.row(url_button1, url_button2)
            keyboard.row(url_button3, url_button4)
            keyboard.row(url_button5)
            keyboard.row(url_button6, url_button7)
            keyboard.row(url_button8, url_button9)
            keyboard.row(url_button10, url_button11)
            bot.send_message(message.chat.id, "📢 IUT Telegram channels", reply_markup=keyboard)
        elif message.text == "🌍 Soc. Net":
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            url_button1 = types.InlineKeyboardButton(text="Facebook IUT group",
                                                     url="https://www.facebook.com/groups/inhauniversityintashkent")
            url_button2 = types.InlineKeyboardButton(text="FB page IUT Students Life", url="https://www.facebook.com/"
                                                                                           "iutstudents/")
            url_button3 = types.InlineKeyboardButton(text="Instagram",
                                                     url="https://www.instagram.com/iutstudents/")
            url_button4 = types.InlineKeyboardButton(text="Twitter",
                                                     url="https://twitter.com/Inha_Tashkent")
            url_button5 = types.InlineKeyboardButton(text="YouTube",
                                                     url="https://www.youtube.com/channel/UC61W3C4BGMIIzYU6orDzzTw")
            url_button6 = types.InlineKeyboardButton(text="Google+",
                                                     url="https://plus.google.com/+InhaUz")
            url_button7 = types.InlineKeyboardButton(text="Linkedin",
                                                     url="https://www.linkedin.com/in/inha-university-in-tashkent-"
                                                         "280000a6/")
            keyboard.row(url_button1)
            keyboard.row(url_button2)
            keyboard.row(url_button3)
            keyboard.row(url_button4)
            keyboard.row(url_button5)
            keyboard.row(url_button6)
            keyboard.row(url_button7)
            bot.send_message(message.chat.id, "🌍 IUT social networks", reply_markup=keyboard)

    # ACADEMICS

        elif message.text == '💰 Accounting':
            bot.send_message(message.from_user.id, 'There you can check your IUT account balance', reply_markup=user_markup_hide)
            askk = bot.reply_to(message, 'Send passport id as:')
            bot.register_next_step_handler(askk, account_check)
            bot.send_message(message.chat.id, " AA*******")

        elif message.text == '👤 Professors':
            bot.send_message(message.chat.id, "Abhijit Tarawade\na.tarawade@inha.uz\n\n"
                                             # "Office #"
                                              "Alessandro Agostini\na.agostini@inha.uz\n\n"
                                              "Alisher Sanetullaev\na.sanetullaev@inha.uz\n\n"
                                              "Andrei Dragunov\na.dragunov@inha.uz\n\n"
                                              "Ashish Seth\na.seth@inha.uz\n\n"
                                              "Bahodir Ahmedov\nb.ahmedov@inha.uz\n\n"
                                              "Bohodir Rakhimov\nb.rakhimov@inha.uz\n\n"
                                              "Chongkoo An\nc.an@inha.uz\n\n"
                                              "Iroda Saydazimova\ni.saydazimova@inha.uz\n\n"
                                              "Irodakhon Maksudova\ni.maksudova@inha.uz\n\n"
                                              "Jasurbek Khodjaev\nj.khodjaev@inha.uz\n\n"
                                              "Joung Yong Lee\njy.lee@inha.uz\n\n"
                                              "Ju Yeon Oh\njy.oh@inha.uz\n\n"
                                              "Khusniddin Olimov\nk.olimov@inha.uz\n\n"
                                              "Kirti Seth\nk.seth@inha.uz\n\n"
                                              "Naseer Abdul Rahim\nn.abdulrahim@inha.uz\n\n"
                                              "Rano Neyaskulova\nr.neyaskulova@inha.uz\n\n"
                                              "Rustam Turdibaev\nr.turdibaev@inha.uz\n\n"
                                              "Sarvar Abdullaev\ns.abdullaev@inha.uz\n\n"
                                              "Steftcho Dokov\ns.dokov@inha.uz\n\n"
                                              "Irfanud Din\nirfan@inha.uz\n\n"
                                              "Shodiya SaydalievaTeacher\nsh.saydalieva@inha.uz\n\n")

        elif message.text == '🗓 Calendar':
            bot.send_message(message.chat.id, "Academic calendar")
            photo = open('media/academic_cal.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            # bot.send_photo(photo ='academic_cal.png')
        elif message.text == 'Data':
            mestext = bot.send_message(message.chat.id, "Send me excel file!")
            #bot.message_handler(func=lambda message: message.document.mime_type == 'application/'
                                #'vnd.openxmlformats-officedocument.spreadsheetml.sheet', content_types=['document'])
            bot.register_next_step_handler(mestext, test_get_file)
            bot.send_message(message.chat.id, "Got you)")
        else:
            bot.send_message(message.chat.id, "Sorry! Retry again later\n Press /start \n[-%s-] is not available now("
                             % message.text)

    except Exception as e:
        bot.reply_to(message, 'Oooops! Press /start to go Main_menu')


if __name__ == '__main__':
    while True:

        try:
            bot.polling(none_stop=True)

        except Exception as e:

            logger.error(e)

            time.sleep(15)

bot.polling()
