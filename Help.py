from pyrogram import Client
import config

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.API_TOKEN,
    name='Botchik'
)

@bot.on_message()
async def echo_and_reply(bot,message):
    if message.text in ['HI', 'hi']:
        await message.reply('Nice to meet you!')
    elif message.text in ['BYE', 'bye']:
        await message.reply('Ok bye!!!')
    else:
        await message.reply(f'you said: {message.text}')
bot.run()