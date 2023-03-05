import string

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hspoiler

from keyboards.default.start import full_name, grades, class_letters
from states.user.user_info import UserInfo


async def bot_start(msg: types.Message, state: FSMContext):
    tg_name_btn = full_name(msg)
    hidden_tip = hspoiler('Вы можете нажать на кнопку, если ваше имя в Telegram по умолчанию устраивает вас.')
    await msg.answer(
        f'Здравствуйте, давайте познакомимся с вами. <i>Как вас зовут? (Введите в формате: <b>Имя Фамилия - на кириллице </b>, '
        f'без дополнительных знаков и цифр.)</i>\n\n<b>{hidden_tip}</b>',
        reply_markup=tg_name_btn)

    await state.set_state(UserInfo.waiting_for_full_name.state)


async def name_defined(msg: types.Message, state: FSMContext):
    grade = grades()
    symbols = string.digits + string.punctuation

    for i in symbols:
        if i in msg.text:
            await msg.answer('Ошибка! Вы ввели имя в неправильном формате.', reply_markup=full_name(msg))
            await state.set_state(UserInfo.waiting_for_full_name.state)
            return

    await msg.answer('Тэкс, ваше имя я заполучил. '
                     '<i>Можете теперь ввести в каком классе вы учитесь? (от 1 до 11)</i>',
                     reply_markup=grade)

    await state.set_state(UserInfo.waiting_for_grade.state)

    await state.update_data({"full_name": msg.text})


async def grade_defined(msg: types.Message, state: FSMContext):
    character = class_letters()
    try:
        if not int(msg.text) <= 11 or not int(msg.text) >= 1:
            await msg.answer('Ввод неправильный, попробуйте ввести еще раз.',
                             reply_markup=grades())
            await state.set_state(UserInfo.waiting_for_grade.state)
            return
    except ValueError:
        await msg.answer('Вы указали неверный тип данных. Повторите попытку.',
                         reply_markup=grades())  # not local variable
        await state.set_state(UserInfo.waiting_for_grade.state)
        return

    await msg.answer('Это мой последний вопрос. '
                     'После этого, приставать к вам я особо не буду. '
                     '<i>Назовите буковку вашего класса пожалуйста. (Буква от "А" до "Г")</i>', reply_markup=character)

    await state.set_state(UserInfo.waiting_for_class_letter.state)

    await state.update_data({"grade": msg.text})


async def class_letter_defined(msg: types.Message, state: FSMContext):
    _characters = ['А', 'Б', 'В', 'Г']
    if msg.text.lower() not in [x.lower() for x in _characters]:
        await msg.answer('Введена неправильная буква класса. Повторите попытку.', reply_markup=class_letters())
        await state.set_state(UserInfo.waiting_for_class_letter.state)
        return

    await state.set_state(UserInfo.finished.state)
    await state.update_data({"grade_character": msg.text})

    user_info = await state.get_data()

    await msg.answer(f"{user_info}")
    await msg.answer(f"Все готово.", reply_markup=ReplyKeyboardRemove())

    await state.finish()
