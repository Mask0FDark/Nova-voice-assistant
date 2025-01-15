import config
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from script import *
#програма сделана Mask_0F_Darkness ❤️
bot = Bot(token=config.NOVA_TG_TOKEN)
dp = Dispatcher(bot)

# Defining and adding buttons 
button01 = InlineKeyboardButton(text="ютуб", callback_data="button01") 
button02 = InlineKeyboardButton(text="стим", callback_data="button02") 
button03 = InlineKeyboardButton(text="03", callback_data="button03") 
button04 = InlineKeyboardButton(text="04", callback_data="button04") 
button05 = InlineKeyboardButton(text="05", callback_data="button05") 
button06 = InlineKeyboardButton(text="06", callback_data="button06") 
button07 = InlineKeyboardButton(text="07", callback_data="button07") 
button08 = InlineKeyboardButton(text="08", callback_data="button08") 
button09 = InlineKeyboardButton(text="09", callback_data="button09") 
button10 = InlineKeyboardButton(text="10", callback_data="button10") 

keyboard_inline = InlineKeyboardMarkup().add(button01, button02, button03, button04, button05, button06, button07, button08, button09, button10) 
#keyboard_inline = InlineKeyboardMarkup().add(button03, button04) 
#keyboard_inline = InlineKeyboardMarkup().add(button05, button06) 
#keyboard_inline = InlineKeyboardMarkup().add(button07, button08) 
#keyboard_inline = InlineKeyboardMarkup().add(button09, button10) 
  
  
@dp.message_handler(commands=['start']) 
async def check(message: types.Message): 
    await message.reply("меню управления пк", reply_markup=keyboard_inline)  
  
@dp.callback_query_handler(text=["button01", "button01","button02", "button03","button04", "button05","button06", "button07","button08", "button09","button10"]) 
async def check_button(call: types.CallbackQuery): 
    if config.NOVA_TG==1:
        if call.data == "button01": 
            NOVA_youtube()
            await call.message.answer("включение ютуба") 
        if call.data == "button02": 
            NOVA_steam()
            await call.message.answer("запуск стима") 
        if call.data == "button03": 
            await call.message.answer("это кнопка 3") 
        if call.data == "button04": 
            await call.message.answer("это кнопка 4") 
        if call.data == "button05": 
            await call.message.answer("это кнопка 5") 
        if call.data == "button06": 
            await call.message.answer("это кнопка 6") 
        if call.data == "button07": 
            await call.message.answer("это кнопка 7") 
        if call.data == "button08": 
            await call.message.answer("это кнопка 8") 
        if call.data == "button09": 
            await call.message.answer("это кнопка 9") 
        if call.data == "button10": 
            await call.message.answer("это кнопка 10") 

        await call.answer() 
    else:
        await call.message.answer("в данный момент функция отключена")
        await call.answer() 
  
# Start the bot 
executor.start_polling(dp) 
