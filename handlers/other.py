from aiogram import types, Dispatcher
import string, json
from create_bot import dp


@dp.message_handler()
async def cenz(message: types.Message):
    if {i.lower().translate(str.makeTrans('', '', string.punctation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply("Маты запрещины")
        await message.delete()


def register_handler_other(dp: Dispatcher):
    def register_handlers_client(dp: Dispatcher):
        dp.register_message_handler(cenz)
