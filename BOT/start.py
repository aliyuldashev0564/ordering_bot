from config import db, bot
from config import admins
from aiogram import  types,executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from adding_to_db import selecting, add_user
from keyboards import savvat
from states import Start, admin
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
@db.message_handler(Command('start'),state='*')
async def  start(msg: types.Message, state: FSMContext):
    user = await selecting(msg.chat.id)
    if user:
        if msg.chat.id == admins:
            await bot.send_message(msg.chat.id, 'malumotlar kelishini kutung')
            await admin.admin.set()
        else:
            await bot.send_message(msg.chat.id,"SIZ BOTNI QAYTA ISHGA TUSHURDIZ", reply_markup=savvat)
            await state.finish()
    else:
        await bot.send_message(msg.chat.id, """parolni kriting""")
        await Start.parol.set()


@db.message_handler(state=Start.parol)
async def  start(msg: types.Message, state: FSMContext):
    user = msg.text
    if user == 'Coder098':
        await bot.send_message(msg.chat.id, f"TO`G`RI TOPDINGIZ\n"
                                            f"ism sharifingizni kriting")
        await Start.next()
    else:
        await bot.send_message(msg.chat.id, f"PAROL NO`TO`G`RI QAYTADAN KRITING")
        await Start.parol.set()
@db.message_handler(state=Start.ism)
async def  start(msg: types.Message, state: FSMContext):
    user = msg.text
    if len(user)>10:
        await bot.send_message(msg.chat.id,
                                            f"telefon raqamingizni kriting")
        await state.update_data({
            'new_user':{
                'name':f'{user}',
                }})
        await Start.next()
    else:
        await bot.send_message(msg.chat.id, f"MALUMOT  NO`TO`G`RI QAYTADAN KRITING")
        await Start.ism.set()
@db.message_handler(state=Start.tell)
async def  start(msg: types.Message, state: FSMContext):
    user = msg.text
    if user[0] == '+' and len(user) == 13:
        await bot.send_message(msg.chat.id,
                                            f"MALUMOTINGIZ QABUL QILINDI\n"
                                            f"START TUGMASINI BOSING", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
                KeyboardButton(text='/start')
            ))
        data = await state.get_data()
        id = msg.chat.id
        name = data['new_user']['name']
        tell = msg.text
        print(f'{id}  {name}   {tell}')
        await add_user(telegram_id = id, name=name,tell = tell)
        await state.finish()
    else:
        await bot.send_message(msg.chat.id, f"MALUMOT  NO`TO`G`RI QAYTADAN KRITING")
        await Start.ism.set()