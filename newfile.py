import os
try :
    import requests,telebot
    from telebot import *
    import random,json
    from time import *
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install telebot')
    os.system('pip install pyTelegramBotAPI==3.7.6')
token="6317132128:AAEH6PLqXWFKTwz4doO7pLdWy4GmsImyv6Q"
bot = telebot.TeleBot(token)
def chooselecture(filepath):
    with open(filepath, 'r') as file:
        lectures = json.load(file)
        selectedlecture = random.choice(lectures)
        return selectedlecture
filepath = 'Lectures.json'
@bot.message_handler(commands=['start'])
def start(message):
    id = message.from_user.id
    name = message.from_user.first_name
    use = message.from_user.username
    key = types.InlineKeyboardMarkup()
    
    bot14 = types.InlineKeyboardButton(f'''
📥  اضافه قناة  📥
''',callback_data='d1')  
    key.add(bot14)
    bot.send_message(message.chat.id,f"""<strong>
مرحبا {name} أهلا بك في بوت القرآن الكريم 🌷.

</strong>""",parse_mode="html",reply_to_message_id=message.message_id,reply_markup=key,timeout=3.5)
    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "d1":
         d1(message,call)
def d1(message,call):
    bot.send_message(message.chat.id, text=f"<strong> قم برفع البوت ادمن في قناتك ثم ارسل ايدي القناة؟</strong>",parse_mode="html",timeout=3.5)
    @bot.message_handler(func=lambda message: True)
    def nn(message):

            user_ch = message.text
            us = bot.get_chat(f"@{user_ch}").id
            chat_id = message.chat.id
            user_id = bot.get_me().id
            user_ch='@'+user_ch

    
     
            is_admin = bot.get_chat_member(user_ch , user_id).status == 'creator' or bot.get_chat_member(user_ch, user_id).status == 'administrator'
        
            if is_admin:
                bot.send_message(message.chat.id, text=f"<strong>تم اضافة القناة إلى الإرسال التلقائي . سيتم ارسال اية قرانية عشوائيه كل 24 ساعة إلى القناة ✅</strong>",parse_mode="html",timeout=3.5)
                while True :
                   try:
                      url = f'https://api.telegram.org/bot{token}/sendVideo'
                      selected_lecture = chooselecture(filepath)
                      path = selected_lecture['FilePath'].replace('./', '')
                      text = selected_lecture['Lectures']        
                      data = {
                        'chat_id': us,
                        'caption':text
        }

        
                      files = {'video': open(path, 'rb')}

        
                      response = requests.post(url, data=data, files=files)
                      time.sleep(86400)
                   except:pass
            else:
                bot.send_message(chat_id, "انت لم تقم باضافة البوت يرجى اضافة البوت اولا ")
            
    
 
        
         
            





bot.infinity_polling()