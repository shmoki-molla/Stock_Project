from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Выбрать компанию')],
                                     [KeyboardButton(text='Отслеживаемые компании')],
                                     [KeyboardButton(text='Где я?')]],
                           resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')