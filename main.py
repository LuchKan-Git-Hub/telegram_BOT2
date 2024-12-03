from email.policy import default

from pyrogram import Client, filters
from pyrogram.filters import reply_keyboard
from pyrogram.raw.types import KeyboardButton, ReplyKeyboardMarkup
import config
import datetime
import Keyboard
import random
from Keyboard import kb_main
from Keyboard import kb_main_2

# Get the current time
current_time = datetime.datetime.now()

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.API_TOKEN,
    name='Botchik'
)

def button_filter(button):
   async def func(_, __, msg):
       return msg.text == button.text
   return filters.create(func, "ButtonFilter", button=button)

@bot.on_message(filters.command('start'))
async def reply(bot, message):
    await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAENLhBnPhNSct_FCoK6HrLHzzMp8f69ogACAQEAAladvQoivp8OuMLmNDYE",
                           reply_markup=Keyboard.kb_main)

@bot.on_message(filters.command('game'))
async def play(bot, message):
    await message.reply('choosing game..',
    reply_markup=Keyboard.kb_main_2)

@bot.on_message(filters.command('info') | button_filter(Keyboard.info_option))
async def test(bot, message):
    await message.reply('/start to send you sticker, /time to check the time, /info to see all commands',
                        '/my_id to your id')

@bot.on_message(filters.command('time'))
async def time(bot, message):

    await message.reply(f'The time is {current_time}')
@bot.on_message(filters.command('my_id'))
async def time(bot, message):
    await message.reply(f'your id is {message.chat.id}')

@bot.on_message(filters.command('return') | button_filter(Keyboard.return_option))
async def returns(bot, message):
    await message.reply('returned',
                  reply_markup=Keyboard.kb_main)

@bot.on_message()
async def echo(bot, message):
    await message.reply(message.txt)
bot.run()
