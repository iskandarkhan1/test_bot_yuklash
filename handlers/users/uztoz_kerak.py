from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from data.config import ADMINS
from loader import dp,bot
from states.personalData import ustoz_kerak
# from keyboards.inline.shogirtinline import menu1
from keyboards.default.shogrt import tugri, menu, tugri1
from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import ReplyKeyboardRemove

Number = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


# /userdata komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text = "Uztoz kerak" ,state=None)
async def uk_salom(message: types.Message):
    await message.answer("To'liq ismingizni kiriting",reply_markup=tugri1)
    await ustoz_kerak.fullName.set()
@dp.message_handler(Text(equals="Orqaga"), state=ustoz_kerak,)
async def ortga(message:types.Message, state : FSMContext):
    await message.answer("Kerakli bulimni tanlang ", reply_markup=menu)
    await state.finish()    


@dp.message_handler(state=ustoz_kerak.fullName)
async def uk_name(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer(" 👨‍💼Yosh :  Yoshingizni kiriting? \n Masalan : 20 ")

    # await ustoz_kerak.adress.set()
    await ustoz_kerak.yosh.set()

@dp.message_handler(state=ustoz_kerak.yosh)
async def sho_yosh(message: types.Message, state: FSMContext):
    fullname  = message.text
    try:
        yosh = int(fullname)
        await state.update_data({"yosh ":yosh})
        await message.answer(" 🛠Ma'lumotingiz  : \n Oliy yoki o'rta maxsus")
        await ustoz_kerak.kasblar.set()
    except ValueError:
        await message.answer("Yoshingizni togri kirgazing !!!") 

@dp.message_handler(state=ustoz_kerak.kasblar)
async def uk_kaslar(message: types.Message, state: FSMContext):
    qila_oladigan_iw= message.text

    await state.update_data(
        {"kasblar": qila_oladigan_iw}
    )
    await message.answer(" 📞 Telfon raqamingizni togri kiriting:  \n masalan +998912345678. ")

    await ustoz_kerak.phone.set()

@dp.message_handler(state=ustoz_kerak.phone, regexp=Number)
async def uk_telefon(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )
    await message.answer(" 🌏 Hududingizni kiriting: \n viloyatingiz yoki shaxringiz.")

    await ustoz_kerak.hudud.set()

@dp.message_handler(state=ustoz_kerak.phone, )
async def uk_phone(message: types.Message, state: FSMContext):

    await message.answer(" Telfonni to'g'ri kirgazing !!!xato ")

    await ustoz_kerak.phone.set()





@dp.message_handler(state=ustoz_kerak.hudud)
async def uk_hudud(message: types.Message, state: FSMContext):
    hudud = message.text

    await state.update_data(
        {"hudud": hudud}
    )
    await message.answer(" 💰 Maoshingiz : \n Pullik yoki tekinmi? \n Kerakli summani kitiring.")

    await ustoz_kerak.narx.set()
    

@dp.message_handler(state=ustoz_kerak.narx)
async def uk_narx(message: types.Message, state: FSMContext):
    price = message.text

    await state.update_data(
        {"narx": price}
    )
    await message.answer("🧑‍💻 Kasbi:\n Qaysi kasbni uztozi kerak   \n Masalan Mexanik. ")

    await ustoz_kerak.job.set()

@dp.message_handler(state=ustoz_kerak.job)
async def uk_job(message: types.Message, state: FSMContext):
    ish = message.text

    await state.update_data(
        {"job": ish}
    )
    await message.answer(" 🕔 Murojaat qilish vaqti : \n Qaysi vatda murojat qilish mumkin ? \n Masalan, 9:00 - 18: 00. ")

    await ustoz_kerak.time.set()

@dp.message_handler(state=ustoz_kerak.time)
async def uk_time(message: types.Message, state: FSMContext):
    vaqt = message.text

    await state.update_data(
        {"time": vaqt}
    )
    await message.answer("💡 Maqsad : \n Maqsadingizni qisqacha tuwintirib bering.  ")

    await ustoz_kerak.concution.set()

@dp.message_handler(state=ustoz_kerak.concution)
async def uk_xulosa(message: types.Message, state: FSMContext):
    maqsad = message.text

    await state.update_data(
        {"concution": maqsad}
    )
    await message.answer("Agar shu malumotlar to'g'ri bulsa HA tugamsini bosing ",reply_markup=tugri)

    await ustoz_kerak.togri.set()  




    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    yosh = data.get("yosh")
    qila_oladigan_iw = data.get("kasblar")
    phone = data.get("phone")
    hudud = data.get("hudud")
    price = data.get("narx")
    job = data.get("job")
    time = data.get("time")
    concution = data.get("concution")
  

    msg = "Siz kiritgan malumotlar to'g'riligiga ishonchingiz komilmi !!!\n  "
    msg += f"Ustoz kerak : - {name}\n"
    msg += f" 👨‍💼 yoshingiz: - {yosh}\n"
    msg += f" 🛠 Kasbingiz: - {qila_oladigan_iw}\n"
    msg += f"📞 Telefon: - {phone}\n "
    msg += f"🌏 Hududingiz: - {hudud}\n"
    msg += f"🛰 Aloqa ucun - @{message.from_user.username}\n "
    msg += f"💰 Narxi: - {price}\n"
    msg += f"🧑‍💻 Kasbi: - {job}\n"
    msg += f"🕔 Murojaat qilish vaqti : {time}\n"
    msg += f"💡 Maqsad - {concution}\n"
    msg += f"#Ustoz  #{hudud}  #{qila_oladigan_iw} #{job}"
    await message.answer(msg)

@dp.message_handler(Text(equals="Ha"), state=ustoz_kerak.togri)
async def ha(message:types.Message,state:FSMContext):
    data = await state.get_data()
    name = data.get("name")
    yosh = data.get("yosh")
    qila_oladigan_iw = data.get("kasblar")
    phone = data.get("phone")
    hudud = data.get("hudud")
    price = data.get("narx")
    job = data.get("job")
    time = data.get("time")
    concution = data.get("concution")
  

    msg = "Ustoz kerak : \n \n  "
    msg += f"Ismingiz: - {name}\n"
    msg += f" 👨‍💼 yoshingiz: - {yosh}\n"
    msg += f" 🛠 Malumoti: - {qila_oladigan_iw}\n"
    msg += f"📞 Telefon: - {phone}\n "
    msg += f"🌏 Hududingiz: - {hudud}\n"
    msg += f"🛰 Aloqa ucun - @{message.from_user.username}\n "
    msg += f"💰 Narxi: - {price}\n"
    msg += f"🧑‍💻 Kasbi: - {job}\n"
    msg += f"🕔 Murojaat qilish vaqti : {time}\n"
    msg += f"💡 Maqsad - {concution}\n"
    msg +=f"#Ustoz #{hudud} #{qila_oladigan_iw} #{job}"





    await message.answer("Yangi malumot qabul qilindi !!!", reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0], text=msg) 
    await state.finish()

@dp.message_handler(Text(equals="Yo'q"), state=ustoz_kerak.togri)
async def yoq(message:types.Message, state:FSMContext):
    await message.answer("Qabul qilinmadi", reply_markup=menu) 
