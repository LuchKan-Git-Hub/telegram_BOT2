from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup
from pyrogram import emoji
start_option = KeyboardButton(f'/start {emoji.FAST_DOWN_BUTTON}')
time_option = KeyboardButton(f'/time {emoji.ALARM_CLOCK}')
info_option = KeyboardButton(f'/info {emoji.INFORMATION}')
id_option = KeyboardButton(f'/my_id {emoji.CREDIT_CARD}')
play_option = KeyboardButton(f'/game {emoji.PLAY_BUTTON}')
rock_paper_scissors_game_option = KeyboardButton(f'/rock_paper_scissors {emoji.ROCK}')
rock_option = KeyboardButton(f'/rock {emoji.ROCK}')
paper_option = KeyboardButton(f'/rock {emoji.PAPERCLIP}')
scissors_option = KeyboardButton(f'/rock {emoji.SCISSORS}')
quest_option = KeyboardButton(f'/quest {emoji.CITYSCAPE}')
return_option = KeyboardButton(f'/return {emoji.MAN_WALKING}')
return_option_2 = KeyboardButton(f'/return {emoji.MAN_WALKING}')


kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [start_option, time_option, id_option, info_option],
        [play_option],
    ],
resize_keyboard = True,
)

kb_main_2 = ReplyKeyboardMarkup(
    keyboard=[
        [rock_paper_scissors_game_option],
        [quest_option, return_option],
    ],
resize_keyboard = True,
)

kb_main_3 = ReplyKeyboardMarkup(
    keyboard=[
        [rock_option, paper_option, scissors_option],
        [return_option_2],
    ],
resize_keyboard = True,
)
