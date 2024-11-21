from aiogram import Bot, Dispatcher, types
import os
import asyncio
from dotenv import load_dotenv
from app.models import async_main
from app.handlers import router
import app.requests as rq
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
import datetime
from app.functions import create_plot
import io
import aiofiles


async def spam(bot: Bot):
    table_names = ['stock_prices', 'stock_amzn', 'stock_googl', 'stock_msft', 'stock_tsla']
    stock_dict = {
        "AAPL": "stock_prices",
        "AMZN": "stock_amzn",
        "GOOGL": "stock_googl",
        "MSFT": "stock_msft",
        "TSLA": "stock_tsla"
    }
    for table_name in table_names:
        plot_image = await create_plot(table_name)
    for user in await rq.get_users():
        try:
            users_companies = await rq.get_companies_from_user(user)
            if users_companies is None:
                await bot.send_message(user, 'Вы не интересуетесь акциями((((((((((')
            else:
                companies = [stock_dict[key] for key in users_companies if key in stock_dict]
                for company in companies:
                    file_path = f"C:/Users/Shmoki Molla/PycharmProjects/Stock_Project/{company}.png"
                    await bot.send_photo(user, photo=types.FSInputFile(path=file_path))
        except Exception as e:
            print(f'{e}')
            await bot.send_message(user, f'{e}')
            continue




async def main():
    await async_main()
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN_API'))
    dp = Dispatcher()
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(spam, trigger='cron', hour=datetime.datetime.now().hour,
                      minute=datetime.datetime.now().minute + 1,
                      start_date=datetime.datetime.now(), args=[bot])
    scheduler.start()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

#TODO
# 1) Функция удаления компании
# 2) Вывод графиков по нажатию кнопки
# 3) Отображение дат в датафрейме и графиках

