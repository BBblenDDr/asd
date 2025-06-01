import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.handlers import router

token = '8197844559:AAHCTLpcPsvtip36n6R39q6eh3_xTz7_pdc'

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=token,
              default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped by user")
