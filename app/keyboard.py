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
        comp_list.add(
            InlineKeyboardButton(text=f'{get_company_name(str(company[0]))}', callback_data=f'0{str(company[0])}'))
    return comp_list.adjust(1).as_markup()


async def delete_button():
    del_btn = InlineKeyboardBuilder()
    del_btn.add(InlineKeyboardButton(text='Удалить компанию', callback_data='delete_company'))
    del_btn.add(InlineKeyboardButton(text='Посмотреть акции', callback_data='check'))
    return del_btn.adjust(1).as_markup()


async def del_companies_list(tg_id):
    comp_list = InlineKeyboardBuilder()
    companies = await rq.get_companies_from_user(tg_id)
    print(tg_id)
    print(companies)
    for company in companies:
        comp_list.add(InlineKeyboardButton(text=f'{get_company_name(str(company))}', callback_data=f'1{str(company)}'))
    return comp_list.adjust(1).as_markup()


async def del_comp_list(companies):
    del_list = InlineKeyboardBuilder()
    for company in companies:
        del_list.add(InlineKeyboardButton(text=f'{company}', callback_data=f'{company}'))
    return del_list.adjust(1).as_markup()
