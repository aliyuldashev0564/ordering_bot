from aiogram import Bot , Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
admins = 'YOUR ADMIN TELEGRAM ID'
token = 'YOUR BOT TOKEN'

agent_url = 'http://127.0.0.1:8000/agents'
product_url = 'http://127.0.0.1:8000/product/'
DB_USER = 'YOUR DATABASE USER'
DB_PASS= 'YOUR DATABASE PASSWORD'
DB_HOST ='YOUR DATABASE HOST'
DB_NAME = 'YOUR DATABASE NAME'

storage = MemoryStorage()
bot = Bot(token=token)
db = Dispatcher(bot, storage=storage)