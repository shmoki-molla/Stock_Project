from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram import types
import app.requests as rq
import app.keyboard as kb
from app.functions import get_companies2, get_company_name
from app.classes import Company

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await rq.set_user(message.from_user.id, message.from_user.full_name)
    await message.answer(f'Привет, {message.from_user.username}', reply_markup=kb.main)


@router.message((F.text == 'Выбрать компанию'))
async def add_company(message: Message, state: FSMContext):
    await state.set_state(Company.tg_id)
    await state.update_data(tg_id=message.from_user.id)
    await message.answer('Выберите интересующие вас компании:', reply_markup=await kb.companies_list())


@router.callback_query(F.data[0] == '0')
async def add_company2(callback: CallbackQuery, state: FSMContext):
    id = await state.get_data()
    tg_id = id.get("tg_id")
    try:
        await rq.add_company_to_user(tg_id, callback.data[1:])
        await callback.message.answer('Успех!')
    except Exception as e:
        await callback.message.answer(f'Что-то пошло не так: {e}')


@router.message((F.text == "Отслеживаемые компании"))
async def show_companies(message: Message):
    companies = await rq.get_companies_from_user(message.from_user.id)
    print(f'!!!TG_ID: {message.from_user.id} ')
    result = f'Вот список интересующих вас компаний:\n'
    for company in companies:
        result += f'{get_company_name(company)}\n'
    await message.answer(result, reply_markup=await kb.delete_button())


@router.message((F.text == 'Где я?'))
async def helper(message: Message):
    help_text = '''
    Нажми на "Выбрать компанию", чтобы отметить интересующие тебя компании
    Ежедневно тебе будут высылаться графики изменения акций этих компаний за последние 100 дней!
    '''
    await message.answer(help_text)


@router.callback_query(F.data == 'delete_company')
async def choose_company_for_delete(callBack: CallbackQuery, state: FSMContext):
    await state.set_state(Company.tg_id)
    await state.update_data(tg_id=callBack.from_user.id)
    print(f'???TG_ID: {callBack.from_user.id}')
    await callBack.message.answer('Выберите компании, которые хотите удалить:',
                                  reply_markup=await kb.del_companies_list(callBack.from_user.id))


@router.callback_query(F.data == 'check')
async def get_plots_now(callBack: CallbackQuery, state: FSMContext):
    table_names = ['stock_prices', 'stock_amzn', 'stock_googl', 'stock_msft', 'stock_tsla']
    stock_dict = {
        "AAPL": "stock_prices",
        "AMZN": "stock_amzn",
        "GOOGL": "stock_googl",
        "MSFT": "stock_msft",
        "TSLA": "stock_tsla"
    }
    await state.set_state(Company.tg_id)
    await state.update_data(tg_id=callBack.from_user.id)
    try:
        users_companies = await rq.get_companies_from_user(callBack.from_user.id)
        if users_companies is None:
            await callBack.message.answer('Вы не выбрали интересующие вас компании')
        else:
            companies = [stock_dict[key] for key in users_companies if key in stock_dict]
            for company in companies:
                file_path = f"C:/Users/Shmoki Molla/PycharmProjects/Stock_Project/{company}.png"
                await callBack.message.answer_photo(photo=types.FSInputFile(path=file_path))
    except Exception as e:
        print(f'{e}')
        await callBack.message.answer(f'{e}')


@router.callback_query(F.data[0] == '1')
async def delete_company(callBack: CallbackQuery, state: FSMContext):
    id = await state.get_data()
    tg_id = id.get("tg_id")
    try:
        await rq.delete_company(tg_id, callBack.data[1:])
        await callBack.message.answer('Успех! Компания удалена')
    except Exception as e:
        await callBack.message.answer(f'Что-то пошло не так: {e}')
