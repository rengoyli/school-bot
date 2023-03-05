from aiogram.dispatcher.filters.state import StatesGroup, State


class UserInfo(StatesGroup):
    waiting_for_full_name = State()
    waiting_for_grade = State()
    waiting_for_class_letter = State()
    finished = State()
