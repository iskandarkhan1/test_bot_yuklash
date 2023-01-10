from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from data.config import ADMINS
from loader import dp,bot
from states.personalData import ish_kerak_state
# from keyboards.inline.shogirtinline import menu1
from keyboards.default.shogrt import tugri, menu, tugri1
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import Text

Number = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


# /userdata komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text = "Ish-joy kerak" ,state=None)
async def enter1(message: types.Message):
    await message.answer(" ismingiz  : ?",reply_markup=tugri1)
    await ish_kerak_state.fullName.set()

@dp.message_handler(Text(equals="Orqaga"), state=ish_kerak_state,)
async def ortga(message:types.Message, state : FSMContext):
    await message.answer("Kerakli bulimni tanlang ", reply_markup=menu)
    await state.finish()

@dp.message_handler(state=ish_kerak_state.fullName)
async def hk_name(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer(" 👨‍💼Yosh :  Yoshingizni kiriting? \n Masalan : 20 ")

    # await hodim_kerak_state.adress.set()
    await ish_kerak_state.yosh.set()

@dp.message_handler(state=ish_kerak_state.yosh)
async def sho_yosh(message: types.Message, state: FSMContext):
    fullname  = message.text
    try:
        yosh = int(fullname)
        await state.update_data({"yosh":yosh})
        await message.answer(" 🛠Ma'lumotingiz  : \nOliy yoki o'rta maxsus :")  
        await ish_kerak_state.kasblar.set()
    except ValueError:
        await message.answer("Yoshingizni togri kirgazing !!!")

@dp.message_handler(state=ish_kerak_state.yosh)
async def ik_yosh(message: types.Message, state: FSMContext):
    yosh  = message.text

    await state.update_data(
        {"yosh": yosh}
    )

    await message.answer(" 🛠 Ma'lumotingiz  : \n Oliy yoki o'rta maxsus: ") 

    await ish_kerak_state.kasblar.set()


@dp.message_handler(state=ish_kerak_state.kasblar)
async def ik_kasblar(message: types.Message, state: FSMContext):
    qila_oladigan_iw= message.text

    await state.update_data(
        {"kasblar": qila_oladigan_iw}
    )
    await message.answer(" 📞 Telfon raqamingizni togri kiriting:  \n masalan +99891-34-56-78. ")

    await ish_kerak_state.phone.set()
@dp.message_handler(state=ish_kerak_state.phone, regexp=Number)
async def ik_raqam(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )
    await message.answer(" 🌏 Hududingizni kiriting: \n viloyatingiz yoki shaxringiz.")

    await ish_kerak_state.hudud.set()

@dp.message_handler(state=ish_kerak_state.phone, )
async def ik_telnuber(message: types.Message, state: FSMContext):

    await message.answer("Telfonni to'g'ri kirgazing !!! ")

    await ish_kerak_state.phone.set()





@dp.message_handler(state=ish_kerak_state.hudud)
async def ik_hudud(message: types.Message, state: FSMContext):
    hudud = message.text

    await state.update_data(
        {"hudud": hudud}
    )
    await message.answer(" 💰maoshingiz  : \n Pullik yoki tekinmi? \n Kerakli summani kitiring.")

    await ish_kerak_state.narx.set()
    

@dp.message_handler(state=ish_kerak_state.narx)
async def ik_narx(message: types.Message, state: FSMContext):
    price = message.text

    await state.update_data(
        {"narx": price}
    )
    await message.answer("🧑‍💻 Kasbi:\n Qaysi kasbda ishlaysz  \n Masalan Shifokor. ")

    await ish_kerak_state.job.set()    



@dp.message_handler(state=ish_kerak_state.job)
async def ik_job(message: types.Message, state: FSMContext):
    ish = message.text

    await state.update_data(
        {"job": ish}
    )
    await message.answer(" 🕔 Murojaat qilish vaqti : \n Qaysi vatda murojat qilish mumkin ? \n Masalan, 9:00 - 18: 00. ")

    await ish_kerak_state.time.set()

@dp.message_handler(state=ish_kerak_state.time)
async def ik_time(message: types.Message, state: FSMContext):
    vaqt = message.text

    await state.update_data(
        {"time": vaqt}
    )
    await message.answer("💡 Maqsad : \n Maqsadingizni qisqacha tuwintirib bering.  ")

    await ish_kerak_state.concution.set()

@dp.message_handler(state=ish_kerak_state.concution)
async def ik_conclution(message: types.Message, state: FSMContext):
    maqsad = message.text

    await state.update_data(
        {"concution": maqsad}
    )
    await message.answer("Agar shu malumotlar to'g'ri bulsa Ha tugamsini bosing",reply_markup=tugri)

    await ish_kerak_state.togri.set()  




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
    msg += f"Ismingiz: - {name}\n"
    msg += f" 👨‍💼 yoshingiz: - {yosh}\n"
    msg += f" 🛠 Malumoti : - {qila_oladigan_iw}\n"
    msg += f"📞 Telefon: - {phone}\n "
    msg += f"🌏 Hududingiz: - {hudud}\n"
    msg += f"🛰 Aloqa ucun - @{message.from_user.username}\n "
    msg += f"💰 Narxi: - {price}\n"
    msg += f"🧑‍💻 Kasbi: - {job}\n"
    msg += f"🕔 Murojaat qilish vaqti : {time}\n"
    msg += f"💡 Maqsad - {concution}\n"
    msg += f"#Idora , #{hudud}, #{qila_oladigan_iw}, #{job}"
    await message.answer(msg)



    
@dp.message_handler(Text(equals="Ha"), state=ish_kerak_state.togri)
async def ik_ha(message:types.Message,state:FSMContext):
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
  

    msg = "Ish-Joy kerak : !!!\n \n   "
    msg += f"Ismingiz: - {name}\n"
    msg += f" 👨‍💼 yoshingiz: - {yosh}\n"
    msg += f" 🛠 Malumotingiz : - {qila_oladigan_iw}\n"
    msg += f"📞 Telefon: - {phone}\n "
    msg += f"🌏 Hududingiz: - {hudud}\n"
    msg += f"🛰 Aloqa ucun - @{message.from_user.username}\n "
    msg += f"💰 Narxi: - {price}\n"
    msg += f"🧑‍💻 Kasbi: - {job}\n"
    msg += f"🕔 Murojaat qilish vaqti : {time}\n"
    msg += f"💡 Maqsad - {concution}\n"
    msg +=f" #Idora #{hudud} ,#{qila_oladigan_iw}, #{job}"  
    
    await message.answer("Yangi malumot qabul qilindi !!!", reply_markup=menu)
    await bot.send_message(chat_id=ADMINS[0], text=msg) 
    await state.finish()

@dp.message_handler(Text(equals="Yo'q"), state=ish_kerak_state.togri)
async def ik_yoq(message:types.Message, state:FSMContext):
    await message.answer("Qabul qilinmadi", reply_markup=menu)   

