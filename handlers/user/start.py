from aiogram import types

from keyboards.inline.start import user_menu
from utils.misc import rate_limit


@rate_limit(1, 'start')
async def bot_start(msg: types.Message):
    menu = user_menu()
    await msg.answer(f'Привет, {msg.from_user.full_name}!. Вас приветстувует BF school bot. '
                     f'Ниже перечислено несколько вариантов взаимодействия с ботом. Выберите какой то из них 👇👇👇',
                     reply_markup=menu)


async def timetable(call: types.CallbackQuery):
    await call.answer('Ты нажал на расписание пон', show_alert=True)
    await call.answer()
