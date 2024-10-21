from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.requests as rq
import app.keyboard as kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await rq.set_user(message.from_user.id, message.from_user.full_name)
    await message.answer(f'Привет, {message.from_user.username}', reply_markup=kb.main)




