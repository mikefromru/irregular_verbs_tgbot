from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def level_verbs():
    builder = InlineKeyboardBuilder()
    builder.button(text='Beginner', callback_data='beginner')
    builder.button(text='Intermediate', callback_data='intermediate')
    builder.button(text='Advanced', callback_data='advanced')
    builder.adjust(1)
    return builder.as_markup()

def get_verb(name):
    '''Get next verb'''
    builder = InlineKeyboardBuilder()
    builder.button(text=name, callback_data='next')
    return builder.as_markup()
