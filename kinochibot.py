import asyncio
import os
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

KANAL_1_ID = "@wenthday2" 
KANAL_LINK_1 = "https://t.me/wenthday2"

KANAL_2_ID = "@s7s_gym"  
KANAL_LINK_2 = "https://t.me/s7s_gym"

bot = Bot(token=TOKEN)
dp = Dispatcher()

conn = sqlite3.connect("kino_bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    referrer INTEGER
)
""")
conn.commit()

KINOLAR_BAZASI = {
    "1": {
        "nomi": "Mr.Robot// Season - 1 Episode - 1// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/2",
        "sifat": "1080p Full HD"
    },
    "2": {
        "nomi": "Mr.Robot// Season - 1 Episode - 2// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/3",
        "sifat": "1080p Full HD"
    },
    "3": {
        "nomi": "Mr.Robot// Season - 1 Episode - 3// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/4",
        "sifat": "1080p Full HD"
    },
    "4": {
        "nomi": "Mr.Robot// Season - 1 Episode - 4// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/5",
        "sifat": "1080p Full HD"
    },
    "5": {
        "nomi": "Mr.Robot// Season - 1 Episode - 5// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/6",
        "sifat": "1080p Full HD"
    },
    "6": {
        "nomi": "Mr.Robot// Season - 1 Episode - 6// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/7",
        "sifat": "1080p Full HD"
    },
    "7": {
        "nomi": "Mr.Robot// Season - 1 Episode - 7// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/8",
        "sifat": "1080p Full HD"
    },
    "8": {
        "nomi": "Mr.Robot// Season - 1 Episode - 8// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/9",
        "sifat": "1080p Full HD"
    },
    "9": {
        "nomi": "Mr.Robot// Season - 1 Episode - 9// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/10",
        "sifat": "1080p Full HD"
    },
    "10": {
        "nomi": "Mr.Robot// Season - 1 Episode - 10// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/11",
        "sifat": "1080p Full HD"
    },
    "11": {
        "nomi": "Mr.Robot// Season - 2 Episode - 1// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/12",
        "sifat": "1080p Full HD"
    },
    "12": {
        "nomi": "Mr.Robot// Season - 2 Episode - 2// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/13",
        "sifat": "1080p Full HD"
    },
    "13": {
        "nomi": "Mr.Robot// Season - 2 Episode - 3// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/14",
        "sifat": "1080p Full HD"
    },
    "14": {
        "nomi": "Mr.Robot// Season - 2 Episode - 4// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/15",
        "sifat": "1080p Full HD"
    },
    "15": {
        "nomi": "Mr.Robot// Season - 2 Episode - 5// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/16",
        "sifat": "1080p Full HD"
    },
    "16": {
        "nomi": "Mr.Robot// Season - 2 Episode - 6// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/17",
        "sifat": "1080p Full HD"
    },
    "17": {
        "nomi": "Mr.Robot// Season - 2 Episode - 7// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/18",
        "sifat": "1080p Full HD"
    },
    "18": {
        "nomi": "Mr.Robot// Season - 2 Episode - 8// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/19",
        "sifat": "1080p Full HD"
    },
    "19": {
        "nomi": "Mr.Robot// Season - 2 Episode - 9// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/20",
        "sifat": "1080p Full HD"
    },
    "20": {
        "nomi": "Mr.Robot// Season - 2 Episode - 10// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/21",
        "sifat": "1080p Full HD"
    },
    "21": {
        "nomi": "Mr.Robot// Season - 2 Episode - 11// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/22",
        "sifat": "1080p Full HD"
    },
    "22": {
        "nomi": "Mr.Robot// Season - 3 Episode - 1// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/23",
        "sifat": "1080p Full HD"
    },
    "23": {
        "nomi": "Mr.Robot// Season - 3 Episode - 2// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/24",
        "sifat": "1080p Full HD"
    },
    "24": {
        "nomi": "Mr.Robot// Season - 3 Episode - 3// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/25",
        "sifat": "1080p Full HD"
    },
    "25": {
        "nomi": "Mr.Robot// Season - 3 Episode - 4// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/26",
        "sifat": "1080p Full HD"
    },
    "26": {
        "nomi": "Mr.Robot// Season - 3 Episode - 5// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/27",
        "sifat": "1080p Full HD"
    },
    "27": {
        "nomi": "Mr.Robot// Season - 3 Episode - 6// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/28",
        "sifat": "1080p Full HD"
    },
    "28": {
        "nomi": "Mr.Robot// Season - 3 Episode - 7// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/29",
        "sifat": "1080p Full HD"
    },
    "29": {
        "nomi": "Mr.Robot// Season - 3 Episode - 8// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/30",
        "sifat": "1080p Full HD"
    },
    "30": {
        "nomi": "Mr.Robot// Season - 3 Episode - 9// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/31",
        "sifat": "1080p Full HD"
    },
    "31": {
        "nomi": "Mr.Robot// Season - 3 Episode - 10// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/32",
        "sifat": "1080p Full HD"
    },
    "32": {
        "nomi": "Mr.Robot// Season - 4 Episode - 1// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/33",
        "sifat": "1080p Full HD"
    },
    "33": {
        "nomi": "Mr.Robot// Season - 4 Episode - 2// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/34",
        "sifat": "1080p Full HD"
    },
    "34": {
        "nomi": "Mr.Robot// Season - 4 Episode - 3// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/35",
        "sifat": "1080p Full HD"
    },
    "35": {
        "nomi": "Mr.Robot// Season - 4 Episode - 4// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/36",
        "sifat": "1080p Full HD"
    },
    "36": {
        "nomi": "Mr.Robot// Season - 4 Episode - 5// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/37",
        "sifat": "1080p Full HD"
    },
    "37": {
        "nomi": "Mr.Robot// Season - 4 Episode - 6// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/38",
        "sifat": "1080p Full HD"
    },
    "38": {
        "nomi": "Mr.Robot// Season - 4 Episode - 7// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/39",
        "sifat": "1080p Full HD"
    },
    "39": {
        "nomi": "Mr.Robot// Season - 4 Episode - 8// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/40",
        "sifat": "1080p Full HD"
    },
    "40": {
        "nomi": "Mr.Robot// Season - 4 Episode - 9// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/41",
        "sifat": "1080p Full HD"
    },
    "41": {
        "nomi": "Mr.Robot// Season - 4 Episode - 10// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/42",
        "sifat": "1080p Full HD"
    },
    "42": {
        "nomi": "Mr.Robot// Season - 4 Episode - 11// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/43",
        "sifat": "1080p Full HD"
    },
    "43": {
        "nomi": "Mr.Robot// Season - 4 Episode - 12// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/44",
        "sifat": "1080p Full HD"
    },
    "44": {
        "nomi": "Mr.Robot// Season - 4 Episode - 13// (Myanmar Subtitle)",
        "file_id": "https://t.me/tgshdkk/45",
        "sifat": "1080p Full HD"
    },
    "45": {
        "nomi": "none",
        "file_id": "https://t.me/tgshdkk/46",
        "sifat": "1080p Full HD"
    }
}

async def obunani_tekshirish(user_id: int) -> bool:
    try:
        member1 = await bot.get_chat_member(chat_id=KANAL_1_ID, user_id=user_id)
        member2 = await bot.get_chat_member(chat_id=KANAL_2_ID, user_id=user_id)
        is_sub1 = member1.status in ["member", "administrator", "creator"]
        is_sub2 = member2.status in ["member", "administrator", "creator"]
        return is_sub1 and is_sub2
    except Exception as e:
        print(f"Obunani tekshirishda xatolik: {e}")
        return False

def obuna_tugmalari():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📢 1-Kanalga qo'shilish", url=KANAL_LINK_1)],
            [InlineKeyboardButton(text="📢 2-Kanalga qo'shilish", url=KANAL_LINK_2)],
            [InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_sub")]
        ]
    )

@dp.message(Command("start"))
async def start_cmd(message: types.Message, state: FSMContext):
    await state.clear()
    uid = message.from_user.id
    uname = message.from_user.username or "Yo'q"

    args = message.text.split()
    referrer = int(args[1]) if len(args) > 1 and args[1].isdigit() and int(args[1]) != uid else None

    cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (uid,))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO users (user_id, username, referrer) VALUES (?, ?, ?)", (uid, uname, referrer))
        conn.commit()

    if await obunani_tekshirish(uid):
        await message.answer(
            f"Salom, <b>{message.from_user.first_name}</b>! 👋\n\nKino ko'rish uchun <b>kino kodini</b> yuboring:",
            parse_mode="HTML"
        )
    else:
        await message.answer(
            f"⚠️ Botdan foydalanish uchun quyidagi kanallarga qo'shiling va <b>'Obunani tekshirish'</b> tugmasini bosing:",
            reply_markup=obuna_tugmalari(),
            parse_mode="HTML"
        )

@dp.callback_query(F.data == "check_sub")
async def check_subscription_callback(call: types.CallbackQuery):
    uid = call.from_user.id
    if await obunani_tekshirish(uid):
        try:
            await call.message.delete()
        except Exception:
            pass
        await call.message.answer("Rahmat! Barcha kanallarga obunangiz tasdiqlandi. 🎉\nEndi kino kodini yuborishingiz mumkin:")
    else:
        await call.answer("❌ Siz hali hamma kanallarga to'liq qo'shilmadingiz!", show_alert=True)

@dp.channel_post(F.video)
async def get_video_file_id(message: types.Message):
    print("\n" + "=" * 40)
    print(f"🎬 KANALGA YANGI KINO YUKLANDI!")
    print(f"📌 Video nomi/caption: {message.caption or 'Nomsiz'}")
    print(f"🔑 Video File ID: {message.video.file_id}")
    print("=" * 40 + "\n")

@dp.message(F.text)
async def kino_qidirish(message: types.Message):
    uid = message.from_user.id
   
    if not await obunani_tekshirish(uid):
        await message.answer(
            "⚠️ Botdan foydalanish uchun avval barcha kanallarga qo'shishingiz kerak!",
            reply_markup=obuna_tugmalari()
        )
        return

    kino_kodi = message.text.strip()

    if kino_kodi in KINOLAR_BAZASI:
        kino = KINOLAR_BAZASI[kino_kodi]
        try:
            await message.answer_video(
                video=kino['file_id'],
                caption=f"🎬 <b>Kino nomi:</b> {kino['nomi']}\n💿 <b>Sifati:</b> {kino['sifat']}\n\n🤖 @discoverfilmbot",
                parse_mode="HTML"
            )
        except Exception as e:
            await message.answer(f"❌ Videoni yuborishda xatolik yuz berdi. File ID (yoki havolani) tekshiring. Xato: {e}")
    else:
        await message.answer("❌ Bunday kodli kino topilmadi. Kodni qaytadan tekshirib ko'ring!")

async def main():
    print("Kino bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
