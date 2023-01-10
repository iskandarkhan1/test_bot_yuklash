import re
from aiogram import types

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from data.config import ADMINS
from loader import dp,bot 
from states.personalData import hodim_kerak_state
from keyboards.inline.inline_ import menu1
from keyboards.default.shogrt import tugri, menu , tugri1
from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove ,CallbackQuery 

Number = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.message_handler(text = "Hodim kerak" ,state=None)
async def enter1(message: types.Message):
    await message.answer("Idora nomi : ?",reply_markup=tugri1)
    await hodim_kerak_state.fullName.set()

@dp.message_handler(Text(equals="Orqaga"), state=hodim_kerak_state,)
async def ortga(message:types.Message, state : FSMContext):
    await message.answer("Kerakli bulimni tanlang ", reply_markup=menu)
    await state.finish()

@dp.message_handler(state=hodim_kerak_state.fullName)
async def hk_name(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer(" 👨‍💼Yosh :  Yoshingizni kiriting? \n Masalan : 20 ")

    # await hodim_kerak_state.adress.set()
    await hodim_kerak_state.yosh.set()

@dp.message_handler(state=hodim_kerak_state.yosh)
async def sho_yosh(message: types.Message, state: FSMContext):
    fullname  = message.text
    try:
        yosh = int(fullname)
        await state.update_data({"yosh":yosh})
        await message.answer(" 🛠Ma'lumotingiz  : \nOliy yoki o'rta maxsus :")  
        await hodim_kerak_state.kasblar.set()
    except ValueError:
        await message.answer("Yoshingizni togri kirgazing !!!") 

@dp.message_handler(state=hodim_kerak_state.kasblar)
async def hk_kasblar(message: types.Message, state: FSMContext):
    qila_oladigan_iw= message.text

    await state.update_data(
        {"kasblar": qila_oladigan_iw}
    )
    await message.answer(" 📞 Telfon raqamingizni togri kiriting:  \n masalan +99891-34-56-78. ")

    await hodim_kerak_state.phone.set()

@dp.message_handler(state=hodim_kerak_state.phone, regexp=Number)
async def hk_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )
    await message.answer(" 🌏 Hududingizni kiriting: \n viloyatingiz yoki shaxringiz.")

    await hodim_kerak_state.hudud.set()

@dp.message_handler(state=hodim_kerak_state.phone) 
async def kh_nuber(message: types.Message, state: FSMContext):

    await message.answer("Telfonni to'g'ri Kirgazing !!! ")

    await hodim_kerak_state.phone.set()





@dp.message_handler(state=hodim_kerak_state.hudud)
async def kh_huud(message: types.Message, state: FSMContext):
    hudud = message.text

    await state.update_data(
        {"hudud": hudud}
    )
    await message.answer(" 💰  Maoshingiz : \nPullik yoki tekinmi? \n Uzingizni ish xaqqingizni kiriting  kitiring.")

    await hodim_kerak_state.narx.set()
    

@dp.message_handler(state=hodim_kerak_state.narx)
async def kh_narx(message: types.Message, state: FSMContext):
    price = message.text

    await state.update_data(
        {"narx": price}
    )
    await message.answer("Ishlash vaqtingiz kuniga nechidan nechchigaca  \n Batafsil kirgazib keting :")

    await hodim_kerak_state.job.set()

@dp.message_handler(state=hodim_kerak_state.job)
async def kh_job(message: types.Message, state: FSMContext):
    ish = message.text

    await state.update_data(
        {"job": ish}
    )
    await message.answer(" 🕔 Murojaat qilish vaqti : \nQaysi vatda murojat qilish mumkin ? \n Masalan, 9:00 - 18: 00. ")

    await hodim_kerak_state.time.set()

@dp.message_handler(state=hodim_kerak_state.time)
async def kh_time(message: types.Message, state: FSMContext):
    vaqt = message.text

    await state.update_data(
        {"time": vaqt}
    )
    await message.answer("Qoshimcha Malumot !!!  ")

    await hodim_kerak_state.concution.set()

@dp.message_handler(state=hodim_kerak_state.concution)
async def kh_concution(message: types.Message, state: FSMContext):
    maqsad = message.text

    await state.update_data(
        {"concution": maqsad}
    )
    await message.answer("Agar shu malumotlar to'g'ri bulsa Ha tugamsini bosing",reply_markup=tugri)

    await hodim_kerak_state.togri.set()  


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
  

    msg = "Siz kiritgan malumotlar to'g'riligiga ishonchingiz komilmi !!! \n  "
    msg += f"Idora nomi : - {name}\n"
    msg += f"👨‍💼 Yoshingiz: - {yosh}\n"
    msg += f"🛠 Malumotingiz : - {qila_oladigan_iw}\n"
    msg += f"📞Telefon: - {phone}\n "
    msg += f"🛰 Aloqa ucun - @{message.from_user.username}\n " 
    msg += f"🌏 Hududingiz: - {hudud}\n"
    msg += f"💰 Narxi: - {price}\n"
    msg += f"🛠 Kasb: - {job}\n"
    msg += f"🕔 Murojaat qilish vaqti : {time}\n"
    msg += f"💡 Maqsad - {concution}\n"
    msg += f"#Hodim , #{hudud}, #{qila_oladigan_iw}, #{job}"
    await message.answer(msg)

xdata={}
 
@dp.message_handler(Text(equals="Ha"), state=hodim_kerak_state.togri, user_id=5748826167)
async def kh_ha(message:types.Message,state:FSMContext):
    data = await state.get_data()
    print("botdan adminga ")
    print(data)
    xdata= data
    name = data.get("name")
    yosh = data.get("yosh")
    qila_oladigan_iw = data.get("kasblar")
    phone = data.get("phone")
    hudud = data.get("hudud")
    price = data.get("narx")
    job = data.get("job")
    time = data.get("time")
    concution = data.get("concution")
  

    msg = "Hodim kerak : \n \n  "
    msg += f"Ismingiz: - {name}\n"
    msg += f" 👨‍💼 yoshingiz: - {yosh}\n"
    msg += f" 🛠 Kasbingiz: - {qila_oladigan_iw}\n"
    msg += f"📞 Telefon: - {phone}\n "
    msg += f"🌏 Hududingiz: - {hudud}\n"
    msg += f"🛰 Aloqa ucun - @{message.from_user.username}\n "
    msg += f"💰 Narxi: - {price}\n"
    msg += f"🧑‍💻 Kasbi: - {job}\n"
    msg += f"🕔 Murojaat qilish vaqti : {time}\n"
    msg += f"💡 Maqsad - {concution}\n"
    msg +=f"#Hodim  #{hudud}, #{qila_oladigan_iw}, #{concution}"
    await message.answer("Yangi malumot qabul qilindi !!! ", reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0], text=msg) 
    await state.finish()
   

@dp.message_handler(Text(equals="Yo'q"), state=hodim_kerak_state.togri)
async def kh_yoq(message:types.Message, state:FSMContext):
    await message.answer("Qabul qilinmadi",reply_markup=menu)   
    await state.finish()
    
