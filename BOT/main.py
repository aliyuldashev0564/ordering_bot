from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import  types
from aiogram.types import CallbackQuery ,Message
from states import Test
from data_fetcher import aget , product
import keyboards
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback_data import product_call, agent_call , order_call, cancel_call, count_call
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from typing import Union
import adding_to_db
from keyboards import countkey
from config import db, bot, admins

@db.callback_query_handler(text='rad_etish', state='*')
async def canncel(msg:types.CallbackQuery, state: FSMContext):
    await msg.answer(cache_time=60)
    await msg.message.answer('savat tozalandi', reply_markup=keyboards.savvat)
    await state.finish()
@db.message_handler(Command('savat'),state='*')
async def  start(msg: types.Message, state: FSMContext):
    datta = await state.get_data()
    resp = await product()
    obnar = 0
    await Test.tavar.set()
    a = await state.get_data()
    txt = ''
    for data in resp:
        try:
            dat = a[f'zakaz_{data["name"]}']
            txt += f'🍫{data["name"].upper()} MAXSULOTIMIZDAN \n'
            txt += f'🔰{dat["kl"]} ta sotib oldiz\n'
            txt += f'🔰{dat["kl"]} * {data["narx"]} = {dat["obn"]} so`m\n'
            obnar += int(dat['obn'])
        except Exception as ex:
            print(ex)
    txt += f'🔰UMUMIY NARX {obnar}\n'
    inline_zakaz = InlineKeyboardMarkup(row_width=1)
    data_d = await adding_to_db.select_agent(telegram_id=msg.chat.id)
    inline_zakaz.insert(InlineKeyboardButton(text='BUYURTMA BERISH', callback_data=f'agent:{msg.chat.id}:{data_d[0]}:{data_d[1]}'))
    inline_zakaz.insert(InlineKeyboardButton(text='savatni tozalash', callback_data='rad_etish'))
    txt += f"✅yana buyurmoqchi bo`lsangiz /maxsulot tugmasini bosing \n"\
           f"❌tugatgan bo`lsangiz gentni tanlang \n"\
           f"buyurmlarni o`chirish uchun bekor qilish tugmasini bosing"
    if obnar == 0:
        await bot.send_message(msg.chat.id, 'buyurma yo`q')
    else:
       await bot.send_message(msg.chat.id, text=txt, reply_markup=inline_zakaz)
       await Test.agent.set()
@db.message_handler(Command('maxsulot'),state='*')
async def  kg(msg: types.Message, state: FSMContext):
    resp = await product()
    await Test.tavar.set()
    key = ReplyKeyboardMarkup(resize_keyboard=True)
    for data in resp:
        NAME =data['name']
        key.add(KeyboardButton(text=NAME))
    await bot.send_message(msg.chat.id, '🍫MAXSULOT TURINI TANLANG', reply_markup=key)

@db.message_handler(state=Test.tavar)
async def productall(msg:types.Message, state:FSMContext):
    name = msg.text
    product_info = await adding_to_db.select_product(name=name)
    narx, image, char = product_info[0], product_info[1], product_info[2]
    char += f'💲narxi: {narx}'
    imag = open(f'D:/python/New/image/{image}','rb')
    await bot.send_photo(msg.chat.id,imag,caption=char)
    await state.update_data({
        'names':{'name':f'{name}','narx':f'{narx}'}
    })
    await bot.send_message(msg.chat.id,'⚖️KELOGRAMINI KRITING!' , reply_markup=countkey)
    await Test.next()
    imag.close()


