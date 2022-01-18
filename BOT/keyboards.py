from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
#location
otmenin = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='lacation',request_location=True),KeyboardButton(text='bosh saxifa'))
#payment keybor

markuo = InlineKeyboardMarkup(row_width=1)
dVOM = InlineKeyboardButton('davom etish', callback_data='can')
otmen = InlineKeyboardButton('rad etish', callback_data='cancel')
markuo.add(dVOM,otmen)

#otmen / xisobot
xisobot = KeyboardButton('Telefon raqam', request_contact=True)
inline_ot = KeyboardButton('bosh saxifa')
otmet_in = ReplyKeyboardMarkup(resize_keyboard=True)
otmet_in.insert(xisobot)
otmet_in.insert(inline_ot)

#agent
agent_bl = InlineKeyboardMarkup()

#tolov turi
nomer = KeyboardButton('NAXT')
moljal = KeyboardButton('KARTA')
ism = KeyboardButton('MUDATLI TO`LOV')
tasdiq = ReplyKeyboardMarkup(resize_keyboard=True).add(nomer,ism, inline_ot)

#proving
otment_product = InlineKeyboardButton(text = 'Bekor qilish', callback_data='deny')
accept = InlineKeyboardButton(text = 'Qabul qilish', callback_data='accept')
profing = InlineKeyboardMarkup().add(otment_product , accept)

counting_ink = InlineKeyboardMarkup()
#counting keyboards
def counting_keyboards(item_id,narx,name,zn):
    mark_up = InlineKeyboardMarkup(row_width=1)
    zero = InlineKeyboardButton(text='Buyurtma berish',callback_data=f'count:{name}:{item_id}:{narx}:{zn}')
    mark_up.add(zero)
    return mark_up

#location/tell number
mark = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='contact', request_contact=True), KeyboardButton(text='location', request_location=True))

#countkey
countkey = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton(text=1),KeyboardButton(text=2),KeyboardButton(text=3),
    KeyboardButton(text=4),KeyboardButton(text=5),KeyboardButton(text=6),
    KeyboardButton(text=7),KeyboardButton(text=8),KeyboardButton(text=9),
    KeyboardButton(text=10)
)
#savat
savvat = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text='/maxsulot'), KeyboardButton(text='/savat'))

