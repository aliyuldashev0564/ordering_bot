from aiogram.dispatcher.filters.state import StatesGroup, State
class admin(StatesGroup):
    admin = State()

class Test(StatesGroup):
    tavar = State()
    kg = State()
    agent = State()
    ism = State()
    tell = State()
    tolov_turi = State()
    moljal = State()


class Start(StatesGroup):
    parol = State()
    ism = State()
    tell = State()