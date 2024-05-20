from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async  def  set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда для запуска бота'),
        types.BotCommand(command='/help', description='Команда для получение инфромации'),
        types.BotCommand(command='/kik', description='Команда для кика учястника бота'),
        types.BotCommand(command='/mute', description='Команда для мута учясткика'),
        types.BotCommand(command='/unmute', description='Команда для размута учясткика')
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, гандон!!!')

@dp.message_handler(commands= 'kik')
async def kik(message: types.Message):
    await message.answer('Минус 1 не очень умный пользователь')

@dp.message_handler(commands= 'mute')
async def mute(message: types.Message):
    await message.answer('Помалчи пока сладенький')

@dp.message_handler(commands= 'unmute')
async def unmute(message: types.Message):
    await message.answer('Эх а так харашо было... в тишене')

@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Что тебе не понятно, БИОМУСОР. Давай помогу')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
