from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
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

@router.callback_query(F.data)
async def add_company2(callback: CallbackQuery, state: FSMContext):
    print('1111111111111111111')
    id = await state.get_data()
    print(f'id: {id}')
    tg_id = id.get("tg_id")
    print(f'tg_id: {tg_id}')
    try:
        print('22222222222222222')
        await rq.add_company_to_user(tg_id, callback.data)
        await callback.message.answer('все кул добавил')
    except Exception as e:
        await callback.message.answer(f'чет пошло не так: {e}')
        print(f'{e}')

@router.message((F.text == "Отслеживаемые компании"))
async def show_companies(message: Message):
    companies = await rq.get_companies_from_user(message.from_user.id)
    result = f'Вот список интересующих вас компаний:\n'
    for company in companies:
        result += f'{get_company_name(company)}\n'
    await message.answer(result)

@router.message((F.text == 'Где я?'))
async def helper(message: Message):
    help_text = '''
    Нажми на "Выбрать компанию", чтобы отметить интересующие тебя компании
    Ежедневно тебе будут высылаться графики изменения акций этих компаний за последние 100 дней!
    '''
    await message.answer(help_text)

