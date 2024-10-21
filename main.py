from aiogram import Bot, Dispatcher
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


async def spam(bot: Bot):
    for user in await rq.get_users():
        try:
            await bot.send_message(user, f'билли джиин')
        except Exception:
            continue


async def spam1(bot: Bot):
    for user in await rq.get_users():
        try:
            await bot.send_message(user, f'насрал в кувшиин')
        except Exception:
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
    scheduler.add_job(spam1, trigger='interval', minutes=1, args=[bot])
    scheduler.start()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
