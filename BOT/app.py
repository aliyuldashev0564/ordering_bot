from config import db
from aiogram import executor
from start import *
from main import *

if __name__ == "__main__":
    executor.start_polling(db)