@db.message_handler(state=Test.kg)
async def agent1(msg: types.Message, state: FSMContext):
    try:
        a = msg.text
        if a.isdigit():
            dat = await state.get_data()
            obshn = eval(f'{dat["names"]["narx"]}*{a}')
            await state.update_data({
                f'zakaz_{dat["names"]["name"]}':{'obn':f'{obshn}','kl':f'{a}'}
            })
            await bot.send_message(msg.chat.id, f'''➕qabul qilindi yana buyurish uchun maxsulot tugmasini bosing. \n✅Tugatgan bo`lsangiz savatga o`ting''', reply_markup=keyboards.savvat)
        else:
            await bot.send_message(msg.chat.id, '''❌NO`TO`G`RI MALUMOT KRITINGIZ 
QAYTADAN KRITING''')
            await Test.kg.set()
    except:
        await bot.send_message(msg.chat.id, '''❌TIZIMDA XATOLIK RO`Y BERDI 
30 SONIYADAN KEYIN 
    ✅   /maxsulot ✅
TUGMASINI BOSING''')
        

@db.callback_query_handler(text = 'cancel', state=Test.agent)
async def canceling(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await call.message.answer('''❌SIZ XOZIR KRITGAN BUYURMALARINGIZ BEKOR QILINDI
QAYTA BUYURTMA BERISH UCHUN maxsulot
TUGMASINI BOSING''', reply_markup=keyboards.savvat)
    await state.finish()


@db.callback_query_handler( agent_call.filter() ,state=Test.agent)
async def ism(call: CallbackQuery, state:FSMContext, callback_data :dict ):
    try:
        await call.answer(cache_time=60)
        a = call.data
        if a == 'bosh saxifa':
            await call.message.answer(f'❌SIZ BOSH SAXIFAGA O`TDINGIZ tavarni ko1rish uchun ✅ maxsulot  ni kritin!', reply_markup=keyboards.savvat)
            await state.finish()
        else:
            agent_id1 = callback_data.get('id')
            agent_name = callback_data.get('name')
            agent_tell = callback_data.get('tell')
            await state.update_data({'agent_id': agent_id1})
            await state.update_data({'agent1': agent_name})
            await state.update_data({'agent_num': agent_tell})
            await call.message.answer('BUYURMACHINING 🔰 ISM SHARIFINI KRITING ', reply_markup= ReplyKeyboardRemove())
            await Test.next()
            await state.update_data(agent=a)

    except:
        await call.answer('''❌TIZIMDA XATOLIK RO`Y BERDI 
30 SONIYADAN KEYIN 
    ✅   /maxsulot ✅
TUGMASINI BOSING''')
        await state.finish()

@db.message_handler(state=Test.ism)
async def tell(msg: types.Message, state: FSMContext):
    try:
        a = msg.text
        if a == 'bosh saxifa':
            await bot.send_message(msg.chat.id,f'''❌SALOM SIZ BOSH SAXIFAGA O`TDINGIZ BUYURTMA BERISH UCHUN
     🔧 /maxsulot 🔧 
NI BOSING''', reply_markup=ReplyKeyboardRemove())
            await state.finish()
        elif len(a)<10:
            await bot.send_message(msg.chat.id,
                                   '❌xato malumot kritingiz iltimos qaytada kriting', reply_markup=ReplyKeyboardRemove())
            await Test.ism.set()
        else:
            await state.update_data({
                'client_ism': a
            })
            await bot.send_message(msg.chat.id, 'Buyurtmachining 🔰 TELEFON RAQAMINI 🔰kriting ', reply_markup=keyboards.otmet_in)
            await Test.next()
            await state.update_data(ism=a)
    except:
        await state.finish()
        await bot.send_message(msg.chat.id, '''TIZIMDA XATOLIK RO`Y BERDI 
30 SONIYADAN KEYIN 
    ✅   /maxsulot ✅
TUGMASINI BOSING''')
@db.message_handler(state=Test.tell,content_types=['contact'])
async def tolov_turi(msg: types.Message, state: FSMContext):
    try:
        a = msg.contact.phone_number
        await state.update_data(
            {
                'client_nomer': a
            }
        )
        await bot.send_message(msg.chat.id, 'TO`LOV TURINI TANLANG', reply_markup=keyboards.tasdiq)
        await Test.next()
    except:
        await bot.send_message(msg.chat.id, 'TIZIMDA XATOLIK', reply_markup=keyboards.savvat)

@db.message_handler(state=Test.tell)
async def tolov_turi(msg: types.Message, state: FSMContext):
    try:
        a = msg.text
        if a == 'bosh saxifa':
            await bot.send_message(msg.chat.id,
                                   f'''SIZ BOSH SAXIFAGA O`TDINGIZ BUYURTMA BERISH UCHUN
                                            🔧 /maxsulot 🔧 
                                   NI BOSING''', reply_markup=keyboards.savvat)
            state.finish()

        elif a[0] =='+' and len(a) == 13:
            await state.update_data(
                {
                    'client_nomer':a
                }
            )
            await bot.send_message(msg.chat.id, 'TO`LOV TURINI TANLANG', reply_markup=keyboards.tasdiq)
            await Test.next()

        else:
            await bot.send_message(msg.chat.id, '''❌ SIZ RAQAMNI NO`TO`G`RI TERDINGIZ❌ 
            ❌ BOSHIDAGI "+"NI UNUTDINGIZ YOKI 
            ❌ TERILGAN RAQAM MAVJUD EMAS ILTIMOS TEKSHIRIB QAYTADAN TERING''', reply_markup=ReplyKeyboardRemove())
            await Test.tell.set()
    except:
        await Test.tell.set()
        await bot.send_message(msg.chat.id, '''TIZIMDA XATOLIK RO`Y BERDI 
        30 SONIYADAN KEYIN 
             ✅   /maxsulot ✅
        TUGMASINI BOSING''', reply_markup=keyboards.savvat)

@db.message_handler(state=Test.tolov_turi)
async def moljal(msg: types.Message, state: FSMContext):
    try:
        a = msg.text
        if a == 'bosh saxifa':
            await bot.send_message(msg.chat.id,
                                   f'''❌SIZ BOSH SAXIFAGA O`TDIZ 
                                   TAVARLARGA BUYURTMA BERISH UCHUN 
                                     ✅   /maxsulot ✅
                                   TUGMASINI BOSING❌''',reply_markup=keyboards.savvat)
            await state.finish()
        elif a == 'NAXT' or a == 'MUDATLI TO`LOV':
            await state.update_data(
                {
                    'tolov_turi':a
                }
            )

            await bot.send_message(msg.chat.id, '➕byurmachini MO`LJALINI(addressini) KRITING', reply_markup=keyboards.otmenin)
            await Test.next()

            await state.update_data(ism=a)


        else:
            await bot.send_message(msg.chat.id,
                                   f'❌NO`TO`G`RI TO`LOV TURINI   KRITINGIZ ILTIMOS QAYTADAN TO`G`IRLAP YUBORING! ❌', )
            await Test.tolov_turi.set()
    except:
        await state.finish()
        await bot.send_message(msg.chat.id, '❌ NO`TO`G`TI KRITINGIZ QAYTADAN KRITING!  ❌', reply_markup=ReplyKeyboardRemove())
@db.message_handler(content_types=['location'],state=Test.moljal)
async def cantactts(msg:types.Message, state:FSMContext):
    lat = msg.location.latitude
    lon = msg.location.longitude
    await state.update_data({
        'location':{'lat':str(lat),'lon':str(lon)}
    })
    await bot.send_message(msg.chat.id,'malumot qabul qilondi tasdiqlaysizmi', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(
        keyboards.inline_ot, KeyboardButton(text='XA')
    ))
@db.message_handler(state=Test.moljal)
async def last(msg: types.Message, state: FSMContext):
    try:
        a = await state.get_data()
        obnar = 0
        b = msg.text
        resp = await product()
        txt = ''
        if b== 'bosh saxifa':
            await bot.send_message(msg.chat.id,
                                   f'⭕️SIZ BOSH SAXIFAGA O`TDIZ TAVARLARGA BUYURTMA BERISH UCHUN 🔰  /maxsulot 🔰  ni kritin! ', reply_markup=ReplyKeyboardRemove())
            await state.finish()
        else:
            await state.update_data({
                'addres':b
            })
            await bot.send_message(msg.chat.id, '✅BUYURTMA YUBORILDI YANGI BUYURTMA BERISH UCHUN 🔰  /maxsulot 🔰 NI BOSING! ', reply_markup=keyboards.savvat)
            data = await state.get_data()
            try:
                lon = data['location']['lon']
                lat = data['location']['lat']
            except:
                pass
            agent1 = data['agent1']
            agent_num = data['agent_num']
            agent_id = data['agent_id']
            client_ism = data['client_ism']
            client_nomer = data['client_nomer']
            tolov_turi = data['tolov_turi']
            if b =='XA':
                b = 'lokatsiya orqali yuborildi'
                addres = b
            elif len(b)<15:
                await bot.send_message(msg.chat.id,'xato malumot kritingiz iltimos qayta yuboring')
                await Test.moljal.set()
                return None
            else:
                addres = b
            product_id = []
            for da in resp:
                try:
                    dat = a[f'zakaz_{da["name"]}']
                    txt += f'🔰{da["name"].upper()} MAXSULOTIMIZDAN \n'
                    txt += f'🔰{dat["kl"]} ta \n'
                    txt += f'🔰{dat["kl"]} * {da["narx"]} = {dat["obn"]} so`m\n'
                    obnar += int(dat['obn'])
                    await adding_to_db.adding_db(agent=agent_id, to_product=da['id'],money=dat['obn'],client_name=client_ism,
                                           client_number=client_nomer,client_addres=addres)
                except Exception as p:
                    print(p, '2')
            tolov= obnar
            txt += f'🔰UMUMIY TO`LOV {tolov} sum'
            if b=='lokatsiya orqali yuborildi':
                await bot.send_location(admins,latitude=lat,longitude=lon)
            text = f"""
🔰agent:   
{agent1}
            
🔰agent telefon raqami:  

{agent_num} 

🔰buyurtmachining ism sharifi: 

{client_ism}   
                        
🔰buyurtmachinig telefon raqami:  

{client_nomer}
                        
🔰buyurmachinig adresi:    

{addres}                        
🔰to`lov turi: {tolov_turi}

"""
            text += txt
            otment_product = InlineKeyboardButton(text='BEKOR QILISH', callback_data=f"deny:{msg.chat.id}:{client_nomer}:{product_id}:{tolov}")
            rep_text = f"order:{msg.chat.id}:{client_nomer}:{product_id}:{tolov}"

            accept = InlineKeyboardButton('qabul qilish',callback_data= rep_text)

            p1 = InlineKeyboardMarkup().add(accept,otment_product)
            await bot.send_message(chat_id=admins, text=text,reply_markup=p1)
            await state.finish()

    except Exception as ex:
        print(ex, '1')
        await state.finish()
        await bot.send_message(msg.chat.id, '''🚫NO`TO`G`TI KRITINGIZ QAYTADAN KRITINGIZ!  
        QAYTADAN BOSHLASH UCHUN✅ /start NI BOSING''')
@db.callback_query_handler(order_call.filter())
async def accepting(call: CallbackQuery, state: FSMContext, callback_data : dict):
    await call.answer(cache_time=30)
    data = callback_data
    client_nomer = data.get('client_nomer')
    kg = data.get('tolov')
    await bot.send_message(chat_id= data.get('agent_id'), text = f'''
    ✅QABUL QILINDI ✅
SIZNING NOMINGIZDAN  {client_nomer} ga {kg} so`mli 
maxsulot qabul qilindi qisqa mudat ichida yetkazib berishga xarakat qilamiz''', reply_markup= ReplyKeyboardRemove() )

@db.callback_query_handler(cancel_call.filter())
async def accepting(call: CallbackQuery, state: FSMContext, callback_data : dict):
    await call.answer(cache_time=30)
    data = callback_data
    client_nomer = data.get('client_nomer')
    kg = data.get('tolov')
    await bot.send_message(chat_id= data.get('agent_id'), text = f'''
        ❌RAD ETILDI❌
SIZNING NOMINGIZDAN  {client_nomer} ga {kg} so`mli maxsulot bekor qilindi, iltimos menejir bilan bog`laning''', reply_markup=ReplyKeyboardRemove() )
