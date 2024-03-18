import qrcode
import telebot
from telebot import types
import gtts
import random


random_numbers = {}
MIN_NUMBER = 1
MAX_NUMBER = 100
random_number = random.randint(MIN_NUMBER, MAX_NUMBER)

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start_chat(message):
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, " سلام " + first_name + " خوش اومدی به:", reply_markup=menu_keys)
    audio_file = open('Assignment 9/source/welcome.mp3', 'rb')
    bot.send_audio(message.chat.id, audio_file)
    audio_file.close()

menu_keys=  types.ReplyKeyboardMarkup(row_width=3)  
key1 = types.KeyboardButton('بازی')
key2 = types.KeyboardButton('تبدیل سن')
key3 = types.KeyboardButton('صدا')
key4 = types.KeyboardButton('ماکزیمم')
key5 = types.KeyboardButton('ماکزیمم اندیس')
key6 = types.KeyboardButton('تولید کیو آر کد')
menu_keys.add(key1,key2,key3,key4,key5,key6)

@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    if message.text == 'تبدیل سن':
        bot.send_message(message.chat.id, "خب تاریخ تولد دقیقتو بگو، مثال: 05/10/1380")
        bot.register_next_step_handler(message, handle_birthdate)
        
    elif message.text == 'بازی':
        bot.send_message(message.chat.id, "یک عدد بین 1 تا 100 حدس بزن")
        bot.register_next_step_handler(message, handle_guess)
        pass
    elif message.text == 'صدا':
        bot.send_message(message.chat.id, "یک متن انگلیسی بفرست")
        bot.register_next_step_handler(message, handle_voice)
        pass
    elif message.text == 'ماکزیمم':
        bot.reply_to(message, "یک چند تا عدد که با اسپیس جدا شدن بهم بده که بزرگ ترین عدد رو بهت بدم")
        bot.register_next_step_handler(message, handle_maximum)
        pass
    elif message.text == 'ماکزیمم اندیس':
        bot.send_message(message.chat.id, "یک چند تا عدد که با اسپیس جدا شدن بهم بده که بزرگ ترین اندیس رو بهت بدم")
        bot.register_next_step_handler(message, handle_maxindex)
        pass
    elif message.text == 'تولید کیو آر کد':
        bot.send_message(message.chat.id, "یک متن رو بده که تبدیل به کد کیو آر کنمش")
        bot.register_next_step_handler(message, handle_qrcode)
        pass


  


def handle_guess(message):
    while True:
            try:
                guess = int(message.text)
                if guess < MIN_NUMBER or guess > MAX_NUMBER:
                    bot.send_message(message.chat.id, ".لطفا یک عدد بین 1 و 100 انتخاب کن")
                else:
                    if guess == random_number:
                        bot.send_message(message.chat.id, "آفرین عددت درست بود")
                        break
                    elif guess < random_number:
                        bot.send_message(message.chat.id, "عدد مورد نظر بزرگ تره")
                    else:
                        bot.send_message(message.chat.id, "عدد مورد نظر کوچیک تره")
                bot.send_message(message.chat.id, "یک عدد دیگه حدس بزن")
                bot.register_next_step_handler(message, handle_guess)
                return
            except ValueError:
                bot.send_message(message.chat.id, "لطفا یک عدد وارد کن")
                bot.register_next_step_handler(message, handle_guess)
                return
def handle_birthdate(message):
    try:
        # Parse the user's input as a Solar Hijri date
        solar_date_str = message.text
        day, month, year = map(int, solar_date_str.split('/'))
        
        # Convert Solar Hijri date to Gregorian date manually
        gregorian_year = year + 621
        gregorian_month = month
        gregorian_day = day
        
        # Adjust the converted date if needed
        if month > 10 or (month == 10 and day >= 12):
            gregorian_month -= 3
        else:
            gregorian_month += 9
            gregorian_year -= 1
        
        # Send the Gregorian date back to the user
        gregorian_date_str = f"{gregorian_day}/{gregorian_month}/{gregorian_year}"
        bot.reply_to(message, f"تاریخ تولد شما: {gregorian_date_str}")
    except ValueError:
        # Handle invalid input format
        bot.reply_to(message, "Invalid input format. Please enter your birthdate in the format: DD/MM/YYYY")



##function
def handle_voice(message):
    text = message.text
    voice = gtts.gTTS(text, lang = "en", slow = False)
    voice.save("Assignment 9/source/voice.mp3")
    audio_file = open('Assignment 9/source/voice.mp3', 'rb')
    bot.send_audio(message.chat.id, audio_file)
    audio_file.close()
    
        
def handle_maximum(message):
    try:
        # Get the text message and split it into a list of numbers
        numbers = [int(num) for num in message.text.split()]
        
        # Find the maximum number in the list
        max_number = max(numbers)
        
        # Send the maximum number back to the user
        bot.reply_to(message, f"بزرگ ترین عدد: {max_number}")
    except ValueError:
        # Handle the case where non-integer input is provided
        bot.reply_to(message, "Please provide a list of valid numbers separated by spaces.")
    except Exception as e:
        # Handle any other errors that may occur
        bot.reply_to(message, f"An error occurred: {str(e)}")

              

def handle_maxindex(message):
    try:
        # Get the text message and split it into a list of numbers
        numbers = [int(num) for num in message.text.split()]
        
        # Find the index of the maximum number in the list
        max_index = numbers.index(max(numbers))
        
        # Send the index of the maximum number back to the user
        bot.reply_to(message, f"بزرگ ترین اندیس: {max_index}")
    except ValueError:
        # Handle the case where non-integer input is provided
        bot.reply_to(message, "Please provide a list of valid numbers separated by spaces.")
    except Exception as e:
        # Handle any other errors that may occur
        bot.reply_to(message, f"An error occurred: {str(e)}")

def handle_qrcode(message):
    qr = qrcode.make(message.text)
    qr.save("Assignment 9/source/Information.png")
    qr_code = open('Assignment 9/source/Information.png', 'rb')
    bot.send_photo(message.chat.id, qr_code)
    qr_code.close()
      
bot.infinity_polling()