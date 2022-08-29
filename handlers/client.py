from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=["start", "help"])
async def commands_start(message: types.Message):
    try:
        await bot.answer(message.from_user.id, 'Приятного Аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботомб через лс, анпишите ему: url')


# @dp.message_handler(commands=["Режим работы"])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, "время работы")


# @dp.message_handler(commands=["Расположение"])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "место положение", reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
