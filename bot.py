# from collections import namedtuple
#
# Book = namedtuple('Book', 'book_id book_name book_author book_year book_price')
#
# Books = [
#     (1, "Бронепароходы", "Алексей Иванов", 2023, 200),
#     (2, "Говори", "Лори Холс Андерсон", 2023, 100),
#     (3, "Наши пропавшие сердца", "Селеста Инг", 2023, 250),
#     (4, "До самого рая", "Ханья Янагихара", 2023, 99.5),
#     (5, "Леон", "Марина и Сергей Дяченко", 2023, 199)
# ]
#
# print("|", "book_id", "|", "book_name", "|", "book_author", "|", "book_year", "|", "book_price")
# for book in Books:
#     book1 = Book(*book)
#     print("|", str(book1.book_id).center(5, " "), "|", str(book1.book_name).center(5, " "), "|", str(book1.book_author).center(5, " "), "|", str(book1.book_year).center(5, " "), "|", str(book1.book_price).center(5, " "))


# ---------------------------------------------------------------------------
# 2

from telebot import TeleBot
from telebot.types import Message

bot = TeleBot(token="6948819597:AAEn1SRyai2hNC4gOyHpYMEp-fbmg9jOulI")
@bot.message_handler(commands=['start'] )
def start(message: Message):
    chat_id = message.chat.id
    print(chat_id)
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu alaykum {full_name}")

@bot.message_handler(content_type= ['text'])
def reaction_to_message(message: Message):
    chat_id = message.chat.id
    bot.copy_message(-4162296122, chat_id, message.text)
@bot.message_handler(content_type= ['photo'])
def reaction_to_photo(message: Message):
    chat_id = message.chat.id
    bot.send_photo(-4162296122, chat_id, message.photo)
@bot.message_handler(content_type= ['video'])
def reaction_to_video(message: Message):
    chat_id = message.chat.id
    bot.send_video(-4162296122, chat_id, message.video)
@bot.message_handler(content_type= ['animation'])
def reaction_to_animation(message: Message):
    chat_id = message.chat.id
    bot.send_animation(-4162296122, chat_id, message.animation)


bot.polling()