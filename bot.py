from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

TOKEN = "8087642219:AAEp-vuWjecCWxjcOMQUGWQjXbcZuKGCwWU"
ADMIN_ID = 7591213135

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    await msg.answer("Bot ishga tushdi. /adminpanel buyrug‘ini sinab ko‘r.")

@dp.message_handler(commands=['adminpanel'])
async def adminpanel_cmd(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("➕ Anime qo‘shish", callback_data="add_anime"),
        InlineKeyboardButton("🎬 Qism qo‘shish", callback_data="add_episode"),
        InlineKeyboardButton("✏️ Anime tahrirlash", callback_data="edit_anime"),
        InlineKeyboardButton("📢 Post tayyorlash", callback_data="prepare_post"),
    )
    await msg.answer("Admin panel:", reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)