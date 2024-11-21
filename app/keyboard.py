from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import app.requests as rq
from app.functions import get_company_name

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Выбрать компанию')],
                                     [KeyboardButton(text='Отслеживаемые компании')],
                                     [KeyboardButton(text='Где я?')]],
                           resize_keyboard=True, input_field_placeholder='Выберите пункт меню...')
async def companies_list():
    comp_list = InlineKeyboardBuilder()
    companies = await rq.get_companies()
    print(companies)
    for company in companies:
        comp_list.add(InlineKeyboardButton(text=f'{get_company_name(str(company[0]))}', callback_data=f'{str(company[0])}'))
    return comp_list.adjust(1).as_markup()

